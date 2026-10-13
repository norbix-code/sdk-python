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


# --- marketplace -------------------------------------------------------------
#
# The 23 routes of Code.Marketplace.md §14: the verb, the resolved path (version
# and ids filled in) and where each parameter goes — GET / DELETE in the query
# string, POST / PUT in the JSON body. Sync and async against a capture
# transport, never a gateway.

# name, verb, expected path, expected query (None: none), expected body (None: none), call
MARKETPLACE_CASES: list[FunctionCase] = [
    ("get_marketplace_listings", "GET", "/v3/code/marketplace/listings", {'search': ['slack']}, None, lambda m: m.get_marketplace_listings(search='slack')),
    ("get_marketplace_listing_function_tokens", "GET", "/v3/code/marketplace/listings/ml_slack_v1/functions/slack.post-message/tokens", None, None, lambda m: m.get_marketplace_listing_function_tokens("ml_slack_v1", "slack.post-message")),
    ("get_marketplace_integrations", "GET", "/v3/code/marketplace/integrations", None, None, lambda m: m.get_marketplace_integrations()),
    ("get_marketplace_integration", "GET", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb", None, None, lambda m: m.get_marketplace_integration("int_6Qp1dW2kRm8NsT4vYc0Hb")),
    ("save_marketplace_integration", "POST", "/v3/code/marketplace/integrations", None, {'integration': {'listingViewId': 'ml_slack_v1', 'config': {'workspace': 'acme'}}, 'secrets': {'botToken': 'xoxb-test'}}, lambda m: m.save_marketplace_integration(integration={'listingViewId': 'ml_slack_v1', 'config': {'workspace': 'acme'}}, secrets={'botToken': 'xoxb-test'})),
    ("delete_marketplace_integration", "DELETE", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb", None, None, lambda m: m.delete_marketplace_integration("int_6Qp1dW2kRm8NsT4vYc0Hb")),
    ("enable_marketplace_integration", "POST", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/enable", None, None, lambda m: m.enable_marketplace_integration("int_6Qp1dW2kRm8NsT4vYc0Hb")),
    ("disable_marketplace_integration", "POST", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/disable", None, None, lambda m: m.disable_marketplace_integration("int_6Qp1dW2kRm8NsT4vYc0Hb")),
    ("get_marketplace_functions", "GET", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/functions", None, None, lambda m: m.get_marketplace_functions("int_6Qp1dW2kRm8NsT4vYc0Hb")),
    ("get_marketplace_function", "GET", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/functions/func_4hT2b9QkLm3XcT1yRfGh7a", None, None, lambda m: m.get_marketplace_function("int_6Qp1dW2kRm8NsT4vYc0Hb", "func_4hT2b9QkLm3XcT1yRfGh7a")),
    ("save_marketplace_function", "POST", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/functions", None, {'function': {'functionKey': 'slack.post-message', 'displayName': 'Post order', 'arguments': {'channel': '#orders'}}}, lambda m: m.save_marketplace_function("int_6Qp1dW2kRm8NsT4vYc0Hb", function={'functionKey': 'slack.post-message', 'displayName': 'Post order', 'arguments': {'channel': '#orders'}})),
    ("delete_marketplace_function", "DELETE", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/functions/func_4hT2b9QkLm3XcT1yRfGh7a", None, None, lambda m: m.delete_marketplace_function("int_6Qp1dW2kRm8NsT4vYc0Hb", "func_4hT2b9QkLm3XcT1yRfGh7a")),
    ("enable_marketplace_function", "POST", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/functions/func_4hT2b9QkLm3XcT1yRfGh7a/enable", None, None, lambda m: m.enable_marketplace_function("int_6Qp1dW2kRm8NsT4vYc0Hb", "func_4hT2b9QkLm3XcT1yRfGh7a")),
    ("disable_marketplace_function", "POST", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/functions/func_4hT2b9QkLm3XcT1yRfGh7a/disable", None, None, lambda m: m.disable_marketplace_function("int_6Qp1dW2kRm8NsT4vYc0Hb", "func_4hT2b9QkLm3XcT1yRfGh7a")),
    ("get_marketplace_function_tokens", "GET", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/functions/func_4hT2b9QkLm3XcT1yRfGh7a/tokens", None, None, lambda m: m.get_marketplace_function_tokens("int_6Qp1dW2kRm8NsT4vYc0Hb", "func_4hT2b9QkLm3XcT1yRfGh7a")),
    ("invoke_marketplace_function", "POST", "/v3/code/marketplace/functions/func_4hT2b9QkLm3XcT1yRfGh7a/invoke", None, {'payload': {'text': 'Order 6ac54a59 shipped'}}, lambda m: m.invoke_marketplace_function("func_4hT2b9QkLm3XcT1yRfGh7a", payload={'text': 'Order 6ac54a59 shipped'})),
    ("get_marketplace_listing", "GET", "/v3/code/marketplace/listings/ml_slack_v1", None, None, lambda m: m.get_marketplace_listing("ml_slack_v1")),
    ("test_marketplace_integration", "POST", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/test", None, None, lambda m: m.test_marketplace_integration("int_6Qp1dW2kRm8NsT4vYc0Hb")),
    ("get_marketplace_integration_tools", "GET", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/tools", None, None, lambda m: m.get_marketplace_integration_tools("int_6Qp1dW2kRm8NsT4vYc0Hb")),
    ("get_marketplace_integration_access", "GET", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/access", None, None, lambda m: m.get_marketplace_integration_access("int_6Qp1dW2kRm8NsT4vYc0Hb")),
    ("set_marketplace_integration_role_access", "PUT", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/access/roles", None, {'roleId': 'acc_6Qp1dW2kRm8NsT4vYc0Hb_nr_3kLm9QwErTyU', 'package': 'ReadOnly', 'manage': False}, lambda m: m.set_marketplace_integration_role_access("int_6Qp1dW2kRm8NsT4vYc0Hb", roleId='acc_6Qp1dW2kRm8NsT4vYc0Hb_nr_3kLm9QwErTyU', package='ReadOnly', manage=False)),
    ("save_marketplace_integration_custom_access", "POST", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/access/roles/custom", None, {'roleId': 'acc_6Qp1dW2kRm8NsT4vYc0Hb_nr_3kLm9QwErTyU', 'basePackage': 'ReadOnly', 'tools': ['create_issue'], 'functions': ['func_4hT2b9QkLm3XcT1yRfGh7a'], 'manage': False, 'newPolicyForThisRoleOnly': True}, lambda m: m.save_marketplace_integration_custom_access("int_6Qp1dW2kRm8NsT4vYc0Hb", roleId='acc_6Qp1dW2kRm8NsT4vYc0Hb_nr_3kLm9QwErTyU', basePackage='ReadOnly', tools=['create_issue'], functions=['func_4hT2b9QkLm3XcT1yRfGh7a'], manage=False, newPolicyForThisRoleOnly=True)),
    ("start_marketplace_integration_sign_in", "POST", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/oauth/start", None, None, lambda m: m.start_marketplace_integration_sign_in("int_6Qp1dW2kRm8NsT4vYc0Hb")),
    ("sign_out_marketplace_integration", "POST", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/oauth/sign-out", None, None, lambda m: m.sign_out_marketplace_integration("int_6Qp1dW2kRm8NsT4vYc0Hb")),
    ("replace_marketplace_integration_secrets", "PUT", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/secrets", None, {'secrets': {'botToken': 'xoxb-new'}}, lambda m: m.replace_marketplace_integration_secrets("int_6Qp1dW2kRm8NsT4vYc0Hb", secrets={'botToken': 'xoxb-new'})),
    ("reveal_marketplace_integration_secrets", "POST", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/secrets/reveal", None, None, lambda m: m.reveal_marketplace_integration_secrets("int_6Qp1dW2kRm8NsT4vYc0Hb")),
    ("set_marketplace_integration_token_mappings", "PUT", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/token-mappings", None, {'tokenMappings': [{'key': 'channel', 'value': '#orders', 'resolver': 'Custom'}]}, lambda m: m.set_marketplace_integration_token_mappings("int_6Qp1dW2kRm8NsT4vYc0Hb", tokenMappings=[{'key': 'channel', 'value': '#orders', 'resolver': 'Custom'}])),
    ("get_marketplace_function_catalog", "GET", "/v3/code/marketplace/integrations/int_6Qp1dW2kRm8NsT4vYc0Hb/catalog", None, None, lambda m: m.get_marketplace_function_catalog("int_6Qp1dW2kRm8NsT4vYc0Hb")),
    ("get_marketplace_function_runs", "GET", "/v3/code/marketplace/functions/runs", {'triggerId': ['trg_1p4R3gTobGZpD6fXvHT4rd'], 'limit': ['5']}, None, lambda m: m.get_marketplace_function_runs(triggerId='trg_1p4R3gTobGZpD6fXvHT4rd', limit=5)),
]


@pytest.mark.parametrize(("name", "verb", "path", "query", "body", "call"), MARKETPLACE_CASES, ids=[c[0] for c in MARKETPLACE_CASES])
def test_marketplace_request_shape(
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


def test_async_marketplace_endpoints_hit_the_same_routes() -> None:
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
            for _, _, _, _, _, call in MARKETPLACE_CASES:
                await call(client.hub.code)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == len(MARKETPLACE_CASES)
    for request, (name, verb, path, query, body, _) in zip(seen, MARKETPLACE_CASES, strict=True):
        _assert_function_request(name, request.method, str(request.url), request.content.decode("utf-8"), verb, path, query, body)


def test_marketplace_surface_size() -> None:
    """29 marketplace routes in the gateway (Code.Marketplace.md §14; 24 = MCP tool catalog, 25–27 = connection access, 28 = OAuth sign-in start, 30 = OAuth sign-out; 29, the callback, is not in the metadata). A new one changes this count."""
    assert len(MARKETPLACE_CASES) == 29
    assert len({case[0] for case in MARKETPLACE_CASES}) == 29
    client, _ = make_client()
    for name, *_ in MARKETPLACE_CASES:
        assert callable(getattr(client.hub.code, name)), name


RUNS_PATH = "/v3/code/marketplace/functions/runs"
RUNS_BY_FUNCTION_QUERY = {"functionId": ["func_1p4R3gTobGZpD6fXvHT4rd"], "limit": ["50"]}


def test_marketplace_function_runs_by_function_id() -> None:
    """Exactly one of functionId / triggerId / taskId (gateway item gw-runs): a function's own runs."""
    client, transport = make_client()
    client.hub.code.get_marketplace_function_runs(functionId="func_1p4R3gTobGZpD6fXvHT4rd", limit=50)
    assert transport.last_request is not None
    _assert_function_request(
        "get_marketplace_function_runs(functionId)",
        transport.last_request["method"],
        transport.last_request["url"],
        transport.last_request["body"],
        "GET",
        RUNS_PATH,
        RUNS_BY_FUNCTION_QUERY,
        None,
    )


def test_async_marketplace_function_runs_by_function_id() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"runs": [{"functionId": "func_1p4R3gTobGZpD6fXvHT4rd", "status": "ok", "hasDetails": True}]})

    async def run() -> Any:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        try:
            return await client.hub.code.get_marketplace_function_runs(functionId="func_1p4R3gTobGZpD6fXvHT4rd", limit=50)
        finally:
            await client.aclose()

    result = asyncio.run(run())

    assert len(seen) == 1
    _assert_function_request(
        "async get_marketplace_function_runs(functionId)",
        seen[0].method,
        str(seen[0].url),
        seen[0].content.decode("utf-8"),
        "GET",
        RUNS_PATH,
        RUNS_BY_FUNCTION_QUERY,
        None,
    )
    assert result == {"runs": [{"functionId": "func_1p4R3gTobGZpD6fXvHT4rd", "status": "ok", "hasDetails": True}]}
