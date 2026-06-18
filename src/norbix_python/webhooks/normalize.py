from __future__ import annotations

from typing import Any

from .models import (
    FileDeleted,
    FileResourceRef,
    Mutation,
    UserDto,
    UserInvited,
    WebhookEntityRef,
    WebhookEnvelope,
    WebhookEventMetadata,
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

    return envelope.data, metadata
