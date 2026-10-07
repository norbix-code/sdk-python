"""Api Database — the schema-content campaign, seen from the SDK.

The gateway branch ``audit/schema-content`` adds ``expandReferences`` to the
record reads, ``arrayFilters`` + nested update paths to the record updates,
nested / array / json field DTOs on the schema read, ``slug`` on terms, and the
record error codes 039–056. The SDK is untyped on the wire: these tests pin
that each option lands where the gateway reads it, that nested documents pass
through untouched, that the new field DTOs come back as sent, and that every
new error code reaches the caller. Every call goes to a fake transport.
"""

from __future__ import annotations

import asyncio
import json
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, NorbixError, ReferenceDisplay

from ..helpers import CaptureTransport


def _client() -> tuple[Norbix, CaptureTransport]:
    transport = CaptureTransport()
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=transport),
    )
    return client, transport


def _answering(body: dict[str, Any], status: int = 200) -> Norbix:
    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(status, json=body)

    return Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )


def _refusing(code: str, message: str, context: dict[str, Any] | None = None) -> Norbix:
    error: dict[str, Any] = {"message": message, "errorCode": code}
    if context is not None:
        error["context"] = context
    return _answering({"responseStatus": {"isSuccess": False, "errors": [error]}}, status=400)


class _AsyncCapture:
    """A recording handler for ``httpx.MockTransport`` (the sync CaptureTransport cannot serve an AsyncClient)."""

    def __init__(self) -> None:
        self.last_request: dict[str, Any] | None = None

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.last_request = {
            "method": request.method,
            "url": str(request.url),
            "body": request.content.decode("utf-8") if request.content else "",
        }
        return httpx.Response(200, json={})


def _async_client() -> tuple[AsyncNorbix, _AsyncCapture]:
    capture = _AsyncCapture()
    client = AsyncNorbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(capture)),
    )
    return client, capture


def _query(transport: CaptureTransport | _AsyncCapture) -> dict[str, list[str]]:
    assert transport.last_request is not None
    return parse_qs(urlparse(transport.last_request["url"]).query)


def _body(transport: CaptureTransport | _AsyncCapture) -> dict[str, Any]:
    assert transport.last_request is not None
    return json.loads(transport.last_request["body"])


# --- expandReferences on the record reads -----------------------------------


def test_find_sends_expand_references_in_the_query() -> None:
    client, transport = _client()
    client.api.database.find("articles", expand_references=True, pageSize=10)
    assert transport.last_request is not None
    assert urlparse(transport.last_request["url"]).path == "/v2/database/collections/articles"
    assert _query(transport) == {"expandReferences": ["true"], "pageSize": ["10"]}


def test_find_one_sends_expand_references_in_the_query() -> None:
    client, transport = _client()
    client.api.database.find_one("articles", "rec_1", expand_references=True)
    assert transport.last_request is not None
    assert urlparse(transport.last_request["url"]).path == "/v2/database/collections/articles/rec_1"
    assert _query(transport) == {"expandReferences": ["true"]}


def test_find_own_sends_expand_references_in_the_query() -> None:
    client, transport = _client()
    client.api.database.find_own("articles", expand_references=True)
    assert transport.last_request is not None
    assert urlparse(transport.last_request["url"]).path == "/v2/database/collections/articles/own"
    assert _query(transport) == {"expandReferences": ["true"]}


def test_expand_references_false_is_sent_as_false() -> None:
    client, transport = _client()
    client.api.database.find("articles", expand_references=False)
    assert _query(transport) == {"expandReferences": ["false"]}


def test_find_without_the_option_sends_nothing_extra() -> None:
    client, transport = _client()
    client.api.database.find("articles")
    assert _query(transport) == {}


def test_expand_references_by_wire_name_still_works() -> None:
    client, transport = _client()
    client.api.database.find("articles", expandReferences=True)
    assert _query(transport) == {"expandReferences": ["true"]}


def test_async_reads_send_expand_references() -> None:
    client, transport = _async_client()

    async def run() -> None:
        await client.api.database.find("articles", expand_references=True)
        assert _query(transport) == {"expandReferences": ["true"]}
        await client.api.database.find_one("articles", "rec_1", expand_references=True)
        assert _query(transport) == {"expandReferences": ["true"]}
        await client.api.database.find_own("articles", expand_references=True)
        assert _query(transport) == {"expandReferences": ["true"]}
        await client.aclose()

    asyncio.run(run())


