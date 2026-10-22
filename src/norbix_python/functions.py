"""The event envelope a Norbix cloud function receives.

When a trigger, a scheduler task or a manual call (`hub.code.invoke_code_function`)
runs one of your functions on AWS Lambda, Azure Functions or Google Cloud
Functions, the function gets one JSON envelope (`CodeFunctionEventDto` in the
Norbix API reference). :func:`parse_function_event` turns it into a
:class:`FunctionEvent`: a thin wrapper over the decoded dict with typed views
of the slots in `data` and the constructor options of a client that acts as
the run-as user. Nothing here re-declares the DTO; every field is read from
the raw envelope on access, and `raw` is always there for the rest.
"""

from __future__ import annotations

import json
from typing import Any

from .errors import NorbixError

#: The envelope version this helper reads.
FUNCTION_EVENT_SPEC_VERSION = "1"


class NorbixFunctionEventError(NorbixError):
    """The payload was not a Norbix function event envelope (or a slot is missing)."""

    def __init__(self, message: str) -> None:
        super().__init__(message, code="FUNCTION_EVENT_INVALID")


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


class _View:
    """A read-only view over one object of the envelope. `raw` is the dict itself."""

    __slots__ = ("raw",)

    def __init__(self, raw: Any) -> None:
        self.raw: dict[str, Any] = _as_dict(raw)

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return f"{type(self).__name__}({self.raw!r})"


class RunAs(_View):
    """`context.runAs` — the service user the function acts as, and its token."""

    @property
    def user_id(self) -> str | None:
        return self.raw.get("userId")

    @property
    def access_token(self) -> str | None:
        """A short-lived bearer token (15 minutes) for the run-as user; Hub and Api."""
        return self.raw.get("accessToken")

    @property
    def expires_at(self) -> str | None:
        return self.raw.get("expiresAt")


class Caller(_View):
    """`context.caller` — who caused the source event, as data, never authority."""

    @property
    def user_id(self) -> str | None:
        return self.raw.get("userId")

    @property
    def email(self) -> str | None:
        return self.raw.get("email")

    @property
    def kind(self) -> str | None:
        """`User`, `ApiKey` or `System`."""
        return self.raw.get("kind")


class FunctionContext(_View):
    """`context` — where the event happened and how to call Norbix back."""

    @property
    def account_id(self) -> str | None:
        return self.raw.get("accountId")

    @property
    def project_id(self) -> str | None:
        return self.raw.get("projectId")

    @property
    def environment(self) -> str | None:
        """The project environment the event happened in (`PROD`, `TEST`, …)."""
        return self.raw.get("environment")

    @property
    def region(self) -> str | None:
        return self.raw.get("region")

    @property
    def hub_url(self) -> str | None:
        return self.raw.get("hubUrl")

    @property
    def api_url(self) -> str | None:
        return self.raw.get("apiUrl")

    @property
    def echo_url(self) -> str | None:
        return self.raw.get("echoUrl")

    @property
    def trigger_id(self) -> str | None:
        return self.raw.get("triggerId")

    @property
    def task_id(self) -> str | None:
        return self.raw.get("taskId")

    @property
    def correlation_id(self) -> str | None:
        return self.raw.get("correlationId")

    @property
    def caller(self) -> Caller | None:
        value = self.raw.get("caller")
        return Caller(value) if isinstance(value, dict) else None

    @property
    def run_as(self) -> RunAs:
        return RunAs(self.raw.get("runAs"))


class DatabaseRecordChange(_View):
    """`data.database` — one record before and after (Database triggers)."""

    @property
    def collection(self) -> str | None:
        return self.raw.get("collection")

    @property
    def schema_id(self) -> str | None:
        return self.raw.get("schemaId")

    @property
    def schema_version(self) -> int | None:
        return self.raw.get("schemaVersion")

    @property
    def record_id(self) -> str | None:
        return self.raw.get("recordId")

    @property
    def old(self) -> dict[str, Any] | None:
        """The document before the change; None on an insert, or when truncated."""
        value = self.raw.get("old")
        return value if isinstance(value, dict) else None

    @property
    def new(self) -> dict[str, Any] | None:
        """The document after the change; None on a delete, or when truncated."""
        value = self.raw.get("new")
        return value if isinstance(value, dict) else None

    @property
    def truncated(self) -> bool:
        """True when `old` / `new` were left out (over 200 KB): fetch them by the refs."""
        return bool(self.raw.get("truncated", False))

    @property
    def old_ref(self) -> dict[str, Any] | None:
        value = self.raw.get("oldRef")
        return value if isinstance(value, dict) else None

    @property
    def new_ref(self) -> dict[str, Any] | None:
        value = self.raw.get("newRef")
        return value if isinstance(value, dict) else None


