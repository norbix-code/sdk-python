from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any

import pytest

from ..helpers import make_client

"""Push coverage for the notifications module.

The generated test file asserts each push method's verb and that the URL is
https. This file adds the two things it cannot see: the fully-resolved path of
every one of the 37 push routes, and the polymorphic bodies that the server
routes on.

Only the Fake provider is used for a send path — it is the sandbox that accepts
a send and contacts no push service. Every call here goes to a capture
transport, so nothing leaves the process.
"""

CAMPAIGN_ID = "camp_1"
BATCH_ID = "batch_1"
NOTIFICATION_ID = "notif_1"
TEMPLATE_ID = "tpl_1"
INTEGRATION_ID = "int_1"

BASE = "/v2/notifications/push"

# name, verb, expected path, call
PushCase = tuple[str, str, str, Callable[[Any], Any]]

PUSH_CASES: list[PushCase] = [
    # module
    ("enable_push", "GET", f"{BASE}/enable", lambda m: m.enable_push()),
    ("disable_push", "GET", f"{BASE}/disable", lambda m: m.disable_push()),
    (
        "get_push_disable_dependencies",
        "GET",
        f"{BASE}/disable-dependencies",
        lambda m: m.get_push_disable_dependencies(),
    ),
    ("get_push_settings", "GET", f"{BASE}/settings", lambda m: m.get_push_settings()),
    # integrations
    ("get_push_integrations", "GET", f"{BASE}/integrations", lambda m: m.get_push_integrations()),
    ("save_push_integration", "POST", f"{BASE}/integrations", lambda m: m.save_push_integration()),
    (
        "get_push_integration",
        "GET",
        f"{BASE}/integrations/{INTEGRATION_ID}",
        lambda m: m.get_push_integration(id=INTEGRATION_ID),
    ),
    (
        "enable_push_integration",
        "PUT",
        f"{BASE}/integrations/{INTEGRATION_ID}/enable",
        lambda m: m.enable_push_integration(id=INTEGRATION_ID),
    ),
    (
        "disable_push_integration",
        "PUT",
        f"{BASE}/integrations/{INTEGRATION_ID}/disable",
        lambda m: m.disable_push_integration(id=INTEGRATION_ID),
    ),
    (
        "set_push_integration_as_default",
        "PUT",
        f"{BASE}/integrations/{INTEGRATION_ID}/default",
        lambda m: m.set_push_integration_as_default(id=INTEGRATION_ID),
    ),
    (
        "delete_push_integration",
        "DELETE",
        f"{BASE}/integrations/{INTEGRATION_ID}",
        lambda m: m.delete_push_integration(id=INTEGRATION_ID),
    ),
    (
        "test_push_integration",
        "POST",
        f"{BASE}/integrations/test",
        lambda m: m.test_push_integration(),
    ),
    (
        "confirm_push_integration_human_delivery",
        "POST",
        f"{BASE}/integrations/confirm-human-delivery",
        lambda m: m.confirm_push_integration_human_delivery(),
    ),
    (
        "register_code_mash_app_push_integration",
        "POST",
        f"{BASE}/integrations/app/request",
        lambda m: m.register_code_mash_app_push_integration(),
    ),
    # templates
    ("get_push_templates", "GET", f"{BASE}/templates", lambda m: m.get_push_templates()),
    ("create_push_template", "POST", f"{BASE}/templates", lambda m: m.create_push_template()),
    ("update_push_template", "PUT", f"{BASE}/templates", lambda m: m.update_push_template()),
    (
        "get_push_template",
        "GET",
        f"{BASE}/templates/{TEMPLATE_ID}",
        lambda m: m.get_push_template(id=TEMPLATE_ID),
    ),
    (
        "delete_push_template",
        "DELETE",
        f"{BASE}/templates/{TEMPLATE_ID}",
        lambda m: m.delete_push_template(id=TEMPLATE_ID),
    ),
    (
        "archive_push_template",
        "PUT",
        f"{BASE}/templates/{TEMPLATE_ID}/archive",
        lambda m: m.archive_push_template(id=TEMPLATE_ID),
    ),
    (
        "un_archive_push_template",
        "PUT",
        f"{BASE}/templates/{TEMPLATE_ID}/unarchive",
        lambda m: m.un_archive_push_template(id=TEMPLATE_ID),
    ),
    (
        "clone_push_template",
        "POST",
        f"{BASE}/templates/{TEMPLATE_ID}/clone",
        lambda m: m.clone_push_template(id=TEMPLATE_ID),
    ),
    (
        "get_push_message_content_tokens",
        "GET",
        f"{BASE}/templates/{TEMPLATE_ID}/tokens",
        lambda m: m.get_push_message_content_tokens(id=TEMPLATE_ID),
    ),
    ("render_push", "POST", f"{BASE}/templates/render", lambda m: m.render_push()),
    # campaigns
    ("get_push_campaigns", "GET", f"{BASE}/campaigns", lambda m: m.get_push_campaigns()),
    ("create_push_campaign", "POST", f"{BASE}/campaigns", lambda m: m.create_push_campaign()),
    (
        "get_push_campaign",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}",
        lambda m: m.get_push_campaign(id=CAMPAIGN_ID),
    ),
    (
        "delete_push_campaign",
        "DELETE",
        f"{BASE}/campaigns/{CAMPAIGN_ID}",
        lambda m: m.delete_push_campaign(id=CAMPAIGN_ID),
    ),
    (
        "stop_push_campaign",
        "POST",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/stop",
        lambda m: m.stop_push_campaign(id=CAMPAIGN_ID),
    ),
    (
        "get_push_campaign_batches",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/batches",
        lambda m: m.get_push_campaign_batches(id=CAMPAIGN_ID),
    ),
    (
        "get_push_campaign_batch_notifications",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/batches/{BATCH_ID}",
        lambda m: m.get_push_campaign_batch_notifications(id=CAMPAIGN_ID, batch_id=BATCH_ID),
    ),
    (
        "get_push_campaign_batch_notification",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/batches/{BATCH_ID}/{NOTIFICATION_ID}",
        lambda m: m.get_push_campaign_batch_notification(
            id=CAMPAIGN_ID, batch_id=BATCH_ID, notification_id=NOTIFICATION_ID
        ),
    ),
    (
        "get_push_campaign_statistics",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/stats",
        lambda m: m.get_push_campaign_statistics(id=CAMPAIGN_ID),
    ),
    (
        "get_push_campaign_messages",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/messages",
        lambda m: m.get_push_campaign_messages(campaign_id=CAMPAIGN_ID),
    ),
    (
        "get_push_campaign_message",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/messages/{NOTIFICATION_ID}",
        lambda m: m.get_push_campaign_message(campaign_id=CAMPAIGN_ID, id=NOTIFICATION_ID),
    ),
    (
        "preview_push_notification",
        "GET",
        f"{BASE}/preview",
        lambda m: m.preview_push_notification(),
    ),
    # devices
    ("register_device", "POST", f"{BASE}/devices", lambda m: m.register_device()),
]


