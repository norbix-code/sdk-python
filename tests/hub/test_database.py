from __future__ import annotations

import asyncio
import inspect
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, NorbixError
from ..helpers import make_client


def test_hub_database_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.database
    assert callable(module.disable_database)
    assert callable(module.enable_database)
    assert callable(module.delete_schema_trigger)
    assert callable(module.disable_schema_trigger)
    assert callable(module.enable_schema_trigger)
    assert callable(module.get_schema_trigger)
    assert callable(module.get_schema_triggers)
    assert callable(module.save_schema_trigger)
    assert callable(module.delete_database_taxonomy)
    assert callable(module.get_database_taxonomy)
    assert callable(module.get_database_taxonomies)
    assert callable(module.save_database_taxonomy)
    assert callable(module.delete_database_taxonomy_term)
    assert callable(module.delete_many_database_taxonomy_terms)
    assert callable(module.get_database_taxonomy_term)
    assert callable(module.save_database_taxonomy_term)
    assert callable(module.update_database_taxonomy_term)
    assert callable(module.delete_database_schema)
    assert callable(module.discard_database_schema_draft)
    assert callable(module.get_database_schema)
    assert callable(module.get_database_schemas)
    assert callable(module.get_database_schema_draft)
    assert callable(module.get_database_schema_version_diff)
    assert callable(module.get_database_schema_versions)
    assert callable(module.publish_database_schema)
    assert callable(module.rename_database_schema)
    assert callable(module.save_database_schema)
    assert callable(module.update_database_schema_draft)
    assert callable(module.update_database_schema_settings)
    assert callable(module.delete_database_integration)
    assert callable(module.disable_database_integration)
    assert callable(module.enable_database_integration)
    assert callable(module.get_database_integration)
    assert callable(module.get_database_integrations)
    assert callable(module.save_database_integration)
    assert callable(module.set_database_integration_as_default)
    assert callable(module.delete_database_aggregate)
    assert callable(module.get_database_aggregate)
    assert callable(module.get_database_aggregates)
    assert callable(module.save_database_aggregate)
    assert callable(module.test_database_aggregate)


