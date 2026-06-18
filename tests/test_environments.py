from __future__ import annotations

import httpx

from norbix_python import Norbix

from .helpers import CaptureTransport


def _client(env: str | None = None) -> tuple[Norbix, CaptureTransport]:
    transport = CaptureTransport()
    http_client = httpx.Client(transport=transport)
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        env=env,
        http_client=http_client,
    )
    return client, transport


def test_prod_omits_env_header() -> None:
    client, transport = _client()
    client.hub.environments.list()
    assert transport.last_request is not None
    assert "norbix-env" not in transport.last_request["headers"]


def test_client_default_env_sets_header() -> None:
    client, transport = _client(env="TEST")
    client.hub.environments.list()
    assert transport.last_request["headers"]["norbix-env"] == "TEST"


def test_per_call_env_overrides_default() -> None:
    client, transport = _client(env="TEST")
    client.hub.environments.list(env="STAGING")
    assert transport.last_request["headers"]["norbix-env"] == "STAGING"


def test_set_env_runtime_and_prod_clears() -> None:
    client, transport = _client()
    client.set_env("TEST")
    assert client.get_env() == "TEST"
    client.hub.environments.list()
    assert transport.last_request["headers"]["norbix-env"] == "TEST"
    client.set_env("PROD")
    client.hub.environments.list()
    assert "norbix-env" not in transport.last_request["headers"]


def test_create_and_delete_routes() -> None:
    client, transport = _client()
    client.hub.environments.create(environment_name="TEST", integration={"name": "db"})
    assert transport.last_request["method"] == "POST"
    assert transport.last_request["url"].endswith("/account/projects/environments")

    client.hub.environments.delete(environment_name="TEST")
    assert transport.last_request["method"] == "DELETE"
    assert transport.last_request["url"].endswith("/account/projects/environments/TEST")
