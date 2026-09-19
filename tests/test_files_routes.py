"""Files endpoints: the route each SDK method actually calls.

The generated tests in ``tests/hub/test_files.py`` and ``tests/api/test_files.py``
only check the HTTP verb and that the address starts with ``https://``. A method
pointed at the wrong path would still pass them. These tests check the path
itself, and that the values the caller passes reach the query string or the body.

One test per endpoint: 12 on the hub (the dashboard API) and 9 on the public API,
plus a few more for ``api.files.test_files_integration`` (slice API-TEST, #39).
Each test builds its own client and its own fake response, so the order the tests
run in does not matter and no real storage provider is contacted.
"""

from __future__ import annotations

import asyncio
import json
from typing import Any
from urllib.parse import urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix
from norbix_python.errors import ValidationError

from .helpers import make_client

INTEGRATION_ID = "44444444-4444-4444-4444-444444444444"


def _sent(transport):
    """The last request, split into the parts the tests care about."""
    request = transport.last_request
    assert request is not None, "no request was sent"
    url = urlparse(request["url"])
    body = json.loads(request["body"]) if request["body"] else {}
    return request["method"], url.path, url.query, body


# --- hub: the module itself --------------------------------------------------


def test_enable_files() -> None:
    client, transport = make_client()
    client.hub.files.enable_files()
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("GET", "/v2/files/enable")


def test_disable_files() -> None:
    client, transport = make_client()
    client.hub.files.disable_files()
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("GET", "/v2/files/disable")


# --- hub: browsing -----------------------------------------------------------


def test_get_folder_files() -> None:
    client, transport = make_client()
    client.hub.files.get_folder_files(filesIntegrationId=INTEGRATION_ID, path="invoices/")
    method, path, query, _ = _sent(transport)
    assert (method, path) == ("GET", "/v2/files/folder")
    assert INTEGRATION_ID in query


def test_get_file() -> None:
    client, transport = make_client()
    client.hub.files.get_file(filesIntegrationId=INTEGRATION_ID, path="invoices/invoice.pdf")
    method, path, query, _ = _sent(transport)
    assert (method, path) == ("GET", "/v2/files/item")
    assert INTEGRATION_ID in query


# --- hub: integrations -------------------------------------------------------


def test_get_files_integrations() -> None:
    client, transport = make_client()
    client.hub.files.get_files_integrations()
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("GET", "/v2/files/integrations")


def test_get_files_integration() -> None:
    client, transport = make_client()
    client.hub.files.get_files_integration(id=INTEGRATION_ID)
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("GET", f"/v2/files/integrations/{INTEGRATION_ID}")


def test_save_files_integration() -> None:
    client, transport = make_client()
    client.hub.files.save_files_integration(
        integration={"integrationName": "Invoices bucket", "bucketName": "norbix-invoices"}
    )
    method, path, _, body = _sent(transport)
    assert (method, path) == ("POST", "/v2/files/integrations")
    assert body["integration"]["bucketName"] == "norbix-invoices"


def test_delete_files_integration() -> None:
    client, transport = make_client()
    client.hub.files.delete_files_integration(id=INTEGRATION_ID)
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("DELETE", f"/v2/files/integrations/{INTEGRATION_ID}")


def test_enable_files_integration() -> None:
    client, transport = make_client()
    client.hub.files.enable_files_integration(id=INTEGRATION_ID)
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("PUT", f"/v2/files/integrations/{INTEGRATION_ID}/enable")


def test_disable_files_integration() -> None:
    client, transport = make_client()
    client.hub.files.disable_files_integration(id=INTEGRATION_ID)
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("PUT", f"/v2/files/integrations/{INTEGRATION_ID}/disable")


def test_set_files_integration_as_default() -> None:
    client, transport = make_client()
    client.hub.files.set_files_integration_as_default(id=INTEGRATION_ID)
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("PUT", f"/v2/files/integrations/{INTEGRATION_ID}/default")


def test_test_files_integration() -> None:
    client, transport = make_client()
    client.hub.files.test_files_integration(integrationId=INTEGRATION_ID)
    method, path, _, body = _sent(transport)
    assert (method, path) == ("POST", "/v2/files/integrations/test")
    assert body["integrationId"] == INTEGRATION_ID


# --- public API --------------------------------------------------------------


def test_list_files() -> None:
    client, transport = make_client()
    client.api.files.list_files(INTEGRATION_ID, path="invoices/")
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("GET", f"/v2/files/{INTEGRATION_ID}")


def test_get_file_info() -> None:
    client, transport = make_client()
    client.api.files.get_file_info(INTEGRATION_ID, path="invoices/invoice.pdf")
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("GET", f"/v2/files/{INTEGRATION_ID}/info")


def test_get_signed_url() -> None:
    client, transport = make_client()
    client.api.files.get_signed_url(INTEGRATION_ID, path="invoices/invoice.pdf")
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("GET", f"/v2/files/{INTEGRATION_ID}/sign")


def test_request_upload_url() -> None:
    client, transport = make_client()
    client.api.files.request_upload_url(
        INTEGRATION_ID, path="invoices/invoice.pdf", contentType="application/pdf"
    )
    method, path, _, body = _sent(transport)
    assert (method, path) == ("POST", f"/v2/files/{INTEGRATION_ID}/upload-url")
    assert body["contentType"] == "application/pdf"


