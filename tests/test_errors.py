"""What the caller sees when a call fails (10b-files slice ERRORS, #66 and #67).

Two rules are pinned here. First, the message and the error code are the
gateway's own: the gateway puts them inside ``responseStatus.errors[]``, so
reading the top of that block gave every caller the whole body as the message
and the code ``HTTP_404`` — that was #66. Second, a call fails when the gateway
says it failed, even with HTTP 200 and ``responseStatus.isSuccess = False`` —
that was #67.

Every test builds its own client and its own fake answer, so the order the
tests run in does not matter and no real server is contacted.
"""

from __future__ import annotations

import asyncio
from typing import Any

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, NorbixError, ValidationError

INTEGRATION_ID = "int_7"


class _Answers(httpx.BaseTransport):
    """Answers every request with one status and one body."""

    def __init__(self, status: int, *, json: Any = None, text: str | None = None) -> None:
        self.status = status
        self.json = json
        self.text = text

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        if self.text is not None:
            return httpx.Response(
                self.status, text=self.text, headers={"Content-Type": "text/html"}
            )
        return httpx.Response(self.status, json=self.json)


def client_answering(status: int, *, json: Any = None, text: str | None = None) -> Norbix:
    return Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=_Answers(status, json=json, text=text)),
    )


def a_call(client: Norbix) -> Any:
    """Any call does; the transport is the same for all of them."""
    return client.api.files.test_files_integration(INTEGRATION_ID)


# (a) HTTP 400 with two errors inside responseStatus.errors
def test_a_400_takes_message_and_code_from_the_first_error_and_keeps_them_all() -> None:
    client = client_answering(
        400,
        json={
            "responseStatus": {
                "isSuccess": False,
                "errors": [
                    {
                        "message": "File name is required",
                        "errorCode": "CM-ERRORS-FILES-002",
                        "fieldName": "fileName",
                    },
                    {
                        "message": "Folder does not exist",
                        "errorCode": "CM-ERRORS-FILES-016",
                        "context": {"Provider": "Local"},
                    },
                ],
            }
        },
    )

    with pytest.raises(ValidationError) as caught:
        a_call(client)

    err = caught.value
    assert err.message == "File name is required"
    assert err.error_code == "CM-ERRORS-FILES-002"
    assert err.http_status == 400
    assert len(err.errors) == 2
    assert err.errors[0].field_name == "fileName"
    assert err.errors[1].error_code == "CM-ERRORS-FILES-016"
    assert err.errors[1].context == {"Provider": "Local"}
    # The body as it arrived is kept for anyone who needs the rest of it.
    assert err.body["responseStatus"]["isSuccess"] is False


# (b) HTTP 200 whose body says the call failed
def test_a_200_that_says_it_failed_raises_with_the_gateway_message() -> None:
    client = client_answering(
        200,
        json={
            "responseStatus": {
                "isSuccess": False,
                "errors": [
                    {
                        "message": 'File not found: "a/b.txt" does not exist in Local (int_7).',
                        "errorCode": "CM-ERRORS-FILES-016",
                    }
                ],
            }
        },
    )

    with pytest.raises(NorbixError) as caught:
        a_call(client)

    err = caught.value
    assert err.http_status == 200
    assert err.message == 'File not found: "a/b.txt" does not exist in Local (int_7).'
    assert err.error_code == "CM-ERRORS-FILES-016"


# (c) HTTP 200 that says the call worked — unchanged
def test_a_200_that_says_it_worked_still_comes_back_as_a_value() -> None:
    client = client_answering(
        200,
        json={
            "items": [{"operation": "UploadFile", "result": "OK"}],
            "responseStatus": {"isSuccess": True},
        },
    )

    result = a_call(client)

    assert result["items"][0]["result"] == "OK"


def test_a_200_with_no_response_status_still_comes_back_as_a_value() -> None:
    client = client_answering(200, json={"items": []})

    assert a_call(client) == {"items": []}


# (d) a 500 whose body is not JSON at all
def test_a_500_with_a_body_that_is_not_json_uses_the_fallback_text() -> None:
    client = client_answering(500, text="<html>Bad Gateway</html>")

    with pytest.raises(NorbixError) as caught:
        a_call(client)

    err = caught.value
    assert err.message == "Request failed (HTTP 500)"
    assert err.error_code == "HTTP_500"
    assert err.body == "<html>Bad Gateway</html>"


def test_an_empty_error_body_uses_the_fallback_text_too() -> None:
    client = client_answering(404, json={})

    with pytest.raises(NorbixError) as caught:
        a_call(client)

    assert caught.value.message == "Request failed (HTTP 404)"


def test_reads_the_top_of_the_body_when_there_is_no_response_status() -> None:
    client = client_answering(
        409, json={"message": "Already exists", "errorCode": "CM-ERRORS-FILES-009"}
    )

    with pytest.raises(NorbixError) as caught:
        a_call(client)

    assert caught.value.message == "Already exists"
    assert caught.value.error_code == "CM-ERRORS-FILES-009"


class _AsyncAnswers(httpx.AsyncBaseTransport):
    def __init__(self, status: int, json: Any) -> None:
        self.status = status
        self.json = json

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        return httpx.Response(self.status, json=self.json)


def test_the_async_client_fails_on_a_200_that_says_it_failed() -> None:
    """The async transport has its own copy of the check; it must agree."""
    transport = _AsyncAnswers(
        200,
        {
            "responseStatus": {
                "isSuccess": False,
                "errors": [
                    {"message": "Integration not found", "errorCode": "CM-ERRORS-INTEGRATIONS-001"}
                ],
            }
        },
    )

    async def run() -> None:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=transport),
        )
        await client.api.files.test_files_integration(INTEGRATION_ID)

    with pytest.raises(NorbixError) as caught:
        asyncio.run(run())

    assert caught.value.http_status == 200
    assert caught.value.message == "Integration not found"
    assert caught.value.error_code == "CM-ERRORS-INTEGRATIONS-001"
