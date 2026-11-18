from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

"""Matrix sections 06 AI · MCP, 07 AI · LLM integration and 08 AI chat, Hub
side, one case per route: every LLM and MCP integration route of
``client.hub.ai`` (the MCP ones are deprecated — save is refused with an
error code ending in -030 — but still served) and the AI tool routes of
``client.hub.account``. The developer AI chat routes (``/account/chat/*``) were
retired on 2026-11-18. Written in the AI cluster coverage
campaign (2026-11-18); the older cases in ``test_ai.py`` assert the verb and
the path but not the host, the query or the body.

Called sync and async. Each case asserts the host (hub), the verb, the exact
path, the query string and the JSON body, plus the key and project headers.
Field names are the gateway's (Hub.AI ``Integrations/{Llms,Mcps}/*.cs``,
``AiToolsBridge.cs``). Every call goes to a mock transport, so nothing leaves
the process and no LLM or MCP server is contacted.
"""

API = "https://api.test"
HUB = "https://hub.test"
CLIENT_ARGS: dict[str, Any] = {
    "project_id": "test-project",
    "api_key": "key_1",
    "base_url_api": API,
    "base_url_hub": HUB,
    "api_version": "v2",
    "hub_version": "v2",
}

# (name, verb, path, query, body, call) — call takes client.hub
CASES: list[tuple[str, str, str, dict[str, list[str]] | None, dict[str, Any] | None, Callable[[Any], Any]]] = [
    # LLM and MCP integrations (client.hub.ai).
    ("get_llm_integrations", "GET", "/v2/ai/integrations/llms/integrations", {"pageSize": ["50"], "startingAfter": ["int_llm0"]}, None,
     lambda c: c.ai.get_llm_integrations(pageSize=50, startingAfter='int_llm0')),
    ("get_llm_integration", "GET", "/v2/ai/integrations/llms/int_llm1", None, None,
     lambda c: c.ai.get_llm_integration("int_llm1")),
    ("save_llm_integration", "POST", "/v2/ai/integrations/llms/", None, {'integration': {'provider': 'OpenAI', 'integrationName': 'OpenAI', 'apiKey': 'sk-test', 'defaultModel': 'gpt-4o-mini', 'isDefault': True, 'isEnabled': True}},
     lambda c: c.ai.save_llm_integration(integration={'provider': 'OpenAI', 'integrationName': 'OpenAI', 'apiKey': 'sk-test', 'defaultModel': 'gpt-4o-mini', 'isDefault': True, 'isEnabled': True})),
    ("test_llm_integration", "POST", "/v2/ai/integrations/llms/test", None, {'integrationId': 'int_llm1'},
     lambda c: c.ai.test_llm_integration(integrationId='int_llm1')),
    ("enable_llm_integration", "PUT", "/v2/ai/integrations/llms/int_llm1/enable", None, None,
     lambda c: c.ai.enable_llm_integration("int_llm1")),
    ("disable_llm_integration", "PUT", "/v2/ai/integrations/llms/int_llm1/disable", None, None,
     lambda c: c.ai.disable_llm_integration("int_llm1")),
    ("set_llm_integration_as_default", "PUT", "/v2/ai/integrations/llms/int_llm1/default", None, None,
     lambda c: c.ai.set_llm_integration_as_default("int_llm1")),
    ("delete_llm_integration", "DELETE", "/v2/ai/integrations/llms/int_llm1", None, None,
     lambda c: c.ai.delete_llm_integration("int_llm1")),
    ("get_mcp_integrations", "GET", "/v2/ai/integrations/mcp/integrations", {"pageSize": ["20"]}, None,
     lambda c: c.ai.get_mcp_integrations(pageSize=20)),
    ("get_mcp_integration", "GET", "/v2/ai/integrations/mcp/int_mcp1", None, None,
     lambda c: c.ai.get_mcp_integration("int_mcp1")),
    ("save_mcp_integration", "POST", "/v2/ai/integrations/mcp/", None, {'integration': {'provider': 'GitHub', 'integrationName': 'GitHub', 'name': 'GitHub', 'category': 'Code', 'serverUrl': 'https://api.githubcopilot.com/mcp/', 'isEnabled': True}},
     lambda c: c.ai.save_mcp_integration(integration={'provider': 'GitHub', 'integrationName': 'GitHub', 'name': 'GitHub', 'category': 'Code', 'serverUrl': 'https://api.githubcopilot.com/mcp/', 'isEnabled': True})),
    ("test_mcp_integration", "POST", "/v2/ai/integrations/mcp/test", None, {'integrationId': 'int_mcp1'},
     lambda c: c.ai.test_mcp_integration(integrationId='int_mcp1')),
    ("enable_mcp_integration", "PUT", "/v2/ai/integrations/mcp/int_mcp1/enable", None, None,
     lambda c: c.ai.enable_mcp_integration("int_mcp1")),
    ("disable_mcp_integration", "PUT", "/v2/ai/integrations/mcp/int_mcp1/disable", None, None,
     lambda c: c.ai.disable_mcp_integration("int_mcp1")),
    ("delete_mcp_integration", "DELETE", "/v2/ai/integrations/mcp/int_mcp1", None, None,
     lambda c: c.ai.delete_mcp_integration("int_mcp1")),
    # Developer AI chat and the AI tool inventory (client.hub.account).
    ("get_ai_tools", "GET", "/v2/account/ai/tools", {"toolset": ["ai:database-read"]}, None,
     lambda c: c.account.get_ai_tools(toolset='ai:database-read')),
    ("invoke_ai_tool", "POST", "/v2/account/ai/tools/get_schemas", None, {'argumentsJson': '{"take":5}'},
     lambda c: c.account.invoke_ai_tool("get_schemas", argumentsJson='{"take":5}')),
]

IDS = [c[0] for c in CASES]


def _capture(seen: list[httpx.Request]) -> Callable[[httpx.Request], httpx.Response]:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    return handler


def _assert_request(
    request: httpx.Request, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None
) -> None:
    assert f"{request.url.scheme}://{request.url.host}" == HUB
    assert request.method == verb
    assert request.url.path == path
    assert parse_qs(request.url.query.decode()) == (query or {})
    if body is None:
        assert request.content == b""
    else:
        assert json.loads(request.content) == body
    assert request.headers["authorization"] == "Bearer key_1"
    assert request.headers["norbix-project-id"] == "test-project"


def test_ai_cluster_hub_route_count() -> None:
    # LLM 8 + MCP 7 + AI tools 2.
    assert len(CASES) == 8 + 7 + 2
    assert len(set(IDS)) == len(IDS)


@pytest.mark.parametrize("name, verb, path, query, body, call", CASES, ids=IDS)
def test_ai_cluster_hub_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))))

    call(client.hub)

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query, body)


@pytest.mark.parametrize("name, verb, path, query, body, call", CASES, ids=IDS)
def test_async_ai_cluster_hub_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(**CLIENT_ARGS, http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))))
        try:
            await call(client.hub)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query, body)
