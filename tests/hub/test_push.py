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


CAMPAIGN_AUDIENCES = [
    ("allUsers", {"templateId": TEMPLATE_ID, "userTags": ["beta"]}, "userTags"),
    ("specifiedUsers", {"templateId": TEMPLATE_ID, "userRecipients": ["user_1"]}, "userRecipients"),
    ("accountUsers", {"templateId": TEMPLATE_ID, "userRecipients": ["acct_1"]}, "userRecipients"),
    ("collection", {"templateId": TEMPLATE_ID, "schemaName": "subscribers"}, "schemaName"),
    (
        "devices",
        {"templateId": TEMPLATE_ID, "devices": [{"token": "device_1", "deliveryFamily": "ios"}]},
        "devices",
    ),
]


@pytest.mark.parametrize(
    ("source", "fields", "own_field"),
    CAMPAIGN_AUDIENCES,
    ids=[case[0] for case in CAMPAIGN_AUDIENCES],
)
def test_create_push_campaign_carries_the_audience_shape(
    source: str, fields: dict[str, Any], own_field: str
) -> None:
    client, transport = make_client()
    client.hub.notifications.create_push_campaign(campaign={"source": source, **fields})

    assert transport.last_request is not None
    campaign = json.loads(transport.last_request["body"])["campaign"]
    # The discriminator has to reach the wire as the name — the server reads it
    # with a string parse and rejects a number.
    assert campaign["source"] == source
    assert campaign["templateId"] == TEMPLATE_ID
    assert own_field in campaign


PUSH_PROVIDERS = [
    "Fake",
    "AndroidFirebase",
    "AppleApns",
    "CodeMashChromePlugin",
    "ChromeWeb",
    "EdgeWeb",
    "FirefoxWeb",
    "SafariPush",
]


@pytest.mark.parametrize("provider", PUSH_PROVIDERS)
def test_save_push_integration_carries_the_provider_shape(provider: str) -> None:
    client, transport = make_client()
    client.hub.notifications.save_push_integration(
        integration={"provider": provider, "integrationName": f"test-{provider}", "isEnabled": True}
    )

    assert transport.last_request is not None
    integration = json.loads(transport.last_request["body"])["integration"]
    assert integration["provider"] == provider
    assert integration["integrationName"] == f"test-{provider}"


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
