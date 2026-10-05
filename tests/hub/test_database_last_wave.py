"""Hub Database — the gateway's last Database wave, seen from the SDK.

The Python SDK is untyped: every request field is a keyword argument that goes
to the wire with the name the caller gives it (``allRecords=True``, like
``pageSize=20`` elsewhere). So a gateway change reaches the SDK in three
places, and each one is pinned here:

- the routes: every Database route the Community Hub serves has a method, and
  every method's verb and path is the gateway's (the list below is taken from
  the Hub's ``/types/metadata``, built from gateway ``refactoringV2``);
- the request: new fields (``allRecords``) land where the gateway reads them
  (query on DELETE, JSON body on PUT), and the per-environment calls carry the
  ``norbix-env`` header;
- the errors: the new error codes reach the caller as ``error_code``, with the
  gateway's metadata in ``errors[0].context``.

Every call goes to a fake transport; no server is contacted.
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

# Every Database route of the Community Hub (verb, path), from /types/metadata.
HUB_DATABASE_ROUTES: list[tuple[str, str]] = [
    ("GET", "/{version}/database/aggregates"),
    ("POST", "/{version}/database/aggregates"),
    ("POST", "/{version}/database/aggregates/test"),
    ("DELETE", "/{version}/database/aggregates/{Id}"),
    ("GET", "/{version}/database/aggregates/{Id}"),
    ("POST", "/{version}/database/collections/seed"),
    ("GET", "/{version}/database/collections/{collectionName}"),
    ("POST", "/{version}/database/collections/{collectionName}"),
    ("POST", "/{version}/database/collections/{collectionName}/aggregate"),
    ("POST", "/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute"),
    ("GET", "/{version}/database/collections/{collectionName}/count"),
    ("GET", "/{version}/database/collections/{collectionName}/distinct"),
    ("GET", "/{version}/database/collections/{collectionName}/indexes"),
    ("DELETE", "/{version}/database/collections/{collectionName}/many"),
    ("POST", "/{version}/database/collections/{collectionName}/many"),
    ("PUT", "/{version}/database/collections/{collectionName}/many"),
    ("DELETE", "/{version}/database/collections/{collectionName}/{id}"),
    ("GET", "/{version}/database/collections/{collectionName}/{id}"),
    ("PUT", "/{version}/database/collections/{collectionName}/{id}"),
    ("PUT", "/{version}/database/collections/{collectionName}/{id}/replace"),
    ("PUT", "/{version}/database/collections/{collectionName}/{id}/responsibility"),
    ("PUT", "/{version}/database/disable"),
    ("PUT", "/{version}/database/enable"),
    ("GET", "/{version}/database/imports"),
    ("POST", "/{version}/database/imports"),
    ("POST", "/{version}/database/imports/analyze"),
    ("POST", "/{version}/database/imports/upload-url"),
    ("DELETE", "/{version}/database/imports/{Id}"),
    ("GET", "/{version}/database/imports/{Id}"),
    ("GET", "/{version}/database/integrations"),
    ("POST", "/{version}/database/integrations"),
    ("GET", "/{version}/database/integrations/flex-tiers"),
    ("POST", "/{version}/database/integrations/test"),
    ("DELETE", "/{version}/database/integrations/{Id}"),
    ("GET", "/{version}/database/integrations/{Id}/connection-string"),
    ("PUT", "/{version}/database/integrations/{Id}/default"),
    ("PUT", "/{version}/database/integrations/{Id}/disable"),
    ("PUT", "/{version}/database/integrations/{Id}/enable"),
    ("GET", "/{version}/database/integrations/{id}"),
    ("GET", "/{version}/database/schemas"),
    ("POST", "/{version}/database/schemas"),
    ("POST", "/{version}/database/schemas/apply-bundle"),
    ("GET", "/{version}/database/schemas/triggers"),
    ("POST", "/{version}/database/schemas/triggers"),
    ("GET", "/{version}/database/schemas/triggers/{id}"),
    ("DELETE", "/{version}/database/schemas/triggers/{triggerId}"),
    ("PATCH", "/{version}/database/schemas/triggers/{triggerId}/disable"),
    ("PATCH", "/{version}/database/schemas/triggers/{triggerId}/enable"),
    ("DELETE", "/{version}/database/schemas/{Id}"),
    ("DELETE", "/{version}/database/schemas/{Id}/draft"),
    ("GET", "/{version}/database/schemas/{Id}/draft"),
    ("PUT", "/{version}/database/schemas/{Id}/draft"),
    ("PUT", "/{version}/database/schemas/{Id}/embed"),
    ("GET", "/{version}/database/schemas/{Id}/list-settings"),
    ("PUT", "/{version}/database/schemas/{Id}/list-settings"),
    ("POST", "/{version}/database/schemas/{Id}/publish"),
    ("PUT", "/{version}/database/schemas/{Id}/rename"),
    ("PUT", "/{version}/database/schemas/{Id}/settings"),
    ("GET", "/{version}/database/schemas/{Id}/versions"),
    ("GET", "/{version}/database/schemas/{Id}/versions/diff"),
    ("GET", "/{version}/database/schemas/{id}"),
    ("GET", "/{version}/database/taxonomies"),
    ("POST", "/{version}/database/taxonomies"),
    ("GET", "/{version}/database/taxonomies/tree"),
    ("DELETE", "/{version}/database/taxonomies/{Id}"),
    ("POST", "/{version}/database/taxonomies/{TaxonomyId}/terms"),
    ("DELETE", "/{version}/database/taxonomies/{TaxonomyId}/terms/many"),
    ("DELETE", "/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"),
    ("GET", "/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"),
    ("PUT", "/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"),
    ("GET", "/{version}/database/taxonomies/{TaxonomyName}/merged-tree"),
    ("GET", "/{version}/database/taxonomies/{TaxonomyName}/terms/tree"),
    ("GET", "/{version}/database/taxonomies/{id}"),
]

_DOC = re.compile(r"^(GET|POST|PUT|PATCH|DELETE) (/\S+)$")
_TOKEN = re.compile(r"\{([^}]+)\}")


def _documented_routes(module: Any) -> dict[str, tuple[str, str]]:
    """method name -> (verb, path), read from each method's one-line docstring."""
    out: dict[str, tuple[str, str]] = {}
    for name, fn in inspect.getmembers(module, callable):
        if name.startswith("_"):
            continue
        match = _DOC.match((fn.__doc__ or "").strip())
        if match:
            out[name] = (match.group(1), match.group(2))
    return out