# --- the { id, display } result ----------------------------------------------

EXPANDED_RECORD: dict[str, Any] = {
    "_id": "rec_1",
    "title": "Hello",
    "author": {"id": "usr_1", "display": "Jane Doe"},
    "tags": [{"id": "6650", "display": {"en": "News"}}, {"id": "6651", "display": None}],
    "cover": {"id": "nbfl_7hK2abc", "display": "cover.png"},
    "customer": {"address": {"region": {"id": "term_lt", "display": "lithuania"}}},
}


def test_expanded_read_returns_id_and_display_untouched() -> None:
    client = _answering({"result": json.dumps(EXPANDED_RECORD), "responseStatus": {"isSuccess": True}})
    answer = client.api.database.find_one("articles", "rec_1", expand_references=True)
    record = json.loads(answer["result"])
    assert record["author"] == {"id": "usr_1", "display": "Jane Doe"}
    assert record["tags"][1] == {"id": "6651", "display": None}
    assert record["customer"]["address"]["region"] == {"id": "term_lt", "display": "lithuania"}


def test_reference_display_parses_one_value() -> None:
    one = ReferenceDisplay.from_value(EXPANDED_RECORD["author"])
    assert isinstance(one, ReferenceDisplay)
    assert (one.id, one.display) == ("usr_1", "Jane Doe")


def test_reference_display_parses_a_list_and_a_missing_target() -> None:
    many = ReferenceDisplay.from_value(EXPANDED_RECORD["tags"])
    assert isinstance(many, list)
    assert [item.id for item in many] == ["6650", "6651"]
    assert many[0].display == {"en": "News"}
    assert many[1].display is None


def test_reference_display_of_none_is_none() -> None:
    assert ReferenceDisplay.from_value(None) is None


def test_reference_display_keeps_extra_members() -> None:
    parsed = ReferenceDisplay.model_validate({"id": "usr_1", "display": "Jane", "kind": "user"})
    assert parsed.model_dump() == {"id": "usr_1", "display": "Jane", "kind": "user"}


# --- arrayFilters and nested paths on the record updates ---------------------


def test_update_one_sends_array_filters_string_as_given() -> None:
    client, transport = _client()
    client.api.database.update_one(
        "orders",
        "rec_1",
        update='{"lines.$[line].qty": 3, "meta.words": 130}',
        array_filters='[{"line.sku": "A-1"}]',
    )
    assert transport.last_request is not None
    assert transport.last_request["method"] == "PUT"
    assert urlparse(transport.last_request["url"]).path == "/v2/database/collections/orders/rec_1"
    assert _body(transport) == {
        "update": '{"lines.$[line].qty": 3, "meta.words": 130}',
        "arrayFilters": '[{"line.sku": "A-1"}]',
    }


def test_update_one_serialises_array_filters_given_as_a_list() -> None:
    client, transport = _client()
    client.api.database.update_one(
        "orders",
        "rec_1",
        update='{"lines.$[line].qty": 3}',
        array_filters=[{"$or": [{"line.sku": "A"}, {"line.sku": "B"}]}],
    )
    sent = _body(transport)
    assert json.loads(sent["arrayFilters"]) == [{"$or": [{"line.sku": "A"}, {"line.sku": "B"}]}]


def test_update_many_sends_array_filters_in_the_body() -> None:
    client, transport = _client()
    client.api.database.update_many(
        "orders",
        filter='{"status": "open"}',
        update='{"lines.$[].qty": 1}',
        array_filters="[]",
    )
    assert transport.last_request is not None
    assert urlparse(transport.last_request["url"]).path == "/v2/database/collections/orders/many"
    assert _body(transport) == {"filter": '{"status": "open"}', "update": '{"lines.$[].qty": 1}', "arrayFilters": "[]"}


def test_update_without_array_filters_sends_no_such_field() -> None:
    client, transport = _client()
    client.api.database.update_one("orders", "rec_1", update='{"address.city": "Vilnius"}')
    assert _body(transport) == {"update": '{"address.city": "Vilnius"}'}


def test_array_filters_by_wire_name_still_works() -> None:
    client, transport = _client()
    client.api.database.update_one("orders", "rec_1", update="{}", arrayFilters='[{"line.sku": "A-1"}]')
    assert _body(transport)["arrayFilters"] == '[{"line.sku": "A-1"}]'