class UserChange(_View):
    """`data.user` — a membership user before and after (Membership triggers)."""

    @property
    def user_id(self) -> str | None:
        return self.raw.get("userId")

    @property
    def old(self) -> dict[str, Any] | None:
        value = self.raw.get("old")
        return value if isinstance(value, dict) else None

    @property
    def new(self) -> dict[str, Any] | None:
        value = self.raw.get("new")
        return value if isinstance(value, dict) else None


class FileChange(_View):
    """`data.file` — an upload (`new`) or a delete (`old`), Files triggers."""

    @property
    def old(self) -> dict[str, Any] | None:
        value = self.raw.get("old")
        return value if isinstance(value, dict) else None

    @property
    def new(self) -> dict[str, Any] | None:
        value = self.raw.get("new")
        return value if isinstance(value, dict) else None

    @property
    def path(self) -> str | None:
        return self.raw.get("path")


class PaymentFact(_View):
    """`data.payment` — the webhook fact a Payments trigger fired on (no "before")."""

    @property
    def integration_id(self) -> str | None:
        return self.raw.get("integrationId")

    @property
    def provider(self) -> str | None:
        return self.raw.get("provider")

    @property
    def provider_event_id(self) -> str | None:
        return self.raw.get("providerEventId")

    @property
    def event_name(self) -> str | None:
        return self.raw.get("eventName")

    @property
    def order_id(self) -> str | None:
        """The payment order (``ord_…``) the callback is about, when it is about one."""
        return self.raw.get("orderId")

    @property
    def status(self) -> str | None:
        return self.raw.get("status")

    @property
    def amount_minor(self) -> int | None:
        return self.raw.get("amountMinor")

    @property
    def currency(self) -> str | None:
        return self.raw.get("currency")

    @property
    def external_ids(self) -> dict[str, str]:
        return _as_dict(self.raw.get("externalIds"))

    @property
    def occurred_on(self) -> str | None:
        return self.raw.get("occurredOn")

    @property
    def received_on(self) -> str | None:
        return self.raw.get("receivedOn")


class PaymentOrder(_View):
    """A stored payment order (``PaymentOrderDto``): lines, totals and status.

    ``lines`` and ``checkouts`` are the raw dicts (``sku``, ``title``,
    ``quantity``, ``unitAmountMinor``, ``amountMinor`` / ``attempt``,
    ``integrationId``, ``provider``, ``paymentUrl``, ``expiresAtUtc``, …).
    """

    @property
    def id(self) -> str | None:
        return self.raw.get("id")

    @property
    def env(self) -> str | None:
        return self.raw.get("env")

    @property
    def buyer_user_id(self) -> str | None:
        return self.raw.get("buyerUserId")

    @property
    def merchant_reference(self) -> str | None:
        return self.raw.get("merchantReference")

    @property
    def currency(self) -> str | None:
        return self.raw.get("currency")

    @property
    def price_version(self) -> str | None:
        return self.raw.get("priceVersion")

    @property
    def lines(self) -> list[dict[str, Any]]:
        value = self.raw.get("lines")
        return [line for line in value if isinstance(line, dict)] if isinstance(value, list) else []

    @property
    def total_minor(self) -> int | None:
        return self.raw.get("totalMinor")

    @property
    def metadata(self) -> dict[str, str]:
        return _as_dict(self.raw.get("metadata"))

    @property
    def status(self) -> str | None:
        """The order status after the last change.

        ``Created``, ``CheckoutStarted``, ``Paid``, ``PartiallyRefunded``,
        ``Refunded``, ``Reversed``, ``Expired``, …
        """
        return self.raw.get("status")

    @property
    def created_on_utc(self) -> str | None:
        return self.raw.get("createdOnUtc")

    @property
    def updated_on_utc(self) -> str | None:
        return self.raw.get("updatedOnUtc")

    @property
    def checkouts(self) -> list[dict[str, Any]]:
        value = self.raw.get("checkouts")
        return [c for c in value if isinstance(c, dict)] if isinstance(value, list) else []

    @property
    def settled_minor(self) -> int | None:
        return self.raw.get("settledMinor")

    @property
    def refunded_minor(self) -> int | None:
        return self.raw.get("refundedMinor")

    @property
    def paid_on_utc(self) -> str | None:
        return self.raw.get("paidOnUtc")

    @property
    def provider_payment_id(self) -> str | None:
        return self.raw.get("providerPaymentId")

    @property
    def mismatches(self) -> list[str]:
        value = self.raw.get("mismatches")
        return list(value) if isinstance(value, list) else []


