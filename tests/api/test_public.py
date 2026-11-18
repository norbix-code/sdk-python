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
    assert seen[0].url.query == b""
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
    assert seen[0].url.host == "api.norbix.ai"
    assert seen[0].url.query == b""
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


PNG = b"\x89PNG\r\n\x1a\n"


def _image(seen: list[httpx.Request]) -> Any:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, content=PNG, headers={"content-type": "image/png"})

    return handler


@pytest.mark.usefixtures("_no_env_credentials")
def test_public_project_brand_asset_gives_back_the_image_bytes_from_the_api_host() -> None:
    seen: list[httpx.Request] = []
    client = Norbix(
        project_id="test-project",
        bearer_token="signed-in",
        http_client=httpx.Client(transport=httpx.MockTransport(_image(seen))),
    )

    result = client.api.public.get_public_project_brand_asset("pr_1", "logo")

    assert result == PNG
    assert len(seen) == 1
    assert seen[0].method == "GET"
    assert seen[0].url.host == "api.norbix.ai"
    assert seen[0].url.path == "/v3/public/projects/pr_1/brand/logo"
    assert seen[0].url.query == b""
    assert seen[0].content == b""
    assert "authorization" not in seen[0].headers


@pytest.mark.usefixtures("_no_env_credentials")
def test_public_project_brand_asset_follows_the_storage_redirect() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        if request.url.host == "api.norbix.ai":
            return httpx.Response(302, headers={"location": "https://bucket.example.com/brand/logo.png?sig=1"})
        return httpx.Response(200, content=PNG, headers={"content-type": "image/png"})

    client = NorbixApi(project_id="test-project", http_client=httpx.Client(transport=httpx.MockTransport(handler)))

    assert client.public.get_public_project_brand_asset("pr_1", "icon") == PNG
    assert [str(r.url) for r in seen] == [
        "https://api.norbix.ai/v3/public/projects/pr_1/brand/icon",
        "https://bucket.example.com/brand/logo.png?sig=1",
    ]


@pytest.mark.usefixtures("_no_env_credentials")
def test_async_public_project_brand_asset_sends_the_same_request() -> None:
    seen: list[httpx.Request] = []

    async def run() -> bytes:
        client = AsyncNorbix(
            project_id="test-project",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_image(seen))),
        )
        try:
            result: bytes = await client.api.public.get_public_project_brand_asset("pr_1", "icon")
            return result
        finally:
            await client.aclose()

    assert asyncio.run(run()) == PNG
    assert seen[0].method == "GET"
    assert seen[0].url.host == "api.norbix.ai"
    assert seen[0].url.path == "/v3/public/projects/pr_1/brand/icon"
    assert "authorization" not in seen[0].headers
