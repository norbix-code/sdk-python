"""The signed-in account user's own profile and phone, and the team list.

The gateway takes the account from the signed-in session for all three
(``Hub.Account/Account/Team/GetAll.cs`` and the account/me services), so every
test here runs on a client WITHOUT ``account_id`` and the call must still go
out. Sync and async clients are both covered. Nothing leaves the process.
"""
from __future__ import annotations

import asyncio
import json
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx

from norbix_python import AsyncNorbix, Norbix

PROFILE = {"item": {"id": "user_1", "email": "ada@example.test", "generalInfo": {"phone": "+37060000000"}}}


def _sync_client(seen: list[httpx.Request], answer: Any = None) -> Norbix:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json=answer if answer is not None else {})

    return Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )


def _async_client(seen: list[httpx.Request], answer: Any = None) -> AsyncNorbix:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json=answer if answer is not None else {})

    return AsyncNorbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
    )


def test_get_my_account_user_profile_reads_the_profile_and_phone() -> None:
    seen: list[httpx.Request] = []
    profile = _sync_client(seen, PROFILE).hub.account.get_my_account_user_profile()

    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [("GET", "/v2/account/me")]
    assert "x-cm-accountid" not in seen[0].headers
    assert profile["item"]["email"] == "ada@example.test"
    assert profile["item"]["generalInfo"]["phone"] == "+37060000000"


def test_update_my_account_user_phone_sends_the_phone_in_a_put_body() -> None:
    seen: list[httpx.Request] = []
    _sync_client(seen).hub.account.update_my_account_user_phone(phone="+37060000000")

    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [("PUT", "/v2/account/me/phone")]
    assert json.loads(seen[0].content) == {"phone": "+37060000000"}


def test_get_account_collaborators_sends_flat_paging_and_the_project_filter() -> None:
    # Flat query fields, no nested `pagingArgs`; `projectId` narrows the list
    # to one project's collaborators.
    seen: list[httpx.Request] = []
    _sync_client(seen).hub.account.get_account_collaborators(
        projectId="proj_2", pageSize=50, startingAfter="member_20"
    )

    url = urlparse(str(seen[0].url))
    assert (seen[0].method, url.path) == ("GET", "/v2/account/collaborators")
    assert parse_qs(url.query) == {"projectId": ["proj_2"], "pageSize": ["50"], "startingAfter": ["member_20"]}
    assert "x-cm-accountid" not in seen[0].headers


def test_async_account_me_and_team_list_need_only_a_token() -> None:
    seen: list[httpx.Request] = []

    async def run() -> Any:
        client = _async_client(seen, PROFILE)
        try:
            account = client.hub.account
            profile = await account.get_my_account_user_profile()
            await account.update_my_account_user_phone(phone="+37060000000")
            await account.get_account_collaborators(pageSize=20)
            return profile
        finally:
            await client.aclose()

    profile = asyncio.run(run())

    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [
        ("GET", "/v2/account/me"),
        ("PUT", "/v2/account/me/phone"),
        ("GET", "/v2/account/collaborators"),
    ]
    assert profile["item"]["generalInfo"]["phone"] == "+37060000000"
    assert json.loads(seen[1].content) == {"phone": "+37060000000"}
    assert parse_qs(urlparse(str(seen[2].url)).query) == {"pageSize": ["20"]}
