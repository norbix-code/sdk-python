from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

"""The Project settings routes of matrix section 21 that had no Python method
or no exact-route test before the settings coverage campaign (2026-11-18):
project health and wait-active, the environment ladder (with the three
``hub.environments`` routes the Cloud Environments tab lists, creates and
deletes through), the AI plans and knowledge, the account usage billing and
the bundle discount / extra regions.

Called through ``client.hub.account`` / ``client.hub.environments`` (sync and
async). Each case asserts the host (hub), the verb, the exact path, the query
string and the JSON body, plus the key and project headers. Field names are
the gateway's (Hub.Account ``Project/*.cs``, ``Project/Settings/Ai/*.cs``,
``Account/Stripe/*.cs``). Every call goes to a mock transport, so nothing
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

PR = "pr_1"
P = f"/v2/account/projects/{PR}"
E = "/v2/account/projects/environments"

PROMOTE = {
    "sourceEnv": "TEST",
    "targetEnv": "PROD",
    "dryRun": True,
    "integrationChoices": [{"id": "int_db", "action": "map", "mapToId": "int_prod_db"}],
}
ROLLBACK = {"targetEnv": "PROD", "fromVersion": 279, "dryRun": False, "confirmRecordLoss": True}
PLANS = {"plans": [{"id": "aip_1", "name": "Free", "quotaUnit": "Credits", "monthlyQuota": 100}]}
ASSIGNMENTS = {"roles": [{"roleId": "rl_pro", "planId": "aip_2"}], "defaultPlanId": "aip_1"}
NEW_ENV = {
    "environmentName": "STAGING",
    "integration": {
        "provider": "MongoDbConnectionString",
        "integrationName": "Staging database",
        "connectionString": "mongodb://db/staging",
    },
}

# (name, verb, path, query, body, call) — call takes client.hub
CASES: list[tuple[str, str, str, dict[str, list[str]] | None, dict[str, Any] | None, Callable[[Any], Any]]] = [
    # General info.
    ("get_project_health", "GET", f"{P}/health", {"refresh": ["true"], "periodDays": ["7"]}, None,
     lambda h: h.account.get_project_health(PR, refresh=True, periodDays=7)),
    ("wait_for_project_active", "GET", f"{P}/wait-active", {"timeoutSeconds": ["60"]}, None,
     lambda h: h.account.wait_for_project_active(PR, timeoutSeconds=60)),
    # Environments.
    ("environments.list", "GET", E, None, None, lambda h: h.environments.list()),
    ("environments.create", "POST", E, None, NEW_ENV,
     lambda h: h.environments.create(environment_name="STAGING", integration=NEW_ENV["integration"])),
    ("environments.delete", "DELETE", f"{E}/STAGING", None, None,
     lambda h: h.environments.delete(environment_name="STAGING")),
    ("set_environment_rank", "PATCH", f"{E}/STAGING/rank", None, {"rank": 2},
     lambda h: h.account.set_environment_rank("STAGING", rank=2)),
    ("promote_environment", "POST", f"{E}/promote", None, PROMOTE,
     lambda h: h.account.promote_environment(**PROMOTE)),
    ("rollback_promotion", "POST", f"{E}/promote/rollback", None, ROLLBACK,
     lambda h: h.account.rollback_promotion(**ROLLBACK)),
    ("repair_environment_built_ins", "POST", f"{E}/built-ins/repair", None, {"environmentName": "TEST", "dryRun": True},
     lambda h: h.account.repair_environment_built_ins(environmentName="TEST", dryRun=True)),
    ("get_environment_admin_url", "GET", f"{E}/TEST/admin-url", None, None,
     lambda h: h.account.get_environment_admin_url("TEST")),
    ("update_environment_admin_url", "PATCH", f"{E}/TEST/admin-url", None, {"url": "https://test-admin.example.com"},
     lambda h: h.account.update_environment_admin_url("TEST", url="https://test-admin.example.com")),
    # AI settings tab.
    ("update_project_ai_knowledge", "PUT", f"{P}/ai/knowledge", None, {"embedFiles": True},
     lambda h: h.account.update_project_ai_knowledge(PR, embedFiles=True)),
    ("get_project_ai_plans", "GET", f"{P}/ai/plans", None, None, lambda h: h.account.get_project_ai_plans(PR)),
    ("update_project_ai_plans", "PUT", f"{P}/ai/plans", None, PLANS,
     lambda h: h.account.update_project_ai_plans(PR, **PLANS)),
    ("update_project_ai_plan_assignments", "PUT", f"{P}/ai/plans/assignments", None, ASSIGNMENTS,
     lambda h: h.account.update_project_ai_plan_assignments(PR, **ASSIGNMENTS)),
    ("get_project_ai_user_plans", "GET", f"{P}/ai/plans/users", None, None,
     lambda h: h.account.get_project_ai_user_plans(PR)),
    ("create_ai_credit_pack_checkout", "POST", f"{P}/ai/credits/checkout", None,
     {"pack": "pack-10", "returnUrl": "/projects/shop/settings?tab=AI"},
     lambda h: h.account.create_ai_credit_pack_checkout(PR, pack="pack-10", returnUrl="/projects/shop/settings?tab=AI")),
    # Billing.
    ("get_account_usage_billing", "GET", "/v2/account/usage-billing", None, None,
     lambda h: h.account.get_account_usage_billing()),
    ("check_bundle_discount", "POST", "/v2/account/stripe/discount/check", None,
     {"code": "LAUNCH20", "bundle": "Growth", "billingPeriod": "Annual"},
     lambda h: h.account.check_bundle_discount(code="LAUNCH20", bundle="Growth", billingPeriod="Annual")),
    ("apply_bundle_discount", "POST", "/v2/account/stripe/discount", None, {"code": "LAUNCH20"},
     lambda h: h.account.apply_bundle_discount(code="LAUNCH20")),
    ("set_extra_regions", "POST", "/v2/account/stripe/extra-regions", None, {"extraRegions": 1},
     lambda h: h.account.set_extra_regions(extraRegions=1)),
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


def test_project_settings_route_count() -> None:
    # General info 2 + environments 9 + AI 6 + billing 4.
    assert len(CASES) == 2 + 9 + 6 + 4
    assert len(set(IDS)) == len(IDS)


@pytest.mark.parametrize("name, verb, path, query, body, call", CASES, ids=IDS)
def test_project_settings_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))))

    call(client.hub)

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query, body)


@pytest.mark.parametrize("name, verb, path, query, body, call", CASES, ids=IDS)
def test_async_project_settings_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(**CLIENT_ARGS, http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))))
        try:
            await call(client.hub)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query, body)