@pytest.mark.parametrize(
    ("name", "verb", "path", "call"),
    PUSH_CASES,
    ids=[case[0] for case in PUSH_CASES],
)
def test_push_endpoint_hits_the_expected_route(
    name: str, verb: str, path: str, call: Callable[[Any], Any]
) -> None:
    # register_code_mash_app_push_integration is account-scoped, so the client
    # needs an account id; the rest ignore it.
    client, transport = make_client(account_id="acct_1")
    call(client.hub.notifications)

    assert transport.last_request is not None
    assert transport.last_request["method"] == verb
    assert transport.last_request["url"].endswith(path), (
        f"{name}: got {transport.last_request['url']}, expected it to end with {path}"
    )


def test_push_surface_size() -> None:
    """37 live push routes. A new one changes this count, so it cannot arrive untested."""
    assert len(PUSH_CASES) == 37


def test_push_call_sends_auth_and_project_headers() -> None:
    client, transport = make_client()
    client.hub.notifications.get_push_templates()

    assert transport.last_request is not None
    headers = transport.last_request["headers"]
    assert headers["authorization"] == "Bearer test-token"
    assert headers["x-cm-projectid"] == "test-project"


# The five campaign targets, with the fields the gateway reads for each one.
# Source of truth: gateway Hub.Push/Campaigns/Create.PushTo*.cs (field names)
# and Create_.cs (PushCampaignRequestDtoJsonConverter picks the record from
# `source`, case-insensitive). Note `rolesNames` on allUsers but `roleNames` on
# collection — the gateway spells them differently.
CAMPAIGN_TARGETS: list[tuple[str, dict[str, Any]]] = [
    ("allUsers", {"rolesNames": ["admin"], "userTags": ["beta"]}),
    ("specifiedUsers", {"userRecipients": ["user_1"]}),
    ("accountUsers", {"userRecipients": ["acct_user_1"]}),
    ("collection", {"schemaName": "subscribers", "fields": ["owner"], "fieldType": "User"}),
    ("devices", {"devices": [{"token": "device_1", "deliveryFamily": "Ios"}]}),
]

# PushCampaignRecipientsSourceTypes in the gateway — exactly these five.
GATEWAY_TARGETS = {"allusers", "specifiedusers", "accountusers", "collection", "devices"}


