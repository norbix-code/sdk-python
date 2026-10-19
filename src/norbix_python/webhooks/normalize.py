from __future__ import annotations

from typing import Any

from ..functions import PaymentFact, PaymentOrderEvent
from .models import (
    FileDeleted,
    FileResourceRef,
    Mutation,
    UserDto,
    UserInvited,
    WebhookEntityRef,
    WebhookEnvelope,
    WebhookEventMetadata,
    WebhookOrderRef,
    WebhookPaymentRef,
    WebhookRecordIds,
    WebhookSchemaInfo,
)


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def normalize_webhook(envelope: WebhookEnvelope) -> tuple[Any, WebhookEventMetadata]:
    """Turn a raw envelope into ``(payload, metadata)``.

    - Entity events   -> ``payload`` is the entity (user / document / file).
    - Mutation events -> ``payload`` is a :class:`Mutation` (``from`` / ``to``).
    - Batch events    -> ``payload`` is the list.

    Wrapper ids (record id, schema, user id, ...) are moved onto ``metadata``.
    Unknown events fall back to ``payload = envelope.data``, ``metadata = {}``.
    """
    event = envelope.event
    data = _as_dict(envelope.data)
    metadata = WebhookEventMetadata()

    if event.startswith("database."):
        schema_name = data.get("schemaName")
        if isinstance(schema_name, str):
            schema = _as_dict(data.get("schema"))
            schema_id = schema.get("id") if isinstance(schema.get("id"), str) else None
            metadata.schema = WebhookSchemaInfo(id=schema_id, name=schema_name)
        if isinstance(data.get("integrationId"), str):
            metadata.integration_id = data["integrationId"]
        if isinstance(data.get("id"), str):
            metadata.record = WebhookEntityRef(id=data["id"])
        if isinstance(data.get("ids"), list):
            metadata.records = WebhookRecordIds(ids=list(data["ids"]))

        if event in ("database.record.inserted", "database.record.deleted"):
            return data.get("document"), metadata
        if event in ("database.record.updated", "database.record.replaced"):
            return Mutation[Any](**{"from": data.get("from"), "to": data.get("to")}), metadata
        if event == "database.records.inserted":
            return data.get("documents") or [], metadata
        return envelope.data, metadata

    if event.startswith("membership."):
        if isinstance(data.get("id"), str):
            metadata.user = WebhookEntityRef(id=data["id"])

        if event in (
            "membership.user.registered",
            "membership.user.verified",
            "membership.user.blocked",
            "membership.user.reactivated",
        ):
            return UserDto.model_validate(_as_dict(data.get("to"))), metadata
        if event == "membership.user.deleted":
            return UserDto.model_validate(_as_dict(data.get("from"))), metadata
        if event == "membership.user.updated":
            from_user = UserDto.model_validate(_as_dict(data.get("from")))
            to_user = UserDto.model_validate(_as_dict(data.get("to")))
            return Mutation[UserDto](**{"from": from_user, "to": to_user}), metadata
        if event == "membership.user.invited":
            return UserInvited(email=data.get("email")), metadata
        return envelope.data, metadata

    if event.startswith("files."):
        if isinstance(data.get("integrationId"), str):
            metadata.integration_id = data["integrationId"]
        if event == "files.file.uploaded":
            return FileResourceRef.model_validate(_as_dict(data.get("file"))), metadata
        if event == "files.file.deleted":
            return FileDeleted(path=data.get("path")), metadata
        return envelope.data, metadata

    if event.startswith("payments."):
        # payments.webhook.received: the whole data object IS the normalized
        # payment fact (the same shape as a Code function's ``data.payment``).
        # payments.order.*: the data is the order event; its ``payment`` is the
        # fact. Either way the provider ids are lifted onto metadata so a
        # handler can de-duplicate on them.
        is_order_event = event.startswith("payments.order.")
        fact = _as_dict(data.get("payment")) if is_order_event else data
        if isinstance(fact.get("integrationId"), str):
            metadata.integration_id = fact["integrationId"]
        if all(isinstance(fact.get(k), str) for k in ("provider", "providerEventId", "eventName")):
            metadata.payment = WebhookPaymentRef(
                provider=fact["provider"],
                providerEventId=fact["providerEventId"],
                eventName=fact["eventName"],
            )
        if is_order_event:
            order = _as_dict(data.get("order"))
            ids = (order.get("id"), data.get("orderEventId"), order.get("status"))
            if all(isinstance(v, str) for v in ids):
                metadata.order = WebhookOrderRef(
                    id=order["id"],
                    orderEventId=data["orderEventId"],
                    status=order["status"],
                )
            return PaymentOrderEvent(data), metadata
        return PaymentFact(data), metadata

    return envelope.data, metadata
