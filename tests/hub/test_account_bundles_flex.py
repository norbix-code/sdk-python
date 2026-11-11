"""Managed Service bundles and the account's Norbix-managed Atlas clusters.

The gateway takes the account from the signed-in session for all four routes,
so every test runs on a client WITHOUT ``account_id``. Each one asserts the
verb, the fully-resolved path and where the parameters go. Sync and async
clients are both covered. Nothing leaves the process.
"""
from __future__ import annotations

import asyncio
import json
from typing import Any
from urllib.parse import urlparse

import httpx

from norbix_python import AsyncNorbix, Norbix

BUNDLES = {
    "bundles": [
        {
            "bundle": "Starter",
            "projectCap": 3,
            "monthly": {"amount": 4900, "currency": "usd"},
            "annual": {"amount": 49000, "currency": "usd"},
        }
    ]
}

CLUSTERS = {
    "clusters": [
        {
            "id": "fc_1",
            "displayName": "Main",
            "tierCode": "FLEX",
            "status": "Active",
            "databases": [{"projectId": "proj_1", "env": "PROD", "integrationId": "int_1"}],
            "usage": {"databaseCount": 1, "storageBytes": 2048},
            "nearLimits": [],
        }
    ],
    "canCreateNew": False,
    "cannotCreateReason": "ClusterLimitReached",
}


def _handler(seen: list[httpx.Request], answer: Any) -> Any:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json=answer if answer is not None else {})

    return handler


def _sync_client(seen: list[httpx.Request], answer: Any = None) -> Norbix:
    return Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=httpx.MockTransport(_handler(seen, answer))),
    )


def _async_client(seen: list[httpx.Request], answer: Any = None) -> AsyncNorbix:
    return AsyncNorbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(_handler(seen, answer))),
    )


def _route(request: httpx.Request) -> tuple[str, str, str]:
    url = urlparse(str(request.url))
    return request.method, url.path, url.query


def test_get_managed_service_bundles_reads_the_bundles_and_prices() -> None:
    seen: list[httpx.Request] = []
    answer = _sync_client(seen, BUNDLES).hub.account.get_managed_service_bundles()

    assert [_route(r) for r in seen] == [("GET", "/v3/account/stripe/bundles", "")]
    assert "norbix-account-id" not in seen[0].headers
    assert answer["bundles"][0]["bundle"] == "Starter"
    assert answer["bundles"][0]["projectCap"] == 3
    assert answer["bundles"][0]["monthly"] == {"amount": 4900, "currency": "usd"}


def test_change_managed_service_bundle_sends_bundle_and_period_in_a_post_body() -> None:
    seen: list[httpx.Request] = []
    _sync_client(seen).hub.account.change_managed_service_bundle(bundle="Growth", billingPeriod="Annual")

    assert [_route(r) for r in seen] == [("POST", "/v3/account/stripe/change-bundle", "")]
    assert "norbix-account-id" not in seen[0].headers
    assert json.loads(seen[0].content) == {"bundle": "Growth", "billingPeriod": "Annual"}


def test_get_flex_clusters_reads_clusters_databases_and_usage() -> None:
    seen: list[httpx.Request] = []
    answer = _sync_client(seen, CLUSTERS).hub.account.get_flex_clusters()

    assert [_route(r) for r in seen] == [("GET", "/v3/account/flex-clusters", "")]
    assert "norbix-account-id" not in seen[0].headers
    assert answer["canCreateNew"] is False
    assert answer["cannotCreateReason"] == "ClusterLimitReached"
    assert answer["clusters"][0]["databases"][0]["integrationId"] == "int_1"
    assert answer["clusters"][0]["usage"]["storageBytes"] == 2048


def test_upgrade_flex_cluster_puts_the_id_in_the_path_and_the_tier_in_the_body() -> None:
    seen: list[httpx.Request] = []
    _sync_client(seen).hub.account.upgrade_flex_cluster("fc_1", tierCode="M10")

    assert [_route(r) for r in seen] == [("POST", "/v3/account/flex-clusters/fc_1/upgrade", "")]
    assert "norbix-account-id" not in seen[0].headers
    assert json.loads(seen[0].content) == {"tierCode": "M10"}


def test_create_stripe_checkout_session_sends_bundle_and_billing_period() -> None:
    seen: list[httpx.Request] = []
    _sync_client(seen).hub.account.create_stripe_checkout_session(
        subscriptionType="ManagedService", bundle="Starter", billingPeriod="Monthly"
    )

    assert [_route(r) for r in seen] == [("POST", "/v3/account/stripe/create-checkout-session", "")]
    assert json.loads(seen[0].content) == {
        "subscriptionType": "ManagedService",
        "bundle": "Starter",
        "billingPeriod": "Monthly",
    }


def test_async_client_has_the_same_four_methods() -> None:
    seen: list[httpx.Request] = []

    async def run() -> Any:
        client = _async_client(seen, CLUSTERS)
        try:
            await client.hub.account.get_managed_service_bundles()
            await client.hub.account.change_managed_service_bundle(bundle="Scale", billingPeriod="Monthly")
            clusters = await client.hub.account.get_flex_clusters()
            await client.hub.account.upgrade_flex_cluster("fc_1", tierCode="M10")
            return clusters
        finally:
            await client.aclose()

    clusters = asyncio.run(run())

    assert [_route(r) for r in seen] == [
        ("GET", "/v3/account/stripe/bundles", ""),
        ("POST", "/v3/account/stripe/change-bundle", ""),
        ("GET", "/v3/account/flex-clusters", ""),
        ("POST", "/v3/account/flex-clusters/fc_1/upgrade", ""),
    ]
    assert json.loads(seen[1].content) == {"bundle": "Scale", "billingPeriod": "Monthly"}
    assert json.loads(seen[3].content) == {"tierCode": "M10"}
    assert clusters["clusters"][0]["id"] == "fc_1"