def _norm(path: str) -> str:
    # Path tokens are matched by place, not by spelling ({Id} vs {id}).
    return _TOKEN.sub("{}", path)


def _client(env: str | None = None) -> tuple[Norbix, CaptureTransport]:
    transport = CaptureTransport()
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        env=env,
        http_client=httpx.Client(transport=transport),
    )
    return client, transport


def _answering(status: int, body: dict[str, Any]) -> Norbix:
    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(status, json=body)

    return Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )


def _failure(code: str, message: str, context: dict[str, Any] | None = None) -> dict[str, Any]:
    error: dict[str, Any] = {"message": message, "errorCode": code}
    if context is not None:
        error["context"] = context
    return {"responseStatus": {"isSuccess": False, "errors": [error]}}


# --- routes ------------------------------------------------------------------


def test_every_hub_database_route_has_exactly_one_method() -> None:
    client, _ = _client()
    documented = _documented_routes(client.hub.database)
    by_route: dict[tuple[str, str], list[str]] = {}
    for name, (verb, path) in documented.items():
        by_route.setdefault((verb, _norm(path)), []).append(name)

    expected = {(verb, _norm(path)) for verb, path in HUB_DATABASE_ROUTES}
    assert set(by_route) == expected
    assert {route: names for route, names in by_route.items() if len(names) > 1} == {}


