from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, NorbixApi

from ..helpers import make_client

"""Workflows (beta) on the Api host (Code.Workflows.md §7, "App users resume
from the API host"): the inbox, the resume by run id and the signed resume
link. Verb, resolved path and parameter placement, sync and async."""

WFR = "wfr_4hT2b9QkLm3XcT1yRfGh7a"
WF_TOKEN = "eyJydW4iOiJ3ZnJfNGhUMmI5In0.sig"

# name, verb, expected path, expected query (None: none), expected body (None: none), call
ApiCase = tuple[str, str, str, dict[str, list[str]] | None, dict[str, Any] | None, Callable[[Any], Any]]

API_WORKFLOW_CASES: list[ApiCase] = [
    ("get_code_workflow_waiting_runs", "GET", "/v3/code/workflows/runs", {"assignee": ["me"], "waitingKind": ["approval"], "pageSize": ["20"]}, None, lambda m: m.get_code_workflow_waiting_runs(assignee="me", waitingKind="approval", pageSize=20)),
    ("resume_code_workflow_run", "POST", f"/v3/code/workflows/runs/{WFR}/resume", None, {"stepId": "approve", "decision": "approved", "payload": {"note": "ok"}}, lambda m: m.resume_code_workflow_run(WFR, stepId="approve", decision="approved", payload={"note": "ok"})),
    ("open_code_workflow_resume_link", "GET", f"/v3/code/workflows/resume/{WF_TOKEN}", None, None, lambda m: m.open_code_workflow_resume_link(WF_TOKEN)),
    ("use_code_workflow_resume_link", "POST", f"/v3/code/workflows/resume/{WF_TOKEN}", None, None, lambda m: m.use_code_workflow_resume_link(WF_TOKEN)),
]


def _assert_request(name: str, request: httpx.Request, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None) -> None:
    url = urlparse(str(request.url))
    assert request.method == verb, f"{name}: verb {request.method}, expected {verb}"
    assert url.netloc == "api.norbix.ai", f"{name}: sent to {url.netloc}, expected the Api host"
    assert url.path == path, f"{name}: path {url.path}, expected {path}"
    assert parse_qs(url.query) == (query or {}), f"{name}: query {url.query!r}"
    content = request.content.decode("utf-8")
    if body is None:
        assert content == "", f"{name}: expected no body, got {content!r}"
    else:
        assert json.loads(content) == body, f"{name}: body {content}"


def _recorder(seen: list[httpx.Request]) -> Callable[[httpx.Request], httpx.Response]:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    return handler


@pytest.fixture(autouse=True)
def _default_api_url(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in ("NORBIX_API_URL", "NORBIX_API_VERSION", "NORBIX_REGION", "NORBIX_API_KEY", "NORBIX_BEARER_TOKEN"):
        monkeypatch.delenv(name, raising=False)


@pytest.mark.parametrize(("name", "verb", "path", "query", "body", "call"), API_WORKFLOW_CASES, ids=[c[0] for c in API_WORKFLOW_CASES])
def test_api_workflow_request_shape(
    name: str,
    verb: str,
    path: str,
    query: dict[str, list[str]] | None,
    body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(project_id="test-project", bearer_token="test-token", http_client=httpx.Client(transport=httpx.MockTransport(_recorder(seen))))
    call(client.api.code)
    assert len(seen) == 1
    _assert_request(name, seen[0], verb, path, query, body)
    assert seen[0].headers["authorization"] == "Bearer test-token"


def test_async_api_workflow_endpoints_hit_the_same_routes() -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_recorder(seen))),
        )
        try:
            for _, _, _, _, _, call in API_WORKFLOW_CASES:
                await call(client.api.code)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == len(API_WORKFLOW_CASES)
    for request, (name, verb, path, query, body, _) in zip(seen, API_WORKFLOW_CASES, strict=True):
        _assert_request(name, request, verb, path, query, body)


def test_api_workflow_surface() -> None:
    """Four Api workflow routes (the inbox, the resume, the two link routes)."""
    assert len(API_WORKFLOW_CASES) == 4
    client, _ = make_client()
    api_only = NorbixApi(project_id="test-project", bearer_token="test-token")
    for name, *_ in API_WORKFLOW_CASES:
        assert callable(getattr(client.api.code, name)), name
        assert callable(getattr(api_only.code, name)), name
    assert api_only.Code is api_only.code
    api_only.close()


def test_api_workflow_resume_links_need_no_credentials() -> None:
    """The signed link is the key: no token, no Authorization header, no failure."""
    seen: list[httpx.Request] = []
    client = Norbix(project_id="test-project", http_client=httpx.Client(transport=httpx.MockTransport(_recorder(seen))))
    client.api.code.open_code_workflow_resume_link(WF_TOKEN)
    client.api.code.use_code_workflow_resume_link(WF_TOKEN)

    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [
        ("GET", f"/v3/code/workflows/resume/{WF_TOKEN}"),
        ("POST", f"/v3/code/workflows/resume/{WF_TOKEN}"),
    ]
    assert all("authorization" not in r.headers for r in seen)
