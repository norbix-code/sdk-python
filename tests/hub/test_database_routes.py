from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

"""Every Database route the Hub serves for the collection, schema, aggregate,
integration, taxonomy and terms-list screens (matrix sections 03 and 04).

Called through ``client.hub.database`` (sync and async). Each case asserts the
host (hub, not api: the taxonomy trees exist on both), the verb, the exact
path, the query (reads and deletes) and the JSON body (saves). Source of truth:
the gateway ``[Route]`` attributes (Hub.Database); field names from the
generated request types. Every call goes to a mock transport, so nothing
leaves the process.
"""

API = "https://api.test"
HUB = "https://hub.test"
CLIENT_ARGS: dict[str, Any] = {
    "project_id": "test-project",
    "api_key": "key_1",
    "base_url_api": API,
    "base_url_hub": HUB,
    "api_version": "v2",
    "hub_version": "v2",
}

SCH = "sch_1"
AGG = "agg_1"
INT = "int_1"
TAX = "txn_1"

SCHEMA_NEW = {"schemaName": "orders", "dataSchema": '{"type":"object"}', "uiSchema": "{}"}
DRAFT = {"dataSchema": '{"type":"object","properties":{"total":{"type":"number"}}}'}
PUBLISH = {"confirmed": True}
RENAME = {"title": "Customer orders"}
SETTINGS = {"settings": {"softDelete": True, "hasRecordOwner": True, "description": "Shop orders", "endUserOwnRecords": True}}
LIST_SETTINGS = {"settings": {"columns": [{"field": "title", "primary": True}], "defaultSort": {"field": "title", "order": -1}}}
EMBED = {"embed": {"enabled": True, "fields": ["title"], "embeddingIntegrationId": "int_emb", "perUser": False}}
BUNDLE = {"bundleJson": '{"schemas":[]}', "tier": "Free", "publish": False}
OWN_RECORDS = {"dryRun": True, "enable": ["orders"]}
AGGREGATE = {"schemaId": SCH, "displayName": "Totals", "description": "Sum per day", "pipeline": '[{"$count":"n"}]'}
AGGREGATE_TEST = {"collectionName": "orders", "pipeline": '[{"$count":"n"}]', "tokens": {"day": "2026-11-18"}}
INTEGRATION = {
    "integration": {
        "provider": "MongoDbConnectionString",
        "integrationName": "Main",
        "isEnabled": True,
        "connectionString": "mongodb://db.example.test/shop",
    }
}
TAXONOMY = {"viewId": TAX, "taxonomyName": "Countries", "description": "Where we ship", "parentId": "txn_0", "dependencies": ["txn_2"]}

# name, verb, path, query (None: no query), body (None: no body), call
Case = tuple[str, str, str, dict[str, list[str]] | None, dict[str, Any] | None, Callable[[Any], Any]]

