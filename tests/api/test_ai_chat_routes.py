from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, NorbixError
from norbix_python.api.ai import ai_chat_channel

"""Matrix section 08 AI chat, API side: every end-user AI chat and AI tool
route of ``client.api.ai``, one case each, sync and async, and the chat
stream (``ai_chat``) against a fake SSE server. Written in the AI cluster
coverage campaign (2026-11-18); the older cases in ``test_ai.py`` assert the
verb and the path but not the host, the query or the body.

Each route case asserts the host (api), the verb, the exact path, the query
string and the JSON body, plus the key and project headers. Field names are
the gateway's (Api.AI ``ChatTurn.cs``, ``ChatSessions.cs``, ``ChatItems.cs``,
``EndUserAiTools.cs``). Nothing leaves the process and no LLM is contacted.
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

# (name, verb, path, query, body, call) — call takes client.api
CASES: list[tuple[str, str, str, dict[str, list[str]] | None, dict[str, Any] | None, Callable[[Any], Any]]] = [
    ("start_end_user_chat_turn", "POST", "/v2/ai/chat/turn", None, {'sessionId': 'aics_1', 'message': 'Where is my order?'},
     lambda c: c.ai.start_end_user_chat_turn(sessionId='aics_1', message='Where is my order?')),
    ("get_end_user_chat_availability", "GET", "/v2/ai/chat/availability", None, None,
     lambda c: c.ai.get_end_user_chat_availability()),
    ("list_end_user_chat_sessions", "GET", "/v2/ai/chat/sessions", {"take": ["10"], "includeArchived": ["true"]}, None,
     lambda c: c.ai.list_end_user_chat_sessions(take=10, includeArchived=True)),
    ("create_end_user_chat_session", "POST", "/v2/ai/chat/sessions", None, {'assistantId': 'ast_1', 'title': 'Orders'},
     lambda c: c.ai.create_end_user_chat_session(assistantId='ast_1', title='Orders')),
    ("get_end_user_chat_session", "GET", "/v2/ai/chat/sessions/aics_1", None, None,
     lambda c: c.ai.get_end_user_chat_session("aics_1")),
    ("rename_end_user_chat_session", "PATCH", "/v2/ai/chat/sessions/aics_1", None, {'title': 'Returns'},
     lambda c: c.ai.rename_end_user_chat_session("aics_1", title='Returns')),
    ("delete_end_user_chat_session", "DELETE", "/v2/ai/chat/sessions/aics_1", None, None,
     lambda c: c.ai.delete_end_user_chat_session("aics_1")),
    ("pin_end_user_chat_session", "PUT", "/v2/ai/chat/sessions/aics_1/pin", None, {'pinned': True},
     lambda c: c.ai.pin_end_user_chat_session("aics_1", pinned=True)),
    ("archive_end_user_chat_session", "PUT", "/v2/ai/chat/sessions/aics_1/archive", None, {'archived': False},
     lambda c: c.ai.archive_end_user_chat_session("aics_1", archived=False)),
    ("get_end_user_chat_entries", "GET", "/v2/ai/chat/sessions/aics_1/entries", {"afterSeq": ["3"], "take": ["50"]}, None,
     lambda c: c.ai.get_end_user_chat_entries("aics_1", afterSeq=3, take=50)),
    ("set_end_user_chat_entry_feedback", "PUT", "/v2/ai/chat/sessions/aics_1/entries/ent_1/feedback", None, {'feedback': 'down'},
     lambda c: c.ai.set_end_user_chat_entry_feedback("aics_1", "ent_1", feedback='down')),
    ("decide_end_user_chat_action", "POST", "/v2/ai/chat/sessions/aics_1/actions/ent_7", None, {'decision': 'apply'},
     lambda c: c.ai.decide_end_user_chat_action("aics_1", "ent_7", decision='apply')),
    ("list_end_user_chat_attachments", "GET", "/v2/ai/chat/sessions/aics_1/attachments", None, None,
     lambda c: c.ai.list_end_user_chat_attachments("aics_1")),
    ("upload_end_user_chat_attachment", "POST", "/v2/ai/chat/sessions/aics_1/attachments", None, {'fileName': 'receipt.pdf', 'contentType': 'application/pdf', 'base64Content': 'JVBERg=='},
     lambda c: c.ai.upload_end_user_chat_attachment("aics_1", fileName='receipt.pdf', contentType='application/pdf', base64Content='JVBERg==')),
    ("delete_end_user_chat_attachment", "DELETE", "/v2/ai/chat/attachments/att_1", None, None,
     lambda c: c.ai.delete_end_user_chat_attachment("att_1")),
    ("list_end_user_chat_memory", "GET", "/v2/ai/chat/memory", {"take": ["25"]}, None,
     lambda c: c.ai.list_end_user_chat_memory(take=25)),
    ("forget_end_user_chat_memory", "DELETE", "/v2/ai/chat/memory/mem_1", None, None,
     lambda c: c.ai.forget_end_user_chat_memory("mem_1")),
    ("get_end_user_ai_tools", "GET", "/v2/ai/tools", None, None,
     lambda c: c.ai.get_end_user_ai_tools()),
    ("invoke_end_user_ai_tool", "POST", "/v2/ai/tools/get_my_orders", None, {'argumentsJson': '{"status":"open"}'},
     lambda c: c.ai.invoke_end_user_ai_tool("get_my_orders", argumentsJson='{"status":"open"}')),
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
    assert f"{request.url.scheme}://{request.url.host}" == API
    assert request.method == verb
    assert request.url.path == path
    assert parse_qs(request.url.query.decode()) == (query or {})
    if body is None:
        assert request.content == b""
    else:
        assert json.loads(request.content) == body
    assert request.headers["authorization"] == "Bearer key_1"
    assert request.headers["norbix-project-id"] == "test-project"


def test_ai_chat_api_route_count() -> None:
    # 16 end-user chat routes + 2 AI tool routes.
    assert len(CASES) == 17 + 2
    assert len(set(IDS)) == len(IDS)


@pytest.mark.parametrize("name, verb, path, query, body, call", CASES, ids=IDS)
def test_ai_chat_api_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))))

    call(client.api)

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query, body)


@pytest.mark.parametrize("name, verb, path, query, body, call", CASES, ids=IDS)
def test_async_ai_chat_api_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(**CLIENT_ARGS, http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))))
        try:
            await call(client.api)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query, body)


# ── The chat stream ──────────────────────────────────────────────────────────


def _envelope(event: str, created: str, **payload: Any) -> str:
    return json.dumps(
        {"channel": "ai-chat", "eventName": event, "projectId": "test-project", "createdAtUtc": created, "payload": payload}
    )


# One turn as the gateway streams it: a heartbeat, a subscription notice that
# is not an envelope, then started → two tokens → completed. The second token
# uses CRLF line ends and splits its JSON over two data lines (legal SSE).
_TOKEN_2 = _envelope("ai.chat.turn.token", "2026-11-18T10:00:02Z", turnId="trn_1", text="has shipped.")
_SPLIT = _TOKEN_2.index('"createdAtUtc"')  # between two JSON members: the joined "\n" is whitespace
STREAM = (
    ": heartbeat\n\n"
    'event: cmd.onConnect\ndata: {"id":"sub_1"}\n\n'
    f"id: 1\nevent: cmd.ai.chat.turn.started\ndata: {_envelope('ai.chat.turn.started', '2026-11-18T10:00:00Z', turnId='trn_1')}\n\n"
    f"id: 2\nevent: cmd.ai.chat.turn.token\ndata: {_envelope('ai.chat.turn.token', '2026-11-18T10:00:01Z', turnId='trn_1', text='Your order ')}\n\n"
    f"id: 3\r\nevent: cmd.ai.chat.turn.token\r\ndata: {_TOKEN_2[:_SPLIT]}\r\ndata: {_TOKEN_2[_SPLIT:]}\r\n\r\n"
    f"id: 4\nevent: cmd.ai.chat.turn.completed\ndata: {_envelope('ai.chat.turn.completed', '2026-11-18T10:00:03Z', turnId='trn_1')}\n\n"
)


def _stream_handler(seen: list[httpx.Request]) -> Callable[[httpx.Request], httpx.Response]:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, headers={"Content-Type": "text/event-stream"}, content=STREAM.encode())

    return handler


def _assert_stream_request(request: httpx.Request) -> None:
    assert f"{request.url.scheme}://{request.url.host}" == API
    assert request.method == "GET"
    assert request.url.path == "/event-stream"
    assert parse_qs(request.url.query.decode()) == {"channels": ["ai-chat:test-project:usr_1"]}
    assert request.content == b""
    assert request.headers["accept"] == "text/event-stream"
    assert request.headers["authorization"] == "Bearer key_1"
    assert request.headers["norbix-project-id"] == "test-project"


def _assert_turn(events: list[dict[str, Any]]) -> None:
    assert [(e["eventName"], e["frameId"]) for e in events] == [
        ("ai.chat.turn.started", "1"),
        ("ai.chat.turn.token", "2"),
        ("ai.chat.turn.token", "3"),
        ("ai.chat.turn.completed", "4"),
    ]
    assert "".join(e["payload"].get("text", "") for e in events) == "Your order has shipped."
    assert {e["payload"]["turnId"] for e in events} == {"trn_1"}


def test_ai_chat_channel_name() -> None:
    assert ai_chat_channel("pr_x", "usr_y") == "ai-chat:pr_x:usr_y"


def test_ai_chat_stream_opens_the_callers_channel_on_the_api_host_and_parses_the_turn() -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(_stream_handler(seen))))

    events = list(client.api.ai.ai_chat("usr_1"))

    assert len(seen) == 1
    _assert_stream_request(seen[0])
    _assert_turn(events)


def test_async_ai_chat_stream_opens_the_callers_channel_on_the_api_host_and_parses_the_turn() -> None:
    seen: list[httpx.Request] = []

    async def run() -> list[dict[str, Any]]:
        client = AsyncNorbix(**CLIENT_ARGS, http_client=httpx.AsyncClient(transport=httpx.MockTransport(_stream_handler(seen))))
        try:
            return [e async for e in client.api.ai.ai_chat("usr_1")]
        finally:
            await client.aclose()

    events = asyncio.run(run())

    assert len(seen) == 1
    _assert_stream_request(seen[0])
    _assert_turn(events)


def test_ai_chat_stream_stops_when_the_caller_stops() -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(_stream_handler(seen))))

    names = []
    for event in client.api.ai.ai_chat("usr_1"):
        names.append(event["eventName"])
        if event["eventName"] == "ai.chat.turn.token":
            break

    assert names == ["ai.chat.turn.started", "ai.chat.turn.token"]


def test_ai_chat_stream_refusal_is_raised_and_not_retried() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(
            403, json={"responseStatus": {"errorCode": "AiChatChannelRefused", "message": "Not your channel."}}
        )

    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(handler)))

    with pytest.raises(NorbixError) as raised:
        list(client.api.ai.ai_chat("usr_other"))

    assert raised.value.status == 403
    assert raised.value.code == "AiChatChannelRefused"
    assert len(seen) == 1


def test_ai_chat_stream_needs_an_auth_id() -> None:
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(200))))

    with pytest.raises(NorbixError):
        list(client.api.ai.ai_chat(""))
