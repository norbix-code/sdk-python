from __future__ import annotations

import asyncio
import json
from urllib.parse import urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, RateLimitError

from ..helpers import make_client


def test_api_logs_module_surface() -> None:
    client, _ = make_client()
    assert callable(client.api.logs.write_logs)


def test_api_logs_write_logs_request_shape() -> None:
    client, transport = make_client(account_id=None)
    entries = [
        {
            "level": "error",
            "title": "Checkout failed",
            "message": "card declined",
            "eventCode": "checkout.failed",
            "correlationId": "req-42",
            "timestamp": "2026-10-21T10:00:00Z",
            "meta": {"orderId": "ord_1"},
        },
        {"title": "Retry scheduled"},
    ]
    client.api.logs.write_logs(entries=entries)
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    url = transport.last_request['url']
    assert url.startswith('https://api.')
    assert urlparse(url).path == '/v3/logs'
    assert json.loads(transport.last_request['body']) == {"entries": entries}


def test_api_logs_write_logs_passes_project_id() -> None:
    client, transport = make_client(account_id=None)
    client.api.logs.write_logs(entries=[{"title": "t"}], projectId="proj_2")
    assert transport.last_request is not None
    assert json.loads(transport.last_request['body']) == {"entries": [{"title": "t"}], "projectId": "proj_2"}


def test_api_logs_write_logs_quota_raises_rate_limit_error() -> None:
    calls: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(
            429,
            headers={"Retry-After": "12"},
            json={"responseStatus": {"errorCode": "CM-ERRORS-LOGGING-003", "message": "quota used up"}},
        )

    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    with pytest.raises(RateLimitError) as info:
        client.api.logs.write_logs(entries=[{"title": "t"}])
    assert info.value.http_status == 429
    assert info.value.error_code == "CM-ERRORS-LOGGING-003"
    assert len(calls) == 1  # a POST is not retried


def test_async_api_logs_write_logs() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"accepted": 1})

    async def run() -> object:
        client = AsyncNorbix(
            project_id='test-project',
            bearer_token='test-token',
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        try:
            return await client.api.logs.write_logs(entries=[{"title": "t"}])
        finally:
            await client.aclose()

    result = asyncio.run(run())
    assert result == {"accepted": 1}
    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [('POST', '/v3/logs')]
    assert json.loads(seen[0].content) == {"entries": [{"title": "t"}]}