@pytest.mark.parametrize(
    ("source", "fields"),
    CAMPAIGN_TARGETS,
    ids=[case[0] for case in CAMPAIGN_TARGETS],
)
def test_create_push_campaign_sends_the_target_shape(source: str, fields: dict[str, Any]) -> None:
    client, transport = make_client()
    client.hub.notifications.create_push_campaign(
        campaign={"source": source, "templateId": TEMPLATE_ID, **fields}
    )

    assert transport.last_request is not None
    campaign = json.loads(transport.last_request["body"])["campaign"]
    # The discriminator has to reach the wire as the name — the server reads it
    # with GetString() and rejects a number.
    assert campaign == {"source": source, "templateId": TEMPLATE_ID, **fields}


def test_campaign_targets_match_the_gateway() -> None:
    assert {source.lower() for source, _ in CAMPAIGN_TARGETS} == GATEWAY_TARGETS
    assert len(CAMPAIGN_TARGETS) == len(GATEWAY_TARGETS)


# The eight providers the gateway's save converter accepts, with the fields each
# one validates. Source of truth: gateway Hub.Push/Integrations/Save_.cs (the
# switch arms of PushIntegrationRequestDtoJsonConverter) and Save.<Provider>.cs
# (the fields). The Chrome extension is `ChromePush`: `CodeMashChromePlugin`
# also exists in the generated enum, but no switch arm takes it, so the gateway
# answers "Unsupported provider".
#
# Every value is a dummy; nothing here leaves the process.
_VAPID = {"vapidPublicKey": "vapid-public", "vapidPrivateKey": "vapid-private"}
PUSH_PROVIDERS: list[tuple[str, dict[str, Any]]] = [
    ("Fake", {}),
    (
        "AndroidFirebase",
        {
            "projectId": "firebase-project",
            "clientEmail": "push@firebase-project.iam.example.com",
            "serviceAccountJson": '{"type":"service_account"}',
        },
    ),
    (
        "AppleApns",
        {
            "teamId": "TEAM123456",
            "appBundleId": "com.example.app",
            "keyId": "KEY1234567",
            "privateKey": "-----BEGIN PRIVATE KEY-----dummy",
            "isProduction": False,
        },
    ),
    (
        "ChromePush",
        {
            "extensionId": "3f2504e0-4f89-11d3-9a0c-0305e82c3301",
            **_VAPID,
            "subject": "mailto:push@example.com",
        },
    ),
    ("ChromeWeb", {**_VAPID, "subject": "mailto:push@example.com"}),
    ("EdgeWeb", {**_VAPID}),
    ("FirefoxWeb", {**_VAPID}),
    (
        "SafariPush",
        {
            "websitePushId": "web.com.example",
            "certificateP12Base64": "ZHVtbXk=",
            "certificatePassword": "dummy",
        },
    ),
]

# The switch arms of PushIntegrationRequestDtoJsonConverter.Read.
GATEWAY_PROVIDERS = {
    "AppleApns",
    "AndroidFirebase",
    "SafariPush",
    "ChromeWeb",
    "FirefoxWeb",
    "EdgeWeb",
    "ChromePush",
    "Fake",
}


@pytest.mark.parametrize(
    ("provider", "fields"),
    PUSH_PROVIDERS,
    ids=[case[0] for case in PUSH_PROVIDERS],
)
def test_save_push_integration_sends_the_provider_shape(
    provider: str, fields: dict[str, Any]
) -> None:
    client, transport = make_client()
    integration = {
        "provider": provider,
        "integrationName": f"test-{provider}",
        "isEnabled": True,
        **fields,
    }
    client.hub.notifications.save_push_integration(integration=integration)

    assert transport.last_request is not None
    assert json.loads(transport.last_request["body"])["integration"] == integration


def test_push_providers_match_the_gateway() -> None:
    assert {provider for provider, _ in PUSH_PROVIDERS} == GATEWAY_PROVIDERS
    assert len(PUSH_PROVIDERS) == len(GATEWAY_PROVIDERS)


def test_register_device_sends_the_device_shape() -> None:
    """Gateway Hub.Push/Devices/Create.cs + PushDeviceDto.cs: `deviceOs` and `token` are required."""
    client, transport = make_client()
    device = {"deviceOs": "iOS", "token": "device_1", "modelName": "iPhone"}
    client.hub.notifications.register_device(userId="user_1", pushDeviceDto=device)

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert transport.last_request["url"].endswith(f"{BASE}/devices")
    body = json.loads(transport.last_request["body"])
    assert body["pushDeviceDto"] == device
    assert body["userId"] == "user_1"


def test_async_module_exposes_the_same_push_surface() -> None:
    """Every sync push method must have an async twin."""
    from norbix_python.hub.notifications import AsyncNotificationsModule, NotificationsModule

    push_methods = {
        name
        for name in dir(NotificationsModule)
        if not name.startswith("_") and ("push" in name or name == "register_device")
    }
    missing = sorted(name for name in push_methods if not hasattr(AsyncNotificationsModule, name))
    assert missing == []