def test_every_hub_database_method_sends_its_documented_verb_and_path() -> None:
    client, transport = _client()
    module = client.hub.database
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
        pattern = "^" + _TOKEN.sub("[^/]+", path.replace("{version}", "v2")) + "$"
        sent = urlparse(transport.last_request["url"]).path
        assert re.match(pattern, sent), (name, sent)
        for arg in args:
            assert arg in sent, (name, sent)


def test_async_hub_database_has_the_same_methods_as_sync() -> None:
    sync_client, _ = _client()
    async_client = AsyncNorbix(project_id="test-project", bearer_token="test-token")
    sync_routes = _documented_routes(sync_client.hub.database)
    async_routes = _documented_routes(async_client.hub.database)
    assert async_routes == sync_routes
    for name in async_routes:
        assert inspect.iscoroutinefunction(getattr(async_client.hub.database, name)), name


# --- collection imports (new methods) -------------------------------------------


@pytest.mark.parametrize(
    ("call", "verb", "path"),
    [
        (lambda db: db.create_collection_import(schemaId="sch_1", file={"path": "imports/a.csv"}), "POST", "/v2/database/imports"),
        (lambda db: db.get_collection_imports(), "GET", "/v2/database/imports"),
        (lambda db: db.get_collection_import("imp_1"), "GET", "/v2/database/imports/imp_1"),
        (lambda db: db.delete_collection_import("imp_1"), "DELETE", "/v2/database/imports/imp_1"),
        (lambda db: db.request_import_upload_url(fileName="a.csv"), "POST", "/v2/database/imports/upload-url"),
        (lambda db: db.analyze_import_file(file={"path": "imports/a.csv"}), "POST", "/v2/database/imports/analyze"),
    ],
)
def test_collection_import_methods(call: Any, verb: str, path: str) -> None:
    client, transport = _client()
    call(client.hub.database)
    assert transport.last_request is not None
    assert transport.last_request["method"] == verb
    assert urlparse(transport.last_request["url"]).path == path


# --- records: empty filter needs allRecords -------------------------------------


def test_update_many_records_sends_all_records_in_the_body() -> None:
    client, transport = _client()
    client.hub.database.update_many_records(
        "products", filter="{}", update='{"status": "archived"}', allRecords=True
    )
    assert transport.last_request is not None
    assert transport.last_request["method"] == "PUT"
    assert urlparse(transport.last_request["url"]).path == "/v2/database/collections/products/many"
    assert json.loads(transport.last_request["body"]) == {
        "filter": "{}",
        "update": '{"status": "archived"}',
        "allRecords": True,
    }


def test_update_many_records_without_filter_sends_no_filter() -> None:
    # The gateway now reads a missing filter as {} (and refuses it without allRecords).
    client, transport = _client()
    client.hub.database.update_many_records("products", update='{"status": "x"}')
    assert transport.last_request is not None
    assert json.loads(transport.last_request["body"]) == {"update": '{"status": "x"}'}


def test_delete_many_records_sends_all_records_in_the_query() -> None:
    client, transport = _client()
    client.hub.database.delete_many_records("products", filter="{}", allRecords=True)
    assert transport.last_request is not None
    url = urlparse(transport.last_request["url"])
    assert transport.last_request["method"] == "DELETE"
    assert url.path == "/v2/database/collections/products/many"
    assert parse_qs(url.query) == {"filter": ["{}"], "allRecords": ["true"]}


def test_async_update_and_delete_many_records_send_all_records() -> None:
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
            await client.hub.database.update_many_records("products", filter="{}", update="{}", allRecords=True)
            await client.hub.database.delete_many_records("products", filter="{}", allRecords=True)
        finally:
            await client.aclose()

    asyncio.run(run())
    assert json.loads(seen[0].content)["allRecords"] is True
    assert parse_qs(urlparse(str(seen[1].url)).query)["allRecords"] == ["true"]


