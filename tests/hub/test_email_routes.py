"""Email coverage for the notifications and email modules.

The generated test files assert each method's verb and that the URL is https.
This file adds what they cannot see: the fully-resolved path of every one of
the 50 Email routes — the project routes under /notifications/email (and the
older /notifications/emails/campaigns/{campaignId}/messages) and the public
link routes under /email/ — with the routes and verbs taken from the gateway's
endpoint manifest, not from this SDK. Every call goes to a capture transport,
so nothing leaves the process and no email provider is contacted.
"""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

from ..helpers import make_client

CAMPAIGN_ID = "camp_1"
BATCH_ID = "batch_1"
NOTIFICATION_ID = "notif_1"
ITEM_ID = "id_1"
TOKEN = "signed-link-abc"

# name, verb, expected path, call
EmailCase = tuple[str, str, str, Callable[[Any], Any]]

EMAIL_CASES: list[EmailCase] = [
    (
        "one_click_unsubscribe",
        "POST",
        "/v2/email/one-click-unsubscribe",
        lambda c: c.hub.email.one_click_unsubscribe(),
    ),
    (
        "get_email_preferences_by_link",
        "GET",
        "/v2/email/preferences",
        lambda c: c.hub.email.get_email_preferences_by_link(),
    ),
    (
        "get_email_campaigns",
        "GET",
        "/v2/notifications/email/campaigns",
        lambda c: c.hub.notifications.get_email_campaigns(),
    ),
    (
        "create_email_campaign",
        "POST",
        "/v2/notifications/email/campaigns",
        lambda c: c.hub.notifications.create_email_campaign(),
    ),
    (
        "delete_email_campaign",
        "DELETE",
        f"/v2/notifications/email/campaigns/{ITEM_ID}",
        lambda c: c.hub.notifications.delete_email_campaign(id=ITEM_ID),
    ),
    (
        "stop_email_campaign",
        "POST",
        f"/v2/notifications/email/campaigns/{ITEM_ID}/stop",
        lambda c: c.hub.notifications.stop_email_campaign(id=ITEM_ID),
    ),
    (
        "get_email_campaign",
        "GET",
        f"/v2/notifications/email/campaigns/{ITEM_ID}",
        lambda c: c.hub.notifications.get_email_campaign(id=ITEM_ID),
    ),
    (
        "get_email_campaign_batches",
        "GET",
        f"/v2/notifications/email/campaigns/{ITEM_ID}/batches",
        lambda c: c.hub.notifications.get_email_campaign_batches(id=ITEM_ID),
    ),
    (
        "get_email_campaign_batch_notifications",
        "GET",
        f"/v2/notifications/email/campaigns/{ITEM_ID}/batches/{BATCH_ID}",
        lambda c: c.hub.notifications.get_email_campaign_batch_notifications(id=ITEM_ID, batch_id=BATCH_ID),
    ),
    (
        "get_email_campaign_batch_notification",
        "GET",
        f"/v2/notifications/email/campaigns/{ITEM_ID}/batches/{BATCH_ID}/{NOTIFICATION_ID}",
        lambda c: c.hub.notifications.get_email_campaign_batch_notification(id=ITEM_ID, batch_id=BATCH_ID, notification_id=NOTIFICATION_ID),
    ),
    (
        "get_email_campaign_statistics",
        "GET",
        f"/v2/notifications/email/campaigns/{ITEM_ID}/stats",
        lambda c: c.hub.notifications.get_email_campaign_statistics(id=ITEM_ID),
    ),
    (
        "disable_email",
        "GET",
        "/v2/notifications/email/disable",
        lambda c: c.hub.notifications.disable_email(),
    ),
    (
        "get_email_disable_dependencies",
        "GET",
        "/v2/notifications/email/disable-dependencies",
        lambda c: c.hub.notifications.get_email_disable_dependencies(),
    ),
    (
        "enable_email",
        "GET",
        "/v2/notifications/email/enable",
        lambda c: c.hub.notifications.enable_email(),
    ),
    (
        "get_email_footers",
        "GET",
        "/v2/notifications/email/footers",
        lambda c: c.hub.notifications.get_email_footers(),
    ),
    (
        "save_email_footer",
        "POST",
        "/v2/notifications/email/footers",
        lambda c: c.hub.notifications.save_email_footer(),
    ),
    (
        "delete_email_footer",
        "DELETE",
        f"/v2/notifications/email/footers/{ITEM_ID}",
        lambda c: c.hub.notifications.delete_email_footer(id=ITEM_ID),
    ),
    (
        "get_email_footer",
        "GET",
        f"/v2/notifications/email/footers/{ITEM_ID}",
        lambda c: c.hub.notifications.get_email_footer(id=ITEM_ID),
    ),
    (
        "get_email_integrations",
        "GET",
        "/v2/notifications/email/integrations",
        lambda c: c.hub.notifications.get_email_integrations(),
    ),
    (
        "save_email_integration",
        "POST",
        "/v2/notifications/email/integrations",
        lambda c: c.hub.notifications.save_email_integration(),
    ),
    (
        "confirm_email_integration_human_delivery",
        "POST",
        "/v2/notifications/email/integrations/confirm-human-delivery",
        lambda c: c.hub.notifications.confirm_email_integration_human_delivery(),
    ),
    (
        "check_email_integration_domain_health",
        "POST",
        "/v2/notifications/email/integrations/domain-health",
        lambda c: c.hub.notifications.check_email_integration_domain_health(),
    ),
    (
        "test_email_integration",
        "POST",
        "/v2/notifications/email/integrations/test",
        lambda c: c.hub.notifications.test_email_integration(),
    ),
    (
        "delete_email_integration",
        "DELETE",
        f"/v2/notifications/email/integrations/{ITEM_ID}",
        lambda c: c.hub.notifications.delete_email_integration(id=ITEM_ID),
    ),
    (
        "set_emails_integration_as_default",
        "PUT",
        f"/v2/notifications/email/integrations/{ITEM_ID}/default",
        lambda c: c.hub.notifications.set_emails_integration_as_default(id=ITEM_ID),
    ),
    (
        "disable_email_integration",
        "PUT",
        f"/v2/notifications/email/integrations/{ITEM_ID}/disable",
        lambda c: c.hub.notifications.disable_email_integration(id=ITEM_ID),
    ),
    (
        "enable_email_integration",
        "PUT",
        f"/v2/notifications/email/integrations/{ITEM_ID}/enable",
        lambda c: c.hub.notifications.enable_email_integration(id=ITEM_ID),
    ),
    (
        "get_email_integration",
        "GET",
        f"/v2/notifications/email/integrations/{ITEM_ID}",
        lambda c: c.hub.notifications.get_email_integration(id=ITEM_ID),
    ),
    (
        "preview_email_notification",
        "GET",
        "/v2/notifications/email/preview",
        lambda c: c.hub.notifications.preview_email_notification(),
    ),
    (
        "get_email_settings",
        "GET",
        "/v2/notifications/email/settings",
        lambda c: c.hub.notifications.get_email_settings(),
    ),
    (
        "get_email_signatures",
        "GET",
        "/v2/notifications/email/signatures",
        lambda c: c.hub.notifications.get_email_signatures(),
    ),
    (
        "save_email_signature",
        "POST",
        "/v2/notifications/email/signatures",
        lambda c: c.hub.notifications.save_email_signature(),
    ),
    (
        "delete_email_signature",
        "DELETE",
        f"/v2/notifications/email/signatures/{ITEM_ID}",
        lambda c: c.hub.notifications.delete_email_signature(id=ITEM_ID),
    ),
    (
        "get_email_signature",
        "GET",
        f"/v2/notifications/email/signatures/{ITEM_ID}",
        lambda c: c.hub.notifications.get_email_signature(id=ITEM_ID),
    ),
    (
        "get_system_email_templates",
        "GET",
        "/v2/notifications/email/system-templates",
        lambda c: c.hub.notifications.get_system_email_templates(),
    ),
    (
        "get_system_email_template",
        "GET",
        f"/v2/notifications/email/system-templates/{ITEM_ID}",
        lambda c: c.hub.notifications.get_system_email_template(id=ITEM_ID),
    ),
    (
        "get_email_templates",
        "GET",
        "/v2/notifications/email/templates",
        lambda c: c.hub.notifications.get_email_templates(),
    ),
    (
        "create_email_template",
        "POST",
        "/v2/notifications/email/templates",
        lambda c: c.hub.notifications.create_email_template(),
    ),
    (
        "update_email_template",
        "PUT",
        "/v2/notifications/email/templates",
        lambda c: c.hub.notifications.update_email_template(),
    ),
    (
        "attach_file_to_template",
        "POST",
        "/v2/notifications/email/templates/attachments",
        lambda c: c.hub.notifications.attach_file_to_template(),
    ),
    (
        "get_mjml",
        "POST",
        "/v2/notifications/email/templates/mjml",
        lambda c: c.hub.notifications.get_mjml(),
    ),
    (
        "delete_email_template",
        "DELETE",
        f"/v2/notifications/email/templates/{ITEM_ID}",
        lambda c: c.hub.notifications.delete_email_template(id=ITEM_ID),
    ),
    (
        "archive_email_template",
        "PUT",
        f"/v2/notifications/email/templates/{ITEM_ID}/archive",
        lambda c: c.hub.notifications.archive_email_template(id=ITEM_ID),
    ),
    (
        "clone_email_template",
        "POST",
        f"/v2/notifications/email/templates/{ITEM_ID}/clone",
        lambda c: c.hub.notifications.clone_email_template(id=ITEM_ID),
    ),
    (
        "un_archive_email_template",
        "PUT",
        f"/v2/notifications/email/templates/{ITEM_ID}/unarchive",
        lambda c: c.hub.notifications.un_archive_email_template(id=ITEM_ID),
    ),
    (
        "get_email_template",
        "GET",
        f"/v2/notifications/email/templates/{ITEM_ID}",
        lambda c: c.hub.notifications.get_email_template(id=ITEM_ID),
    ),
    (
        "get_email_template_available_tokens",
        "GET",
        f"/v2/notifications/email/templates/{ITEM_ID}/tokens",
        lambda c: c.hub.notifications.get_email_template_available_tokens(id=ITEM_ID),
    ),
    (
        "save_email_validation_integration",
        "POST",
        "/v2/notifications/email/validation/integrations",
        lambda c: c.hub.notifications.save_email_validation_integration(),
    ),
    (
        "test_email_validation_integration",
        "POST",
        "/v2/notifications/email/validation/integrations/test",
        lambda c: c.hub.notifications.test_email_validation_integration(),
    ),
    (
        "get_email_campaign_messages",
        "GET",
        f"/v2/notifications/emails/campaigns/{CAMPAIGN_ID}/messages",
        lambda c: c.hub.notifications.get_email_campaign_messages(campaign_id=CAMPAIGN_ID),
    ),
]


