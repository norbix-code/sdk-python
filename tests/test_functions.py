"""The cloud-function event envelope (Code.Functions.md §4).

`parse_function_event` reads the JSON a function receives, one sample per
source, and the typed views read the slot of `data` for that source. A bad
`specVersion` or a non-object is refused. `client_options()` must build a
`Norbix` that calls the deployment of the envelope as the run-as user — checked
against a capture transport, never a gateway.
"""

from __future__ import annotations

import json
from typing import Any

import httpx
import pytest

from norbix_python import (
    FunctionEvent,
    Norbix,
    NorbixError,
    NorbixFunctionEventError,
    parse_function_event,
)
from norbix_python.functions import FUNCTION_EVENT_SPEC_VERSION

from .helpers import CaptureTransport

CONTEXT: dict[str, Any] = {
    "accountId": "acc_1",
    "projectId": "prj_1",
    "environment": "TEST",
    "region": "nb-eu-germany",
    "hubUrl": "https://hub.example.test",
    "apiUrl": "https://api.example.test",
    "echoUrl": "https://api.example.test/v3/echo",
    "triggerId": "trg_1",
    "correlationId": "corr_1",
    "caller": {"userId": "usr_caller", "email": "ada@example.test", "kind": "User"},
    "runAs": {"userId": "usr_svc", "accessToken": "run-as-token", "expiresAt": "2026-10-12T08:15:00Z"},
}


def envelope(source: str, event: str, data: dict[str, Any], **extra: Any) -> dict[str, Any]:
    return {
        "specVersion": "1",
        "id": "dlv_1",
        "eventId": "evt_1",
        "event": event,
        "source": source,
        "createdOn": "2026-10-12T08:00:00Z",
        "context": CONTEXT,
        "data": data,
        **extra,
    }


DATABASE = envelope(
    "database",
    "database.record.updated",
    {
        "database": {
            "collection": "orders",
            "schemaId": "sch_1",
            "schemaVersion": 3,
            "recordId": "6ac54a59212c29912eaddd81",
            "old": {"_id": "6ac54a59212c29912eaddd81", "status": "new"},
            "new": {"_id": "6ac54a59212c29912eaddd81", "status": "processing"},
            "truncated": False,
        }
    },
    config={"acceptStatus": "processing", "imageWidth": 568},
)


# --- parsing ------------------------------------------------------------------


def test_parse_reads_json_text_bytes_and_a_decoded_object() -> None:
    text = json.dumps(DATABASE)
    for raw in (text, text.encode("utf-8"), DATABASE):
        event = parse_function_event(raw)
        assert isinstance(event, FunctionEvent)
        assert event.spec_version == FUNCTION_EVENT_SPEC_VERSION == "1"
        assert event.id == "dlv_1"
        assert event.event_id == "evt_1"
        assert event.event == "database.record.updated"
        assert event.source == "database"
        assert event.created_on == "2026-10-12T08:00:00Z"
        assert event.config == {"acceptStatus": "processing", "imageWidth": 568}
    assert parse_function_event(DATABASE).raw is DATABASE


def test_context_is_typed() -> None:
    context = parse_function_event(DATABASE).context
    assert context.account_id == "acc_1"
    assert context.project_id == "prj_1"
    assert context.environment == "TEST"
    assert context.region == "nb-eu-germany"
    assert context.hub_url == "https://hub.example.test"
    assert context.api_url == "https://api.example.test"
    assert context.echo_url == "https://api.example.test/v3/echo"
    assert context.trigger_id == "trg_1"
    assert context.task_id is None
    assert context.correlation_id == "corr_1"
    assert context.caller is not None
    assert (context.caller.user_id, context.caller.email, context.caller.kind) == ("usr_caller", "ada@example.test", "User")
    assert context.run_as.user_id == "usr_svc"
    assert context.run_as.access_token == "run-as-token"
    assert context.run_as.expires_at == "2026-10-12T08:15:00Z"
    assert context.raw is CONTEXT


@pytest.mark.parametrize(
    "raw",
    [
        {**DATABASE, "specVersion": "2"},
        {**DATABASE, "specVersion": 1},
        {k: v for k, v in DATABASE.items() if k != "specVersion"},
    ],
    ids=["other-version", "number-not-text", "missing"],
)
def test_bad_spec_version_is_refused(raw: dict[str, Any]) -> None:
    with pytest.raises(NorbixFunctionEventError) as exc:
        parse_function_event(raw)
    assert "specVersion" in str(exc.value)
    assert exc.value.code == "FUNCTION_EVENT_INVALID"
    assert isinstance(exc.value, NorbixError)


@pytest.mark.parametrize("raw", ["not json", "[1, 2]", "42"], ids=["not-json", "list", "number"])
def test_non_object_is_refused(raw: str) -> None:
    with pytest.raises(NorbixFunctionEventError):
        parse_function_event(raw)


# --- one sample per source ----------------------------------------------------


