"""Keyless cloud connections — GET /{version}/integrations/keyless/setup.

A fake httpx transport only: no gateway and no cloud are contacted.
"""

from __future__ import annotations

import asyncio
import json
from typing import Any
from urllib.parse import parse_qs, urlsplit

import httpx

from norbix_python import AsyncNorbix, Norbix

SETUP = {
    "integrationId": "int_1",
    "env": "PROD",
    "module": "files",
    "cloud": "aws",
    "issuer": "https://issuer.example",
    "available": True,
    "subject": "p/test-project/e/PROD/files/i/int_1",
    "audience": "sts.amazonaws.com",
    "script": "aws iam create-role ...",
}


class _Answer(httpx.BaseTransport):
    def __init__(self, body: dict[str, Any]) -> None:
        self.body = body
        self.request: httpx.Request | None = None

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self.request = request
        return httpx.Response(200, json=self.body)


class _AsyncAnswer(httpx.AsyncBaseTransport):
    def __init__(self, body: dict[str, Any]) -> None:
        self.body = body
        self.request: httpx.Request | None = None

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        self.request = request
        return httpx.Response(200, json=self.body)


def test_keyless_setup_sends_module_cloud_and_id_in_the_query() -> None:
    transport = _Answer(SETUP)
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=transport),
    )

    result = client.hub.integrations.get_keyless_integration_setup(
        module="files", cloud="aws", integrationId="int_1"
    )

    sent = transport.request
    assert sent is not None
    assert sent.method == "GET"
    url = urlsplit(str(sent.url))
    assert url.path.endswith("/integrations/keyless/setup")
    query = parse_qs(url.query)
    assert query["module"] == ["files"]
    assert query["cloud"] == ["aws"]
    assert query["integrationId"] == ["int_1"]
    assert sent.content == b""
    assert sent.headers["norbix-project-id"] == "test-project"
    assert result == SETUP


def test_keyless_setup_passes_the_reason_when_unavailable() -> None:
    body = {"integrationId": "int_2", "module": "email", "cloud": "azure", "available": False,
            "unavailableReason": "no signing key"}
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=_Answer(body)),
    )

    result = client.hub.integrations.get_keyless_integration_setup(module="email", cloud="azure")

    assert result["available"] is False
    assert result["unavailableReason"] == "no signing key"


def test_async_keyless_setup_uses_the_same_route() -> None:
    transport = _AsyncAnswer(SETUP)

    async def run() -> Any:
        async with AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=transport),
        ) as client:
            return await client.hub.integrations.get_keyless_integration_setup(module="files", cloud="aws")

    result = asyncio.run(run())

    assert transport.request is not None
    assert transport.request.method == "GET"
    assert urlsplit(str(transport.request.url)).path.endswith("/integrations/keyless/setup")
    assert json.loads(json.dumps(result)) == SETUP
