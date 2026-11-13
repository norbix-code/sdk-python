from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

"""Every Membership route the Hub serves for the dashboard screens.

Users list, user edit, roles, policies, the five settings tabs and the
service-user API keys, called through ``client.hub.membership`` (sync and
async). Each case asserts the host (hub, not api: the contact routes exist on
both), the verb, the exact path, the query (reads and deletes) and the JSON
body (saves). Source of truth: the gateway ``[Route]`` attributes
(Hub.Membership, Hub.Contacts); field names from the generated request types.
Every call goes to a mock transport, so nothing leaves the process.
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

CT = "ct_1"
AUTH = "usr_1"
ROLE = "role_1"
POLICY = "pol_1"

CREATE_CONTACT = {"primaryEmail": "ana@example.test", "displayName": "Ana", "firstName": "Ana", "lastName": "Berg", "tags": ["vip"]}
MERGE = {"survivorId": CT, "mergedIds": ["ct_2", "ct_3"]}
DRY_RUN = {"dryRun": True}
IMPORT_USERS = {"dryRun": False, "ignoreDefaultRoles": True, "users": [{"email": "ana@example.test"}]}
UPDATE_CONTACT = {"displayName": "Ana B.", "company": "Norbix", "city": "Vilnius"}
IDENTITY = {"authId": AUTH}
AI_PLAN = {"planId": "plan_pro"}
ROLE_NEW = {"roleName": "Editor", "description": "Edits records", "policies": ["pol_1"]}
ROLE_UPDATE = {"id": ROLE, "roleName": "Editor", "policies": ["pol_1", "pol_2"]}
POLICY_NEW = {"policyName": "Read orders", "description": "Orders only", "policyDocumentJson": '{"statements":[]}'}
POLICY_UPDATE = {"id": POLICY, "policyName": "Read orders", "policyDocumentJson": '{"statements":[]}'}
AUTHN = {"logoutUrl": "https://app.example.test/bye", "allowUsernames": True}
AUTHZ = {"allowAnyoneToSignUp": False, "inviteOnly": True, "defaultRoles": ["User"]}
COMPLEXITY = {"minLength": 12, "minNumbers": 1, "allowedSpecial": "!@#"}
PASSKEY = {"enabled": True, "codeTtlMinutes": 10, "rpId": "app.example.test"}
API_KEY = {"name": "ci", "scopes": ["database:read"], "expiresInDays": 30, "notes": "build server"}

# name, verb, path, query (None: no query), body (None: no body), call
Case = tuple[str, str, str, dict[str, list[str]] | None, dict[str, Any] | None, Callable[[Any], Any]]

CASES: list[Case] = [
    # Users list.
    ("get_all_contacts", "GET", "/v2/membership/users", {"search": ["ana"], "pageSize": ["25"]}, None,
     lambda m: m.get_all_contacts(search="ana", pageSize=25)),
    ("create_contact", "POST", "/v2/membership/users", None, CREATE_CONTACT, lambda m: m.create_contact(**CREATE_CONTACT)),
    ("merge_contacts", "POST", "/v2/membership/users/merge", None, MERGE, lambda m: m.merge_contacts(**MERGE)),
    ("delete_contact", "DELETE", f"/v2/membership/users/{CT}", None, None, lambda m: m.delete_contact(CT)),
    ("import_users", "POST", "/v2/membership/users/import", None, IMPORT_USERS, lambda m: m.import_users(**IMPORT_USERS)),
    ("repair_login_project_ids", "POST", "/v2/membership/users/repair-logins", None, DRY_RUN,
     lambda m: m.repair_login_project_ids(**DRY_RUN)),
    ("repair_contact_roles", "POST", "/v2/membership/users/repair-roles", None, DRY_RUN,
     lambda m: m.repair_contact_roles(**DRY_RUN)),
    # User edit / detail.
    ("get_contact", "GET", f"/v2/membership/users/{CT}", None, None, lambda m: m.get_contact(CT)),
    ("update_contact", "PATCH", f"/v2/membership/users/{CT}", None, UPDATE_CONTACT,
     lambda m: m.update_contact(CT, **UPDATE_CONTACT)),
    ("add_contact_identity", "POST", f"/v2/membership/users/{CT}/identities", None, IDENTITY,
     lambda m: m.add_contact_identity(CT, **IDENTITY)),
    ("remove_contact_identity", "DELETE", f"/v2/membership/users/{CT}/identities/{AUTH}", None, None,
     lambda m: m.remove_contact_identity(CT, AUTH)),
    ("promote_contact_identity", "POST", f"/v2/membership/users/{CT}/identities/{AUTH}/promote", None, None,
     lambda m: m.promote_contact_identity(CT, AUTH)),
    ("clear_contact_bounce", "POST", f"/v2/membership/users/{CT}/marketing-state/Email/clear-bounce", None, None,
     lambda m: m.clear_contact_bounce(CT, "Email")),
    ("set_user_ai_plan", "PUT", f"/v2/membership/users/{AUTH}/ai-plan", None, AI_PLAN,
     lambda m: m.set_user_ai_plan(AUTH, **AI_PLAN)),
    # Roles. The delete id goes on the query: the route has no {Id} (same as the .NET snapshot).
    ("get_roles", "GET", "/v2/membership/roles", None, None, lambda m: m.get_roles()),
    ("get_role", "GET", f"/v2/membership/roles/{ROLE}", None, None, lambda m: m.get_role(ROLE)),
    ("create_role", "POST", "/v2/membership/roles", None, ROLE_NEW, lambda m: m.create_role(**ROLE_NEW)),
    ("update_role_policies", "PATCH", "/v2/membership/roles", None, ROLE_UPDATE, lambda m: m.update_role_policies(**ROLE_UPDATE)),
    ("delete_role", "DELETE", "/v2/membership/roles", {"id": [ROLE]}, None, lambda m: m.delete_role(id=ROLE)),
    # Policies.
    ("get_policies", "GET", "/v2/membership/policies", None, None, lambda m: m.get_policies()),
    ("get_policy", "GET", f"/v2/membership/policies/{POLICY}", None, None, lambda m: m.get_policy(POLICY)),
    ("create_policy", "POST", "/v2/membership/policies", None, POLICY_NEW, lambda m: m.create_policy(**POLICY_NEW)),
    ("update_policy", "PUT", "/v2/membership/policies", None, POLICY_UPDATE, lambda m: m.update_policy(**POLICY_UPDATE)),
    ("delete_policy", "DELETE", "/v2/membership/policies", {"id": [POLICY]}, None, lambda m: m.delete_policy(id=POLICY)),
    # Settings — module switch, authentication, authorization, password complexity, passkeys.
    ("enable_membership", "PUT", "/v2/membership/enable", None, None, lambda m: m.enable_membership()),
    ("get_authentication_settings", "GET", "/v2/membership/authentication", None, None,
     lambda m: m.get_authentication_settings()),
    ("update_authentication_settings", "PUT", "/v2/membership/authentication", None, AUTHN,
     lambda m: m.update_authentication_settings(**AUTHN)),
    ("get_authorization_settings", "GET", "/v2/membership/authorization", None, None,
     lambda m: m.get_authorization_settings()),
    ("update_authorization_settings", "PUT", "/v2/membership/authorization", None, AUTHZ,
     lambda m: m.update_authorization_settings(**AUTHZ)),
    ("update_password_complexity", "PUT", "/v2/membership/authorization/password-complexity", None, COMPLEXITY,
     lambda m: m.update_password_complexity(**COMPLEXITY)),
    ("get_passkey_settings", "GET", "/v2/membership/passkey/settings", None, None, lambda m: m.get_passkey_settings()),
    ("save_passkey_settings", "POST", "/v2/membership/passkey/settings", None, PASSKEY,
     lambda m: m.save_passkey_settings(**PASSKEY)),
    # Service-user API keys.
    ("list_service_user_api_keys", "GET", f"/v2/membership/users/{AUTH}/api-keys", None, None,
     lambda m: m.list_service_user_api_keys(AUTH)),
    ("issue_service_user_api_key", "POST", f"/v2/membership/users/{AUTH}/api-keys", None, API_KEY,
     lambda m: m.issue_service_user_api_key(AUTH, **API_KEY)),
    ("delete_service_user_api_key", "DELETE", f"/v2/membership/users/{AUTH}/api-keys/7", None, None,
     lambda m: m.delete_service_user_api_key(AUTH, "7")),
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


def test_hub_membership_route_count() -> None:
    # Users list 7 + user edit 7 + roles 5 + policies 5 + settings 8 + API keys 3.
    # (Membership cannot be disabled, so settings has no disable route.)
    assert len(CASES) == 7 + 7 + 5 + 5 + 8 + 3


@pytest.mark.parametrize("name, verb, path, query, body, call", CASES, ids=IDS)
def test_hub_membership_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))))

    call(client.hub.membership)

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query, body)


@pytest.mark.parametrize("name, verb, path, query, body, call", CASES, ids=IDS)
def test_async_hub_membership_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(**CLIENT_ARGS, http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))))
        try:
            await call(client.hub.membership)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query, body)