def test_database_record_change() -> None:
    change = parse_function_event(DATABASE).as_database_record_change()
    assert change.collection == "orders"
    assert change.schema_id == "sch_1"
    assert change.schema_version == 3
    assert change.record_id == "6ac54a59212c29912eaddd81"
    assert change.old == {"_id": "6ac54a59212c29912eaddd81", "status": "new"}
    assert change.new == {"_id": "6ac54a59212c29912eaddd81", "status": "processing"}
    assert change.truncated is False
    assert change.old_ref is None and change.new_ref is None


def test_database_insert_has_no_old_and_a_truncated_change_carries_refs() -> None:
    inserted = envelope("database", "database.record.inserted", {"database": {"collection": "orders", "new": {"a": 1}}})
    change = parse_function_event(inserted).as_database_record_change()
    assert change.old is None
    assert change.new == {"a": 1}

    ref = {"kind": "document", "projectId": "prj_1", "databaseIntegrationId": "int_db", "schemaId": "sch_1", "externalId": "rec_1"}
    big = envelope("database", "database.record.updated", {"database": {"collection": "orders", "truncated": True, "oldRef": ref, "newRef": ref}})
    change = parse_function_event(big).as_database_record_change()
    assert change.truncated is True
    assert change.old is None and change.new is None
    assert change.old_ref == ref and change.new_ref == ref


def test_user_change() -> None:
    raw = envelope(
        "membership",
        "membership.user.updated",
        {"user": {"userId": "usr_1", "old": {"email": "a@x.test"}, "new": {"email": "b@x.test"}}},
    )
    change = parse_function_event(raw).as_user_change()
    assert change.user_id == "usr_1"
    assert change.old == {"email": "a@x.test"}
    assert change.new == {"email": "b@x.test"}


def test_file_change() -> None:
    uploaded = envelope("files", "files.file.uploaded", {"file": {"new": {"path": "img/a.png", "size": 10}, "path": "img/a.png"}})
    change = parse_function_event(uploaded).as_file_change()
    assert change.old is None
    assert change.new == {"path": "img/a.png", "size": 10}
    assert change.path == "img/a.png"


def test_payment_fact() -> None:
    raw = envelope(
        "payments",
        "payments.webhook.received",
        {
            "payment": {
                "integrationId": "int_pay",
                "provider": "Stripe",
                "providerEventId": "evt_stripe",
                "eventName": "payment_intent.succeeded",
                "status": "succeeded",
                "amountMinor": 1999,
                "currency": "EUR",
                "externalIds": {"paymentIntentId": "pi_1"},
                "occurredOn": "2026-10-12T07:59:00Z",
                "receivedOn": "2026-10-12T08:00:00Z",
            }
        },
    )
    event = parse_function_event({**raw, "context": {**CONTEXT, "caller": None}})
    assert event.context.caller is None
    payment = event.as_payment()
    assert payment.integration_id == "int_pay"
    assert payment.provider == "Stripe"
    assert payment.provider_event_id == "evt_stripe"
    assert payment.event_name == "payment_intent.succeeded"
    assert payment.status == "succeeded"
    assert payment.amount_minor == 1999
    assert payment.currency == "EUR"
    assert payment.external_ids == {"paymentIntentId": "pi_1"}
    assert payment.occurred_on == "2026-10-12T07:59:00Z"
    assert payment.received_on == "2026-10-12T08:00:00Z"


ORDER_EVENT: dict[str, Any] = {
    "orderEventId": "ord_2ToIiRM03X63TZaJ2dJdv2:2",
    "event": "payments.order.paid",
    "from": "CheckoutStarted",
    "to": "Paid",
    "reason": "paid in attempt 1",
    "order": {
        "id": "ord_2ToIiRM03X63TZaJ2dJdv2",
        "env": "PROD",
        "buyerUserId": "usr_1szWVIyZFBV8HfvC4SfVw",
        "merchantReference": "ad-1042-promo-1",
        "currency": "EUR",
        "priceVersion": "2026-10-01",
        "lines": [{"sku": "star-day", "title": "Star × day", "quantity": 21, "unitAmountMinor": 30, "amountMinor": 630}],
        "totalMinor": 630,
        "metadata": {"adId": "ad_1042"},
        "status": "Paid",
        "checkouts": [],
        "settledMinor": 630,
        "refundedMinor": 0,
        "providerPaymentId": "mnt-1",
        "mismatches": [],
    },
    "payment": {
        "integrationId": "int_montonio",
        "provider": "Montonio",
        "providerEventId": "order:mnt-1:PAID",
        "orderId": "ord_2ToIiRM03X63TZaJ2dJdv2",
        "eventName": "order.paid",
        "status": "Succeeded",
        "amountMinor": 630,
        "currency": "EUR",
        "receivedOn": "2026-10-19T09:54:43Z",
    },
}


