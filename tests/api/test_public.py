"""api.public — the public project config and legal pages, served by the API host with no sign-in."""
from __future__ import annotations

import asyncio
from typing import Any

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, NorbixApi

LEGAL = {"kind": "terms", "title": "Terms", "body": "# Terms", "available": True}


@pytest.fixture
def _no_env_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("NORBIX_API_KEY", raising=False)
    monkeypatch.delenv("NORBIX_BEARER_TOKEN", raising=False)


def _capture(seen: list[httpx.Request], answer: Any) -> Any:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json=answer)

    return handler


@pytest.mark.usefixtures("_no_env_credentials")
@pytest.mark.parametrize("bearer_token", [None, "signed-in"], ids=["no_credentials", "signed_in"])
def test_public_project_config_goes_to_the_api_host_without_auth(bearer_token: str | None) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(
        project_id="test-project",
        bearer_token=bearer_token,
        http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen, {"displayName": "Shop"}))),
    )

    result = client.api.public.get_public_project_config("pr_1")

    assert result == {"displayName": "Shop"}
    assert seen[0].method == "GET"
    assert seen[0].url.host == "api.norbix.ai"
    assert seen[0].url.path == "/v3/public/projects/pr_1/config"
    assert "authorization" not in seen[0].headers


@pytest.mark.usefixtures("_no_env_credentials")
def test_public_project_legal_puts_project_and_kind_in_the_path() -> None:
    seen: list[httpx.Request] = []
    client = NorbixApi(
        project_id="test-project",
        http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen, LEGAL))),
    )

    result = client.public.get_public_project_legal("pr_1", "terms")

    assert result == LEGAL
    assert seen[0].method == "GET"
    assert seen[0].url.path == "/v3/public/projects/pr_1/legal/terms"
    assert "authorization" not in seen[0].headers
    assert client.Public is client.public


@pytest.mark.usefixtures("_no_env_credentials")
def test_async_public_module_sends_the_same_requests() -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(
            project_id="test-project",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen, LEGAL))),
        )
        try:
            await client.api.public.get_public_project_config("pr_1")
            await client.api.public.get_public_project_legal("pr_1", "privacy")
        finally:
            await client.aclose()

    asyncio.run(run())

    assert [r.url.path for r in seen] == [
        "/v3/public/projects/pr_1/config",
        "/v3/public/projects/pr_1/legal/privacy",
    ]
    assert all("authorization" not in r.headers for r in seen)
