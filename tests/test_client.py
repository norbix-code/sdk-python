from __future__ import annotations

import httpx

import pytest

from norbix_python import LoginCredentials, Norbix, NorbixError
from norbix_python.facade.database import Collection
from norbix_python.models import AuthLoginResult


def test_norbix_allows_init_without_project_for_login_flow() -> None:
    with Norbix(base_url_api="https://api.example.test") as client:
        assert client._transport._cfg.project_id is None


def test_project_scope_requires_project_id() -> None:
    client = Norbix(bearer_token="token")
    with pytest.raises(NorbixError) as excinfo:
        client.api.echo.echo({})
    assert excinfo.value.code == "NORBIX_PROJECT_SCOPE_REQUIRED"


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
    result = client.login(LoginCredentials(user_name="alice", password="secret"))
    assert result["bearerToken"] == "new-token"
    assert client.is_authenticated() is True
    AuthLoginResult.model_validate(result)


def test_context_manager_closes() -> None:
    c = httpx.Client()
    with Norbix(project_id="p1", http_client=c) as _client:
        pass
    assert c.is_closed


def test_collection_facade() -> None:
    client = Norbix(project_id="p1", bearer_token="t")
    col = client.collection("orders")
    assert isinstance(col, Collection)
    assert col.name == "orders"