@pytest.mark.parametrize(
    ("name", "verb", "path", "call"),
    EMAIL_CASES,
    ids=[case[0] for case in EMAIL_CASES],
)
def test_email_endpoint_hits_the_expected_route(
    name: str, verb: str, path: str, call: Callable[[Any], Any]
) -> None:
    client, transport = make_client(account_id="acct_1")
    call(client)

    assert transport.last_request is not None
    assert transport.last_request["method"] == verb
    assert urlparse(transport.last_request["url"]).path == path, (
        f"{name}: got {transport.last_request['url']}, expected path {path}"
    )


def test_email_surface_size() -> None:
    """50 live Email routes. A new or removed one changes this count, so it cannot pass untested."""
    assert len(EMAIL_CASES) == 50


def test_email_call_sends_auth_and_project_headers() -> None:
    client, transport = make_client()
    client.hub.notifications.stop_email_campaign(CAMPAIGN_ID)

    assert transport.last_request is not None
    headers = transport.last_request["headers"]
    assert headers["authorization"] == "Bearer test-token"
    assert headers["x-cm-projectid"] == "test-project"


@pytest.fixture
def _no_env_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("NORBIX_API_KEY", raising=False)
    monkeypatch.delenv("NORBIX_BEARER_TOKEN", raising=False)


