"""Sessions (D18): the rememberMe sign-in flag and the norbix-session-token swap.

A project sign-in's JWT slides 12 hours (30 days with rememberMe, never past
90 days from sign-in). Past half its window an answer carries a fresh JWT in
the ``norbix-session-token`` header; a client that sent its stored bearer
token swaps it and tells the app through ``on_session_token``.
"""

from __future__ import annotations

import asyncio
import json

import httpx

from norbix_python import AsyncNorbix, LoginCredentials, Norbix, NorbixApi, NorbixHub

FRESH = "fresh-jwt"


def _handler(header: str | None, seen: list[httpx.Request]):  # type: ignore[no-untyped-def]
    def handle(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        headers = {} if header is None else {"norbix-session-token": header}
        return httpx.Response(200, json={}, headers=headers)

    return handle


def _client(
    header: str | None,
    *,
    bearer_token: str | None = "old-jwt",
    api_key: str | None = None,
    tokens: list[str] | None = None,
) -> tuple[Norbix, list[httpx.Request]]:
    seen: list[httpx.Request] = []
    client = Norbix(
        project_id="test-project",
        bearer_token=bearer_token,
        api_key=api_key,
        on_session_token=None if tokens is None else tokens.append,
        http_client=httpx.Client(transport=httpx.MockTransport(_handler(header, seen))),
    )
    return client, seen


def test_header_present_swaps_the_bearer_token_and_calls_back() -> None:
    tokens: list[str] = []
    client, seen = _client(FRESH, tokens=tokens)
    client.hub.account.get_account_profile()
    assert tokens == [FRESH]
    assert client._transport._cfg.bearer_token == FRESH
    # The next call sends the new token.
    client.hub.account.get_account_profile()
    assert seen[0].headers["authorization"] == "Bearer old-jwt"
    assert seen[1].headers["authorization"] == f"Bearer {FRESH}"


def test_header_absent_leaves_the_token_alone() -> None:
    tokens: list[str] = []
    client, _ = _client(None, tokens=tokens)
    client.hub.account.get_account_profile()
    assert tokens == []
    assert client._transport._cfg.bearer_token == "old-jwt"


def test_empty_header_is_ignored() -> None:
    tokens: list[str] = []
    client, _ = _client("  ", tokens=tokens)
    client.hub.account.get_account_profile()
    assert tokens == []
    assert client._transport._cfg.bearer_token == "old-jwt"


def test_api_key_client_never_swaps() -> None:
    tokens: list[str] = []
    client, seen = _client(FRESH, bearer_token=None, api_key="sk_test", tokens=tokens)
    client.hub.account.get_account_profile()
    assert seen[0].headers["authorization"] == "Bearer sk_test"
    assert tokens == []
    assert client._transport._cfg.bearer_token is None
    assert client._transport._cfg.api_key == "sk_test"


def test_a_per_call_token_does_not_replace_the_stored_one() -> None:
    tokens: list[str] = []
    client, _ = _client(FRESH, tokens=tokens)
    client.hub.account.get_account_profile(bearer_token="other-jwt")
    assert tokens == []
    assert client._transport._cfg.bearer_token == "old-jwt"


def test_swap_works_without_a_callback() -> None:
    client, _ = _client(FRESH)
    client.hub.account.get_account_profile()
    assert client._transport._cfg.bearer_token == FRESH


def test_split_clients_take_the_callback() -> None:
    for cls in (NorbixApi, NorbixHub):
        tokens: list[str] = []
        seen: list[httpx.Request] = []
        client = cls(
            project_id="test-project",
            bearer_token="old-jwt",
            on_session_token=tokens.append,
            http_client=httpx.Client(transport=httpx.MockTransport(_handler(FRESH, seen))),
        )
        client.echo.echo()
        assert tokens == [FRESH], cls.__name__


def test_async_client_swaps_and_calls_back() -> None:
    tokens: list[str] = []
    seen: list[httpx.Request] = []

    async def run() -> str | None:
        async with AsyncNorbix(
            project_id="test-project",
            bearer_token="old-jwt",
            on_session_token=tokens.append,
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_handler(FRESH, seen))),
        ) as client:
            await client.hub.account.get_account_profile()
            return client._transport._cfg.bearer_token

    assert asyncio.run(run()) == FRESH
    assert tokens == [FRESH]


def test_async_api_key_client_never_swaps() -> None:
    tokens: list[str] = []
    seen: list[httpx.Request] = []

    async def run() -> str | None:
        async with AsyncNorbix(
            project_id="test-project",
            api_key="sk_test",
            on_session_token=tokens.append,
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_handler(FRESH, seen))),
        ) as client:
            await client.hub.account.get_account_profile()
            return client._transport._cfg.bearer_token

    assert asyncio.run(run()) is None
    assert tokens == []


def _login_body(credentials: LoginCredentials) -> dict[str, object]:
    seen: list[httpx.Request] = []
    client = Norbix(
        project_id="test-project",
        http_client=httpx.Client(transport=httpx.MockTransport(_handler(None, seen))),
    )
    client.login(credentials)
    assert seen[0].url.path == "/auth"
    body: dict[str, object] = json.loads(seen[0].content)
    return body


def test_login_sends_remember_me_false_by_default() -> None:
    body = _login_body(LoginCredentials(user_name="alice@team.io", password="secret"))
    assert body["rememberMe"] is False
    assert body["provider"] == "credentials"


def test_login_sends_remember_me_true() -> None:
    body = _login_body(LoginCredentials(user_name="alice@team.io", password="secret", remember_me=True))
    assert body["rememberMe"] is True


def test_async_login_sends_remember_me() -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        async with AsyncNorbix(
            project_id="test-project",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_handler(None, seen))),
        ) as client:
            await client.login(LoginCredentials(userName="alice@team.io", password="secret", rememberMe=True))

    asyncio.run(run())
    assert json.loads(seen[0].content)["rememberMe"] is True
