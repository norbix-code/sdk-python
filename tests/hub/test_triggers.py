from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix

from ..helpers import make_client

"""Triggers: the cross-module "needs attention" list, and the action shape that
every trigger save sends.

The gateway requires the provider ``integrationId`` on a trigger action, and
takes an optional ``language`` (template language) and ``initiatorId`` (who the
send is attributed to). The SDK passes the request through as-is, so these
tests pin that the three fields reach the wire under ``trigger.action``.
"""

INTEGRATION_ID = "int_1"
TEMPLATE_ID = "tpl_1"
INITIATOR_ID = "user_1"


def test_hub_triggers_module_surface() -> None:
    client, _ = make_client()
    assert callable(client.hub.triggers.get_triggers_needing_attention)


def test_get_triggers_needing_attention_hits_the_route_with_query_values() -> None:
    client, transport = make_client()
    client.hub.triggers.get_triggers_needing_attention(triggerType="Schema")

    assert transport.last_request is not None
    assert transport.last_request["method"] == "GET"
    url = urlparse(transport.last_request["url"])
    assert url.path == "/v3/triggers/attention"
    assert parse_qs(url.query) == {"triggerType": ["Schema"]}
    assert transport.last_request["body"] == ""
    assert transport.last_request["headers"]["x-cm-projectid"] == "test-project"


def test_async_get_triggers_needing_attention_hits_the_route() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"items": []})

    async def run() -> Any:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        try:
            return await client.hub.triggers.get_triggers_needing_attention(triggerType="Files")
        finally:
            await client.aclose()

    result = asyncio.run(run())

    assert result == {"items": []}
    assert [(r.method, urlparse(str(r.url)).path, urlparse(str(r.url)).query) for r in seen] == [
        ("GET", "/v3/triggers/attention", "triggerType=Files"),
    ]


# name, expected path, call — every trigger save in the hub.
SaveCase = tuple[str, str, Callable[[Any, dict[str, Any]], Any]]
TRIGGER_SAVES: list[SaveCase] = [
    ("save_schema_trigger", "/v3/database/schemas/triggers", lambda c, b: c.hub.database.save_schema_trigger(**b)),
    ("save_files_trigger", "/v3/files/triggers", lambda c, b: c.hub.files.save_files_trigger(**b)),
    ("save_membership_trigger", "/v3/membership/triggers", lambda c, b: c.hub.membership.save_membership_trigger(**b)),
    ("save_payments_trigger", "/v3/payments/triggers", lambda c, b: c.hub.payments.save_payments_trigger(**b)),
]


@pytest.mark.parametrize(("name", "path", "call"), TRIGGER_SAVES, ids=[c[0] for c in TRIGGER_SAVES])
@pytest.mark.parametrize("action_type", ["Email", "Push", "Sms"])
def test_trigger_save_sends_integration_language_and_initiator(
    name: str, path: str, call: Callable[[Any, dict[str, Any]], Any], action_type: str
) -> None:
    action = {
        "type": action_type,
        "integrationId": INTEGRATION_ID,
        "templateId": TEMPLATE_ID,
        "language": "de",
        "initiatorId": INITIATOR_ID,
    }
    client, transport = make_client()
    call(client, {"trigger": {"name": "welcome", "isEnabled": True, "action": action}})

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert urlparse(transport.last_request["url"]).path == path
    body = json.loads(transport.last_request["body"])
    assert body == {"trigger": {"name": "welcome", "isEnabled": True, "action": action}}