CASES: list[Case] = [
    # Collection new / edit and schema new / edit (one route set).
    ("save_database_schema", "POST", "/v2/database/schemas", None, SCHEMA_NEW, lambda m: m.save_database_schema(**SCHEMA_NEW)),
    ("get_database_schema", "GET", f"/v2/database/schemas/{SCH}", {"version": ["2"]}, None,
     lambda m: m.get_database_schema(SCH, version=2)),
    ("delete_database_schema", "DELETE", f"/v2/database/schemas/{SCH}", None, None, lambda m: m.delete_database_schema(SCH)),
    ("get_database_schema_draft", "GET", f"/v2/database/schemas/{SCH}/draft", None, None,
     lambda m: m.get_database_schema_draft(SCH)),
    ("update_database_schema_draft", "PUT", f"/v2/database/schemas/{SCH}/draft", None, DRAFT,
     lambda m: m.update_database_schema_draft(SCH, **DRAFT)),
    ("discard_database_schema_draft", "DELETE", f"/v2/database/schemas/{SCH}/draft", None, None,
     lambda m: m.discard_database_schema_draft(SCH)),
    ("publish_database_schema", "POST", f"/v2/database/schemas/{SCH}/publish", None, PUBLISH,
     lambda m: m.publish_database_schema(SCH, **PUBLISH)),
    ("rename_database_schema", "PUT", f"/v2/database/schemas/{SCH}/rename", None, RENAME,
     lambda m: m.rename_database_schema(SCH, **RENAME)),
    ("update_database_schema_settings", "PUT", f"/v2/database/schemas/{SCH}/settings", None, SETTINGS,
     lambda m: m.update_database_schema_settings(SCH, **SETTINGS)),
    ("get_database_schema_list_settings", "GET", f"/v2/database/schemas/{SCH}/list-settings", None, None,
     lambda m: m.get_database_schema_list_settings(SCH)),
    ("update_database_schema_list_settings", "PUT", f"/v2/database/schemas/{SCH}/list-settings", None, LIST_SETTINGS,
     lambda m: m.update_database_schema_list_settings(SCH, **LIST_SETTINGS)),
    ("update_database_schema_embed", "PUT", f"/v2/database/schemas/{SCH}/embed", None, EMBED,
     lambda m: m.update_database_schema_embed(SCH, **EMBED)),
    ("get_database_schema_versions", "GET", f"/v2/database/schemas/{SCH}/versions", None, None,
     lambda m: m.get_database_schema_versions(SCH)),
    ("get_database_schema_version_diff", "GET", f"/v2/database/schemas/{SCH}/versions/diff",
     {"fromVersion": ["1"], "toVersion": ["2"]}, None,
     lambda m: m.get_database_schema_version_diff(SCH, fromVersion=1, toVersion=2)),
    ("get_database_schema_index_status", "GET", f"/v2/database/schemas/{SCH}/index-status", None, None,
     lambda m: m.get_database_schema_index_status(SCH)),
    ("apply_database_schema_bundle", "POST", "/v2/database/schemas/apply-bundle", None, BUNDLE,
     lambda m: m.apply_database_schema_bundle(**BUNDLE)),
    ("end_user_own_records_report", "POST", "/v2/database/schemas/end-user-own-records", None, OWN_RECORDS,
     lambda m: m.end_user_own_records_report(**OWN_RECORDS)),
    # Aggregates list.
    ("get_database_aggregates", "GET", "/v2/database/aggregates", {"schemaId": [SCH]}, None,
     lambda m: m.get_database_aggregates(schemaId=SCH)),
    ("delete_database_aggregate", "DELETE", f"/v2/database/aggregates/{AGG}", {"schemaId": [SCH]}, None,
     lambda m: m.delete_database_aggregate(AGG, schemaId=SCH)),
    # Aggregate new / edit.
    ("get_database_aggregate", "GET", f"/v2/database/aggregates/{AGG}", {"schemaId": [SCH]}, None,
     lambda m: m.get_database_aggregate(AGG, schemaId=SCH)),
    ("save_database_aggregate", "POST", "/v2/database/aggregates", None, AGGREGATE,
     lambda m: m.save_database_aggregate(**AGGREGATE)),
    ("test_database_aggregate", "POST", "/v2/database/aggregates/test", None, AGGREGATE_TEST,
     lambda m: m.test_database_aggregate(**AGGREGATE_TEST)),
    # DB integrations.
    ("get_database_integrations", "GET", "/v2/database/integrations", None, None, lambda m: m.get_database_integrations()),
    ("get_database_integration", "GET", f"/v2/database/integrations/{INT}", None, None,
     lambda m: m.get_database_integration(INT)),
    ("save_database_integration", "POST", "/v2/database/integrations", None, INTEGRATION,
     lambda m: m.save_database_integration(**INTEGRATION)),
    ("delete_database_integration", "DELETE", f"/v2/database/integrations/{INT}", None, None,
     lambda m: m.delete_database_integration(INT)),
    ("enable_database_integration", "PUT", f"/v2/database/integrations/{INT}/enable", None, None,
     lambda m: m.enable_database_integration(INT)),
    ("disable_database_integration", "PUT", f"/v2/database/integrations/{INT}/disable", None, None,
     lambda m: m.disable_database_integration(INT)),
    ("set_database_integration_as_default", "PUT", f"/v2/database/integrations/{INT}/default", None, None,
     lambda m: m.set_database_integration_as_default(INT)),
    ("get_allowed_flex_tiers", "GET", "/v2/database/integrations/flex-tiers", None, None, lambda m: m.get_allowed_flex_tiers()),
    ("test_database_integration", "POST", "/v2/database/integrations/test", None, {"integrationId": INT},
     lambda m: m.test_database_integration(integrationId=INT)),
    ("get_network_addresses", "GET", "/v2/database/network-addresses", {"regionCode": ["nb-eu-germany"]}, None,
     lambda m: m.get_network_addresses(regionCode="nb-eu-germany")),
    # Taxonomies list.
    ("get_database_taxonomies", "GET", "/v2/database/taxonomies", {"pageSize": ["25"]}, None,
     lambda m: m.get_database_taxonomies(pageSize=25)),
    ("delete_database_taxonomy", "DELETE", f"/v2/database/taxonomies/{TAX}", None, None,
     lambda m: m.delete_database_taxonomy(TAX)),
    ("get_database_taxonomy_tree", "GET", "/v2/database/taxonomies/tree", {"includeTerms": ["true"]}, None,
     lambda m: m.get_database_taxonomy_tree(includeTerms=True)),
    # Taxonomy new / edit.
    ("get_database_taxonomy", "GET", f"/v2/database/taxonomies/{TAX}", None, None, lambda m: m.get_database_taxonomy(TAX)),
    ("save_database_taxonomy", "POST", "/v2/database/taxonomies", None, TAXONOMY, lambda m: m.save_database_taxonomy(**TAXONOMY)),
    # Terms list.
    ("delete_many_database_taxonomy_terms", "DELETE", f"/v2/database/taxonomies/{TAX}/terms/many",
     {"filter": ['{"active":false}']}, None,
     lambda m: m.delete_many_database_taxonomy_terms(TAX, filter='{"active":false}')),
    ("get_database_taxonomy_term_tree", "GET", "/v2/database/taxonomies/countries/terms/tree",
     {"rootTermId": ["t_1"], "depth": ["2"]}, None,
     lambda m: m.get_database_taxonomy_term_tree("countries", rootTermId="t_1", depth=2)),
    ("get_database_merged_term_tree", "GET", "/v2/database/taxonomies/countries/merged-tree",
     {"databaseIntegrationId": [INT]}, None,
     lambda m: m.get_database_merged_term_tree("countries", databaseIntegrationId=INT)),
]

