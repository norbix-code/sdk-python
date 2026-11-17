from __future__ import annotations

import asyncio

import httpx
import pytest

from norbix_python import (
    AsyncNorbix,
    LoginCredentials,
    Norbix,
    NorbixApi,
    NorbixHub,
    project_host_label,
)

from .helpers import CaptureTransport
from .test_regions import AsyncCaptureTransport

# The first three labels are the server's own values (project DTO `hostLabel`,
# a project's DNS record), not this decoder's — devops docs/tasks/clients-project-host.md.
VECTORS = [
    ("pr_5XvmrTA6JVggZdmEE5bGdm", "pr-022c4aca9f9e4df787ab0a20c83c44b6"),
    ("pr_3vlTD52e9VK8lXzdv0SmWG", "pr-184336d00e2141c3be5138e8dcf52e81"),
    ("pr_89W9MJvt0StwxsEvyohlJ", "pr-60d101b1938747659947d507192a5204"),
    ("pr_xCeyU0VjHvjVi5MpOYSGY", "pr-6b8b6182960c416098d153d3eb0e601f"),
]
NOT_A_PROJECT_ID = [
    "p1",
    "proj_123",
    "pr_",
    "pr_!!!",
    "pr_zzzzzzzzzzzzzzzzzzzzzzz",
    "acc_oOAAIfAzbauZ6f0NHEHjP",
    "",
    # 22 digits, but 2^128 or more.
    "pr_zzzzzzzzzzzzzzzzzzzzzz",
    # A GUID that is not version 4.
    "pr_1",
    # Digits str.isdigit() accepts that are not base62.
    "pr_٣",
]

VIRGINIA = "pr_5XvmrTA6JVggZdmEE5bGdm"
VIRGINIA_HOST = "https://pr-022c4aca9f9e4df787ab0a20c83c44b6.api.norbix.ai/"
GERMANY = "pr_3vlTD52e9VK8lXzdv0SmWG"
GERMANY_HOST = "https://pr-184336d00e2141c3be5138e8dcf52e81.api.norbix.ai/"

URL_ENV_VARS = ("NORBIX_API_URL", "NORBIX_HUB_URL", "NORBIX_REGION", "NORBIX_PROJECT_ID")


@pytest.fixture(autouse=True)
def _no_norbix_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in URL_ENV_VARS:
        monkeypatch.delenv(name, raising=False)


def _client(
    project_id: str | None = VIRGINIA,
    region: str | None = None,
    base_url_api: str | None = None,
    base_url_hub: str | None = None,
) -> tuple[Norbix, CaptureTransport]:
    transport = CaptureTransport()
    client = Norbix(
        project_id=project_id,
        api_key="k",
        account_id="test-account",
        region=region,
        base_url_api=base_url_api,
        base_url_hub=base_url_hub,
        http_client=httpx.Client(transport=transport),
    )
    return client, transport


def _async_client(
    project_id: str | None = VIRGINIA,
    region: str | None = None,
    base_url_api: str | None = None,
    base_url_hub: str | None = None,
) -> tuple[AsyncNorbix, AsyncCaptureTransport]:
    transport = AsyncCaptureTransport()
    client = AsyncNorbix(
        project_id=project_id,
        api_key="k",
        account_id="test-account",
        region=region,
        base_url_api=base_url_api,
        base_url_hub=base_url_hub,
        http_client=httpx.AsyncClient(transport=transport),
    )
    return client, transport


# -- the label ---------------------------------------------------------------


@pytest.mark.parametrize(("project_id", "label"), VECTORS)
def test_label_vectors(project_id: str, label: str) -> None:
    assert project_host_label(project_id) == label


@pytest.mark.parametrize("value", NOT_A_PROJECT_ID)
def test_not_a_project_id_gives_no_label_and_does_not_raise(value: str) -> None:
    assert project_host_label(value) is None


@pytest.mark.parametrize("value", [None, 5, b"pr_5XvmrTA6JVggZdmEE5bGdm", ["pr_1"]])
def test_a_value_that_is_not_text_gives_no_label(value: object) -> None:
    assert project_host_label(value) is None


# -- default base URL --------------------------------------------------------


def test_api_calls_go_to_the_project_host_and_still_send_the_project_header() -> None:
    client, transport = _client()
    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith(VIRGINIA_HOST)
    assert transport.last_request["headers"]["norbix-project-id"] == VIRGINIA
    assert "nb-region" not in transport.last_request["headers"]


