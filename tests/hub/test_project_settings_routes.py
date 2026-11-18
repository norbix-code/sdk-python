from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

"""Every Hub route of matrix section 21 (Project settings), one case each:
general info, brand, access, languages, environments (with the three
``hub.environments`` routes the Cloud Environments tab lists, creates and
deletes through), admin portal, legal + expose switches, AI, termination,
regions and billing. The public API-host routes are in
``tests/api/test_public.py``. Written in the settings coverage campaign
(2026-11-18); the older tables of these routes assert the verb and the path
but not the host, the query or the body.

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

FILE_REF = {"resource": {"id": "fl_1"}, "integrationId": "int_files", "provider": "Local", "path": "brand/logo.png", "isPublic": True}
NEW_PROJECT = {
    "projectName": "Shop",
    "primaryRegion": "nb-eu-germany",
    "additionalRegions": ["nb-us-east"],
    "description": "Orders",
    "integration": NEW_ENV["integration"],
}
ASSISTANT = {"name": "Support", "systemPrompt": "Be brief.", "toolsets": ["own:records"], "memoryEnabled": False, "isDefault": True}
LEGAL = {"termsMarkdown": "# Terms", "privacyMarkdown": "# Privacy"}

# (name, verb, path, query, body, call) — call takes client.hub
CASES: list[tuple[str, str, str, dict[str, list[str]] | None, dict[str, Any] | None, Callable[[Any], Any]]] = [
    # General info.
    ("get_projects", "GET", "/v2/account/projects", None, None, lambda h: h.account.get_projects()),
    ("create_project", "POST", "/v2/account/projects", None, NEW_PROJECT,
     lambda h: h.account.create_project(
         primary_region="nb-eu-germany", additional_regions=["nb-us-east"],
         projectName="Shop", description="Orders", integration=NEW_ENV["integration"])),
    ("get_project", "GET", P, None, None, lambda h: h.account.get_project(PR)),
    ("get_project_tokens", "GET", f"{P}/tokens", {"recipientId": ["usr_1"]}, None,
     lambda h: h.account.get_project_tokens(PR, recipientId="usr_1")),
    ("get_project_health", "GET", f"{P}/health", {"refresh": ["true"], "periodDays": ["7"]}, None,
     lambda h: h.account.get_project_health(PR, refresh=True, periodDays=7)),
    ("wait_for_project_active", "GET", f"{P}/wait-active", {"timeoutSeconds": ["60"]}, None,
     lambda h: h.account.wait_for_project_active(PR, timeoutSeconds=60)),
    # Brand.
    ("update_project_name", "PATCH", f"{P}/settings/name", None, {"name": "Shop"},
     lambda h: h.account.update_project_name(PR, name="Shop")),
    ("update_project_description", "PATCH", f"{P}/settings/description", None, {"description": "Orders"},
     lambda h: h.account.update_project_description(PR, description="Orders")),
    ("update_project_url", "PATCH", f"{P}/settings/url", None, {"url": "https://shop.example.com"},
     lambda h: h.account.update_project_url(PR, url="https://shop.example.com")),
    ("update_project_icon", "PATCH", f"{P}/settings/icon", None, {"fileResource": FILE_REF},
     lambda h: h.account.update_project_icon(PR, fileResource=FILE_REF)),
    ("update_project_logo", "PATCH", f"{P}/settings/logo", None, {"fileResource": FILE_REF},
     lambda h: h.account.update_project_logo(PR, fileResource=FILE_REF)),
    ("update_project_main_color", "PATCH", f"{P}/settings/main-color", None, {"color": "#1F6FEB"},
     lambda h: h.account.update_project_main_color(PR, color="#1F6FEB")),
    ("update_project_accent_color", "PATCH", f"{P}/settings/accent-color", None, {"color": "#F78166"},
     lambda h: h.account.update_project_accent_color(PR, color="#F78166")),
    # Access (CORS) and regions.
    ("update_project_allowed_origins", "PATCH", f"{P}/settings/origins", None,
     {"origins": ["https://app.example.com"], "removeAdminPortalOrigin": True},
     lambda h: h.account.update_project_allowed_origins(PR, origins=["https://app.example.com"], removeAdminPortalOrigin=True)),
    ("update_project_regions", "PATCH", f"{P}/settings/regions", None, {"additionalRegions": ["nb-us-east"]},
     lambda h: h.account.update_project_regions(PR, additionalRegions=["nb-us-east"])),
    # Languages.
    ("update_project_languages", "PATCH", f"{P}/settings/languages", None, {"languages": ["en", "lt"]},
     lambda h: h.account.update_project_languages(PR, languages=["en", "lt"])),
    ("update_project_default_language", "PATCH", f"{P}/settings/default-language", None, {"defaultLanguage": "lt"},
     lambda h: h.account.update_project_default_language(PR, defaultLanguage="lt")),
    ("check_project_languages", "POST", f"{P}/settings/languages/check", None, {"languages": ["en", "de"], "defaultLanguage": "en"},
     lambda h: h.account.check_project_languages(PR, languages=["en", "de"], defaultLanguage="en")),
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
    # Admin portal.
    ("set_admin_portal_enabled", "PUT", f"{P}/admin-portal/enabled", None, {"enabled": True},
     lambda h: h.account.set_admin_portal_enabled(PR, enabled=True)),
    ("get_admin_portal_structure", "GET", f"{P}/admin-portal/structure", None, None,
     lambda h: h.account.get_admin_portal_structure(PR)),
    ("assign_admin_portal_service_user", "PUT", f"{P}/settings/admin-portal/service-user", None, {"serviceUserId": "su_1"},
     lambda h: h.account.assign_admin_portal_service_user(PR, serviceUserId="su_1")),
    ("update_project_admin_url", "PATCH", f"{P}/settings/admin-url", None, {"url": "https://admin.example.com"},
     lambda h: h.account.update_project_admin_url(PR, url="https://admin.example.com")),
    # Legal + expose switches.
    ("update_project_legal_documents", "PATCH", f"{P}/settings/legal", None, LEGAL,
     lambda h: h.account.update_project_legal_documents(PR, **LEGAL)),
    ("update_project_expose_legal", "PATCH", f"{P}/settings/legal/expose", None, {"exposed": True},
     lambda h: h.account.update_project_expose_legal(PR, exposed=True)),
    ("update_project_expose_auth", "PATCH", f"{P}/settings/auth/expose", None, {"exposed": True},
     lambda h: h.account.update_project_expose_auth(PR, exposed=True)),
    ("update_project_expose_brand", "PATCH", f"{P}/settings/brand/expose", None, {"exposed": False},
     lambda h: h.account.update_project_expose_brand(PR, exposed=False)),
    # AI settings tab.
    ("get_project_ai_settings", "GET", f"{P}/ai/settings", None, None, lambda h: h.account.get_project_ai_settings(PR)),
    ("update_project_ai_settings", "PUT", f"{P}/ai/settings", None,
     {"enabled": True, "defaultLlmIntegrationId": "int_llm", "defaultModel": "gpt-4o-mini"},
     lambda h: h.account.update_project_ai_settings(PR, enabled=True, defaultLlmIntegrationId="int_llm", defaultModel="gpt-4o-mini")),
    ("create_project_ai_assistant", "POST", f"{P}/ai/assistants", None, ASSISTANT,
     lambda h: h.account.create_project_ai_assistant(PR, **ASSISTANT)),
    ("update_project_ai_assistant", "PUT", f"{P}/ai/assistants/ast_1", None, ASSISTANT,
     lambda h: h.account.update_project_ai_assistant(PR, "ast_1", **ASSISTANT)),
    ("delete_project_ai_assistant", "DELETE", f"{P}/ai/assistants/ast_1", None, None,
     lambda h: h.account.delete_project_ai_assistant(PR, "ast_1")),
    ("get_project_ai_usage", "GET", f"{P}/ai/usage", {"top": ["5"]}, None, lambda h: h.account.get_project_ai_usage(PR, top=5)),
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
    # Termination.
    ("disable_project", "PATCH", f"{P}/disable", None, None, lambda h: h.account.disable_project(PR)),
    ("enable_project", "PATCH", f"{P}/enable", None, None, lambda h: h.account.enable_project(PR)),
    ("delete_project", "DELETE", P, None, None, lambda h: h.account.delete_project(PR)),
    # Billing.
    ("get_stripe_billing_portal_url", "POST", "/v2/account/stripe/get-portal-url", None,
     {"subscriptionType": "ManagedService", "returnUrl": "https://cloud.example.com/billing"},
     lambda h: h.account.get_stripe_billing_portal_url(subscriptionType="ManagedService", returnUrl="https://cloud.example.com/billing")),
    ("get_managed_service_bundles", "GET", "/v2/account/stripe/bundles", None, None,
     lambda h: h.account.get_managed_service_bundles()),
    ("change_managed_service_bundle", "POST", "/v2/account/stripe/change-bundle", None, {"bundle": "Growth", "billingPeriod": "Annual"},
     lambda h: h.account.change_managed_service_bundle(bundle="Growth", billingPeriod="Annual")),
    ("create_stripe_checkout_session", "POST", "/v2/account/stripe/create-checkout-session", None,
     {"subscriptionType": "ManagedService", "bundle": "Starter", "billingPeriod": "Monthly"},
     lambda h: h.account.create_stripe_checkout_session(subscriptionType="ManagedService", bundle="Starter", billingPeriod="Monthly")),
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
    # General info 6 + brand 7 + access 1 + regions 1 + languages 3 + environments 9 + admin portal 4
    # + legal / expose 4 + AI 12 + termination 3 + billing 8.
    assert len(CASES) == 6 + 7 + 1 + 1 + 3 + 9 + 4 + 4 + 12 + 3 + 8
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
