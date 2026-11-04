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
    assert callable(client.hub.triggers.check_trigger_execution_identity)
    assert callable(client.hub.triggers.get_trigger_runs)
    assert callable(client.hub.triggers.get_trigger_run)
    assert callable(client.hub.triggers.get_trigger_definition)
    assert callable(client.hub.triggers.test_trigger_pre_execute_code)


def test_get_triggers_needing_attention_hits_the_route_with_query_values() -> None:
    client, transport = make_client()
    client.hub.triggers.get_triggers_needing_attention(triggerType="Schema")

    assert transport.last_request is not None
    assert transport.last_request["method"] == "GET"
    url = urlparse(transport.last_request["url"])
    assert url.path == "/v3/triggers/attention"
    assert parse_qs(url.query) == {"triggerType": ["Schema"]}
    assert transport.last_request["body"] == ""
    assert transport.last_request["headers"]["norbix-project-id"] == "test-project"


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
    ("save_ai_project_trigger", "/v3/ai/triggers", lambda c, b: c.hub.ai.save_ai_project_trigger(**b)),
]

CODE_ACTION = {
    "type": "Code",
    "functionRef": {"integrationId": "int_lambda", "functionId": "notify-sales", "qualifier": "live"},
    "invocationType": "Async",
    "config": '{"source": "python"}',
}
WORKFLOW_ACTION = {"type": "Workflow", "workflowRef": "wf_onboard", "payload": {"source": "python"}}


@pytest.mark.parametrize(("name", "path", "call"), TRIGGER_SAVES, ids=[c[0] for c in TRIGGER_SAVES])
@pytest.mark.parametrize("action", [CODE_ACTION, WORKFLOW_ACTION], ids=["Code", "Workflow"])
def test_trigger_save_sends_code_and_workflow_actions_as_they_are(
    name: str, path: str, call: Callable[[Any, dict[str, Any]], Any], action: dict[str, Any]
) -> None:
    # A Code action names the function (functionRef) and how to call it; a
    # Workflow action names the workflow (workflowRef) and its payload. Who runs
    # is the trigger's executionIdentityId, never a runAsUserId on the action.
    client, transport = make_client()
    call(client, {"trigger": {"name": "run " + action["type"], "executionIdentityId": "usr_1", "action": action}})

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert urlparse(transport.last_request["url"]).path == path
    body = json.loads(transport.last_request["body"])
    assert body["trigger"]["action"] == action
    assert "runAsUserId" not in body["trigger"]["action"]
    assert body["trigger"]["executionIdentityId"] == "usr_1"


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


@pytest.mark.parametrize("action_type", ["Email", "Push", "Sms"])
def test_membership_trigger_save_sends_the_trigger_subject_audience(action_type: str) -> None:
    # A saved trigger names no person: only the audience goes out, and the SDK
    # passes it through as-is. The gateway fills the subject fields when it fires.
    action = {
        "type": action_type,
        "integrationId": INTEGRATION_ID,
        "templateId": TEMPLATE_ID,
        "deliverySettings": {"recipientsSourceType": "TriggerSubject"},
    }
    client, transport = make_client()
    client.hub.membership.save_membership_trigger(
        trigger={"type": "Membership", "name": "welcome", "when": "OnRegistered", "action": action}
    )

    assert transport.last_request is not None
    assert urlparse(transport.last_request["url"]).path == "/v3/membership/triggers"
    assert json.loads(transport.last_request["body"])["trigger"]["action"] == action


def test_get_trigger_runs_sends_the_filters_on_the_query() -> None:
    client, transport = make_client()
    client.hub.triggers.get_trigger_runs(triggerType="Schema", triggerId="trg_1", status="failed")

    assert transport.last_request is not None
    assert transport.last_request["method"] == "GET"
    url = urlparse(transport.last_request["url"])
    assert url.path == "/v3/triggers/runs"
    assert parse_qs(url.query) == {"triggerType": ["Schema"], "triggerId": ["trg_1"], "status": ["failed"]}


def test_get_trigger_run_puts_the_id_in_the_path_and_keeps_the_type() -> None:
    client, transport = make_client()
    client.hub.triggers.get_trigger_run("trr_1", triggerType="Membership")

    assert transport.last_request is not None
    url = urlparse(transport.last_request["url"])
    assert url.path == "/v3/triggers/runs/trr_1"
    assert parse_qs(url.query) == {"triggerType": ["Membership"]}


