"""Api Database — the gateway's last Database wave, seen from the SDK.

Same idea as ``tests/hub/test_database_last_wave.py``: every Database route the
Community Api serves has a method with the gateway's verb and path (list taken
from the Api's ``/types/metadata``, gateway ``refactoringV2``), the new
``allRecords`` field lands where the gateway reads it, and the new error codes
reach the caller. Every call goes to a fake transport.
"""

from __future__ import annotations

import asyncio
import inspect
import json
import re
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, NorbixError

from ..helpers import CaptureTransport

API_DATABASE_ROUTES: list[tuple[str, str]] = [
    ("GET", "/{version}/database/collections/{collectionName}"),
    ("POST", "/{version}/database/collections/{collectionName}"),
    ("POST", "/{version}/database/collections/{collectionName}/aggregate"),
    ("POST", "/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute"),
    ("GET", "/{version}/database/collections/{collectionName}/count"),
    ("GET", "/{version}/database/collections/{collectionName}/distinct"),
    ("DELETE", "/{version}/database/collections/{collectionName}/many"),
    ("POST", "/{version}/database/collections/{collectionName}/many"),
    ("PUT", "/{version}/database/collections/{collectionName}/many"),
    ("GET", "/{version}/database/collections/{collectionName}/own"),
    ("DELETE", "/{version}/database/collections/{collectionName}/{id}"),
    ("GET", "/{version}/database/collections/{collectionName}/{id}"),
    ("PUT", "/{version}/database/collections/{collectionName}/{id}"),
    ("PUT", "/{version}/database/collections/{collectionName}/{id}/replace"),
    ("PUT", "/{version}/database/collections/{collectionName}/{id}/responsibility"),
    ("GET", "/{version}/database/schemas"),
    ("GET", "/{version}/database/schemas/{id}"),
    ("GET", "/{version}/database/taxonomies/tree"),
    ("GET", "/{version}/database/taxonomies/{taxonomyName}/merged-tree"),
    ("GET", "/{version}/database/taxonomies/{taxonomyName}/terms"),
    ("GET", "/{version}/database/taxonomies/{taxonomyName}/terms/tree"),
    ("GET", "/{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children"),
]

_DOC = re.compile(r"^(GET|POST|PUT|PATCH|DELETE) (/\S+)$")
_TOKEN = re.compile(r"\{([^}]+)\}")


def _documented_routes(module: Any) -> dict[str, tuple[str, str]]:
    out: dict[str, tuple[str, str]] = {}
    for name, fn in inspect.getmembers(module, callable):
        if name.startswith("_"):
            continue
        match = _DOC.match((fn.__doc__ or "").strip().splitlines()[0] if fn.__doc__ else "")
        if match:
            out[name] = (match.group(1), match.group(2))
    return out


def _client() -> tuple[Norbix, CaptureTransport]:
    transport = CaptureTransport()
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=transport),
    )
    return client, transport


def _answering(status: int, code: str, message: str, context: dict[str, Any] | None = None) -> Norbix:
    error: dict[str, Any] = {"message": message, "errorCode": code}
    if context is not None:
        error["context"] = context
    body = {"responseStatus": {"isSuccess": False, "errors": [error]}}

    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(status, json=body)

    return Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )


def test_every_api_database_route_has_exactly_one_method() -> None:
    client, _ = _client()
    documented = _documented_routes(client.api.database)
    by_route: dict[tuple[str, str], list[str]] = {}
    for name, (verb, path) in documented.items():
        by_route.setdefault((verb, _TOKEN.sub("{}", path)), []).append(name)
    assert set(by_route) == {(verb, _TOKEN.sub("{}", path)) for verb, path in API_DATABASE_ROUTES}
    assert {route: names for route, names in by_route.items() if len(names) > 1} == {}