def test_async_updates_send_array_filters() -> None:
    client, transport = _async_client()

    async def run() -> None:
        await client.api.database.update_one("orders", "rec_1", update="{}", array_filters=[{"line.sku": "A-1"}])
        assert _body(transport)["arrayFilters"] == '[{"line.sku": "A-1"}]'
        await client.api.database.update_many("orders", filter="{}", update="{}", allRecords=True, array_filters="[]")
        assert _body(transport)["arrayFilters"] == "[]"
        await client.aclose()

    asyncio.run(run())


# --- nested documents pass through as sent -----------------------------------

NESTED_DOCUMENT: dict[str, Any] = {
    "title": "Order 1",
    "address": {"city": "Vilnius", "geo": {"lat": 54.68, "lng": 25.28}},
    "lines": [{"sku": "A-1", "qty": 2}, {"sku": "B-2", "qty": 1}],
    "settings": {"theme": {"dark": True}},
}


def test_insert_one_sends_a_nested_document_untouched() -> None:
    client, transport = _client()
    client.api.database.insert_one("orders", document=json.dumps(NESTED_DOCUMENT))
    assert json.loads(_body(transport)["document"]) == NESTED_DOCUMENT


def test_find_sends_a_nested_filter_and_a_dotted_sort() -> None:
    client, transport = _client()
    client.api.database.find(
        "orders",
        filter='{"lines": {"$elemMatch": {"sku": "A-1", "qty": {"$gte": 2}}}}',
        sortBy="address.city",
    )
    assert _query(transport) == {
        "filter": ['{"lines": {"$elemMatch": {"sku": "A-1", "qty": {"$gte": 2}}}}'],
        "sortBy": ["address.city"],
    }


# --- the new schema field DTOs come back as sent ----------------------------

SCHEMA_WITH_NESTED_FIELDS: dict[str, Any] = {
    "fields": [
        {"$fieldType": "string", "name": "title", "default": "Untitled", "unique": True},
        {
            "$fieldType": "object",
            "name": "address",
            "properties": [
                {"$fieldType": "string", "name": "city"},
                {"$fieldType": "object", "name": "geo", "properties": [{"$fieldType": "decimal", "name": "lat"}]},
            ],
            "required": ["city"],
        },
        {
            "$fieldType": "array",
            "name": "lines",
            "items": {"$fieldType": "object", "name": "line", "properties": [{"$fieldType": "integer", "name": "qty"}]},
            "minItems": 1,
            "maxItems": 50,
            "uniqueItems": False,
        },
        {"$fieldType": "json", "name": "settings", "maxBytes": 65536},
        {"$fieldType": "currency", "name": "price", "multipleOf": 0.01, "minimum": 0, "default": {"value": 9.99, "currency": "EUR"}},
        {"$fieldType": "file", "name": "cover", "minItems": 0, "maxItems": 3, "allowedFileType": "image/*", "maxSizeMb": 5},
        {"$fieldType": "userSelection", "name": "author", "displayField": "displayName"},
        {"$fieldType": "collectionSelection", "name": "customer", "collectionId": "sch_customers", "displayField": "name"},
        {"$fieldType": "taxonomySelection", "name": "region", "taxonomyId": "txn_regions", "displayField": "slug"},
        {"$fieldType": "tags", "name": "tags", "minItems": 1, "maxItems": 10, "default": ["news"]},
    ]
}


def test_get_database_schema_returns_the_nested_field_dtos_as_sent() -> None:
    client = _answering({"result": SCHEMA_WITH_NESTED_FIELDS, "responseStatus": {"isSuccess": True}})
    answer = client.api.database.get_database_schema("sch_orders")
    fields = {field["name"]: field for field in answer["result"]["fields"]}
    assert fields["address"]["$fieldType"] == "object"
    assert fields["address"]["properties"][1]["properties"][0]["name"] == "lat"
    assert fields["lines"]["items"]["$fieldType"] == "object"
    assert (fields["lines"]["minItems"], fields["lines"]["maxItems"]) == (1, 50)
    assert fields["settings"] == {"$fieldType": "json", "name": "settings", "maxBytes": 65536}
    assert fields["price"]["default"] == {"value": 9.99, "currency": "EUR"}
    assert fields["cover"]["allowedFileType"] == "image/*"
    assert fields["author"]["displayField"] == "displayName"
    assert fields["region"]["displayField"] == "slug"
    assert fields["tags"]["default"] == ["news"]