def test_hub_database_disable_database_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.disable_database()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_enable_database_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.enable_database()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_schema_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_schema_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_disable_schema_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.disable_schema_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_enable_schema_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.enable_schema_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_schema_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_schema_trigger(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_schema_triggers_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_schema_triggers()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_save_schema_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.save_schema_trigger()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_database_taxonomy_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_database_taxonomy(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_taxonomy_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_taxonomy(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_taxonomies_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_taxonomies()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_save_database_taxonomy_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.save_database_taxonomy()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_database_taxonomy_term_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_database_taxonomy_term(taxonomy_id="stub-TaxonomyId", id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_many_database_taxonomy_terms_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_many_database_taxonomy_terms(taxonomy_id="stub-TaxonomyId")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_taxonomy_term_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_taxonomy_term(taxonomy_id="stub-TaxonomyId", id="stub-Id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_save_database_taxonomy_term_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.save_database_taxonomy_term(taxonomy_id="stub-TaxonomyId")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_update_database_taxonomy_term_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.update_database_taxonomy_term(taxonomy_id="stub-TaxonomyId", id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_database_schema_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_database_schema(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_discard_database_schema_draft_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.discard_database_schema_draft(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_schema_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_schema(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_schemas_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_schemas()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_schema_draft_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_schema_draft(id="stub-Id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_schema_version_diff_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_schema_version_diff(id="stub-Id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_schema_versions_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_schema_versions(id="stub-Id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_publish_database_schema_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.publish_database_schema(id="stub-Id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_rename_database_schema_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.rename_database_schema(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_save_database_schema_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.save_database_schema()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_update_database_schema_draft_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.update_database_schema_draft(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_update_database_schema_settings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.update_database_schema_settings(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_database_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_database_integration(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_disable_database_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.disable_database_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_enable_database_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.enable_database_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_save_database_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.save_database_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_set_database_integration_as_default_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.set_database_integration_as_default(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_database_aggregate_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_database_aggregate(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_aggregate_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_aggregate(id="stub-Id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_aggregates_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_aggregates()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_save_database_aggregate_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.save_database_aggregate()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_test_database_aggregate_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.test_database_aggregate()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_database_new_endpoints_surface() -> None:
    client, _ = make_client()
    module = client.hub.database
    assert callable(module.get_allowed_flex_tiers)
    assert callable(module.test_database_integration)
    assert callable(module.reveal_managed_flex_connection_string)


def test_hub_database_get_allowed_flex_tiers_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_allowed_flex_tiers()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_database_test_database_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.test_database_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_database_reveal_managed_flex_connection_string_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.reveal_managed_flex_connection_string(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


# --- Database audit (2026-10): Hub records, trees, list settings, embed, bundle ---
#
# The generated tests above check only the verb and the https scheme. The cases
# below check the fully resolved path of every method added in the database
# audit, that query values reach a GET and a JSON body reaches a write, and
# that the async module has the same methods. Every call goes to a capture
# transport; nothing leaves the process.


DB = "/v2/database"
COLL = "products"
REC = "rec_1"
SCHEMA = "sch_1"
TAX = "services"
AGG = "agg_1"

DbCase = tuple[str, str, str, Callable[[Any], Any]]

HUB_DB_AUDIT_CASES: list[DbCase] = [
    # taxonomies
    ("get_database_taxonomy_tree", "GET", f"{DB}/taxonomies/tree", lambda m: m.get_database_taxonomy_tree()),
    ("get_database_merged_term_tree", "GET", f"{DB}/taxonomies/{TAX}/merged-tree", lambda m: m.get_database_merged_term_tree(TAX)),
    ("get_database_taxonomy_term_tree", "GET", f"{DB}/taxonomies/{TAX}/terms/tree", lambda m: m.get_database_taxonomy_term_tree(TAX)),
    # schemas
    ("apply_database_schema_bundle", "POST", f"{DB}/schemas/apply-bundle", lambda m: m.apply_database_schema_bundle()),
    ("get_database_schema_list_settings", "GET", f"{DB}/schemas/{SCHEMA}/list-settings", lambda m: m.get_database_schema_list_settings(SCHEMA)),
    ("update_database_schema_list_settings", "PUT", f"{DB}/schemas/{SCHEMA}/list-settings", lambda m: m.update_database_schema_list_settings(SCHEMA)),
    ("update_database_schema_embed", "PUT", f"{DB}/schemas/{SCHEMA}/embed", lambda m: m.update_database_schema_embed(SCHEMA)),
    # collections / records
    ("seed_collection_records", "POST", f"{DB}/collections/seed", lambda m: m.seed_collection_records()),
    ("find_records", "GET", f"{DB}/collections/{COLL}", lambda m: m.find_records(COLL)),
    ("insert_record", "POST", f"{DB}/collections/{COLL}", lambda m: m.insert_record(COLL)),
    ("find_one_record", "GET", f"{DB}/collections/{COLL}/{REC}", lambda m: m.find_one_record(COLL, REC)),
    ("update_one_record", "PUT", f"{DB}/collections/{COLL}/{REC}", lambda m: m.update_one_record(COLL, REC)),
    ("delete_record", "DELETE", f"{DB}/collections/{COLL}/{REC}", lambda m: m.delete_record(COLL, REC)),
    ("replace_record", "PUT", f"{DB}/collections/{COLL}/{REC}/replace", lambda m: m.replace_record(COLL, REC)),
    ("change_record_responsibility", "PUT", f"{DB}/collections/{COLL}/{REC}/responsibility", lambda m: m.change_record_responsibility(COLL, REC)),
    ("insert_many_records", "POST", f"{DB}/collections/{COLL}/many", lambda m: m.insert_many_records(COLL)),
    ("update_many_records", "PUT", f"{DB}/collections/{COLL}/many", lambda m: m.update_many_records(COLL)),
    ("delete_many_records", "DELETE", f"{DB}/collections/{COLL}/many", lambda m: m.delete_many_records(COLL)),
    ("count_records", "GET", f"{DB}/collections/{COLL}/count", lambda m: m.count_records(COLL)),
    ("distinct_record_values", "GET", f"{DB}/collections/{COLL}/distinct", lambda m: m.distinct_record_values(COLL)),
    ("get_collection_indexes", "GET", f"{DB}/collections/{COLL}/indexes", lambda m: m.get_collection_indexes(COLL)),
    ("aggregate_records", "POST", f"{DB}/collections/{COLL}/aggregate", lambda m: m.aggregate_records(COLL)),
    ("execute_records_aggregate", "POST", f"{DB}/collections/{COLL}/aggregates/{AGG}/execute", lambda m: m.execute_records_aggregate(COLL, AGG)),
]


@pytest.mark.parametrize(
    ("name", "verb", "path", "call"),
    HUB_DB_AUDIT_CASES,
    ids=[case[0] for case in HUB_DB_AUDIT_CASES],
)
def test_hub_database_audit_method_hits_the_gateway_route(
    name: str, verb: str, path: str, call: Callable[[Any], Any]
) -> None:
    client, transport = make_client(account_id=None)
    call(client.hub.database)

    assert transport.last_request is not None
    assert transport.last_request["method"] == verb
    url = urlparse(transport.last_request["url"])
    assert url.netloc == "hub.norbix.ai"
    assert url.path == path, f"{name}: got {transport.last_request['url']}, expected the path {path}"


def test_hub_database_audit_surface_size() -> None:
    """23 Hub database routes were missing before the audit; all of them are covered here."""
    assert len(HUB_DB_AUDIT_CASES) == 23
    assert len({case[0] for case in HUB_DB_AUDIT_CASES}) == 23


def test_hub_database_find_records_sends_query_values() -> None:
    client, transport = make_client()
    client.hub.database.find_records(COLL, filter='{"status":"active"}', pageSize=5, pageNumber=2)

    assert transport.last_request is not None
    url = urlparse(transport.last_request["url"])
    assert url.path == f"{DB}/collections/{COLL}"
    assert parse_qs(url.query) == {
        "filter": ['{"status":"active"}'],
        "pageSize": ["5"],
        "pageNumber": ["2"],
    }
    assert transport.last_request["body"] == ""


def test_hub_database_insert_record_sends_the_document_as_json() -> None:
    client, transport = make_client()
    client.hub.database.insert_record(COLL, document={"title": "Lamp", "price": 12})

    assert transport.last_request is not None
    assert urlparse(transport.last_request["url"]).query == ""
    assert json.loads(transport.last_request["body"]) == {"document": {"title": "Lamp", "price": 12}}


def test_hub_database_update_schema_list_settings_keeps_the_id_in_the_path_only() -> None:
    client, transport = make_client()
    client.hub.database.update_database_schema_list_settings(SCHEMA, columns=["title", "price"])

    assert transport.last_request is not None
    assert urlparse(transport.last_request["url"]).path == f"{DB}/schemas/{SCHEMA}/list-settings"
    assert json.loads(transport.last_request["body"]) == {"columns": ["title", "price"]}


def test_hub_database_record_call_sends_auth_and_project_headers() -> None:
    client, transport = make_client()
    client.hub.database.count_records(COLL)

    assert transport.last_request is not None
    headers = transport.last_request["headers"]
    assert headers["authorization"] == "Bearer test-token"
    assert headers["x-cm-projectid"] == "test-project"


def test_hub_database_audit_methods_exist_on_the_async_module() -> None:
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
            module = client.hub.database
            for name, _, _, _ in HUB_DB_AUDIT_CASES:
                assert inspect.iscoroutinefunction(getattr(module, name)), name
            await module.delete_record(COLL, REC)
            await module.get_database_merged_term_tree(TAX)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [
        ("DELETE", f"{DB}/collections/{COLL}/{REC}"),
        ("GET", f"{DB}/taxonomies/{TAX}/merged-tree"),
    ]
