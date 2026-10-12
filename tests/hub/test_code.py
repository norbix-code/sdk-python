from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix

from ..helpers import make_client


def test_hub_code_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.code
    assert callable(module.disable_code)
    assert callable(module.enable_code)
    assert callable(module.get_code_integrations)
    assert callable(module.save_code_integration)
    assert callable(module.confirm_code_integration_human_delivery)
    assert callable(module.test_code_integration)
    assert callable(module.delete_code_integration)
    assert callable(module.disable_code_integration)
    assert callable(module.enable_code_integration)
    assert callable(module.get_code_integration)
    assert callable(module.get_marketplace_integrations)
    assert callable(module.save_marketplace_integration)
    assert callable(module.delete_marketplace_integration)
    assert callable(module.get_marketplace_integration)
    assert callable(module.get_marketplace_bindings)
    assert callable(module.save_marketplace_function_binding)
    assert callable(module.delete_marketplace_function_binding)
    assert callable(module.get_marketplace_binding)
    assert callable(module.disable_marketplace_function_binding)
    assert callable(module.enable_marketplace_function_binding)
    assert callable(module.invoke_marketplace_function_binding)
    assert callable(module.get_marketplace_binding_tokens)
    assert callable(module.disable_marketplace_integration)
    assert callable(module.enable_marketplace_integration)
    assert callable(module.get_marketplace_function_catalog)
    assert callable(module.get_marketplace_listings)
    assert callable(module.get_marketplace_listing_function_tokens)
    # cloud functions (gateway audit/code, Code.Functions.md §3.3, §3.4, §5.1)
    assert callable(module.get_code_functions)
    assert callable(module.get_code_function_qualifiers)
    assert callable(module.invoke_code_function)
    assert callable(module.get_code_function_event_sample)
    assert callable(module.get_code_function_runs)