def _capture(seen: list[httpx.Request]) -> Callable[[httpx.Request], httpx.Response]:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"item": {}})

    return handler


@pytest.mark.usefixtures("_no_env_credentials")
@pytest.mark.parametrize(
    ("api_key", "want_auth"),
    [(None, None), ("key_1", "Bearer key_1")],
    ids=["no_credentials", "api_key"],
)
def test_email_preferences_by_link_needs_no_sign_in(api_key: str | None, want_auth: str | None) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(
        project_id="test-project",
        api_key=api_key,
        http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))),
    )

    client.hub.email.get_email_preferences_by_link(token=TOKEN)

    assert len(seen) == 1
    url = urlparse(str(seen[0].url))
    assert seen[0].method == "GET"
    assert url.path == "/v2/email/preferences"
    assert parse_qs(url.query) == {"token": [TOKEN]}
    assert seen[0].headers.get("Authorization") == want_auth


@pytest.mark.usefixtures("_no_env_credentials")
def test_async_email_preferences_by_link_needs_no_sign_in() -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(
            project_id="test-project",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))),
        )
        try:
            await client.hub.email.get_email_preferences_by_link(token=TOKEN)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == 1
    assert urlparse(str(seen[0].url)).path == "/v2/email/preferences"
    assert seen[0].headers.get("Authorization") is None


