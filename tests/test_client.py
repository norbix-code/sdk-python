from __future__ import annotations

import httpx

from norbix_python import LoginCredentials, Norbix


def test_requires_project_scope() -> None:
    try:
        Norbix()
    except ValueError:
        return
    raise AssertionError("Expected project_id validation error")


def test_auth_state_transitions() -> None:
    client = Norbix(project_id="p1", api_key="k1")
    assert client.is_authenticated() is True
    client.set_api_key(None)
    assert client.is_authenticated() is False
    client.set_bearer_token("jwt")
    assert client.is_authenticated() is True


def test_login_updates_bearer_token() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/auth"):
            return httpx.Response(200, json={"bearerToken": "new-token"})
        return httpx.Response(200, json={})

    mock_client = httpx.Client(transport=httpx.MockTransport(handler))
    client = Norbix(project_id="p1", http_client=mock_client)
    result = client.login(LoginCredentials(userName="alice", password="secret"))
    assert result["bearerToken"] == "new-token"
    assert client.is_authenticated() is True