def test_hub_code_disable_code_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.disable_code()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_enable_code_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.enable_code()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_code_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_code_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_save_code_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.save_code_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_confirm_code_integration_human_delivery_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.confirm_code_integration_human_delivery()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_test_code_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.test_code_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_delete_code_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.delete_code_integration(id="stub-id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_disable_code_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.disable_code_integration(id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_enable_code_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.enable_code_integration(id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_code_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_code_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_save_marketplace_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.save_marketplace_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_delete_marketplace_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.delete_marketplace_integration(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_integration(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_bindings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_bindings(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_save_marketplace_function_binding_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.save_marketplace_function_binding(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_delete_marketplace_function_binding_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.delete_marketplace_function_binding(integration_view_id="stub-integration_view_id", binding_view_id="stub-binding_view_id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_binding_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_binding(integration_view_id="stub-integration_view_id", binding_view_id="stub-binding_view_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_disable_marketplace_function_binding_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.disable_marketplace_function_binding(integration_view_id="stub-integration_view_id", binding_view_id="stub-binding_view_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_enable_marketplace_function_binding_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.enable_marketplace_function_binding(integration_view_id="stub-integration_view_id", binding_view_id="stub-binding_view_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_invoke_marketplace_function_binding_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.invoke_marketplace_function_binding(integration_view_id="stub-integration_view_id", binding_view_id="stub-binding_view_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_binding_tokens_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_binding_tokens(integration_view_id="stub-integration_view_id", binding_view_id="stub-binding_view_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_disable_marketplace_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.disable_marketplace_integration(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_enable_marketplace_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.enable_marketplace_integration(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_function_catalog_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_function_catalog(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_listings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_listings()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_listing_function_tokens_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_listing_function_tokens(listing_view_id="stub-listing_view_id", function_key="stub-function_key")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


# --- cloud functions ---------------------------------------------------------
#
# The five routes of Code.Functions.md: the verb, the resolved path, and where
# each parameter goes — GET filters in the query string, the invoke request in
# the JSON body. Sync and async against a capture transport, never a gateway.

INTEGRATION_ID = "int_1"
FUNCTION_REF = {"integrationId": INTEGRATION_ID, "functionId": "orders-on-update", "qualifier": "prod"}
INVOKE_REQUEST: dict[str, Any] = {
    "functionRef": FUNCTION_REF,
    "payload": {"orderId": "6ac54a59212c29912eaddd81", "dryRun": True},
    "invocationType": "Sync",
    "runAsUserId": "usr_svc",
}

# name, verb, expected path, expected query (None: none), expected body (None: none), call
FunctionCase = tuple[str, str, str, dict[str, list[str]] | None, dict[str, Any] | None, Callable[[Any], Any]]

FUNCTION_CASES: list[FunctionCase] = [
    (
        "get_code_functions",
        "GET",
        "/v3/code/functions",
        {"integrationId": [INTEGRATION_ID], "prefix": ["orders-"], "tag": ["team=orders"], "pageSize": ["50"]},
        None,
        lambda m: m.get_code_functions(integrationId=INTEGRATION_ID, prefix="orders-", tag="team=orders", pageSize=50),
    ),
    (
        "get_code_function_qualifiers",
        "GET",
        "/v3/code/functions/qualifiers",
        {"integrationId": [INTEGRATION_ID], "functionId": ["orders-on-update"]},
        None,
        lambda m: m.get_code_function_qualifiers(integrationId=INTEGRATION_ID, functionId="orders-on-update"),
    ),
    (
        "invoke_code_function",
        "POST",
        "/v3/code/functions/invoke",
        None,
        INVOKE_REQUEST,
        lambda m: m.invoke_code_function(**INVOKE_REQUEST),
    ),
    (
        "get_code_function_event_sample",
        "GET",
        "/v3/code/functions/event-sample",
        {"source": ["database"], "event": ["database.record.updated"], "schemaId": ["sch_1"]},
        None,
        lambda m: m.get_code_function_event_sample(source="database", event="database.record.updated", schemaId="sch_1"),
    ),
    (
        "get_code_function_runs",
        "GET",
        "/v3/code/functions/runs",
        {"triggerId": ["trg_1"], "limit": ["5"]},
        None,
        lambda m: m.get_code_function_runs(triggerId="trg_1", limit=5),
    ),
]


def _assert_function_request(
    name: str,
    method: str,
    url: str,
    body: str,
    verb: str,
    path: str,
    query: dict[str, list[str]] | None,
    expected_body: dict[str, Any] | None,
) -> None:
    parsed = urlparse(url)
    assert method == verb, f"{name}: verb {method}, expected {verb}"
    assert parsed.path == path, f"{name}: got {url}, expected the path {path}"
    assert parse_qs(parsed.query) == (query or {}), f"{name}: query {parsed.query!r}"
    if expected_body is None:
        assert body == "", f"{name}: expected no body, got {body!r}"
    else:
        assert json.loads(body) == expected_body, f"{name}: body {body}"


@pytest.mark.parametrize(("name", "verb", "path", "query", "body", "call"), FUNCTION_CASES, ids=[c[0] for c in FUNCTION_CASES])
def test_code_function_request_shape(
    name: str,
    verb: str,
    path: str,
    query: dict[str, list[str]] | None,
    body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    client, transport = make_client()
    call(client.hub.code)
    assert transport.last_request is not None
    _assert_function_request(
        name,
        transport.last_request["method"],
        transport.last_request["url"],
        transport.last_request["body"],
        verb,
        path,
        query,
        body,
    )
    assert transport.last_request["headers"]["authorization"] == "Bearer test-token"


def test_async_code_function_endpoints_hit_the_same_routes() -> None:
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
            for _, _, _, _, _, call in FUNCTION_CASES:
                await call(client.hub.code)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == len(FUNCTION_CASES)
    for request, (name, verb, path, query, body, _) in zip(seen, FUNCTION_CASES, strict=True):
        _assert_function_request(name, request.method, str(request.url), request.content.decode("utf-8"), verb, path, query, body)


def test_code_function_surface_size() -> None:
    """Five cloud-function routes in the gateway (Code.Functions.md). A new one changes this count."""
    assert len(FUNCTION_CASES) == 5
    assert len({case[0] for case in FUNCTION_CASES}) == 5


def test_invoke_code_function_sends_the_function_ref_in_the_body() -> None:
    client, transport = make_client()
    client.hub.code.invoke_code_function(functionRef=FUNCTION_REF, invocationType="Async")

    assert transport.last_request is not None
    sent = json.loads(transport.last_request["body"])
    assert sent == {"functionRef": FUNCTION_REF, "invocationType": "Async"}
