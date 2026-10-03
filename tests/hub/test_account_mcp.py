"""The developer MCP endpoint: POST / GET / DELETE /{version}/account/mcp.

The session id travels in the ``Mcp-Session-Id`` header, and a ``tools/call``
may be answered as an SSE stream, so these tests check headers both ways and
the parsing of a stream answer.
"""
from __future__ import annotations

import asyncio
import json
from typing import Any

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, NorbixError

INIT = {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-11-25"}}

SSE_ANSWER = (
    "id: p1:0\nretry: 3000\ndata: \n\n"
    'id: p1:1\ndata: {"jsonrpc":"2.0","method":"notifications/progress","params":{"progress":1}}\n\n'
    ": ping\n\n"
    'id: p1:2\ndata: {"jsonrpc":"2.0","id":2,"result":{"content":[{"type":"text","text":"ok"}]}}\n\n'
)


def _client(handler: Any) -> Norbix:
    return Norbix(
        project_id="test-project",
        bearer_token="nbsu_test",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )


def test_initialize_returns_the_session_id_from_the_response_header() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(
            200,
            headers={"Mcp-Session-Id": "mcps_1"},
            json={"jsonrpc": "2.0", "id": 1, "result": {"protocolVersion": "2025-11-25"}},
        )

    result = _client(handler).hub.account.mcp(INIT, toolsets="ai:campaigns,ai:project-context")

    assert result == {
        "status": 200,
        "sessionId": "mcps_1",
        "body": {"jsonrpc": "2.0", "id": 1, "result": {"protocolVersion": "2025-11-25"}},
        "events": [],
    }
    request = seen[0]
    assert request.method == "POST"
    assert request.url.path == "/v2/account/mcp"
    assert request.url.params["toolsets"] == "ai:campaigns,ai:project-context"
    assert json.loads(request.content) == INIT
    assert request.headers["accept"] == "application/json, text/event-stream"
    assert request.headers["authorization"] == "Bearer nbsu_test"
    assert "mcp-session-id" not in request.headers


def test_tools_call_answered_as_a_stream_gives_the_final_answer_and_all_events() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, headers={"Content-Type": "text/event-stream"}, text=SSE_ANSWER)

    message = {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "list_campaigns"}}
    result = _client(handler).hub.account.mcp(message, session_id="mcps_1", protocol_version="2025-11-25")

    assert result["body"] == {"jsonrpc": "2.0", "id": 2, "result": {"content": [{"type": "text", "text": "ok"}]}}
    assert [e.get("method") for e in result["events"]] == ["notifications/progress", None]
    assert seen[0].headers["mcp-session-id"] == "mcps_1"
    assert seen[0].headers["mcp-protocol-version"] == "2025-11-25"
    assert "toolsets" not in seen[0].url.params


def test_a_notification_is_answered_202_with_no_body() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(202)

    result = _client(handler).hub.account.mcp(
        {"jsonrpc": "2.0", "method": "notifications/initialized"}, session_id="mcps_1"
    )

    assert result == {"status": 202, "sessionId": None, "body": None, "events": []}


def test_stream_asks_for_event_stream_and_resumes_from_the_last_event() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        body = 'id: g1:4\ndata: {"jsonrpc":"2.0","method":"notifications/tools/list_changed","params":{}}\n\n'
        return httpx.Response(200, headers={"Content-Type": "text/event-stream"}, text=body)

    result = _client(handler).hub.account.mcp_stream("mcps_1", last_event_id="g1:3")

    assert result["events"] == [{"jsonrpc": "2.0", "method": "notifications/tools/list_changed", "params": {}}]
    assert result["body"] is None
    request = seen[0]
    assert request.method == "GET"
    assert request.url.path == "/v2/account/mcp"
    assert request.url.query == b""
    assert request.headers["accept"] == "text/event-stream"
    assert request.headers["mcp-session-id"] == "mcps_1"
    assert request.headers["last-event-id"] == "g1:3"


def test_end_session_sends_delete_with_the_session_header() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200)

    result = _client(handler).hub.account.mcp_end_session("mcps_1")

    assert result == {"status": 200, "sessionId": None, "body": None, "events": []}
    assert seen[0].method == "DELETE"
    assert seen[0].url.path == "/v2/account/mcp"
    assert seen[0].headers["mcp-session-id"] == "mcps_1"


def test_an_expired_session_raises_with_the_404_status() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            404,
            json={"jsonrpc": "2.0", "id": None, "error": {"code": -32001, "message": "Session not found"}},
        )

    with pytest.raises(NorbixError) as raised:
        _client(handler).hub.account.mcp({"jsonrpc": "2.0", "id": 3, "method": "ping"}, session_id="gone")

    assert raised.value.status == 404


def test_async_twins_send_the_same_requests() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, headers={"Mcp-Session-Id": "mcps_9"}, json={"jsonrpc": "2.0", "id": 1, "result": {}})

    async def run() -> list[dict[str, Any]]:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="nbsu_test",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        try:
            return [
                await client.hub.account.mcp(INIT),
                await client.hub.account.mcp_stream("mcps_9"),
                await client.hub.account.mcp_end_session("mcps_9"),
            ]
        finally:
            await client.aclose()

    results = asyncio.run(run())

    assert [r["sessionId"] for r in results] == ["mcps_9", "mcps_9", "mcps_9"]
    assert [(r.method, r.headers["accept"]) for r in seen] == [
        ("POST", "application/json, text/event-stream"),
        ("GET", "text/event-stream"),
        ("DELETE", "application/json"),
    ]
    assert json.loads(seen[0].content) == INIT
