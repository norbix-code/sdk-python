"""Trigger "order" and "break on failure" reach the gateway on every save.

The four save methods send the caller's map as the body, so `trigger.order`
and `trigger.breakOnError` must arrive exactly as given (gateway task
trigger-order-break: the fields were added to every trigger kind).
"""

import json

import pytest

from tests.helpers import make_client

TRIGGER = {
    "name": "welcome first",
    "isEnabled": True,
    "order": 0,
    "breakOnError": True,
    "action": {"type": "WebhookCall"},
}


@pytest.mark.parametrize(
    ("module", "method", "kind", "path"),
    [
        ("membership", "save_membership_trigger", "Membership", "/membership/triggers"),
        ("database", "save_schema_trigger", "Schema", "/database/schemas/triggers"),
        ("files", "save_files_trigger", "Files", "/files/triggers"),
        ("payments", "save_payments_trigger", "Payments", "/payments/triggers"),
    ],
)
def test_save_trigger_sends_order_and_break_on_error(module: str, method: str, kind: str, path: str) -> None:
    client, transport = make_client(account_id=None)

    getattr(getattr(client.hub, module), method)(trigger={"type": kind, **TRIGGER})

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert transport.last_request["url"].endswith(path)
    sent = json.loads(transport.last_request["body"])["trigger"]
    assert {k: sent[k] for k in ("type", "order", "breakOnError")} == {
        "type": kind,
        "order": 0,
        "breakOnError": True,
    }