def test_hub_calls_stay_on_the_shared_host() -> None:
    client, transport = _client()
    client.hub.regions.list()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith("https://hub.norbix.ai/")
    assert transport.last_request["headers"]["norbix-project-id"] == VIRGINIA


def test_project_id_from_the_environment_gives_the_project_host(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("NORBIX_PROJECT_ID", GERMANY)
    client, transport = _client(project_id=None)
    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith(GERMANY_HOST)


def test_login_goes_to_the_project_host() -> None:
    client, transport = _client()
    client.login(LoginCredentials(user_name="alice", password="x"))
    assert transport.last_request is not None
    assert transport.last_request["url"] == f"{VIRGINIA_HOST}auth"


def test_a_project_id_that_is_not_a_norbix_id_keeps_the_shared_host() -> None:
    client, transport = _client(project_id="p1")
    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith("https://api.norbix.ai/")
    assert transport.last_request["headers"]["norbix-project-id"] == "p1"


def test_set_scope_moves_the_calls_to_the_new_project() -> None:
    client, transport = _client()

    client.set_scope(project_id=GERMANY)
    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith(GERMANY_HOST)
    assert transport.last_request["headers"]["norbix-project-id"] == GERMANY

    client.set_scope(project_id="p1")
    client.api.echo.echo()
    assert transport.last_request["url"].startswith("https://api.norbix.ai/")
    assert transport.last_request["headers"]["norbix-project-id"] == "p1"


def test_the_api_only_client_uses_the_project_host() -> None:
    transport = CaptureTransport()
    client = NorbixApi(
        project_id=VIRGINIA, api_key="k", http_client=httpx.Client(transport=transport)
    )
    client.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith(VIRGINIA_HOST)


def test_the_hub_only_client_stays_on_the_shared_host() -> None:
    transport = CaptureTransport()
    client = NorbixHub(
        project_id=VIRGINIA, api_key="k", http_client=httpx.Client(transport=transport)
    )
    client.regions.list()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith("https://hub.norbix.ai/")


def test_the_social_sign_in_link_stays_on_the_shared_host() -> None:
    client, _ = _client()
    url = client.api.membership.social_sign_in_url("google")
    assert url.startswith("https://api.norbix.ai/v3/membership/auth/social/google?")
    assert f"projectId={VIRGINIA}" in url


# -- with a region -----------------------------------------------------------


def test_region_api_on_the_project_host_hub_regional_header_sent() -> None:
    client, transport = _client(project_id=GERMANY, region="nb-eu-germany")

    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith(GERMANY_HOST)
    assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"
    assert transport.last_request["headers"]["norbix-project-id"] == GERMANY

    client.hub.regions.list()
    assert transport.last_request["url"].startswith("https://nb-eu-germany.hub.norbix.ai/")
    assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"


def test_region_from_the_environment_does_not_label_the_project_host(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("NORBIX_REGION", "nb-eu-germany")
    client, transport = _client(project_id=GERMANY)
    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith(GERMANY_HOST)
    assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"


def test_set_region_changes_the_hub_host_only() -> None:
    client, transport = _client(project_id=GERMANY)

    client.set_region("nb-eu-germany")
    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith(GERMANY_HOST)
    client.hub.regions.list()
    assert transport.last_request["url"].startswith("https://nb-eu-germany.hub.norbix.ai/")

    client.set_region(None)
    client.api.echo.echo()
    assert transport.last_request["url"].startswith(GERMANY_HOST)
    client.hub.regions.list()
    assert transport.last_request["url"].startswith("https://hub.norbix.ai/")


def test_region_with_an_id_that_does_not_decode_keeps_the_regional_host() -> None:
    client, transport = _client(project_id="p1", region="nb-eu-germany")
    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith("https://nb-eu-germany.api.norbix.ai/")


def test_the_social_sign_in_link_uses_the_regional_shared_host() -> None:
    client, _ = _client(project_id=GERMANY, region="nb-eu-germany")
    url = client.api.membership.social_sign_in_url("google")
    assert url.startswith("https://nb-eu-germany.api.norbix.ai/")


# -- a custom base URL is never rewritten ------------------------------------


def test_base_url_option_is_never_rewritten() -> None:
    client, transport = _client(
        region="nb-eu-germany",
        base_url_api="https://api.norbix.io",
        base_url_hub="https://hub.norbix.io",
    )

    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith("https://api.norbix.io/")
    assert transport.last_request["headers"]["norbix-project-id"] == VIRGINIA

    client.set_scope(project_id=GERMANY)
    client.api.echo.echo()
    assert transport.last_request["url"].startswith("https://api.norbix.io/")

    client.set_region(None)
    client.api.echo.echo()
    assert transport.last_request["url"].startswith("https://api.norbix.io/")

    assert client.api.membership.social_sign_in_url("google").startswith("https://api.norbix.io/")


def test_norbix_api_url_is_never_rewritten(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("NORBIX_API_URL", "https://api.norbix.io")
    client, transport = _client()
    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith("https://api.norbix.io/")


def test_norbix_api_url_with_the_default_address_written_out_is_not_rewritten(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("NORBIX_API_URL", "https://api.norbix.ai")
    client, transport = _client()
    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith("https://api.norbix.ai/")


def test_base_url_option_with_the_default_address_written_out_is_not_rewritten() -> None:
    client, transport = _client(base_url_api="https://api.norbix.ai")
    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith("https://api.norbix.ai/")


def test_custom_api_url_with_the_default_hub_url_only_the_hub_follows_the_region() -> None:
    client, transport = _client(region="nb-eu-germany", base_url_api="http://localhost:5002")
    client.api.echo.echo()
    assert transport.last_request is not None
    assert transport.last_request["url"].startswith("http://localhost:5002/")
    client.hub.regions.list()
    assert transport.last_request["url"].startswith("https://nb-eu-germany.hub.norbix.ai/")


# -- the async client --------------------------------------------------------


def test_async_default_url_project_host_and_shared_hub() -> None:
    async def run() -> None:
        client, transport = _async_client()
        await client.api.echo.echo()
        assert transport.last_request is not None
        assert transport.last_request["url"].startswith(VIRGINIA_HOST)
        assert transport.last_request["headers"]["norbix-project-id"] == VIRGINIA

        await client.hub.regions.list()
        assert transport.last_request["url"].startswith("https://hub.norbix.ai/")

        await client.login(LoginCredentials(user_name="alice", password="x"))
        assert transport.last_request["url"] == f"{VIRGINIA_HOST}auth"

        url = client.api.membership.social_sign_in_url("google")
        assert url.startswith("https://api.norbix.ai/v3/membership/auth/social/google?")
        await client.aclose()

    asyncio.run(run())


def test_async_region_api_on_the_project_host_hub_regional() -> None:
    async def run() -> None:
        client, transport = _async_client(project_id=GERMANY, region="nb-eu-germany")
        await client.api.echo.echo()
        assert transport.last_request is not None
        assert transport.last_request["url"].startswith(GERMANY_HOST)
        assert transport.last_request["headers"]["nb-region"] == "nb-eu-germany"

        await client.hub.regions.list()
        assert transport.last_request["url"].startswith("https://nb-eu-germany.hub.norbix.ai/")

        client.set_region(None)
        await client.api.echo.echo()
        assert transport.last_request["url"].startswith(GERMANY_HOST)
        await client.hub.regions.list()
        assert transport.last_request["url"].startswith("https://hub.norbix.ai/")
        await client.aclose()

    asyncio.run(run())


def test_async_custom_base_url_and_undecodable_id() -> None:
    async def run() -> None:
        client, transport = _async_client(
            region="nb-eu-germany", base_url_api="https://api.norbix.io"
        )
        await client.api.echo.echo()
        assert transport.last_request is not None
        assert transport.last_request["url"].startswith("https://api.norbix.io/")
        assert transport.last_request["headers"]["norbix-project-id"] == VIRGINIA
        await client.aclose()

        client, transport = _async_client(project_id="p1")
        await client.api.echo.echo()
        assert transport.last_request is not None
        assert transport.last_request["url"].startswith("https://api.norbix.ai/")
        assert transport.last_request["headers"]["norbix-project-id"] == "p1"
        await client.aclose()

        client, transport = _async_client(project_id="p1", region="nb-eu-germany")
        await client.api.echo.echo()
        assert transport.last_request is not None
        assert transport.last_request["url"].startswith("https://nb-eu-germany.api.norbix.ai/")
        await client.aclose()

    asyncio.run(run())
