from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, NorbixError

"""The routes the gateway does not authenticate must leave the SDK with no token.

Public sign-up (``/membership/auth/register/email`` and ``/register/user-name``)
and the password reset request are called by a visitor who is not signed in
yet. They go through the real ``client.api.membership`` methods (sync and
async) of a client that has a project id but no api key and no bearer token:
the request is sent, with no ``Authorization`` header and with the
``norbix-project-id`` header. A client that has a key still sends it. A route
that needs sign-in (block user) still refuses before anything is sent.
"""

API = "https://api.test"
HUB = "https://hub.test"
PROJECT = "test-project"
CLIENT_ARGS: dict[str, Any] = {
    "project_id": PROJECT,
    "base_url_api": API,
    "base_url_hub": HUB,
    "api_version": "v2",
    "hub_version": "v2",
}

EMAIL = {"email": "ana@example.test", "password": "S3cret-pass!"}
USER_NAME = {"userName": "ana", "password": "S3cret-pass!"}
RESET = {"email": "ana@example.test"}

# method name, request body, exact path
PUBLIC_CASES = [
    ("save_email_user", EMAIL, "/v2/membership/auth/register/email"),
    ("save_user_name_user", USER_NAME, "/v2/membership/auth/register/user-name"),
    ("request_password_reset", RESET, "/v2/membership/userauth/password/reset/request"),
]
PUBLIC_IDS = [case[0] for case in PUBLIC_CASES]


def _capture(seen: list[httpx.Request]) -> Callable[[httpx.Request], httpx.Response]:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    return handler


def _call_sync(
    name: str, body: dict[str, Any], seen: list[httpx.Request], **credentials: str
) -> None:
    client = Norbix(
        **CLIENT_ARGS,
        **credentials,
        http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))),
    )
    try:
        getattr(client.api.membership, name)(**body)
    finally:
        client.close()


def _call_async(
    name: str, body: dict[str, Any], seen: list[httpx.Request], **credentials: str
) -> None:
    async def run() -> None:
        async with httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))) as http:
            client = AsyncNorbix(**CLIENT_ARGS, **credentials, http_client=http)
            await getattr(client.api.membership, name)(**body)

    asyncio.run(run())


CALLERS = [_call_sync, _call_async]
CALLER_IDS = ["sync", "async"]


def _assert_public_request(request: httpx.Request, path: str, body: dict[str, Any]) -> None:
    assert request.method == "POST"
    assert str(request.url) == f"{API}{path}"
    assert json.loads(request.content) == body
    assert request.headers.get("norbix-project-id") == PROJECT


@pytest.mark.parametrize("call", CALLERS, ids=CALLER_IDS)
@pytest.mark.parametrize("name, body, path", PUBLIC_CASES, ids=PUBLIC_IDS)
def test_public_route_goes_out_with_no_credentials(
    call: Callable[..., None], name: str, body: dict[str, Any], path: str
) -> None:
    seen: list[httpx.Request] = []
    call(name, body, seen)

    assert len(seen) == 1
    _assert_public_request(seen[0], path, body)
    assert "Authorization" not in seen[0].headers


@pytest.mark.parametrize("call", CALLERS, ids=CALLER_IDS)
def test_register_with_email_sends_the_api_key_when_set(
    call: Callable[..., None],
) -> None:
    seen: list[httpx.Request] = []
    call("save_email_user", EMAIL, seen, api_key="key_1")

    assert len(seen) == 1
    _assert_public_request(seen[0], "/v2/membership/auth/register/email", EMAIL)
    assert seen[0].headers.get("Authorization") == "Bearer key_1"


@pytest.mark.parametrize("call", CALLERS, ids=CALLER_IDS)
def test_register_with_email_sends_the_bearer_token_when_set(
    call: Callable[..., None],
) -> None:
    seen: list[httpx.Request] = []
    call("save_email_user", EMAIL, seen, bearer_token="tok_1")

    assert len(seen) == 1
    assert seen[0].headers.get("Authorization") == "Bearer tok_1"


@pytest.mark.parametrize("call", CALLERS, ids=CALLER_IDS)
def test_signed_in_route_still_refuses_with_no_credentials(
    call: Callable[..., None],
) -> None:
    seen: list[httpx.Request] = []

    with pytest.raises(NorbixError) as exc:
        call("block_user", {"id": "usr_1"}, seen)

    assert exc.value.code == "NORBIX_NOT_AUTHENTICATED"
    assert seen == []
