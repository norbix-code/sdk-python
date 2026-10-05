"""Every account route that needs only a token (no ``account_id``).

The gateway takes the account from the signed-in session on each route below
(``UserSession.UserAuth.AccountId``), or from the project id in the path, or
needs no account at all — and it never reads the ``X-CM-AccountId`` header.
So each method must work on a client WITHOUT ``account_id``, like the
TypeScript, .NET, Go, Kotlin and Swift SDKs. One test per method, for the
sync and the async client: verb, resolved path, Bearer header and no account
header. Nothing leaves the process.

Four routes are public on the gateway (no ``[Authenticate]``): sign-up
(``create_account``), accepting an invitation
(``create_team_member_from_invitation``), the region list
(``get_account_regions`` / ``regions.list``) and ``verify_account``. They go
out with NO token at all; ``verify_account`` sends the account id once, in the
request (the gateway reads ``VerifyAccount.AccountId``, ``Account/Verify.cs``).
"""
from __future__ import annotations

import asyncio
import json
from typing import Any
from urllib.parse import parse_qsl, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

# (module, method, verb, path, positional route ids)
CASES: list[tuple[str, str, str, str, dict[str, str]]] = [
    ("account", "get_account_profile", "GET", "/v2/account/profile", {}),
    ("account", "update_account_profile", "PUT", "/v2/account/profile", {}),
    ("account", "resend_account_verification_token", "GET", "/v2/account/verify/resend", {}),
    ("account", "get_account_status", "GET", "/v2/account/status", {}),
    ("account", "create_stripe_checkout_session", "POST", "/v2/account/stripe/create-checkout-session", {}),
    ("account", "get_stripe_billing_portal_url", "POST", "/v2/account/stripe/get-portal-url", {}),
    ("account", "delete_notifications_group", "DELETE", "/v2/account/projects/project_id_1/notifications/settings/group", {'project_id': "project_id_1"}),
    ("account", "delete_notifications_tag", "DELETE", "/v2/account/projects/project_id_1/notifications/settings/tag", {'project_id': "project_id_1"}),
    ("account", "remove_tag_from_notifications_group", "DELETE", "/v2/account/projects/project_id_1/notifications/settings/group/tag", {'project_id': "project_id_1"}),
    ("account", "save_notifications_group", "POST", "/v2/account/projects/project_id_1/notifications/settings/group", {'project_id': "project_id_1"}),
    ("account", "save_notifications_tag", "POST", "/v2/account/projects/project_id_1/notifications/settings/tag", {'project_id': "project_id_1"}),
    ("account", "create_project", "POST", "/v2/account/projects", {}),
    ("account", "delete_project", "DELETE", "/v2/account/projects/project_id_1", {'project_id': "project_id_1"}),
    ("account", "get_project", "GET", "/v2/account/projects/project_id_1", {'project_id': "project_id_1"}),
    ("account", "get_projects", "GET", "/v2/account/projects", {}),
    ("account", "get_project_tokens", "GET", "/v2/account/projects/project_id_1/tokens", {'project_id': "project_id_1"}),
    ("account", "update_project_accent_color", "PATCH", "/v2/account/projects/project_id_1/settings/accent-color", {'project_id': "project_id_1"}),
    ("account", "update_project_icon", "PATCH", "/v2/account/projects/project_id_1/settings/icon", {'project_id': "project_id_1"}),
    ("account", "update_project_logo", "PATCH", "/v2/account/projects/project_id_1/settings/logo", {'project_id': "project_id_1"}),
    ("account", "update_project_main_color", "PATCH", "/v2/account/projects/project_id_1/settings/main-color", {'project_id': "project_id_1"}),
    ("account", "update_project_allowed_origins", "PATCH", "/v2/account/projects/project_id_1/settings/origins", {'project_id': "project_id_1"}),
    ("account", "update_project_default_language", "PATCH", "/v2/account/projects/project_id_1/settings/default-language", {'project_id': "project_id_1"}),
    ("account", "update_project_description", "PATCH", "/v2/account/projects/project_id_1/settings/description", {'project_id': "project_id_1"}),
    ("account", "disable_project", "PATCH", "/v2/account/projects/project_id_1/disable", {'project_id': "project_id_1"}),
    ("account", "enable_project", "PATCH", "/v2/account/projects/project_id_1/enable", {'project_id': "project_id_1"}),
    ("account", "check_project_languages", "POST", "/v2/account/projects/project_id_1/settings/languages/check", {'project_id': "project_id_1"}),
    ("account", "update_project_languages", "PATCH", "/v2/account/projects/project_id_1/settings/languages", {'project_id': "project_id_1"}),
    ("account", "update_project_url", "PATCH", "/v2/account/projects/project_id_1/settings/url", {'project_id': "project_id_1"}),
    ("account", "update_project_name", "PATCH", "/v2/account/projects/project_id_1/settings/name", {'project_id': "project_id_1"}),
    ("account", "update_project_regions", "PATCH", "/v2/account/projects/project_id_1/settings/regions", {'project_id': "project_id_1"}),
    ("account", "send_invite_to_team_member", "POST", "/v2/account/team/member/invite", {}),
    ("account", "get_licenses", "GET", "/v2/account/licenses", {}),
    ("regions", "update_project_regions", "PATCH", "/v2/account/projects/project_id_1/settings/regions", {'project_id': "project_id_1"}),
]

