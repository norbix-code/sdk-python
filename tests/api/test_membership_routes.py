from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

"""Every Membership route the API host serves.

The user list and user edit screens (contacts and the ``/membership/auth`` user
routes), user registration and invitation, and the end-user passkey, password
and token routes (``/membership/userauth/*``), called through
``client.api.membership`` (sync and async). Each case asserts the host (api,
not hub: the contact routes exist on both), the verb, the exact path, the
query (reads and deletes) and the JSON body (saves). Source of truth: the
gateway ``[Route]`` attributes (Api.Membership, and Hub.Contacts served again on
the API host); field names from the generated request types. Every call goes
to a mock transport, so nothing leaves the process.
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
USR = "usr_1"
AUTH = "auth_1"
CRED = "cred_1"
DB = "int_db"

CREATE_CONTACT = {"primaryEmail": "ana@example.test", "displayName": "Ana", "tags": ["vip"]}
MERGE = {"survivorId": CT, "mergedIds": ["ct_2"]}
DRY_RUN = {"dryRun": True}
UPDATE_CONTACT = {"displayName": "Ana B.", "language": "lt"}
IDENTITY = {"authId": AUTH}
AI_PLAN = {"planId": "plan_pro"}

INVITE = {"email": "ana@example.test", "fullName": "Ana Berg", "roles": ["Editor"]}
FINISH = {"token": "inv_tok", "password": "S3cret-pass!", "firstName": "Ana"}
EMAIL = {"email": "ana@example.test", "password": "S3cret-pass!", "roles": ["User"]}
EMAIL_PERM = {"email": "ana@example.test", "password": "S3cret-pass!"}
GUEST = {"userGeneralInfo": {"displayName": "Guest"}}
PHONE = {"phone": "+37060000000"}
SERVICE = {"userGeneralInfo": {"displayName": "ci-bot"}, "roles": ["Service"]}
USER_NAME = {"userName": "ana", "password": "S3cret-pass!", "roles": ["User"]}
USER_NAME_PERM = {"userName": "ana", "password": "S3cret-pass!"}

UPDATE_USER = {"id": USR, "userGeneralInfo": {"displayName": "Ana B."}}
ASSIGN_ROLES = {"id": USR, "roles": ["Editor"]}
BY_ID = {"id": USR}
PREFS = {"blockAllMarketingMessages": False, "blockedTags": ["promo"]}
LINK = {"provider": "Google", "providerToken": "g_tok"}
TAG = {"subscribed": True}
MAP_AUTH = {"authId": AUTH, "databaseIntegrationId": DB}
SET_ROLES = {"roles": ["Editor", "User"]}
CONSENT = {"lawfulBasis": "Consent", "source": "signup-form"}
UNSUBSCRIBE = {"reason": "too many emails"}

MAIL = {"email": "ana@example.test"}
CONFIRM_MAIL = {"email": "ana@example.test", "code": "123456"}
REFRESH = {"refreshToken": "rt_1"}
REG_OPTIONS = {"verificationToken": "vt_1"}
VERIFY_AUTHN = {"ceremonyId": "cer_1", "assertionResponse": {"id": "cred"}}
VERIFY_REG = {"verificationToken": "vt_1", "ceremonyId": "cer_1", "attestationResponse": {"id": "cred"}, "friendlyName": "Laptop"}
RENAME = {"friendlyName": "Phone"}
CHANGE_PASSWORD = {"currentPassword": "old-pass", "newPassword": "new-pass-1!"}
CONFIRM_RESET = {"token": "rst_1", "newPassword": "new-pass-1!"}
CONSUME = {"token": "ml_1"}
RECOVERY = {"email": "ana@example.test", "recoveryCode": "AAAA-BBBB"}

U = "/v2/membership/users"
A = "/v2/membership/auth"
UA = "/v2/membership/userauth"

# name, verb, path, query (None: no query), body (None: no body), call
Case = tuple[str, str, str, dict[str, list[str]] | None, dict[str, Any] | None, Callable[[Any], Any]]

CASES: list[Case] = [
    # Users list.
    ("get_all_contacts", "GET", U, {"search": ["ana"], "pageSize": ["25"]}, None,
     lambda m: m.get_all_contacts(search="ana", pageSize=25)),
    ("create_contact", "POST", U, None, CREATE_CONTACT, lambda m: m.create_contact(**CREATE_CONTACT)),
    ("merge_contacts", "POST", f"{U}/merge", None, MERGE, lambda m: m.merge_contacts(**MERGE)),
    ("repair_contact_roles", "POST", f"{U}/repair-roles", None, DRY_RUN, lambda m: m.repair_contact_roles(**DRY_RUN)),
    ("delete_contact", "DELETE", f"{U}/{CT}", None, None, lambda m: m.delete_contact(CT)),
    ("get_users", "GET", A, {"search": ["ana"], "roleNames": ["Editor", "User"]}, None,
     lambda m: m.get_users(search="ana", roleNames=["Editor", "User"])),
    # The id goes on the query: the route has no {id} (same as the .NET snapshot).
    ("delete_user", "DELETE", A, {"id": [USR]}, None, lambda m: m.delete_user(**BY_ID)),
    # User — new: invitation and the eight registration routes.
    ("invite_user", "POST", f"{A}/invite", None, INVITE, lambda m: m.invite_user(**INVITE)),
    ("finish_invitation", "POST", f"{A}/invitation/finish", None, FINISH, lambda m: m.finish_invitation(**FINISH)),
    ("save_email_user", "POST", f"{A}/register/email", None, EMAIL, lambda m: m.save_email_user(**EMAIL)),
    ("save_email_user_name_with_permissions", "POST", f"{A}/register/email-with-permissions", None, EMAIL_PERM,
     lambda m: m.save_email_user_name_with_permissions(**EMAIL_PERM)),
    ("save_guest_user", "POST", f"{A}/register/guest", None, GUEST, lambda m: m.save_guest_user(**GUEST)),
    ("save_phone_user", "POST", f"{A}/register/phone", None, PHONE, lambda m: m.save_phone_user(**PHONE)),
    ("save_phone_user_name_with_permissions", "POST", f"{A}/register/phone-with-permissions", None, PHONE,
     lambda m: m.save_phone_user_name_with_permissions(**PHONE)),
    ("save_system_user_with_permissions", "POST", f"{A}/register/service", None, SERVICE,
     lambda m: m.save_system_user_with_permissions(**SERVICE)),
    ("save_user_name_user", "POST", f"{A}/register/user-name", None, USER_NAME, lambda m: m.save_user_name_user(**USER_NAME)),
    ("save_user_name_with_permissions", "POST", f"{A}/register/user-name-with-permissions", None, USER_NAME_PERM,
     lambda m: m.save_user_name_with_permissions(**USER_NAME_PERM)),
    # User edit / detail — contact routes on the API host.
    ("get_contact", "GET", f"{U}/{CT}", None, None, lambda m: m.get_contact(CT)),
    ("update_contact", "PATCH", f"{U}/{CT}", None, UPDATE_CONTACT, lambda m: m.update_contact(CT, **UPDATE_CONTACT)),
    ("add_contact_identity", "POST", f"{U}/{CT}/identities", None, IDENTITY, lambda m: m.add_contact_identity(CT, **IDENTITY)),
    ("remove_contact_identity", "DELETE", f"{U}/{CT}/identities/{AUTH}", None, None, lambda m: m.remove_contact_identity(CT, AUTH)),
    ("promote_contact_identity", "POST", f"{U}/{CT}/identities/{AUTH}/promote", None, None,
     lambda m: m.promote_contact_identity(CT, AUTH)),
    ("clear_contact_bounce", "POST", f"{U}/{CT}/marketing-state/Sms/clear-bounce", None, None,
     lambda m: m.clear_contact_bounce(CT, "Sms")),
    ("set_user_ai_plan", "PUT", f"{U}/{USR}/ai-plan", None, AI_PLAN, lambda m: m.set_user_ai_plan(USR, **AI_PLAN)),
    # User edit / detail — /membership/auth user routes.
    ("update_user", "PUT", A, None, UPDATE_USER, lambda m: m.update_user(**UPDATE_USER)),
    ("assign_role_permissions", "PUT", f"{A}/assign-roles", None, ASSIGN_ROLES, lambda m: m.assign_role_permissions(**ASSIGN_ROLES)),
    ("block_user", "PATCH", f"{A}/block", None, BY_ID, lambda m: m.block_user(**BY_ID)),
    ("unblock_user", "PATCH", f"{A}/unblock", None, BY_ID, lambda m: m.unblock_user(**BY_ID)),
    ("get_user", "GET", f"{A}/{USR}", {"databaseIntegrationId": [DB]}, None, lambda m: m.get_user(USR, databaseIntegrationId=DB)),
    ("get_user_preferences", "GET", f"{A}/{USR}/preferences", None, None, lambda m: m.get_user_preferences(USR)),
    ("update_user_preferences", "PUT", f"{A}/{USR}/preferences", None, PREFS, lambda m: m.update_user_preferences(USR, **PREFS)),
    ("link_identity", "POST", f"{A}/{USR}/link-identity", None, LINK, lambda m: m.link_identity(USR, **LINK)),
    ("set_contact_tag_subscription", "PUT", f"{U}/{CT}/marketing-state/Email/Marketing/tags/news", None, TAG,
     lambda m: m.set_contact_tag_subscription(CT, "Email", "Marketing", "news", **TAG)),
    ("map_auth_to_user", "POST", f"{U}/{USR}/map-auth", None, MAP_AUTH, lambda m: m.map_auth_to_user(USR, **MAP_AUTH)),
    ("set_contact_roles", "PUT", f"{U}/{USR}/roles", None, SET_ROLES, lambda m: m.set_contact_roles(USR, **SET_ROLES)),
    ("grant_contact_consent", "POST", f"{U}/{CT}/marketing-state/Email/consent", None, CONSENT,
     lambda m: m.grant_contact_consent(CT, "Email", **CONSENT)),
    ("unsubscribe_contact", "POST", f"{U}/{CT}/marketing-state/Email/unsubscribe", None, UNSUBSCRIBE,
     lambda m: m.unsubscribe_contact(CT, "Email", **UNSUBSCRIBE)),
    # Passkey & user-auth (API only, no screen).
    ("confirm_email_verification", "POST", f"{UA}/email/confirm-verification", None, CONFIRM_MAIL,
     lambda m: m.confirm_email_verification(**CONFIRM_MAIL)),
    ("start_email_verification", "POST", f"{UA}/email/start-verification", None, MAIL, lambda m: m.start_email_verification(**MAIL)),
    ("has_passkey", "POST", f"{UA}/has-passkey", None, MAIL, lambda m: m.has_passkey(**MAIL)),
    ("passkey_logout", "POST", f"{UA}/logout", None, REFRESH, lambda m: m.passkey_logout(**REFRESH)),
    ("passkey_authentication_options", "POST", f"{UA}/passkey/authentication-options", None, MAIL,
     lambda m: m.passkey_authentication_options(**MAIL)),
    ("passkey_registration_options", "POST", f"{UA}/passkey/registration-options", None, REG_OPTIONS,
     lambda m: m.passkey_registration_options(**REG_OPTIONS)),
    ("verify_passkey_authentication", "POST", f"{UA}/passkey/verify-authentication", None, VERIFY_AUTHN,
     lambda m: m.verify_passkey_authentication(**VERIFY_AUTHN)),
    ("verify_passkey_registration", "POST", f"{UA}/passkey/verify-registration", None, VERIFY_REG,
     lambda m: m.verify_passkey_registration(**VERIFY_REG)),
    ("list_passkeys", "GET", f"{UA}/passkeys", None, None, lambda m: m.list_passkeys()),
    ("rename_passkey", "POST", f"{UA}/passkeys/{CRED}/rename", None, RENAME, lambda m: m.rename_passkey(CRED, **RENAME)),
    ("revoke_passkey", "POST", f"{UA}/passkeys/{CRED}/revoke", None, None, lambda m: m.revoke_passkey(CRED)),
    ("change_password", "POST", f"{UA}/password/change", None, CHANGE_PASSWORD, lambda m: m.change_password(**CHANGE_PASSWORD)),
    ("confirm_password_reset", "POST", f"{UA}/password/reset/confirm", None, CONFIRM_RESET,
     lambda m: m.confirm_password_reset(**CONFIRM_RESET)),
    ("request_password_reset", "POST", f"{UA}/password/reset/request", None, MAIL, lambda m: m.request_password_reset(**MAIL)),
    ("send_test_password_reset", "POST", f"{UA}/password/reset/test", None, MAIL, lambda m: m.send_test_password_reset(**MAIL)),
    ("consume_magic_link", "POST", f"{UA}/recovery/magic-link/consume", None, CONSUME, lambda m: m.consume_magic_link(**CONSUME)),
    ("request_magic_link", "POST", f"{UA}/recovery/magic-link/request", None, MAIL, lambda m: m.request_magic_link(**MAIL)),
    ("use_recovery_code", "POST", f"{UA}/recovery/use-code", None, RECOVERY, lambda m: m.use_recovery_code(**RECOVERY)),
    ("refresh_passkey_token", "POST", f"{UA}/token/refresh", None, REFRESH, lambda m: m.refresh_passkey_token(**REFRESH)),
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
    assert f"{request.url.scheme}://{request.url.host}" == API
    assert request.method == verb
    assert request.url.path == path
    assert parse_qs(request.url.query.decode()) == (query or {})
    if body is None:
        assert request.content == b""
    else:
        assert json.loads(request.content) == body
    assert request.headers["authorization"] == "Bearer key_1"
    assert request.headers["norbix-project-id"] == "test-project"


def test_api_membership_route_count() -> None:
    # Users list 7 + user new 10 + user edit 20 + passkey & user-auth 19.
    assert len(CASES) == 7 + 10 + 20 + 19


@pytest.mark.parametrize("name, verb, path, query, body, call", CASES, ids=IDS)
def test_api_membership_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))))

    call(client.api.membership)

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query, body)


@pytest.mark.parametrize("name, verb, path, query, body, call", CASES, ids=IDS)
def test_async_api_membership_route(
    name: str, verb: str, path: str, query: dict[str, list[str]] | None, body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(**CLIENT_ARGS, http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))))
        try:
            await call(client.api.membership)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == 1
    _assert_request(seen[0], verb, path, query, body)