def test_payment_order_event_and_as_payment_is_its_callback() -> None:
    raw = envelope("payments", "payments.order.paid", {"order": ORDER_EVENT, "payment": ORDER_EVENT["payment"]})
    event = parse_function_event(raw)
    order_event = event.as_payment_order()
    assert order_event.order_event_id == "ord_2ToIiRM03X63TZaJ2dJdv2:2"
    assert (order_event.event, order_event.from_, order_event.to) == ("payments.order.paid", "CheckoutStarted", "Paid")
    assert order_event.reason == "paid in attempt 1"
    order = order_event.order
    assert order.id == "ord_2ToIiRM03X63TZaJ2dJdv2"
    assert order.status == "Paid"
    assert order.settled_minor == 630
    assert order.total_minor == 630
    assert order.refunded_minor == 0
    assert order.metadata == {"adId": "ad_1042"}
    assert order.lines[0]["quantity"] == 21
    assert order.checkouts == []
    assert order_event.payment is not None
    assert order_event.payment.provider == "Montonio"
    payment = event.as_payment()
    assert payment.provider_event_id == "order:mnt-1:PAID"
    assert payment.order_id == "ord_2ToIiRM03X63TZaJ2dJdv2"


def test_as_payment_order_is_refused_for_a_plain_payment_event() -> None:
    event = parse_function_event(
        envelope("payments", "payments.webhook.received", {"payment": ORDER_EVENT["payment"]})
    )
    with pytest.raises(NorbixFunctionEventError) as exc:
        event.as_payment_order()
    assert "data.order" in str(exc.value)


def test_ai_usage() -> None:
    raw = envelope("ai", "ai.credits.warning", {"ai": {"payload": {"used": 90, "limit": 100}, "targetUserId": "usr_9"}})
    usage = parse_function_event(raw).as_ai_usage()
    assert usage.payload == {"used": 90, "limit": 100}
    assert usage.target_user_id == "usr_9"


def test_scheduled_task_and_its_static_payload() -> None:
    raw = envelope(
        "scheduler",
        "scheduler.task.fired",
        {"task": {"taskId": "tsk_1", "name": "nightly", "firedAt": "2026-10-12T02:00:00Z"}, "payload": {"mode": "full"}},
    )
    event = parse_function_event({**raw, "context": {**CONTEXT, "triggerId": None, "taskId": "tsk_1"}})
    assert event.context.trigger_id is None
    assert event.context.task_id == "tsk_1"
    task = event.as_scheduled_task()
    assert (task.task_id, task.name, task.fired_at) == ("tsk_1", "nightly", "2026-10-12T02:00:00Z")
    assert event.payload() == {"mode": "full"}


def test_manual_invoke_payload_and_no_config() -> None:
    raw = envelope("manual", "manual.invoke", {"payload": {"orderId": "o1", "dryRun": True}})
    event = parse_function_event(raw)
    assert event.payload() == {"orderId": "o1", "dryRun": True}
    assert event.config is None
    assert event.data == {"payload": {"orderId": "o1", "dryRun": True}}


def test_a_view_of_a_missing_slot_is_refused() -> None:
    event = parse_function_event(envelope("files", "files.file.deleted", {"file": {"old": {"path": "a"}}}))
    with pytest.raises(NorbixFunctionEventError) as exc:
        event.as_database_record_change()
    assert "data.database" in str(exc.value)
    assert event.payload() is None


# --- calling Norbix back --------------------------------------------------------


def test_client_options_are_the_norbix_constructor_kwargs() -> None:
    options = parse_function_event(DATABASE).client_options()
    assert options == {
        "project_id": "prj_1",
        "account_id": "acc_1",
        "env": "TEST",
        "region": "nb-eu-germany",
        "bearer_token": "run-as-token",
        "base_url_hub": "https://hub.example.test",
        "base_url_api": "https://api.example.test",
    }


def test_client_options_leave_out_what_the_envelope_has_not() -> None:
    bare = {**DATABASE, "context": {"projectId": "prj_1", "hubUrl": "https://hub.example.test", "apiUrl": "https://api.example.test", "runAs": {"accessToken": "t"}}}
    assert parse_function_event(bare).client_options() == {
        "project_id": "prj_1",
        "bearer_token": "t",
        "base_url_hub": "https://hub.example.test",
        "base_url_api": "https://api.example.test",
    }


def test_a_client_built_from_the_event_calls_the_deployment_as_the_run_as_user() -> None:
    event = parse_function_event(DATABASE)
    transport = CaptureTransport()
    norbix = Norbix(**event.client_options(), http_client=httpx.Client(transport=transport))

    norbix.hub.code.get_code_function_runs(triggerId=event.context.trigger_id)
    assert transport.last_request is not None
    hub = httpx.URL(transport.last_request["url"])
    assert f"{hub.scheme}://{hub.host}" == "https://hub.example.test"
    assert hub.path == "/v3/code/functions/runs"
    assert transport.last_request["headers"]["authorization"] == "Bearer run-as-token"
    assert transport.last_request["headers"]["norbix-env"] == "TEST"
    assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"

    norbix.api.database.find("orders")
    api = httpx.URL(transport.last_request["url"])
    assert f"{api.scheme}://{api.host}" == "https://api.example.test"
    assert norbix.get_env() == "TEST"