@pytest.mark.parametrize(
    ("code", "message"),
    [
        ("CM-ERRORS-DATABASE-037", "An empty filter matches every record. Set AllRecords to true to change all records."),
        ("CM-ERRORS-DATABASE-035", "Update operators ($inc, $set, ...) are not allowed in the update document."),
        ("CM-ERRORS-DATABASE-036", "Invalid record document"),
    ],
)
def test_new_record_write_errors_reach_the_caller(code: str, message: str) -> None:
    client = _answering(400, _failure(code, message))
    with pytest.raises(NorbixError) as caught:
        client.hub.database.update_many_records("products", filter="{}", update="{}")
    assert caught.value.error_code == code
    assert caught.value.message == message


def test_insert_many_invalid_document_error_keeps_the_index() -> None:
    client = _answering(400, _failure("CM-ERRORS-DATABASE-036", "Invalid record document", {"Index": 2}))
    with pytest.raises(NorbixError) as caught:
        client.hub.database.insert_many_records("products", documents=["{}", "{}", "{bad"])
    assert caught.value.error_code == "CM-ERRORS-DATABASE-036"
    assert caught.value.errors[0].context == {"Index": 2}


def test_change_owner_to_a_non_user_reaches_the_caller() -> None:
    client = _answering(400, _failure("CM-ERRORS-MEMBERSHIP-USERS-012", "User not found in this project"))
    with pytest.raises(NorbixError) as caught:
        client.hub.database.change_record_responsibility("products", "rec_1", newResponsibleUserId="usr_x")
    assert caught.value.error_code == "CM-ERRORS-MEMBERSHIP-USERS-012"


# --- schemas -----------------------------------------------------------------------


def test_rename_schema_sends_only_the_new_name() -> None:
    client, transport = _client()
    client.hub.database.rename_database_schema("sch_1", title="Products")
    assert transport.last_request is not None
    assert transport.last_request["method"] == "PUT"
    assert urlparse(transport.last_request["url"]).path == "/v2/database/schemas/sch_1/rename"
    assert json.loads(transport.last_request["body"]) == {"title": "Products"}


def test_rename_schema_to_a_taken_name_reaches_the_caller() -> None:
    client = _answering(400, _failure("CM-ERRORS-SCHEMA-002", "A schema named 'Products' already exists"))
    with pytest.raises(NorbixError) as caught:
        client.hub.database.rename_database_schema("sch_1", title="Products")
    assert caught.value.error_code == "CM-ERRORS-SCHEMA-002"


def test_delete_schema_used_by_an_aggregate_names_the_aggregates() -> None:
    context = {"SchemaId": "sch_1", "BlockerAggregateIds": ["agg_1"], "BlockerAggregateNames": ["Orders by month"]}
    client = _answering(
        400,
        _failure(
            "CM-ERRORS-SCHEMA-018",
            "Schema sch_1 is still used by 1 MongoDB aggregate(s) ('Orders by month') as the start or a joined collection",
            context,
        ),
    )
    with pytest.raises(NorbixError) as caught:
        client.hub.database.delete_database_schema("sch_1")
    assert caught.value.error_code == "CM-ERRORS-SCHEMA-018"
    assert caught.value.errors[0].context["BlockerAggregateNames"] == ["Orders by month"]


# --- schema triggers per environment ----------------------------------------------


