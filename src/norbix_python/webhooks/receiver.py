from __future__ import annotations

import inspect
import json
import os
from collections.abc import Awaitable, Callable, Mapping, Sequence
from typing import Any

from .errors import NorbixWebhookParseError, NorbixWebhookSignatureError
from .models import (
    WebhookContext,
    WebhookEnvelope,
    WebhookEvent,
    WebhookHandleResult,
)
from .normalize import normalize_webhook
from .signature import DeliveryHeaders, parse_webhook_headers, verify_signature

# A typed handler: (payload, event) -> None | Awaitable[None]
Handler = Callable[[Any, WebhookEvent], Any]
# A raw handler: (envelope, ctx) -> None | Awaitable[None]
RawHandler = Callable[[WebhookEnvelope, WebhookContext], Any]


def _resolve(
    *,
    secret: str | None,
    tolerance_seconds: int | None,
    project_id: str | None,
    account_id: str | None,
) -> tuple[str | None, int, str | None, str | None]:
    env = os.environ
    tol = tolerance_seconds
    if tol is None:
        raw = env.get("NORBIX_WEBHOOK_TOLERANCE_SECONDS")
        tol = int(raw) if raw and raw.isdigit() else None
    return (
        secret if secret is not None else env.get("NORBIX_WEBHOOK_SIGNING_SECRET"),
        tol if tol is not None else 300,
        project_id if project_id is not None else env.get("NORBIX_PROJECT_ID"),
        account_id if account_id is not None else env.get("NORBIX_ACCOUNT_ID"),
    )


def _parse_envelope(raw_body: str) -> WebhookEnvelope:
    try:
        parsed = json.loads(raw_body)
    except json.JSONDecodeError as exc:
        raise NorbixWebhookParseError("Webhook body is not valid JSON") from exc
    if not isinstance(parsed, dict):
        raise NorbixWebhookParseError("Webhook body must be a JSON object")
    if not parsed.get("id"):
        raise NorbixWebhookParseError("Webhook envelope missing id")
    if not parsed.get("event"):
        raise NorbixWebhookParseError("Webhook envelope missing event")
    return WebhookEnvelope.model_validate(parsed)


class _BaseReceiver:
    """Shared registration + verification logic for the sync/async receivers."""

    def __init__(
        self,
        *,
        secret: str | None = None,
        tolerance_seconds: int | None = None,
        project_id: str | None = None,
        account_id: str | None = None,
    ) -> None:
        self._secret, self._tolerance, self._project_id, self._account_id = _resolve(
            secret=secret,
            tolerance_seconds=tolerance_seconds,
            project_id=project_id,
            account_id=account_id,
        )
        self._handlers: dict[str, Handler] = {}
        self._on_all: dict[str, list[RawHandler]] = {}

    # -- Registration: works as a method OR a decorator --

    def on(self, event: str, handler: Handler | None = None) -> Any:
        """Register the typed handler for one event.

        Use as a method::

            receiver.on("membership.user.registered", handle_user)

        or as a decorator::

            @receiver.on("membership.user.registered")
            def handle_user(user, event): ...
        """

        def register(fn: Handler) -> Handler:
            self._handlers[event] = fn
            return fn

        return register if handler is None else register(handler)

    def on_all(
        self, events: Sequence[str], handler: RawHandler | None = None
    ) -> Any:
        """Register a raw handler for many events. Runs after ``on`` for each.

        Works as a method or a decorator (decorator form binds the events list).
        """

        def register(fn: RawHandler) -> RawHandler:
            for event in events:
                self._on_all.setdefault(event, []).append(fn)
            return fn

        return register if handler is None else register(handler)

    # -- Shared internals --

    def _verify(self, raw_body: str, dh: DeliveryHeaders, verify: bool) -> bool | None:
        if not verify or not self._secret:
            return None
        ok, reason = verify_signature(
            secret=self._secret,
            raw_body=raw_body,
            signature=dh.signature,
            timestamp=dh.timestamp,
            tolerance_seconds=self._tolerance,
        )
        if not ok:
            raise NorbixWebhookSignatureError(reason or "Invalid signature")
        return True

    def _guard(self, envelope: WebhookEnvelope) -> None:
        if self._project_id and envelope.project_id != self._project_id:
            raise NorbixWebhookSignatureError(
                f"delivery projectId {envelope.project_id} does not match "
                f"configured {self._project_id}"
            )
        if self._account_id and envelope.account_id != self._account_id:
            raise NorbixWebhookSignatureError(
                f"delivery accountId {envelope.account_id} does not match "
                f"configured {self._account_id}"
            )

    def _build_event(
        self, envelope: WebhookEnvelope, dh: DeliveryHeaders, verified: bool | None
    ) -> tuple[Any, WebhookEvent, WebhookContext]:
        payload, metadata = normalize_webhook(envelope)
        event = WebhookEvent(
            name=envelope.event,
            deliveryId=envelope.id,
            createdOn=envelope.created_on,
            triggerId=envelope.trigger_id,
            correlationId=None,
            accountId=dh.account_id or envelope.account_id,
            projectId=dh.project_id or envelope.project_id,
            integrationId=dh.integration_id,
            destinationId=dh.destination_id,
            verified=verified,
            metadata=metadata,
            raw=envelope,
        )
        ctx = WebhookContext(
            path=None,
            verified=verified,
            accountId=dh.account_id or envelope.account_id,
            projectId=dh.project_id or envelope.project_id,
            integrationId=dh.integration_id,
            destinationId=dh.destination_id,
        )
        return payload, event, ctx

    @staticmethod
    def _result(envelope: WebhookEnvelope, verified: bool | None, handled: bool) -> WebhookHandleResult:
        return WebhookHandleResult(
            event=envelope.event,
            deliveryId=envelope.id,
            verified=verified,
            handled=handled,
            triggerId=envelope.trigger_id,
        )