def test_commit_upload() -> None:
    client, transport = make_client()
    client.api.files.commit_upload(
        INTEGRATION_ID, path="invoices/invoice.pdf", contentType="application/pdf", sizeBytes=1024
    )
    method, path, _, body = _sent(transport)
    assert (method, path) == ("POST", f"/v2/files/{INTEGRATION_ID}/commit")
    assert body["path"] == "invoices/invoice.pdf"


def test_download_file() -> None:
    client, transport = make_client()
    client.api.files.download_file_api(INTEGRATION_ID, path="invoices/invoice.pdf")
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("GET", f"/v2/files/{INTEGRATION_ID}/download")


def test_delete_file() -> None:
    client, transport = make_client()
    client.api.files.delete_file_api(INTEGRATION_ID, path="invoices/invoice.pdf")
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("DELETE", f"/v2/files/{INTEGRATION_ID}")


def test_delete_many_files() -> None:
    client, transport = make_client()
    client.api.files.delete_many_files_api(
        INTEGRATION_ID, paths=["invoices/a.pdf", "invoices/b.pdf"]
    )
    method, path, _, _ = _sent(transport)
    assert (method, path) == ("DELETE", f"/v2/files/{INTEGRATION_ID}/bulk")


# --- public API: testing an integration (slice API-TEST, #39) ----------------
#
# POST /{version}/files/{filesIntegrationId}/test is the public API twin of the
# hub's POST /{version}/files/integrations/test. The two must not be mixed up:
# the id goes in the path here, in the body there.

PROBE_ANSWER = {
    "items": [
        {"operation": "Upload", "result": "OK", "errors": []},
        {"operation": "Read", "result": "OK", "errors": []},
        {"operation": "List", "result": "OK", "errors": []},
        {"operation": "Delete", "result": "Failed", "errors": ["Access denied"]},
    ],
    "responseStatus": {"errorCode": "", "message": ""},
}


class _Answers(httpx.BaseTransport):
    """Records the request and answers with a fixed status and JSON body."""

    def __init__(self, status: int, payload: dict[str, Any]) -> None:
        self.status = status
        self.payload = payload
        self.last_request: dict[str, Any] | None = None

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self.last_request = {
            "method": request.method,
            "url": str(request.url),
            "headers": dict(request.headers),
            "body": request.content.decode("utf-8") if request.content else "",
        }
        return httpx.Response(self.status, json=self.payload)


class _AsyncAnswers(httpx.AsyncBaseTransport):
    def __init__(self, status: int, payload: dict[str, Any]) -> None:
        self.status = status
        self.payload = payload
        self.last_request: dict[str, Any] | None = None

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        self.last_request = {
            "method": request.method,
            "url": str(request.url),
            "headers": dict(request.headers),
            "body": request.content.decode("utf-8") if request.content else "",
        }
        return httpx.Response(self.status, json=self.payload)


def test_api_test_files_integration_route() -> None:
    client, transport = make_client()
    client.api.files.test_files_integration(INTEGRATION_ID)
    method, path, _, body = _sent(transport)
    assert (method, path) == ("POST", f"/v2/files/{INTEGRATION_ID}/test")
    # The id travels in the path only, not in the body as on the hub route.
    assert "integrationId" not in body


def test_api_test_files_integration_sends_project_scope_headers() -> None:
    client, transport = make_client()
    client.api.files.test_files_integration(INTEGRATION_ID)
    headers = transport.last_request["headers"]
    assert headers["authorization"] == "Bearer test-token"
    assert headers["x-cm-projectid"] == "test-project"


def test_api_test_files_integration_gives_back_the_parsed_items() -> None:
    transport = _Answers(200, PROBE_ANSWER)
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=transport),
    )

    result = client.api.files.test_files_integration(INTEGRATION_ID)

    assert [item["operation"] for item in result["items"]] == ["Upload", "Read", "List", "Delete"]
    assert result["items"][0]["result"] == "OK"
    assert result["items"][3] == {"operation": "Delete", "result": "Failed", "errors": ["Access denied"]}


def test_api_test_files_integration_error_status_raises() -> None:
    answer = {
        "responseStatus": {
            "errorCode": "IntegrationNotFound",
            "message": "Files integration was not found",
        }
    }
    transport = _Answers(400, answer)
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=transport),
    )

    with pytest.raises(ValidationError) as caught:
        client.api.files.test_files_integration(INTEGRATION_ID)

    assert caught.value.status == 400
    assert caught.value.details["responseStatus"]["errorCode"] == "IntegrationNotFound"


def test_api_test_files_integration_async() -> None:
    transport = _AsyncAnswers(200, PROBE_ANSWER)
    client = AsyncNorbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.AsyncClient(transport=transport),
    )

    async def run() -> Any:
        return await client.api.files.test_files_integration(INTEGRATION_ID)

    result = asyncio.run(run())

    request = transport.last_request
    assert request is not None
    assert request["method"] == "POST"
    assert urlparse(request["url"]).path == f"/v2/files/{INTEGRATION_ID}/test"
    assert request["headers"]["x-cm-projectid"] == "test-project"
    assert result["items"][2]["operation"] == "List"
