"""Public file links — the five endpoints slice PUB added to the gateway.

10b-files, slice SDK-2. Written by hand: the generated tests in
``tests/hub/test_files.py`` and ``tests/api/test_files.py`` are refreshed from
the module sources and would lose these.

Each test builds its own client and its own fake response, so the order the
tests run in does not matter and no real storage provider is contacted.
"""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import urlparse

import httpx
import pytest

from norbix_python import Norbix

from .helpers import make_client

INTEGRATION_ID = "44444444-4444-4444-4444-444444444444"
PUBLIC_ID = "nbpf_7hK2abc"


def _sent(transport):
    request = transport.last_request
    assert request is not None, "no request was sent"
    url = urlparse(request["url"])
    body = json.loads(request["body"]) if request["body"] else {}
    return request["method"], url.path, body, request["headers"]


# --- hub: make it public, make it private ------------------------------------


@pytest.mark.parametrize(
    ("method_name", "expected_path"),
    [
        ("make_file_public", "/v2/files/item/public"),
        ("make_file_private", "/v2/files/item/private"),
        ("make_folder_public", "/v2/files/folder/public"),
        ("make_folder_private", "/v2/files/folder/private"),
    ],
)
def test_hub_method_hits_its_own_route(method_name: str, expected_path: str) -> None:
    client, transport = make_client()
    getattr(client.hub.files, method_name)(
        filesIntegrationId=INTEGRATION_ID, path="invoices/invoice.pdf"
    )
    verb, path, body, headers = _sent(transport)
    assert (verb, path) == ("POST", expected_path)
    assert body == {"filesIntegrationId": INTEGRATION_ID, "path": "invoices/invoice.pdf"}
    assert headers["authorization"] == "Bearer test-token"
    assert headers["x-cm-projectid"] == "test-project"


def test_make_file_public_gives_back_the_minted_id() -> None:
    class Answers(httpx.BaseTransport):
        def handle_request(self, request: httpx.Request) -> httpx.Response:
            return httpx.Response(200, json={"id": PUBLIC_ID, "status": "Success"})

    client = Norbix(
        project_id="p",
        bearer_token="t",
        http_client=httpx.Client(transport=Answers()),
    )
    result = client.hub.files.make_file_public(
        filesIntegrationId=INTEGRATION_ID, path="invoices/invoice.pdf"
    )
    assert result["id"] == PUBLIC_ID


def test_all_four_methods_exist_sync_and_async() -> None:
    from norbix_python.hub.files import AsyncFilesModule, FilesModule

    for name in (
        "make_file_public",
        "make_file_private",
        "make_folder_public",
        "make_folder_private",
    ):
        assert callable(getattr(FilesModule, name)), name
        assert callable(getattr(AsyncFilesModule, name)), name


# --- api: the link anyone can open -------------------------------------------


class BinaryTransport(httpx.BaseTransport):
    """Answers with real bytes, like a file server does."""

    def __init__(self, payload: bytes, status: int = 200) -> None:
        self.payload = payload
        self.status = status
        self.last_request: dict[str, Any] | None = None

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self.last_request = {
            "url": str(request.url),
            "headers": dict(request.headers),
        }
        return httpx.Response(
            self.status,
            content=self.payload,
            headers={"Content-Type": "application/pdf"},
        )


def _public_client(transport: httpx.BaseTransport) -> Norbix:
    # No bearer token and no API key: somebody who has never signed in. A
    # project_id is still required to build the client at all — see finding F3
    # in the slice report; a public link itself carries none.
    return Norbix(
        project_id="not-used-by-a-public-link",
        api_version="v3",
        http_client=httpx.Client(transport=transport),
    )


def test_get_public_file_returns_the_bytes_unchanged() -> None:
    payload = b"%PDF-1.7 hello"
    transport = BinaryTransport(payload)

    result = _public_client(transport).api.files.get_public_file(PUBLIC_ID, "invoice.pdf")

    assert result == payload
    assert urlparse(transport.last_request["url"]).path == f"/v3/files/public/{PUBLIC_ID}/invoice.pdf"


def test_get_public_file_sends_no_authorization_header() -> None:
    transport = BinaryTransport(b"x")

    _public_client(transport).api.files.get_public_file(PUBLIC_ID, "invoice.pdf")

    assert "authorization" not in transport.last_request["headers"]


def test_get_public_file_sends_no_authorization_even_when_signed_in() -> None:
    transport = BinaryTransport(b"x")
    client = Norbix(
        project_id="test-project",
        bearer_token="a-real-session",
        api_version="v3",
        http_client=httpx.Client(transport=transport),
    )

    client.api.files.get_public_file(PUBLIC_ID, "invoice.pdf")

    assert "authorization" not in transport.last_request["headers"]


def test_a_folder_relative_path_keeps_its_slashes() -> None:
    transport = BinaryTransport(b"x")

    _public_client(transport).api.files.get_public_file("nbpf_folder1", "2026/q1/report.pdf")

    assert (
        urlparse(transport.last_request["url"]).path
        == "/v3/files/public/nbpf_folder1/2026/q1/report.pdf"
    )


def test_a_link_that_points_at_nothing_raises() -> None:
    transport = BinaryTransport(b"", status=404)

    with pytest.raises(Exception) as caught:
        _public_client(transport).api.files.get_public_file("nbpf_gone", "invoice.pdf")

    assert getattr(caught.value, "status", None) == 404


def test_it_follows_the_redirect_a_signing_provider_answers_with() -> None:
    """S3 / Azure / Google Cloud sign their own links, so the gateway replies
    302 and the bytes come from the provider. httpx does NOT follow redirects
    by default, so without ``follow_redirects=True`` this call would hand back
    an empty 302 and look like an empty file."""
    payload = b"bytes-from-the-provider"

    class Redirecting(httpx.BaseTransport):
        def handle_request(self, request: httpx.Request) -> httpx.Response:
            if "files/public" in str(request.url):
                return httpx.Response(
                    302, headers={"Location": "https://bucket.s3.example.com/signed"}
                )
            return httpx.Response(200, content=payload)

    result = _public_client(Redirecting()).api.files.get_public_file(PUBLIC_ID, "invoice.pdf")

    assert result == payload


def test_get_public_file_exists_sync_and_async() -> None:
    from norbix_python.api.files import AsyncFilesModule, FilesModule

    assert callable(FilesModule.get_public_file)
    assert callable(AsyncFilesModule.get_public_file)