@pytest.mark.parametrize(
    ("call", "verb", "path"),
    [
        (lambda db: db.get_schema_triggers(), "GET", "/v2/database/schemas/triggers"),
        (lambda db: db.get_schema_trigger("trg_1"), "GET", "/v2/database/schemas/triggers/trg_1"),
        (lambda db: db.save_schema_trigger(schemaId="sch_1"), "POST", "/v2/database/schemas/triggers"),
        (lambda db: db.enable_schema_trigger("trg_1"), "PATCH", "/v2/database/schemas/triggers/trg_1/enable"),
        (lambda db: db.disable_schema_trigger("trg_1"), "PATCH", "/v2/database/schemas/triggers/trg_1/disable"),
        (lambda db: db.delete_schema_trigger("trg_1"), "DELETE", "/v2/database/schemas/triggers/trg_1"),
    ],
)
def test_schema_trigger_calls_carry_the_client_env(call: Any, verb: str, path: str) -> None:
    client, transport = _client(env="TEST")
    call(client.hub.database)
    assert transport.last_request is not None
    assert transport.last_request["method"] == verb
    assert urlparse(transport.last_request["url"]).path == path
    assert transport.last_request["headers"]["norbix-env"] == "TEST"


def test_schema_trigger_calls_without_env_send_no_env_header() -> None:
    # No header = PROD on the gateway: the list shows only PROD rows, and
    # enable / disable / delete act on the PROD copy.
    client, transport = _client()
    client.hub.database.enable_schema_trigger("trg_1")
    assert transport.last_request is not None
    assert "norbix-env" not in transport.last_request["headers"]


def test_schema_trigger_missing_in_the_env_reaches_the_caller() -> None:
    client = _answering(404, _failure("CM-ERRORS-TRIGGERS-002", "Trigger not found"))
    with pytest.raises(NorbixError) as caught:
        client.hub.database.delete_schema_trigger("trg_1")
    assert caught.value.error_code == "CM-ERRORS-TRIGGERS-002"


# --- taxonomies --------------------------------------------------------------------


def test_taxonomy_list_rows_come_back_with_dependency_refs() -> None:
    body = {
        "list": {
            "items": [
                {
                    "id": "tax_cities",
                    "name": "cities",
                    "dependencies": ["tax_countries", "tax_gone"],
                    "dependencyRefs": [{"id": "tax_countries", "name": "countries"}, {"id": "tax_gone", "name": None}],
                }
            ]
        }
    }
    client = _answering(200, body)
    result = client.hub.database.get_database_taxonomies()
    row = result["list"]["items"][0]
    assert "dependencyNames" not in row
    assert row["dependencyRefs"] == [{"id": "tax_countries", "name": "countries"}, {"id": "tax_gone", "name": None}]


@pytest.mark.parametrize(
    "code",
    ["CM-ERRORS-TAXONOMIES-010", "CM-ERRORS-TAXONOMIES-011", "CM-ERRORS-TAXONOMIES-005"],
)
def test_new_taxonomy_term_read_errors_reach_the_caller(code: str) -> None:
    client = _answering(400, _failure(code, "refused"))
    with pytest.raises(NorbixError) as caught:
        client.hub.database.get_database_merged_term_tree("services")
    assert caught.value.error_code == code


def test_taxonomy_tree_with_terms_sends_include_terms() -> None:
    client, transport = _client()
    client.hub.database.get_database_taxonomy_tree(includeTerms=True)
    assert transport.last_request is not None
    url = urlparse(transport.last_request["url"])
    assert url.path == "/v2/database/taxonomies/tree"
    assert parse_qs(url.query) == {"includeTerms": ["true"]}


# --- aggregates ------------------------------------------------------------------------


def test_aggregate_rows_come_back_with_joined_collections() -> None:
    client = _answering(
        200, {"result": {"id": "agg_1", "schemaId": "sch_orders", "joinedCollections": ["sch_customers"]}}
    )
    result = client.hub.database.get_database_aggregate("agg_1")
    assert result["result"]["joinedCollections"] == ["sch_customers"]


def test_test_aggregate_without_write_rights_reaches_the_caller() -> None:
    # Testing an aggregate now needs database:create or database:update, plus read.
    client = _answering(403, {"responseStatus": {"isSuccess": False, "message": "Forbidden"}})
    with pytest.raises(NorbixError) as caught:
        client.hub.database.test_database_aggregate(schemaId="sch_1", query="[]")
    assert caught.value.status == 403
