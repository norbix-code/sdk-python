from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any

import httpx
import pytest

from norbix_python import (
    EMAIL_NOT_VERIFIED_ERROR_CODE,
    AsyncNorbix,
    AuthenticationError,
    ErrorItem,
    LoginCredentials,
    Norbix,
    NorbixError,
    is_email_not_verified_error,
)

"""E-mail address verification for e-mail + password project users.

``verify_email_address(token)`` and ``resend_email_address_verification(email)``
call the two public routes under ``/membership/userauth/email-verification``
(sync and async). They are sent by a visitor who is not signed in: a client
with a project id but no api key and no bearer token sends them with no
``Authorization`` header. A password sign-in refused with
``CM-ERRORS-MEMBERSHIP-USERS-052`` is told apart with
``is_email_not_verified_error``. Every call goes to a mock transport.
"""

API = "https://api.test"
CLIENT_ARGS: dict[str, Any] = {
    "project_id": "test-project",
    "base_url_api": API,
    "base_url_hub": "https://hub.test",
    "api_version": "v2",
    "hub_version": "v2",
}

VERIFIED = {"authId": "auth_1", "verifiedAtUtc": "2026-11-22T10:00:00Z"}

# method name, positional argument, extra kwargs, exact path, expected body
CASES = [
    (
        "verify_email_address",
        "tok_1",
        {},
        "/v2/membership/userauth/email-verification/confirm",
        {"token": "tok_1"},
    ),
    (
        "verify_email_address",
        "tok_1",
        {"databaseIntegrationId": "int_1"},
        "/v2/membership/userauth/email-verification/confirm",
        {"token": "tok_1", "databaseIntegrationId": "int_1"},
    ),
    (
        "resend_email_address_verification",
        "ana@example.test",
        {},
        "/v2/membership/userauth/email-verification/resend",
        {"email": "ana@example.test"},
    ),
    (
        "resend_email_address_verification",
        "ana@example.test",
        {"databaseIntegrationId": "int_1"},
        "/v2/membership/userauth/email-verification/resend",
        {"email": "ana@example.test", "databaseIntegrationId": "int_1"},
    ),
]
IDS = [f"{c[0]}-{'db' if c[2] else 'plain'}" for c in CASES]


def _capture(seen: list[httpx.Request], answer: Any = None) -> Callable[[httpx.Request], httpx.Response]:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json=answer if answer is not None else {})

    return handler


def _assert_public_post(request: httpx.Request, path: str, body: dict[str, Any]) -> None:
    assert request.method == "POST"
    assert request.url.host == "api.test"
    assert request.url.path == path
    assert json.loads(request.content) == body
    assert "authorization" not in request.headers
    assert request.headers["norbix-project-id"] == "test-project"


@pytest.mark.parametrize(("name", "arg", "extra", "path", "body"), CASES, ids=IDS)
def test_sync_route_is_public(name: str, arg: str, extra: dict[str, Any], path: str, body: dict[str, Any]) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))))
    try:
        getattr(client.api.membership, name)(arg, **extra)
    finally:
        client.close()
    assert len(seen) == 1
    _assert_public_post(seen[0], path, body)


@pytest.mark.parametrize(("name", "arg", "extra", "path", "body"), CASES, ids=IDS)
def test_async_route_is_public(name: str, arg: str, extra: dict[str, Any], path: str, body: dict[str, Any]) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        async with httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))) as http:
            client = AsyncNorbix(**CLIENT_ARGS, http_client=http)
            await getattr(client.api.membership, name)(arg, **extra)

    asyncio.run(run())
    assert len(seen) == 1
    _assert_public_post(seen[0], path, body)


def test_verify_returns_the_answer() -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen, VERIFIED))))
    try:
        answer = client.api.membership.verify_email_address("tok_1")
    finally:
        client.close()
    assert answer["authId"] == "auth_1"
    assert answer["verifiedAtUtc"] == "2026-11-22T10:00:00Z"


def test_a_client_with_a_key_still_sends_it() -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, api_key="key_1", http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))))
    try:
        client.api.membership.resend_email_address_verification("ana@example.test")
    finally:
        client.close()
    assert seen[0].headers["authorization"] == "Bearer key_1"


def test_constant_is_the_gateway_code() -> None:
    assert EMAIL_NOT_VERIFIED_ERROR_CODE == "CM-ERRORS-MEMBERSHIP-USERS-052"


def test_helper_matches_the_code_or_an_item() -> None:
    assert is_email_not_verified_error(NorbixError("x", status=401, code=EMAIL_NOT_VERIFIED_ERROR_CODE))
    assert is_email_not_verified_error(
        NorbixError("x", status=401, code="OTHER", errors=[ErrorItem(error_code=EMAIL_NOT_VERIFIED_ERROR_CODE)])
    )
    assert not is_email_not_verified_error(NorbixError("x", status=401, code="CM-ERRORS-MEMBERSHIP-USERS-050"))
    assert not is_email_not_verified_error(ValueError(EMAIL_NOT_VERIFIED_ERROR_CODE))
    assert not is_email_not_verified_error(None)


def test_password_sign_in_refusal_is_recognised() -> None:
    """A 401 with responseStatus.errorCode 052 from the sign-in call."""

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            401,
            json={
                "responseStatus": {
                    "errorCode": EMAIL_NOT_VERIFIED_ERROR_CODE,
                    "message": "E-mail address is not verified.",
                }
            },
        )

    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(handler)))
    try:
        with pytest.raises(AuthenticationError) as caught:
            client.login(LoginCredentials(user_name="ana@example.test", password="S3cret-pass!"))
    finally:
        client.close()
    assert is_email_not_verified_error(caught.value)
    assert caught.value.error_code == EMAIL_NOT_VERIFIED_ERROR_CODE
