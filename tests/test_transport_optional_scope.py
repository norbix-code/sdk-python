from __future__ import annotations

import asyncio
from collections.abc import Callable

import httpx
import pytest

from norbix_python.errors import NorbixError
from norbix_python.transport import AsyncTransport, Transport, TransportConfig

"""The "optional" scope sends auth when the client has a token and never
requires one — used by the signed notification preview links. The other
scopes are unchanged: "project" still refuses to send without a token."""

PATH = "/{version}/notifications/push/preview"


def _cfg(api_key: str | None) -> TransportConfig:
    return TransportConfig(
        api_key=api_key,
        bearer_token=None,
        project_id="proj_1",
        account_id=None,
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


@pytest.mark.parametrize(
    "api_key, want_auth",
    [(None, None), ("key_1", "Bearer key_1")],
    ids=["no_credentials", "api_key"],
)
def test_optional_scope_sends_auth_only_when_present(
    api_key: str | None, want_auth: str | None
) -> None:
    seen: list[httpx.Request] = []
    transport = Transport(
        _cfg(api_key), httpx.Client(transport=httpx.MockTransport(_capture(seen)))
    )

    transport.send(
        target="hub", path=PATH, method="GET", request={"hash": "h1"}, scope="optional"
    )

    assert len(seen) == 1
    assert seen[0].headers.get("Authorization") == want_auth
    assert seen[0].url.params.get("hash") == "h1"
    assert seen[0].headers.get("X-CM-ProjectId") == "proj_1"


@pytest.mark.parametrize(
    "api_key, want_auth",
    [(None, None), ("key_1", "Bearer key_1")],
    ids=["no_credentials", "api_key"],
)
def test_async_optional_scope_sends_auth_only_when_present(
    api_key: str | None, want_auth: str | None
) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        async with httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))) as http:
            await AsyncTransport(_cfg(api_key), http).send(
                target="hub", path=PATH, method="GET", request={"hash": "h1"}, scope="optional"
            )

    asyncio.run(run())

    assert len(seen) == 1
    assert seen[0].headers.get("Authorization") == want_auth


def test_project_scope_still_requires_auth() -> None:
    seen: list[httpx.Request] = []
    transport = Transport(_cfg(None), httpx.Client(transport=httpx.MockTransport(_capture(seen))))

    with pytest.raises(NorbixError) as exc:
        transport.send(target="hub", path=PATH, method="GET", scope="project")

    assert exc.value.code == "NORBIX_NOT_AUTHENTICATED"
    assert seen == []