class PaymentOrderEvent(_View):
    """`data.order` — a stored payment order changed (``payments.order.*``).

    ``order`` is the order as stored after the change; ``payment`` is the
    provider callback that changed it. ``order_event_id`` is the
    de-duplication key: it is the same on every retry of the same change.
    """

    @property
    def order_event_id(self) -> str | None:
        """The de-duplication key — the same on every retry of this change."""
        return self.raw.get("orderEventId")

    @property
    def event(self) -> str | None:
        """The event name: ``payments.order.paid``, ``…refunded``, ``…expired``, …"""
        return self.raw.get("event")

    @property
    def from_(self) -> str | None:
        """The order status before the change (``from`` on the wire)."""
        return self.raw.get("from")

    @property
    def to(self) -> str | None:
        """The order status after the change."""
        return self.raw.get("to")

    @property
    def reason(self) -> str | None:
        return self.raw.get("reason")

    @property
    def order(self) -> PaymentOrder:
        return PaymentOrder(self.raw.get("order"))

    @property
    def payment(self) -> PaymentFact | None:
        value = self.raw.get("payment")
        return PaymentFact(value) if isinstance(value, dict) else None


class ScheduledTaskInfo(_View):
    """`data.task` — the scheduler task that fired (`scheduler.task.fired`)."""

    @property
    def task_id(self) -> str | None:
        return self.raw.get("taskId")

    @property
    def name(self) -> str | None:
        return self.raw.get("name")

    @property
    def fired_at(self) -> str | None:
        return self.raw.get("firedAt")


class AiUsageEvent(_View):
    """`data.ai` — an AI trigger's payload."""

    @property
    def payload(self) -> dict[str, Any]:
        return _as_dict(self.raw.get("payload"))

    @property
    def target_user_id(self) -> str | None:
        return self.raw.get("targetUserId")


