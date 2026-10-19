from __future__ import annotations

import asyncio
from collections.abc import Callable

import httpx
import pytest

from norbix_python.transport import AsyncTransport, Scope, Target, Transport, TransportConfig

"""The project and account ids go out under the header names the gateway
reads (AuthStatics): norbix-project-id and norbix-account-id. The legacy
X-CM-* names are not sent — the gateway never read them, so with an account
bearer token every Api project call failed with "ProjectId is required"."""

CASES = [
    ("api", "/{version}/db/records/find", "project"),
    ("hub", "/{version}/account/projects", "account"),
]
IDS = ["api_project_call", "hub_account_call"]


def _cfg() -> TransportConfig:
    return TransportConfig(
        api_key=None,
        bearer_token="account_token",
        project_id="proj_1",
        account_id="acc_1",
        base_url_api="https://api.test",
        base_url_hub="https://hub.test",
        api_version="v2",
        hub_version="v2",
        timeout=5.0,
    )


def _capture(seen: list[httpx.Request]) -> Callable[[httpx.Request], httpx.Response]:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    return handler


def _assert_scope_headers(request: httpx.Request) -> None:
    assert request.headers.get("Authorization") == "Bearer account_token"
    assert request.headers.get("norbix-project-id") == "proj_1"
    assert request.headers.get("norbix-account-id") == "acc_1"
    assert "X-CM-ProjectId" not in request.headers
    assert "X-CM-AccountId" not in request.headers


@pytest.mark.parametrize("target, path, scope", CASES, ids=IDS)
def test_sends_norbix_scope_headers(target: Target, path: str, scope: Scope) -> None:
    seen: list[httpx.Request] = []
    transport = Transport(_cfg(), httpx.Client(transport=httpx.MockTransport(_capture(seen))))

    transport.send(target=target, path=path, method="POST", request={}, scope=scope)

    assert len(seen) == 1
    _assert_scope_headers(seen[0])


@pytest.mark.parametrize("target, path, scope", CASES, ids=IDS)
def test_async_sends_norbix_scope_headers(target: Target, path: str, scope: Scope) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        async with httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))) as http:
            await AsyncTransport(_cfg(), http).send(
                target=target, path=path, method="POST", request={}, scope=scope
            )

    asyncio.run(run())

    assert len(seen) == 1
    _assert_scope_headers(seen[0])