IDS = [f"{module}.{method}" for module, method, *_ in CASES]


@pytest.fixture(autouse=True)
def _no_account_id_from_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("NORBIX_ACCOUNT_ID", raising=False)


def _handler(seen: list[httpx.Request]) -> Any:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    return handler


def _assert_token_only(seen: list[httpx.Request], verb: str, path: str) -> None:
    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [(verb, path)]
    assert seen[0].headers["authorization"] == "Bearer test-token"
    assert "x-cm-accountid" not in seen[0].headers


@pytest.mark.parametrize(("module", "method", "verb", "path", "ids"), CASES, ids=IDS)
def test_account_route_works_with_a_token_and_no_account_id(
    module: str, method: str, verb: str, path: str, ids: dict[str, str]
) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=httpx.MockTransport(_handler(seen))),
    )

    getattr(getattr(client.hub, module), method)(**ids)

    _assert_token_only(seen, verb, path)


@pytest.mark.parametrize(("module", "method", "verb", "path", "ids"), CASES, ids=IDS)
def test_async_account_route_works_with_a_token_and_no_account_id(
    module: str, method: str, verb: str, path: str, ids: dict[str, str]
) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_handler(seen))),
        )
        try:
            await getattr(getattr(client.hub, module), method)(**ids)
        finally:
            await client.aclose()

    asyncio.run(run())

    _assert_token_only(seen, verb, path)


# (module, method, verb, path, request fields)
PUBLIC_CASES: list[tuple[str, str, str, str, dict[str, str]]] = [
    ("account", "create_account", "POST", "/v2/account", {"email": "ada@example.test", "password": "pw", "displayName": "Ada"}),
    ("account", "create_team_member_from_invitation", "POST", "/v2/account/team/member", {"token": "invite-1", "password": "pw", "displayName": "Ada"}),
    ("account", "get_account_regions", "GET", "/v2/account/regions", {}),
    ("regions", "list", "GET", "/v2/account/regions", {}),
    ("account", "verify_account", "GET", "/v2/account/verify", {"accountId": "acc-1", "token": "verify-1"}),
]

PUBLIC_IDS = [f"{module}.{method}" for module, method, *_ in PUBLIC_CASES]


def _assert_public(seen: list[httpx.Request], verb: str, path: str, fields: dict[str, str]) -> None:
    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [(verb, path)]
    assert "authorization" not in seen[0].headers
    assert "x-cm-accountid" not in seen[0].headers
    if verb == "GET":
        assert dict(parse_qsl(urlparse(str(seen[0].url)).query)) == fields
    else:
        assert json.loads(seen[0].content) == fields


@pytest.mark.parametrize(("module", "method", "verb", "path", "fields"), PUBLIC_CASES, ids=PUBLIC_IDS)
def test_public_account_route_works_with_no_token_and_no_account_id(
    module: str, method: str, verb: str, path: str, fields: dict[str, str], monkeypatch: pytest.MonkeyPatch
) -> None:
    for name in ("NORBIX_API_KEY", "NORBIX_BEARER_TOKEN"):
        monkeypatch.delenv(name, raising=False)
    seen: list[httpx.Request] = []
    client = Norbix(
        project_id="test-project",
        http_client=httpx.Client(transport=httpx.MockTransport(_handler(seen))),
    )

    getattr(getattr(client.hub, module), method)(**fields)

    _assert_public(seen, verb, path, fields)


@pytest.mark.parametrize(("module", "method", "verb", "path", "fields"), PUBLIC_CASES, ids=PUBLIC_IDS)
def test_async_public_account_route_works_with_no_token_and_no_account_id(
    module: str, method: str, verb: str, path: str, fields: dict[str, str], monkeypatch: pytest.MonkeyPatch
) -> None:
    for name in ("NORBIX_API_KEY", "NORBIX_BEARER_TOKEN"):
        monkeypatch.delenv(name, raising=False)
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(
            project_id="test-project",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_handler(seen))),
        )
        try:
            await getattr(getattr(client.hub, module), method)(**fields)
        finally:
            await client.aclose()

    asyncio.run(run())

    _assert_public(seen, verb, path, fields)
