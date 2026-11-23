"""Saved secrets of an integration — GET /{version}/integrations/{IntegrationId}/secrets and
POST /{version}/integrations/{IntegrationId}/secrets/remove. The read never carries a value.

A fake httpx transport only: no gateway is contacted.
"""

from __future__ import annotations

import asyncio
import json
from typing import Any
from urllib.parse import parse_qs, urlsplit

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix
from norbix_python.errors import NorbixError

ROWS = {
    "result": [
        {"key": "secretKey", "field": "secretKey", "isSet": True, "isOptional": False},
        {"key": "webhookSigningSecret", "field": "webhookSigningSecret", "isSet": False, "isOptional": True},
    ]
}


class _Answer(httpx.BaseTransport):
    def __init__(self, body: dict[str, Any], status: int = 200) -> None:
        self.body = body
        self.status = status
        self.request: httpx.Request | None = None

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self.request = request
        return httpx.Response(self.status, json=self.body)


class _AsyncAnswer(httpx.AsyncBaseTransport):
    def __init__(self, body: dict[str, Any]) -> None:
        self.body = body
        self.request: httpx.Request | None = None

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        self.request = request
        return httpx.Response(200, json=self.body)


def _client(transport: httpx.BaseTransport) -> Norbix:
    return Norbix(project_id="test-project", bearer_token="test-token", http_client=httpx.Client(transport=transport))


def test_get_integration_secrets_puts_the_id_in_the_path_and_env_in_the_query() -> None:
    transport = _Answer(ROWS)

    result = _client(transport).hub.integrations.get_integration_secrets("int_1", env="TEST")

    sent = transport.request
    assert sent is not None
    assert sent.method == "GET"
    url = urlsplit(str(sent.url))
    assert url.path.endswith("/integrations/int_1/secrets")
    assert parse_qs(url.query).get("env") == ["TEST"]
    assert result["result"][0] == {"key": "secretKey", "field": "secretKey", "isSet": True, "isOptional": False}
    assert all("value" not in row for row in result["result"])


def test_remove_integration_secrets_sends_the_keys_in_the_body() -> None:
    transport = _Answer({"id": "int_1"})

    result = _client(transport).hub.integrations.remove_integration_secrets("int_1", ["webhookSigningSecret"])

    sent = transport.request
    assert sent is not None
    assert sent.method == "POST"
    assert urlsplit(str(sent.url)).path.endswith("/integrations/int_1/secrets/remove")
    assert json.loads(sent.content)["keys"] == ["webhookSigningSecret"]
    assert result["id"] == "int_1"


def test_remove_integration_secrets_needed_key_raises() -> None:
    transport = _Answer(
        {"responseStatus": {"isSuccess": False, "errorCode": "CM-ERRORS-SECRETS-012", "message": "needed"}}, 400
    )

    with pytest.raises(NorbixError):
        _client(transport).hub.integrations.remove_integration_secrets("int_1", ["secretKey"])


def test_async_integration_secrets() -> None:
    transport = _AsyncAnswer(ROWS)

    async def run() -> Any:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=transport),
        )
        rows = await client.hub.integrations.get_integration_secrets("int_1")
        assert transport.request is not None
        assert urlsplit(str(transport.request.url)).path.endswith("/integrations/int_1/secrets")
        await client.hub.integrations.remove_integration_secrets("int_1", ["webhookSigningSecret"])
        assert transport.request is not None
        assert json.loads(transport.request.content)["keys"] == ["webhookSigningSecret"]
        return rows

    rows = asyncio.run(run())
    assert len(rows["result"]) == 2
