from __future__ import annotations

import asyncio
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

"""The taxonomy routes the API serves for the taxonomies list and the terms
list (matrix section 04), called through ``client.api.database`` (sync and
async). Each case asserts the host (api, not hub: the trees exist on both),
the verb, the exact path and the query. Source of truth: the gateway
``[Route]`` attributes (Api.Database/Taxonomies). Every call goes to a mock
transport, so nothing leaves the process.
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

# name, verb, path, query (None: no query), call
Case = tuple[str, str, str, dict[str, list[str]] | None, Callable[[Any], Any]]

CASES: list[Case] = [
    # Taxonomies list.
    ("find_taxonomy_tree", "GET", "/v2/database/taxonomies/tree", {"includeTerms": ["true"]},
     lambda m: m.find_taxonomy_tree(includeTerms=True)),
    # Terms list.
    ("find_terms", "GET", "/v2/database/taxonomies/countries/terms", {"pageSize": ["10"], "filter": ['{"name":"Lithuania"}']},
     lambda m: m.find_terms("countries", pageSize=10, filter='{"name":"Lithuania"}')),
    ("find_term_tree", "GET", "/v2/database/taxonomies/countries/terms/tree", {"depth": ["2"]},
     lambda m: m.find_term_tree("countries", depth=2)),
    ("find_merged_term_tree", "GET", "/v2/database/taxonomies/countries/merged-tree", {"databaseIntegrationId": ["int_1"]},
     lambda m: m.find_merged_term_tree("countries", databaseIntegrationId="int_1")),
    ("find_terms_children", "GET", "/v2/database/taxonomies/countries/terms/t_1/children", {"pageSize": ["10"]},
     lambda m: m.find_terms_children("countries", "t_1", pageSize=10)),
]

IDS = [c[0] for c in CASES]


def _capture(seen: list[httpx.Request]) -> Callable[[httpx.Request], httpx.Response]:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    return handler


def _assert_request(request: httpx.Request, verb: str, path: str, query: dict[str, list[str]] | None) -> None:
    assert f"{request.url.scheme}://{request.url.host}" == API
    assert request.method == verb
    assert request.url.path == path
    assert parse_qs(request.url.query.decode()) == (query or {})
    assert request.content == b""
    assert request.headers["authorization"] == "Bearer key_1"
    assert request.headers["norbix-project-id"] == "test-project"


def test_api_database_taxonomy_route_count() -> None:
    # Taxonomies list 1 + terms list 4.
    assert len(CASES) == 1 + 4


@pytest.mark.parametrize("name, verb, path, query, call", CASES, ids=IDS)
def test_api_database_taxonomy_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, call: Callable[[Any], Any]
) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))))

    call(client.api.database)

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query)


@pytest.mark.parametrize("name, verb, path, query, call", CASES, ids=IDS)
def test_async_api_database_taxonomy_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, call: Callable[[Any], Any]
) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(**CLIENT_ARGS, http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))))
        try:
            await call(client.api.database)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query)