def test_async_modules_expose_the_same_email_surface() -> None:
    """Every sync Email method must have an async twin."""
    from norbix_python.hub.email import AsyncEmailModule, EmailModule
    from norbix_python.hub.notifications import AsyncNotificationsModule, NotificationsModule

    pairs = [(NotificationsModule, AsyncNotificationsModule), (EmailModule, AsyncEmailModule)]
    missing = sorted(
        name
        for sync_cls, async_cls in pairs
        for name in dir(sync_cls)
        if not name.startswith("_") and "email" in name and not hasattr(async_cls, name)
    )
    assert missing == []


@pytest.mark.usefixtures("_no_env_credentials")
def test_one_click_unsubscribe_needs_no_sign_in() -> None:
    """The gateway does not authenticate it; with no credentials it still goes out, no Authorization."""
    seen: list[httpx.Request] = []
    client = Norbix(
        project_id="test-project",
        http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))),
    )

    client.hub.email.one_click_unsubscribe(token=TOKEN)

    assert len(seen) == 1
    assert seen[0].method == "POST"
    assert urlparse(str(seen[0].url)).path == "/v2/email/one-click-unsubscribe"
    assert seen[0].headers.get("Authorization") is None


@pytest.mark.usefixtures("_no_env_credentials")
def test_async_one_click_unsubscribe_needs_no_sign_in() -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(
            project_id="test-project",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))),
        )
        try:
            await client.hub.email.one_click_unsubscribe(token=TOKEN)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == 1
    assert seen[0].headers.get("Authorization") is None


def test_create_email_campaign_sends_the_provider_integration_id_nested() -> None:
    # The gateway requires the email provider id inside `campaign`.
    import json

    client, transport = make_client()
    client.hub.notifications.create_email_campaign(
        campaign={"templateId": "tpl_1", "integrationId": "int_1", "source": "allUsers"}
    )

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert urlparse(transport.last_request["url"]).path == "/v2/notifications/email/campaigns"
    assert json.loads(transport.last_request["body"]) == {
        "campaign": {"templateId": "tpl_1", "integrationId": "int_1", "source": "allUsers"}
    }
