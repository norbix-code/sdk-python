from __future__ import annotations

import json
import time

import pytest

from norbix_python.webhooks import (
    NORBIX_WEBHOOK_EVENT_NAMES,
    AsyncNorbixWebhookReceiver,
    Mutation,
    NorbixWebhookEvents,
    NorbixWebhookReceiver,
    NorbixWebhookSignatureError,
    UserDto,
    compute_signature,
)


def _body(event: str, data: dict[str, object], **extra: object) -> str:
    payload = {
        "id": extra.get("id", "dlv_1"),
        "event": event,
        "createdOn": "2026-01-01T00:00:00Z",
        "accountId": extra.get("accountId", "acc_1"),
        "projectId": extra.get("projectId", "pr_1"),
        "triggerId": extra.get("triggerId", "trg_1"),
        "data": data,
    }
    return json.dumps(payload)


def test_registered_payload_is_user_entity() -> None:
    user = {"id": "usr_1", "userName": "alice", "status": "registered"}
    receiver = NorbixWebhookReceiver()
    captured: dict[str, object] = {}

    @receiver.on(NorbixWebhookEvents.Membership.USER_REGISTERED)
    def handle(payload: UserDto, event: object) -> None:  # noqa: ANN401
        captured["payload"] = payload
        captured["event"] = event

    result = receiver.handle(
        raw_body=_body("membership.user.registered", {"id": "usr_1", "to": user}),
        headers={"X-Norbix-Integration": "whi_1"},
    )

    assert result.handled is True
    payload = captured["payload"]
    assert isinstance(payload, UserDto)
    assert payload.user_name == "alice"
    event = captured["event"]
    assert event.metadata.user is not None  # type: ignore[attr-defined]
    assert event.metadata.user.id == "usr_1"  # type: ignore[attr-defined]
    assert event.integration_id == "whi_1"  # type: ignore[attr-defined]


def test_updated_payload_is_mutation() -> None:
    receiver = NorbixWebhookReceiver()
    captured: dict[str, object] = {}
    frm = {"id": "usr_1", "email": "old@x.io"}
    to = {"id": "usr_1", "email": "new@x.io"}

    @receiver.on(NorbixWebhookEvents.Membership.USER_UPDATED)
    def handle(payload: Mutation[UserDto], event: object) -> None:  # noqa: ANN401
        captured["payload"] = payload

    receiver.handle(
        raw_body=_body("membership.user.updated", {"id": "usr_1", "from": frm, "to": to}),
        headers={},
    )

    payload = captured["payload"]
    assert isinstance(payload, Mutation)
    assert payload.from_.email == "old@x.io"  # type: ignore[union-attr]
    assert payload.to.email == "new@x.io"  # type: ignore[union-attr]


def test_verified_payload_is_user_no_from_to() -> None:
    receiver = NorbixWebhookReceiver()
    captured: dict[str, object] = {}
    user = {"id": "usr_1", "status": "verified"}

    receiver.on(
        NorbixWebhookEvents.Membership.USER_VERIFIED,
        lambda payload, event: captured.__setitem__("payload", payload),
    )
    receiver.handle(
        raw_body=_body("membership.user.verified", {"id": "usr_1", "from": None, "to": user}),
        headers={},
    )

    payload = captured["payload"]
    assert isinstance(payload, UserDto)
    assert payload.status == "verified"


def test_record_inserted_payload_is_document_with_metadata() -> None:
    receiver = NorbixWebhookReceiver()
    captured: dict[str, object] = {}
    doc = {"id": "rec_1", "email": "a@b.io"}

    receiver.on(
        NorbixWebhookEvents.Database.RECORD_INSERTED,
        lambda payload, event: captured.update(payload=payload, event=event),
    )
    receiver.handle(
        raw_body=_body(
            "database.record.inserted",
            {
                "schemaName": "users",
                "integrationId": "int_1",
                "id": "rec_1",
                "document": doc,
                "schema": {"id": "sch_1"},
            },
        ),
        headers={},
    )

    assert captured["payload"] == doc
    event = captured["event"]
    assert event.metadata.schema.id == "sch_1"  # type: ignore[attr-defined]
    assert event.metadata.schema.name == "users"  # type: ignore[attr-defined]
    assert event.metadata.record.id == "rec_1"  # type: ignore[attr-defined]


def test_records_inserted_payload_is_list() -> None:
    receiver = NorbixWebhookReceiver()
    captured: dict[str, object] = {}
    docs = [{"id": "r1"}, {"id": "r2"}]

    receiver.on(
        NorbixWebhookEvents.Database.RECORDS_INSERTED,
        lambda payload, event: captured.update(payload=payload, event=event),
    )
    receiver.handle(
        raw_body=_body(
            "database.records.inserted",
            {"schemaName": "users", "ids": ["r1", "r2"], "documents": docs},
        ),
        headers={},
    )

    assert captured["payload"] == docs
    assert captured["event"].metadata.records.ids == ["r1", "r2"]  # type: ignore[attr-defined]


def test_on_all_runs_in_addition_to_on() -> None:
    receiver = NorbixWebhookReceiver()
    calls: list[str] = []

    receiver.on(
        NorbixWebhookEvents.Membership.USER_REGISTERED,
        lambda payload, event: calls.append("typed"),
    )
    receiver.on_all(
        NORBIX_WEBHOOK_EVENT_NAMES,
        lambda envelope, ctx: calls.append(f"all:{envelope.event}"),
    )

    receiver.handle(
        raw_body=_body("membership.user.registered", {"id": "u", "to": {"id": "u"}}),
        headers={},
    )

    assert calls == ["typed", "all:membership.user.registered"]


def test_env_secret_drives_verification(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("NORBIX_WEBHOOK_SIGNING_SECRET", "env_secret")
    receiver = NorbixWebhookReceiver()
    body = _body("files.file.uploaded", {"integrationId": "int_1", "file": {"path": "/a.png"}})
    ts = str(int(time.time()))
    sig = compute_signature("env_secret", ts, body)

    result = receiver.handle(
        raw_body=body,
        headers={"X-Norbix-Signature": sig, "X-Norbix-Timestamp": ts},
    )
    assert result.verified is True


def test_bad_signature_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    receiver = NorbixWebhookReceiver(secret="whsec")
    with pytest.raises(NorbixWebhookSignatureError):
        receiver.handle(
            raw_body='{"id":"x","event":"files.file.uploaded","data":{}}',
            headers={"X-Norbix-Signature": "sha256=dead", "X-Norbix-Timestamp": str(int(time.time()))},
        )


def test_project_guard_rejects_mismatch() -> None:
    receiver = NorbixWebhookReceiver(project_id="pr_expected")
    with pytest.raises(NorbixWebhookSignatureError):
        receiver.handle(
            raw_body=_body("files.file.uploaded", {}, projectId="pr_other"),
            headers={},
        )


def test_async_receiver_awaits_async_handler() -> None:
    import asyncio

    receiver = AsyncNorbixWebhookReceiver()
    captured: dict[str, object] = {}

    @receiver.on(NorbixWebhookEvents.Membership.USER_REGISTERED)
    async def handle(payload: UserDto, event: object) -> None:  # noqa: ANN401
        captured["payload"] = payload

    async def run() -> None:
        await receiver.handle(
            raw_body=_body(
                "membership.user.registered",
                {"id": "u", "to": {"id": "u", "email": "x@y.io"}},
            ),
            headers={},
        )

    asyncio.run(run())
    assert isinstance(captured["payload"], UserDto)
    assert captured["payload"].email == "x@y.io"  # type: ignore[union-attr]
