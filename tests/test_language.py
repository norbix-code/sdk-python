from __future__ import annotations

import asyncio

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, NorbixApi, NorbixHub

from .helpers import CaptureTransport
from .test_regions import AsyncCaptureTransport

# The gateway reads the response language only from the standard
# Accept-Language header. The SDK has no default: when no language is set the
# header is not sent at all, so traffic stays byte-identical.


@pytest.fixture(autouse=True)
def _no_language_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("NORBIX_LANGUAGE", raising=False)


def _client(language: str | None = None) -> tuple[Norbix, CaptureTransport]:
    transport = CaptureTransport()
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        account_id="test-account",
        language=language,
        http_client=httpx.Client(transport=transport),
    )
    return client, transport


def _async_client(language: str | None = None) -> tuple[AsyncNorbix, AsyncCaptureTransport]:
    transport = AsyncCaptureTransport()
    client = AsyncNorbix(
        project_id="test-project",
        bearer_token="test-token",
        account_id="test-account",
        language=language,
        http_client=httpx.AsyncClient(transport=transport),
    )
    return client, transport


def test_unset_language_omits_header() -> None:
    client, transport = _client()
    client.hub.regions.list()
    assert transport.last_request is not None
    assert "accept-language" not in transport.last_request["headers"]
    client.api.echo.echo()
    assert "accept-language" not in transport.last_request["headers"]


def test_client_language_sets_header() -> None:
    client, transport = _client(language="lt-LT, en;q=0.8")
    client.hub.regions.list()
    assert transport.last_request["headers"]["accept-language"] == "lt-LT, en;q=0.8"
    client.api.echo.echo()
    assert transport.last_request["headers"]["accept-language"] == "lt-LT, en;q=0.8"


def test_per_call_language_overrides_default() -> None:
    client, transport = _client(language="lt")
    client.hub.regions.list(language="de")
    assert transport.last_request["headers"]["accept-language"] == "de"
    client.hub.regions.list()
    assert transport.last_request["headers"]["accept-language"] == "lt"


def test_per_call_language_is_not_sent_in_body() -> None:
    client, transport = _client()
    client.hub.regions.update_project_regions("proj-1", primary_region="nb-eu-germany", language="lt")
    assert transport.last_request["headers"]["accept-language"] == "lt"
    assert "language" not in transport.last_request["body"]


def test_norbix_language_env_var_fallback(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("NORBIX_LANGUAGE", "lt")
    client, transport = _client()
    assert client.get_language() == "lt"
    client.hub.regions.list()
    assert transport.last_request["headers"]["accept-language"] == "lt"


def test_explicit_language_beats_env_var(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("NORBIX_LANGUAGE", "lt")
    client, transport = _client(language="en")
    client.hub.regions.list()
    assert transport.last_request["headers"]["accept-language"] == "en"


def test_set_language_runtime_and_clear() -> None:
    client, transport = _client()
    assert client.get_language() is None
    client.set_language("lt")
    assert client.get_language() == "lt"
    client.hub.regions.list()
    assert transport.last_request["headers"]["accept-language"] == "lt"
    client.set_language(None)
    assert client.get_language() is None
    client.hub.regions.list()
    assert "accept-language" not in transport.last_request["headers"]


def test_api_and_hub_only_clients_accept_language() -> None:
    api_transport = CaptureTransport()
    api = NorbixApi(
        project_id="p",
        bearer_token="t",
        language="lt",
        http_client=httpx.Client(transport=api_transport),
    )
    api.echo.echo()
    assert api_transport.last_request["headers"]["accept-language"] == "lt"

    hub_transport = CaptureTransport()
    hub = NorbixHub(
        project_id="p",
        bearer_token="t",
        language="lt",
        http_client=httpx.Client(transport=hub_transport),
    )
    hub.regions.list()
    assert hub_transport.last_request["headers"]["accept-language"] == "lt"


def test_no_legacy_language_headers_or_fields() -> None:
    client, transport = _client(language="lt")
    client.hub.regions.list()
    headers = {k.lower() for k in transport.last_request["headers"]}
    assert "culturecode" not in headers
    assert "norbix-language" not in headers
    assert "cultureCode" not in transport.last_request["url"]


def test_async_language_header_override_and_unset() -> None:
    async def run() -> None:
        client, transport = _async_client()
        await client.hub.regions.list()
        assert "accept-language" not in transport.last_request["headers"]

        client.set_language("lt")
        assert client.get_language() == "lt"
        await client.hub.regions.list()
        assert transport.last_request["headers"]["accept-language"] == "lt"

        await client.hub.regions.update_project_regions(
            "proj-1", primary_region="nb-eu-germany", language="de"
        )
        assert transport.last_request["headers"]["accept-language"] == "de"
        await client.aclose()

    asyncio.run(run())


def test_async_client_language_and_env(monkeypatch: pytest.MonkeyPatch) -> None:
    async def run() -> None:
        client, transport = _async_client(language="lt-LT, en;q=0.8")
        await client.hub.regions.list()
        assert transport.last_request["headers"]["accept-language"] == "lt-LT, en;q=0.8"
        await client.aclose()

        monkeypatch.setenv("NORBIX_LANGUAGE", "en")
        client2, transport2 = _async_client()
        await client2.hub.regions.list()
        assert transport2.last_request["headers"]["accept-language"] == "en"
        await client2.aclose()

    asyncio.run(run())
