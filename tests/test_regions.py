from __future__ import annotations

import asyncio
import json
from typing import Any

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

from .helpers import CaptureTransport


class AsyncCaptureTransport(httpx.AsyncBaseTransport):
    def __init__(self) -> None:
        self.last_request: dict[str, Any] | None = None

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        self.last_request = {
            "method": request.method,
            "url": str(request.url),
            "headers": dict(request.headers),
            "body": request.content.decode("utf-8") if request.content else "",
        }
        return httpx.Response(200, json={})


def _client(
    region: str | None = None,
    base_url_api: str | None = None,
    base_url_hub: str | None = None,
) -> tuple[Norbix, CaptureTransport]:
    transport = CaptureTransport()
    http_client = httpx.Client(transport=transport)
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        account_id="test-account",
        region=region,
        base_url_api=base_url_api,
        base_url_hub=base_url_hub,
        http_client=http_client,
    )
    return client, transport


def _async_client(region: str | None = None) -> tuple[AsyncNorbix, AsyncCaptureTransport]:
    transport = AsyncCaptureTransport()
    http_client = httpx.AsyncClient(transport=transport)
    client = AsyncNorbix(
        project_id="test-project",
        bearer_token="test-token",
        account_id="test-account",
        region=region,
        http_client=http_client,
    )
    return client, transport


def test_unset_region_omits_header() -> None:
    client, transport = _client()
    client.hub.regions.list()
    assert transport.last_request is not None
    assert "nb-region" not in transport.last_request["headers"]


def test_client_region_sets_header() -> None:
    client, transport = _client(region="nb-eu-germany")
    client.hub.regions.list()
    assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"


def test_per_call_region_overrides_default() -> None:
    client, transport = _client(region="nb-eu-germany")
    client.hub.regions.list(region="nb-us-east")
    assert transport.last_request["headers"]["nb-region"] == "nb-us-east"


def test_norbix_region_env_var_fallback(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("NORBIX_REGION", "nb-eu-germany")
    client, transport = _client()
    client.hub.regions.list()
    assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"
    assert transport.last_request["url"].startswith("https://nb-eu-germany.hub.norbix.ai/")


def test_region_composes_default_base_urls() -> None:
    client, transport = _client(region="nb-eu-germany")
    client.hub.regions.list()
    assert transport.last_request["url"].startswith("https://nb-eu-germany.hub.norbix.ai/")
    client.api.echo.echo()
    assert transport.last_request["url"].startswith("https://nb-eu-germany.api.norbix.ai/")


def test_region_never_rewrites_custom_base_url() -> None:
    client, transport = _client(
        region="nb-eu-germany",
        base_url_api="https://api.example.com",
        base_url_hub="https://hub.example.com",
    )
    client.hub.regions.list()
    assert transport.last_request["url"].startswith("https://hub.example.com/")
    assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"
    client.api.echo.echo()
    assert transport.last_request["url"].startswith("https://api.example.com/")


def test_per_call_region_only_sets_header_not_url() -> None:
    client, transport = _client()
    client.hub.regions.list(region="nb-eu-germany")
    assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"
    assert transport.last_request["url"].startswith("https://hub.norbix.ai/")


def test_set_region_runtime_and_clear() -> None:
    client, transport = _client()
    assert client.get_region() is None
    client.set_region("nb-eu-germany")
    assert client.get_region() == "nb-eu-germany"
    client.hub.regions.list()
    assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"
    assert transport.last_request["url"].startswith("https://nb-eu-germany.hub.norbix.ai/")
    client.set_region(None)
    assert client.get_region() is None
    client.hub.regions.list()
    assert "nb-region" not in transport.last_request["headers"]
    assert transport.last_request["url"].startswith("https://hub.norbix.ai/")


def test_set_region_keeps_custom_base_url() -> None:
    client, transport = _client(base_url_hub="https://hub.example.com")
    client.set_region("nb-eu-germany")
    client.hub.regions.list()
    assert transport.last_request["url"].startswith("https://hub.example.com/")
    assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"


def test_list_and_update_project_regions_routes() -> None:
    client, transport = _client()
    client.hub.regions.list()
    assert transport.last_request["method"] == "GET"
    assert transport.last_request["url"].endswith("/account/regions")

    client.hub.regions.update_project_regions(
        "proj-1",
        primary_region="nb-eu-germany",
        additional_regions=["nb-us-east"],
    )
    assert transport.last_request["method"] == "PATCH"
    assert transport.last_request["url"].endswith("/account/projects/proj-1/settings/regions")
    body = json.loads(transport.last_request["body"])
    assert body == {"primaryRegion": "nb-eu-germany", "additionalRegions": ["nb-us-east"]}


def test_update_project_regions_omits_unset_fields() -> None:
    client, transport = _client()
    client.hub.regions.update_project_regions("proj-1", primary_region="nb-eu-germany")
    body = json.loads(transport.last_request["body"])
    assert body == {"primaryRegion": "nb-eu-germany"}


def test_create_project_accepts_regions() -> None:
    client, transport = _client()
    client.hub.account.create_project(
        primary_region="nb-eu-germany", additional_regions=["nb-us-east"]
    )
    assert transport.last_request["method"] == "POST"
    assert transport.last_request["url"].endswith("/account/projects")
    body = json.loads(transport.last_request["body"])
    assert body["primaryRegion"] == "nb-eu-germany"
    assert body["additionalRegions"] == ["nb-us-east"]


def test_create_project_without_regions_sends_no_region_fields() -> None:
    client, transport = _client()
    client.hub.account.create_project(name="my-project")
    body = json.loads(transport.last_request["body"])
    assert body == {"name": "my-project"}


def test_async_region_header_and_routes() -> None:
    async def run() -> None:
        client, transport = _async_client(region="nb-eu-germany")
        await client.hub.regions.list()
        assert transport.last_request["method"] == "GET"
        assert transport.last_request["url"].endswith("/account/regions")
        assert transport.last_request["url"].startswith("https://nb-eu-germany.hub.norbix.ai/")
        assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"

        await client.hub.regions.update_project_regions(
            "proj-1", primary_region="nb-eu-germany", region="nb-us-east"
        )
        assert transport.last_request["method"] == "PATCH"
        assert transport.last_request["url"].endswith("/account/projects/proj-1/settings/regions")
        assert transport.last_request["headers"]["nb-region"] == "nb-us-east"
        await client.aclose()

    asyncio.run(run())


def test_async_set_region_and_unset_omits_header() -> None:
    async def run() -> None:
        client, transport = _async_client()
        await client.hub.regions.list()
        assert "nb-region" not in transport.last_request["headers"]
        assert transport.last_request["url"].startswith("https://hub.norbix.ai/")

        client.set_region("nb-eu-germany")
        assert client.get_region() == "nb-eu-germany"
        await client.hub.regions.list()
        assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"
        assert transport.last_request["url"].startswith("https://nb-eu-germany.hub.norbix.ai/")
        await client.aclose()

    asyncio.run(run())
