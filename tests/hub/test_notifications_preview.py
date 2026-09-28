from __future__ import annotations

import asyncio
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

"""The three notification preview routes open with a signed link alone.

The ``hash`` query value is the key, so a client with no API key and no bearer
token must still send the request — with no Authorization header. A client
that has a key still sends it. Every call goes to a capture transport, so
nothing leaves the process.
"""

HASH = "signed-link-abc"

# channel, expected path, call
PreviewCase = tuple[str, str, Callable[[Any], Any]]

PREVIEW_CASES: list[PreviewCase] = [
    (
        "push",
        "/v2/notifications/push/preview",
        lambda m: m.preview_push_notification(hash=HASH),
    ),
    (
        "email",
        "/v2/notifications/email/preview",
        lambda m: m.preview_email_notification(hash=HASH),
    ),
    (
        "sms",
        "/v2/notifications/sms/preview",
        lambda m: m.preview_sms_notification(hash=HASH),
    ),
]

# name, api_key, expected Authorization (None = header must be absent)
AUTH_CASES = [
    ("no_credentials", None, None),
    ("api_key", "key_1", "Bearer key_1"),
]


def _capture(seen: list[httpx.Request]) -> Callable[[httpx.Request], httpx.Response]:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"result": {}})

    return handler


@pytest.fixture(autouse=True)
def _no_env_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("NORBIX_API_KEY", raising=False)
    monkeypatch.delenv("NORBIX_BEARER_TOKEN", raising=False)


def _assert_request(request: httpx.Request, path: str, want_auth: str | None) -> None:
    url = urlparse(str(request.url))
    assert request.method == "GET"
    assert url.path == path
    assert parse_qs(url.query) == {"hash": [HASH]}
    assert request.headers.get("Authorization") == want_auth


@pytest.mark.parametrize("auth_name, api_key, want_auth", AUTH_CASES, ids=[a[0] for a in AUTH_CASES])
@pytest.mark.parametrize("channel, path, call", PREVIEW_CASES, ids=[c[0] for c in PREVIEW_CASES])
def test_preview_with_signed_link_needs_no_sign_in(
    channel: str,
    path: str,
    call: Callable[[Any], Any],
    auth_name: str,
    api_key: str | None,
    want_auth: str | None,
) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(
        project_id="test-project",
        api_key=api_key,
        http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))),
    )

    call(client.hub.notifications)

    assert len(seen) == 1
    _assert_request(seen[0], path, want_auth)


@pytest.mark.parametrize("channel, path, call", PREVIEW_CASES, ids=[c[0] for c in PREVIEW_CASES])
def test_async_preview_with_signed_link_needs_no_sign_in(
    channel: str, path: str, call: Callable[[Any], Any]
) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(
            project_id="test-project",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))),
        )
        try:
            await call(client.hub.notifications)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == 1
    _assert_request(seen[0], path, None)