class FunctionEvent:
    """One delivery to a cloud function: the envelope of `Code.Functions.md` §4.

    Built by :func:`parse_function_event`. `raw` is the decoded envelope; the
    properties read it on access. The `as_*` views return the typed slot of
    `data` for the source, and raise :class:`NorbixFunctionEventError` when the
    event carries no such slot (a file event asked for a record change).
    """

    __slots__ = ("raw",)

    def __init__(self, raw: dict[str, Any]) -> None:
        self.raw = raw

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return f"FunctionEvent(id={self.id!r}, event={self.event!r}, source={self.source!r})"

    # -- envelope fields ---------------------------------------------------

    @property
    def spec_version(self) -> str:
        return str(self.raw.get("specVersion"))

    @property
    def id(self) -> str | None:
        """This delivery."""
        return self.raw.get("id")

    @property
    def event_id(self) -> str | None:
        """The change; the same for a webhook delivery of the same change."""
        return self.raw.get("eventId")

    @property
    def event(self) -> str | None:
        """The handler key: `database.record.updated`, `scheduler.task.fired`, `manual.invoke`, …"""
        return self.raw.get("event")

    @property
    def source(self) -> str | None:
        """`database`, `membership`, `files`, `payments`, `ai`, `scheduler` or `manual`."""
        return self.raw.get("source")

    @property
    def created_on(self) -> str | None:
        return self.raw.get("createdOn")

    @property
    def context(self) -> FunctionContext:
        return FunctionContext(self.raw.get("context"))

    @property
    def data(self) -> dict[str, Any]:
        """The raw `data` object: one optional slot per source."""
        return _as_dict(self.raw.get("data"))

    @property
    def config(self) -> dict[str, Any] | None:
        """The developer's JSON config, bound at fire time; None when the action has none."""
        value = self.raw.get("config")
        return value if isinstance(value, dict) else None

    # -- typed views of `data` ----------------------------------------------

    def _slot(self, name: str) -> dict[str, Any]:
        value = self.data.get(name)
        if not isinstance(value, dict):
            raise NorbixFunctionEventError(
                f"The function event {self.id!r} ({self.event!r}, source {self.source!r}) "
                f"carries no data.{name}."
            )
        return value

    def as_database_record_change(self) -> DatabaseRecordChange:
        """`data.database` — Database triggers."""
        return DatabaseRecordChange(self._slot("database"))

    def as_user_change(self) -> UserChange:
        """`data.user` — Membership triggers."""
        return UserChange(self._slot("user"))

    def as_file_change(self) -> FileChange:
        """`data.file` — Files triggers."""
        return FileChange(self._slot("file"))

    def as_payment(self) -> PaymentFact:
        """`data.payment` — Payments triggers.

        On ``payments.order.*`` it is the provider callback that changed the order.
        """
        return PaymentFact(self._slot("payment"))

    def as_payment_order(self) -> PaymentOrderEvent:
        """`data.order` — Payments order triggers (``payments.order.*``).

        The order as stored after the change; de-duplicate on
        ``order_event_id``. :meth:`as_payment` still returns the callback.
        """
        return PaymentOrderEvent(self._slot("order"))

    def as_scheduled_task(self) -> ScheduledTaskInfo:
        """`data.task` — a scheduler task fire."""
        return ScheduledTaskInfo(self._slot("task"))

    def as_ai_usage(self) -> AiUsageEvent:
        """`data.ai` — AI triggers."""
        return AiUsageEvent(self._slot("ai"))

    def payload(self) -> dict[str, Any] | None:
        """`data.payload` — the caller's JSON (manual invoke) or a task's static payload."""
        value = self.data.get("payload")
        return value if isinstance(value, dict) else None

    # -- calling Norbix back -------------------------------------------------

    def client_options(self) -> dict[str, Any]:
        """Keyword arguments for :class:`norbix_python.Norbix` / `AsyncNorbix` as the run-as user.

        `project_id`, `account_id`, `env`, `region`, `bearer_token` (the run-as
        token) and `base_url_hub` / `base_url_api` (the deployment the event came
        from). Keys without a value in the envelope are left out, so
        `Norbix(**event.client_options())` is enough.
        """
        context = self.context
        options: dict[str, Any] = {
            "project_id": context.project_id,
            "account_id": context.account_id,
            "env": context.environment,
            "region": context.region,
            "bearer_token": context.run_as.access_token,
            "base_url_hub": context.hub_url,
            "base_url_api": context.api_url,
        }
        return {key: value for key, value in options.items() if value}


def parse_function_event(raw: str | bytes | bytearray | dict[str, Any]) -> FunctionEvent:
    """Read the envelope a cloud function received.

    `raw` is the JSON text (or bytes) of the request body, or the already
    decoded object your platform hands you (a Lambda `event`). Raises
    :class:`NorbixFunctionEventError` when it is not an object, not JSON, or
    not `specVersion` "1".
    """
    if isinstance(raw, (bytes, bytearray)):
        raw = raw.decode("utf-8")
    if isinstance(raw, str):
        try:
            decoded: Any = json.loads(raw)
        except ValueError as exc:
            raise NorbixFunctionEventError(f"The function event is not JSON: {exc}") from exc
    else:
        decoded = raw
    if not isinstance(decoded, dict):
        raise NorbixFunctionEventError(
            f"The function event must be a JSON object, got {type(decoded).__name__}."
        )
    spec_version = decoded.get("specVersion")
    if spec_version != FUNCTION_EVENT_SPEC_VERSION:
        raise NorbixFunctionEventError(
            f"Unknown function event specVersion {spec_version!r}; "
            f"this SDK reads {FUNCTION_EVENT_SPEC_VERSION!r}. Upgrade the SDK or check the sender."
        )
    return FunctionEvent(decoded)


__all__ = [
    "FUNCTION_EVENT_SPEC_VERSION",
    "AiUsageEvent",
    "Caller",
    "DatabaseRecordChange",
    "FileChange",
    "FunctionContext",
    "FunctionEvent",
    "NorbixFunctionEventError",
    "PaymentFact",
    "PaymentOrder",
    "PaymentOrderEvent",
    "RunAs",
    "ScheduledTaskInfo",
    "UserChange",
    "parse_function_event",
]