def test_every_api_database_method_sends_its_documented_verb_and_path() -> None:
    client, transport = _client()
    module = client.api.database
    for name, (verb, path) in sorted(_documented_routes(module).items()):
        fn = getattr(module, name)
        args = [
            f"p-{p.name}"
            for p in inspect.signature(fn).parameters.values()
            if p.kind is inspect.Parameter.POSITIONAL_OR_KEYWORD
        ]
        fn(*args)
        assert transport.last_request is not None
        assert transport.last_request["method"] == verb, name
        sent = urlparse(transport.last_request["url"]).path
        pattern = "^" + _TOKEN.sub("[^/]+", path.replace("{version}", "v3")) + "$"
        assert re.match(pattern, sent), (name, sent)


def test_async_api_database_has_the_same_methods_as_sync() -> None:
    sync_client, _ = _client()
    async_client = AsyncNorbix(project_id="test-project", bearer_token="test-token")
    assert _documented_routes(async_client.api.database) == _documented_routes(sync_client.api.database)


def test_update_many_sends_all_records_in_the_body() -> None:
    client, transport = _client()
    client.api.database.update_many("products", filter="{}", update='{"seen": true}', allRecords=True)
    assert transport.last_request is not None
    assert transport.last_request["method"] == "PUT"
    assert urlparse(transport.last_request["url"]).path == "/v3/database/collections/products/many"
    assert json.loads(transport.last_request["body"]) == {
        "filter": "{}",
        "update": '{"seen": true}',
        "allRecords": True,
    }


def test_delete_many_sends_all_records_in_the_query() -> None:
    client, transport = _client()
    client.api.database.delete_many("products", filter="{}", allRecords=True)
    assert transport.last_request is not None
    url = urlparse(transport.last_request["url"])
    assert transport.last_request["method"] == "DELETE"
    assert parse_qs(url.query) == {"filter": ["{}"], "allRecords": ["true"]}


def test_async_update_and_delete_many_send_all_records() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    async def run() -> None:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        try:
            await client.api.database.update_many("products", filter="{}", update="{}", allRecords=True)
            await client.api.database.delete_many("products", filter="{}", allRecords=True)
        finally:
            await client.aclose()

    asyncio.run(run())
    assert json.loads(seen[0].content)["allRecords"] is True
    assert parse_qs(urlparse(str(seen[1].url)).query)["allRecords"] == ["true"]


@pytest.mark.parametrize(
    ("call", "code"),
    [
        (lambda db: db.delete_many("products", filter="{}"), "CM-ERRORS-DATABASE-037"),
        (lambda db: db.update_one("products", "rec_1", update='{"$inc": {"n": 1}}'), "CM-ERRORS-DATABASE-035"),
        (lambda db: db.insert_one("products", document="{bad"), "CM-ERRORS-DATABASE-036"),
        (lambda db: db.change_responsibility("products", "rec_1", newResponsibleUserId="usr_x"), "CM-ERRORS-MEMBERSHIP-USERS-012"),
        (lambda db: db.find_terms("services", filter='{"$where": "1"}'), "CM-ERRORS-DATABASE-031"),
        (lambda db: db.find_terms_children("services", "term_1", filter='{"$where": "1"}'), "CM-ERRORS-DATABASE-031"),
        (lambda db: db.find_term_tree("a" * 41), "CM-ERRORS-TAXONOMIES-005"),
        (lambda db: db.find_merged_term_tree("unknown"), "CM-ERRORS-TAXONOMIES-010"),
        (lambda db: db.find_term_tree("huge"), "CM-ERRORS-TAXONOMIES-011"),
    ],
)
def test_new_error_codes_reach_the_caller(call: Any, code: str) -> None:
    client = _answering(400, code, "refused")
    with pytest.raises(NorbixError) as caught:
        call(client.api.database)
    assert caught.value.error_code == code


def test_insert_many_invalid_document_error_keeps_the_index() -> None:
    client = _answering(400, "CM-ERRORS-DATABASE-036", "Invalid record document", {"Index": 1})
    with pytest.raises(NorbixError) as caught:
        client.api.database.insert_many("products", documents=["{}", "{bad"])
    assert caught.value.errors[0].context == {"Index": 1}