IDS = [c[0] for c in CASES]


def _capture(seen: list[httpx.Request]) -> Callable[[httpx.Request], httpx.Response]:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    return handler


def _assert_request(
    request: httpx.Request, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None
) -> None:
    assert f"{request.url.scheme}://{request.url.host}" == HUB
    assert request.method == verb
    assert request.url.path == path
    assert parse_qs(request.url.query.decode()) == (query or {})
    if body is None:
        assert request.content == b""
    else:
        assert json.loads(request.content) == body
    assert request.headers["authorization"] == "Bearer key_1"
    assert request.headers["norbix-project-id"] == "test-project"


def test_hub_database_route_count() -> None:
    # Schema routes 17 (shared by collection new / edit and schema new / edit)
    # + aggregates list 2 + aggregate new / edit 3 + integrations 10
    # + taxonomies list 3 + taxonomy new / edit 2 + terms list 3.
    assert len(CASES) == 17 + 2 + 3 + 10 + 3 + 2 + 3
    assert len(set(IDS)) == len(IDS)


@pytest.mark.parametrize("name, verb, path, query, body, call", CASES, ids=IDS)
def test_hub_database_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))))

    call(client.hub.database)

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query, body)


@pytest.mark.parametrize("name, verb, path, query, body, call", CASES, ids=IDS)
def test_async_hub_database_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(**CLIENT_ARGS, http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))))
        try:
            await call(client.hub.database)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query, body)