class NorbixWebhookReceiver(_BaseReceiver):
    """Synchronous inbound webhook receiver.

    Example::

        from norbix_python.webhooks import NorbixWebhookReceiver, NorbixWebhookEvents

        receiver = NorbixWebhookReceiver()  # reads env

        @receiver.on(NorbixWebhookEvents.Membership.USER_REGISTERED)
        def on_registered(user, event):
            print(user.email or user.user_name, event.metadata.user)

        receiver.on_all(NORBIX_WEBHOOK_EVENT_NAMES, lambda env, ctx: log(env))

        result = receiver.handle(raw_body=body, headers=request.headers)
    """

    def handle(
        self,
        *,
        raw_body: str,
        headers: Mapping[str, str],
        path: str | None = None,
        verify: bool = True,
    ) -> WebhookHandleResult:
        dh = parse_webhook_headers(headers)
        verified = self._verify(raw_body, dh, verify)
        envelope = _parse_envelope(raw_body)
        self._guard(envelope)

        payload, event, ctx = self._build_event(envelope, dh, verified)
        if path is not None:
            ctx.path = path

        handled = False
        handler = self._handlers.get(envelope.event)
        if handler is not None:
            _run_sync(handler(payload, event))
            handled = True
        for raw_fn in self._on_all.get(envelope.event, []):
            _run_sync(raw_fn(envelope, ctx))

        return self._result(envelope, verified, handled)


class AsyncNorbixWebhookReceiver(_BaseReceiver):
    """Asynchronous inbound webhook receiver. Handlers may be sync or async."""

    async def handle(
        self,
        *,
        raw_body: str,
        headers: Mapping[str, str],
        path: str | None = None,
        verify: bool = True,
    ) -> WebhookHandleResult:
        dh = parse_webhook_headers(headers)
        verified = self._verify(raw_body, dh, verify)
        envelope = _parse_envelope(raw_body)
        self._guard(envelope)

        payload, event, ctx = self._build_event(envelope, dh, verified)
        if path is not None:
            ctx.path = path

        handled = False
        handler = self._handlers.get(envelope.event)
        if handler is not None:
            await _run_async(handler(payload, event))
            handled = True
        for raw_fn in self._on_all.get(envelope.event, []):
            await _run_async(raw_fn(envelope, ctx))

        return self._result(envelope, verified, handled)


def _run_sync(result: Any) -> None:
    if inspect.isawaitable(result):
        raise NorbixWebhookParseError(
            "an async handler was registered on the sync NorbixWebhookReceiver; "
            "use AsyncNorbixWebhookReceiver instead"
        )


async def _run_async(result: Any) -> None:
    if inspect.isawaitable(result):
        await result