def test_find_terms_returns_the_slug() -> None:
    body = {
        "list": {"items": [{"id": "term_fr", "name": "France", "slug": "france"}], "hasMore": False},
        "responseStatus": {"isSuccess": True},
    }
    client = _answering(body)
    answer = client.api.database.find_terms("countries")
    assert answer["list"]["items"][0]["slug"] == "france"


# --- the new error codes reach the caller ------------------------------------

RECORD_ERROR_CODES = [
    ("CM-ERRORS-DATABASE-039", "type"),
    ("CM-ERRORS-DATABASE-040", "length"),
    ("CM-ERRORS-DATABASE-041", "pattern"),
    ("CM-ERRORS-DATABASE-042", "format"),
    ("CM-ERRORS-DATABASE-043", "range"),
    ("CM-ERRORS-DATABASE-044", "multipleOf"),
    ("CM-ERRORS-DATABASE-045", "enum"),
    ("CM-ERRORS-DATABASE-046", "uniqueItems"),
    ("CM-ERRORS-DATABASE-047", "properties"),
    ("CM-ERRORS-DATABASE-048", "coordinates"),
    ("CM-ERRORS-DATABASE-049", "translateOptions"),
    ("CM-ERRORS-DATABASE-050", "reference"),
    ("CM-ERRORS-DATABASE-051", "reference"),
    ("CM-ERRORS-DATABASE-052", "reference"),
    ("CM-ERRORS-DATABASE-053", "reference"),
    ("CM-ERRORS-DATABASE-054", "reference"),
    ("CM-ERRORS-DATABASE-055", "reference"),
]


@pytest.mark.parametrize(("code", "keyword"), RECORD_ERROR_CODES)
def test_record_validation_codes_reach_the_caller_with_the_field_path(code: str, keyword: str) -> None:
    client = _refusing(code, "Field 'lines[1].qty' is invalid: must be at least 1", {"FieldName": "lines[1].qty", "Keyword": keyword})
    with pytest.raises(NorbixError) as caught:
        client.api.database.insert_one("orders", document=json.dumps(NESTED_DOCUMENT))
    assert caught.value.error_code == code
    assert caught.value.errors[0].context == {"FieldName": "lines[1].qty", "Keyword": keyword}


def test_reference_expansion_refusal_names_the_source() -> None:
    context = {
        "SourceKind": "users",
        "Source": "users",
        "Fields": ["author"],
        "MissingPermissions": ["membership:read"],
    }
    client = _refusing("CM-ERRORS-DATABASE-056", "You can read articles, but not the people it links to", context)
    with pytest.raises(NorbixError) as caught:
        client.api.database.find("articles", expand_references=True)
    assert caught.value.error_code == "CM-ERRORS-DATABASE-056"
    assert caught.value.errors[0].context == context


@pytest.mark.parametrize(
    "code",
    ["CM-ERRORS-SCHEMA-036", "CM-ERRORS-SCHEMA-037", "CM-ERRORS-SCHEMA-038", "CM-ERRORS-SCHEMA-039", "CM-ERRORS-SCHEMA-040", "CM-ERRORS-SCHEMA-041", "CM-ERRORS-TAXONOMIES-012", "CM-ERRORS-TAXONOMIES-013"],
)
def test_schema_and_term_codes_reach_the_caller(code: str) -> None:
    client = _refusing(code, "refused")
    with pytest.raises(NorbixError) as caught:
        client.api.database.get_database_schema("sch_orders")
    assert caught.value.error_code == code


def test_array_filters_shape_error_reaches_the_caller() -> None:
    client = _refusing(
        "CM-ERRORS-PROPERTY-002",
        "ArrayFilters: identifier 'line' has no filter",
        {"Property": "ArrayFilters", "Reasons": ["identifier 'line' has no filter"]},
    )
    with pytest.raises(NorbixError) as caught:
        client.api.database.update_one("orders", "rec_1", update='{"lines.$[line].qty": 3}', array_filters="[]")
    assert caught.value.errors[0].context["Property"] == "ArrayFilters"