def test_check_trigger_execution_identity_posts_the_action() -> None:
    client, transport = make_client()
    client.hub.triggers.check_trigger_execution_identity(triggerType="Schema", action={"type": "Email"})

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert urlparse(transport.last_request["url"]).path == "/v3/triggers/execution-identity/check"
    body = json.loads(transport.last_request["body"])
    assert body["triggerType"] == "Schema"
    assert body["action"] == {"type": "Email"}


def test_get_trigger_definition_puts_the_id_in_the_path_and_the_type_and_schema_on_the_query() -> None:
    client, transport = make_client()
    client.hub.triggers.get_trigger_definition("trg_1", triggerType="Schema", schemaId="sch_1")

    assert transport.last_request is not None
    assert transport.last_request["method"] == "GET"
    url = urlparse(transport.last_request["url"])
    assert url.path == "/v3/triggers/trg_1/definition"
    assert parse_qs(url.query) == {"triggerType": ["Schema"], "schemaId": ["sch_1"]}
    assert transport.last_request["body"] == ""


def test_test_trigger_pre_execute_code_posts_the_code_and_the_records_as_text() -> None:
    client, transport = make_client()
    client.hub.triggers.test_trigger_pre_execute_code(
        code='return New.status == "published";',
        triggerType="Schema",
        newRecord='{"status":"published"}',
        oldRecord='{"status":"draft"}',
        eventKind="Updated",
        eventName="database.record.updated",
    )

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert urlparse(transport.last_request["url"]).path == "/v3/triggers/pre-execute-code/test"
    assert json.loads(transport.last_request["body"]) == {
        "code": 'return New.status == "published";',
        "triggerType": "Schema",
        "newRecord": '{"status":"published"}',
        "oldRecord": '{"status":"draft"}',
        "eventKind": "Updated",
        "eventName": "database.record.updated",
    }


def test_execution_identities_list_and_create() -> None:
    client, transport = make_client()
    client.hub.membership.get_execution_identities()
    assert transport.last_request is not None
    assert transport.last_request["method"] == "GET"
    assert urlparse(transport.last_request["url"]).path == "/v3/membership/execution-identities"

    client.hub.membership.create_execution_identity(name="Orders bot", roleIds=["Editor"])
    assert transport.last_request["method"] == "POST"
    body = json.loads(transport.last_request["body"])
    assert body["name"] == "Orders bot"
    assert body["roleIds"] == ["Editor"]


def test_async_trigger_runs_and_identities_hit_their_routes() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    async def run() -> None:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        await client.hub.triggers.get_trigger_runs(triggerType="Schema", triggerId="trg_1")
        await client.hub.triggers.get_trigger_run("trr_1", triggerType="Schema")
        await client.hub.triggers.check_trigger_execution_identity(triggerType="Schema", action={"type": "Email"})
        await client.hub.triggers.get_trigger_definition("trg_1", triggerType="Files")
        await client.hub.triggers.test_trigger_pre_execute_code(code="return true;", triggerType="Files")
        await client.hub.membership.get_execution_identities()
        await client.hub.membership.create_execution_identity(name="Orders bot", roleIds=[])
        await client.hub.ai.save_ai_project_trigger(trigger={"type": "Ai", "when": "OnQuotaExhausted", "name": "q", "action": {"type": "Email"}})
        await client.hub.ai.get_ai_project_triggers()
        await client.hub.ai.get_ai_project_trigger("trg_1")
        await client.hub.ai.enable_ai_project_trigger("trg_1")
        await client.hub.ai.disable_ai_project_trigger("trg_1")
        await client.hub.ai.delete_ai_project_trigger("trg_1")

    asyncio.run(run())
    assert [(r.method, r.url.path) for r in seen] == [
        ("GET", "/v3/triggers/runs"),
        ("GET", "/v3/triggers/runs/trr_1"),
        ("POST", "/v3/triggers/execution-identity/check"),
        ("GET", "/v3/triggers/trg_1/definition"),
        ("POST", "/v3/triggers/pre-execute-code/test"),
        ("GET", "/v3/membership/execution-identities"),
        ("POST", "/v3/membership/execution-identities"),
        ("POST", "/v3/ai/triggers"),
        ("GET", "/v3/ai/triggers"),
        ("GET", "/v3/ai/triggers/trg_1"),
        ("PATCH", "/v3/ai/triggers/trg_1/enable"),
        ("PATCH", "/v3/ai/triggers/trg_1/disable"),
        ("DELETE", "/v3/ai/triggers/trg_1"),
    ]
