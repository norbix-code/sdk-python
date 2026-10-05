from __future__ import annotations

import asyncio
import inspect
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix

from ..helpers import make_client

"""SMS coverage for the notifications module.

The generated test file asserts each SMS method's verb and that the URL is
https. This file adds what it cannot see: the fully-resolved path of every one
of the 34 SMS routes, and the bodies whose shape the server picks from a value
inside the body (the campaign audience and the integration provider).

Only the Fake provider is used for a send path — it is the sandbox that accepts
a send and contacts no SMS service. Every call here goes to a capture
transport, so nothing leaves the process.
"""

CAMPAIGN_ID = "camp_1"
BATCH_ID = "batch_1"
NOTIFICATION_ID = "notif_1"
TEMPLATE_ID = "tpl_1"
INTEGRATION_ID = "int_1"
CAMPAIGN_TIME = 1_900_000_000  # unix seconds, UTC — a future time

BASE = "/v2/notifications/sms"

# name, verb, expected path, call
SmsCase = tuple[str, str, str, Callable[[Any], Any]]

SMS_CASES: list[SmsCase] = [
    # module
    ("enable_sms", "PUT", f"{BASE}/enable", lambda m: m.enable_sms()),
    ("disable_sms", "PUT", f"{BASE}/disable", lambda m: m.disable_sms()),
    (
        "get_sms_disable_dependencies",
        "GET",
        f"{BASE}/disable-dependencies",
        lambda m: m.get_sms_disable_dependencies(),
    ),
    ("get_sms_settings", "GET", f"{BASE}/settings", lambda m: m.get_sms_settings()),
    # integrations
    ("get_sms_integrations", "GET", f"{BASE}/integrations", lambda m: m.get_sms_integrations()),
    ("save_sms_integration", "POST", f"{BASE}/integrations", lambda m: m.save_sms_integration()),
    (
        "get_sms_integration",
        "GET",
        f"{BASE}/integrations/{INTEGRATION_ID}",
        lambda m: m.get_sms_integration(id=INTEGRATION_ID),
    ),
    (
        "enable_sms_integration",
        "PUT",
        f"{BASE}/integrations/{INTEGRATION_ID}/enable",
        lambda m: m.enable_sms_integration(id=INTEGRATION_ID),
    ),
    (
        "disable_sms_integration",
        "PUT",
        f"{BASE}/integrations/{INTEGRATION_ID}/disable",
        lambda m: m.disable_sms_integration(id=INTEGRATION_ID),
    ),
    (
        "set_sms_integration_as_default",
        "PUT",
        f"{BASE}/integrations/{INTEGRATION_ID}/default",
        lambda m: m.set_sms_integration_as_default(id=INTEGRATION_ID),
    ),
    (
        "delete_sms_integration",
        "DELETE",
        f"{BASE}/integrations/{INTEGRATION_ID}",
        lambda m: m.delete_sms_integration(id=INTEGRATION_ID),
    ),
    (
        "test_sms_integration",
        "POST",
        f"{BASE}/integrations/test",
        lambda m: m.test_sms_integration(),
    ),
    (
        "confirm_sms_integration_human_delivery",
        "POST",
        f"{BASE}/integrations/confirm-human-delivery",
        lambda m: m.confirm_sms_integration_human_delivery(),
    ),
    # templates
    ("get_sms_templates", "GET", f"{BASE}/templates", lambda m: m.get_sms_templates()),
    ("create_sms_template", "POST", f"{BASE}/templates", lambda m: m.create_sms_template()),
    ("update_sms_template", "PUT", f"{BASE}/templates", lambda m: m.update_sms_template()),
    (
        "get_sms_template",
        "GET",
        f"{BASE}/templates/{TEMPLATE_ID}",
        lambda m: m.get_sms_template(id=TEMPLATE_ID),
    ),
    (
        "delete_sms_template",
        "DELETE",
        f"{BASE}/templates/{TEMPLATE_ID}",
        lambda m: m.delete_sms_template(id=TEMPLATE_ID),
    ),
    (
        "archive_sms_template",
        "PUT",
        f"{BASE}/templates/{TEMPLATE_ID}/archive",
        lambda m: m.archive_sms_template(id=TEMPLATE_ID),
    ),
    (
        "un_archive_sms_template",
        "PUT",
        f"{BASE}/templates/{TEMPLATE_ID}/unarchive",
        lambda m: m.un_archive_sms_template(id=TEMPLATE_ID),
    ),
    (
        "clone_sms_template",
        "POST",
        f"{BASE}/templates/{TEMPLATE_ID}/clone",
        lambda m: m.clone_sms_template(id=TEMPLATE_ID),
    ),
    (
        "get_sms_message_content_tokens",
        "GET",
        f"{BASE}/templates/{TEMPLATE_ID}/tokens",
        lambda m: m.get_sms_message_content_tokens(id=TEMPLATE_ID),
    ),
    ("render_sms", "POST", f"{BASE}/templates/render", lambda m: m.render_sms()),
    # campaigns
    ("get_sms_campaigns", "GET", f"{BASE}/campaigns", lambda m: m.get_sms_campaigns()),
    ("create_sms_campaign", "POST", f"{BASE}/campaigns", lambda m: m.create_sms_campaign()),
    (
        "get_sms_campaign",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}",
        lambda m: m.get_sms_campaign(id=CAMPAIGN_ID),
    ),
    (
        "delete_sms_campaign",
        "DELETE",
        f"{BASE}/campaigns/{CAMPAIGN_ID}",
        lambda m: m.delete_sms_campaign(id=CAMPAIGN_ID),
    ),
    (
        "stop_sms_campaign",
        "POST",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/stop",
        lambda m: m.stop_sms_campaign(id=CAMPAIGN_ID),
    ),
    (
        "get_sms_campaign_batches",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/batches",
        lambda m: m.get_sms_campaign_batches(id=CAMPAIGN_ID),
    ),
    (
        "get_sms_campaign_batch_notifications",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/batches/{BATCH_ID}",
        lambda m: m.get_sms_campaign_batch_notifications(id=CAMPAIGN_ID, batch_id=BATCH_ID),
    ),
    (
        "get_sms_campaign_batch_notification",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/batches/{BATCH_ID}/{NOTIFICATION_ID}",
        lambda m: m.get_sms_campaign_batch_notification(
            id=CAMPAIGN_ID, batch_id=BATCH_ID, notification_id=NOTIFICATION_ID
        ),
    ),
    (
        "get_sms_campaign_statistics",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/stats",
        lambda m: m.get_sms_campaign_statistics(id=CAMPAIGN_ID),
    ),
    (
        "get_sms_campaign_messages",
        "GET",
        f"{BASE}/campaigns/{CAMPAIGN_ID}/messages",
        lambda m: m.get_sms_campaign_messages(campaign_id=CAMPAIGN_ID),
    ),
    (
        "preview_sms_notification",
        "GET",
        f"{BASE}/preview",
        lambda m: m.preview_sms_notification(),
    ),
]


@pytest.mark.parametrize(
    ("name", "verb", "path", "call"),
    SMS_CASES,
    ids=[case[0] for case in SMS_CASES],
)
def test_sms_endpoint_hits_the_expected_route(
    name: str, verb: str, path: str, call: Callable[[Any], Any]
) -> None:
    # The client carries an account id; project-scoped routes ignore it.
    client, transport = make_client(account_id="acct_1")
    call(client.hub.notifications)

    assert transport.last_request is not None
    assert transport.last_request["method"] == verb
    assert urlparse(transport.last_request["url"]).path == path, (
        f"{name}: got {transport.last_request['url']}, expected the path {path}"
    )


def test_sms_surface_size() -> None:
    """34 live SMS routes in the gateway. A new one changes this count, so it cannot arrive untested."""
    assert len(SMS_CASES) == 34
    assert len({case[0] for case in SMS_CASES}) == 34


def test_sms_call_sends_auth_and_project_headers() -> None:
    client, transport = make_client()
    client.hub.notifications.get_sms_templates()

    assert transport.last_request is not None
    headers = transport.last_request["headers"]
    assert headers["authorization"] == "Bearer test-token"
    assert headers["x-cm-projectid"] == "test-project"


# The four campaign audiences the gateway accepts, each with the settings
# object it reads. Source of truth: gateway Hub.Sms/Campaigns/Create.cs —
# `deliveryType` names the audience and the `Settings` switch picks the one
# matching object (`allUsers`, `specifiedUsers`, `collection`, `phoneNumbers`).
# Unlike push, the request is flat (no `campaign` wrapper) and the audience
# object repeats its own name in `recipientsSourceType`. The gateway enum also
# lists `AccountUsers`, but the create request has no settings object for it,
# so it is not sent from here.
CAMPAIGN_AUDIENCES: list[tuple[str, str, dict[str, Any]]] = [
    (
        "AllUsers",
        "allUsers",
        {
            "recipientsSourceType": "AllUsers",
            "rolesNames": ["authenticated"],
            "userTags": [],
            "campaignTime": CAMPAIGN_TIME,
        },
    ),
    (
        "SpecifiedUsers",
        "specifiedUsers",
        {
            "recipientsSourceType": "SpecifiedUsers",
            "recipients": ["user_1"],
            "campaignTime": CAMPAIGN_TIME,
        },
    ),
    (
        "AccountUsers",
        "accountUsers",
        {
            "recipientsSourceType": "AccountUsers",
            "recipients": ["owner_1", "member_2"],
            "campaignTime": CAMPAIGN_TIME,
        },
    ),
    (
        "Collection",
        "collection",
        {
            "recipientsSourceType": "Collection",
            "schemaName": "subscribers",
            "fields": ["owner"],
            "fieldType": "User",
            "campaignTime": CAMPAIGN_TIME,
        },
    ),
    (
        "PhoneNumbers",
        "phoneNumbers",
        {
            "recipientsSourceType": "PhoneNumbers",
            "phoneNumbers": ["+37060000000"],
            "campaignTime": CAMPAIGN_TIME,
        },
    ),
]

# The `Settings` switch arms in gateway Hub.Sms/Campaigns/Create.cs — exactly these five.
# AccountUsers = the account owner and team members by id (members without a phone are skipped).
GATEWAY_AUDIENCES = {"allusers", "specifiedusers", "accountusers", "collection", "phonenumbers"}


@pytest.mark.parametrize(
    ("delivery_type", "settings_key", "settings"),
    CAMPAIGN_AUDIENCES,
    ids=[case[0] for case in CAMPAIGN_AUDIENCES],
)
def test_create_sms_campaign_sends_the_audience_shape(
    delivery_type: str, settings_key: str, settings: dict[str, Any]
) -> None:
    client, transport = make_client()
    client.hub.notifications.create_sms_campaign(
        templateId=TEMPLATE_ID,
        deliveryType=delivery_type,
        **{settings_key: settings},
    )

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    body = json.loads(transport.last_request["body"])
    # The audience name has to reach the wire as the name, not a number, and
    # the settings object has to sit under the key the gateway reads.
    assert body == {
        "templateId": TEMPLATE_ID,
        "deliveryType": delivery_type,
        settings_key: settings,
    }


def test_campaign_audiences_match_the_gateway() -> None:
    assert {delivery_type.lower() for delivery_type, _, _ in CAMPAIGN_AUDIENCES} == GATEWAY_AUDIENCES
    assert len(CAMPAIGN_AUDIENCES) == len(GATEWAY_AUDIENCES)


def test_create_sms_campaign_sends_the_provider_integration_id_top_level() -> None:
    # The gateway requires the SMS provider id as a top-level `integrationId`.
    # It is a different field from `databaseIntegrationId` (the database that
    # holds a `Collection` audience), so both must reach the wire side by side.
    client, transport = make_client()
    client.hub.notifications.create_sms_campaign(
        templateId=TEMPLATE_ID,
        integrationId=INTEGRATION_ID,
        databaseIntegrationId="db_1",
        deliveryType="Collection",
        collectionSettings={"schemaName": "subscribers", "fields": ["phone"], "campaignTime": CAMPAIGN_TIME},
    )

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert urlparse(transport.last_request["url"]).path == f"{BASE}/campaigns"
    body = json.loads(transport.last_request["body"])
    assert body == {
        "templateId": TEMPLATE_ID,
        "integrationId": INTEGRATION_ID,
        "databaseIntegrationId": "db_1",
        "deliveryType": "Collection",
        "collectionSettings": {"schemaName": "subscribers", "fields": ["phone"], "campaignTime": CAMPAIGN_TIME},
    }


# The eight providers the gateway's save converter accepts, with the fields
# each one validates. Source of truth: gateway Hub.Sms/Integrations/Save_.cs
# (the switch arms of the converter, read from `provider`) and
# Save.<Provider>.cs (the `required` fields of each record).
#
# Every value is a dummy; nothing here leaves the process.
SMS_PROVIDERS: list[tuple[str, dict[str, Any]]] = [
    ("Fake", {}),
    (
        "Twilio",
        {"accountSid": "AC000", "fromPhoneNumber": "+15550000001", "authToken": "token"},
    ),
    (
        "Vonage",
        {"apiKey": "key", "fromSender": "Norbix", "apiSecret": "secret"},
    ),
    (
        "Plivo",
        {"authId": "MA000", "fromPhoneNumber": "+15550000002", "authToken": "token"},
    ),
    (
        "Telnyx",
        {"messagingProfileId": "mp_1", "fromPhoneNumber": "+15550000003", "apiKey": "key"},
    ),
    (
        "Bird",
        {"originator": "Norbix", "region": "eu", "apiKey": "key"},
    ),
    (
        "Telesign",
        {"customerId": "cust_1", "fromSender": "Norbix", "apiKey": "key"},
    ),
    (
        "Sinch",
        {
            "servicePlanId": "plan_1",
            "fromPhoneNumber": "+15550000004",
            "apiKey": "key",
            "apiSecret": "secret",
        },
    ),
]

# SmsProvider in the gateway — exactly these eight.
GATEWAY_PROVIDERS = {"Fake", "Twilio", "Vonage", "Plivo", "Telnyx", "Bird", "Telesign", "Sinch"}


@pytest.mark.parametrize(
    ("provider", "fields"),
    SMS_PROVIDERS,
    ids=[case[0] for case in SMS_PROVIDERS],
)
def test_save_sms_integration_sends_the_provider_shape(
    provider: str, fields: dict[str, Any]
) -> None:
    client, transport = make_client()
    integration = {
        "provider": provider,
        "integrationName": f"sms-sdk-py {provider}",
        "isEnabled": True,
        **fields,
    }
    client.hub.notifications.save_sms_integration(integration=integration)

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert json.loads(transport.last_request["body"])["integration"] == integration


def test_sms_providers_match_the_gateway() -> None:
    assert {provider for provider, _ in SMS_PROVIDERS} == GATEWAY_PROVIDERS
    assert len(SMS_PROVIDERS) == len(GATEWAY_PROVIDERS)


def test_fake_provider_needs_only_its_name() -> None:
    """`integrationName` is optional on save; the Fake sandbox takes no field at all.

    Source of truth: gateway Hub.Sms/Integrations/Save.Fake.cs — a client posts
    `{ "integration": { "provider": "Fake" } }` and the server builds the rest.
    """
    client, transport = make_client()
    client.hub.notifications.save_sms_integration(integration={"provider": "Fake"})

    assert transport.last_request is not None
    assert json.loads(transport.last_request["body"]) == {"integration": {"provider": "Fake"}}


def test_render_sms_sends_code_tokens_and_the_preview_flag() -> None:
    """Gateway RenderSms reads `code`, `tokens` (key/value pairs) and `isForPreview`."""
    client, transport = make_client()
    client.hub.notifications.render_sms(
        code="Hi @Model.FirstName",
        tokens=[{"key": "FirstName", "value": "Ada"}],
        isForPreview=True,
    )

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert urlparse(transport.last_request["url"]).path == f"{BASE}/templates/render"
    assert json.loads(transport.last_request["body"]) == {
        "code": "Hi @Model.FirstName",
        "tokens": [{"key": "FirstName", "value": "Ada"}],
        "isForPreview": True,
    }


def test_stop_sms_campaign_fills_the_route_token_and_sends_no_body() -> None:
    client, transport = make_client()
    client.hub.notifications.stop_sms_campaign(id=CAMPAIGN_ID)

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert urlparse(transport.last_request["url"]).path == f"{BASE}/campaigns/{CAMPAIGN_ID}/stop"
    assert transport.last_request["body"] == ""


def test_get_sms_campaigns_sends_its_filters_as_query_values() -> None:
    client, transport = make_client()
    client.hub.notifications.get_sms_campaigns(templateId=TEMPLATE_ID, pageSize=10, pageNumber=0)

    assert transport.last_request is not None
    url = urlparse(transport.last_request["url"])
    assert url.path == f"{BASE}/campaigns"
    assert parse_qs(url.query) == {
        "templateId": [TEMPLATE_ID],
        "pageSize": ["10"],
        "pageNumber": ["0"],
    }


def test_get_sms_campaigns_sends_the_campaign_id_filter() -> None:
    # The gateway returns only the campaign with this id.
    client, transport = make_client()
    client.hub.notifications.get_sms_campaigns(campaignId=CAMPAIGN_ID, pageSize=10)

    assert transport.last_request is not None
    url = urlparse(transport.last_request["url"])
    assert url.path == f"{BASE}/campaigns"
    assert parse_qs(url.query) == {"campaignId": [CAMPAIGN_ID], "pageSize": ["10"]}


def test_async_module_exposes_the_same_sms_surface() -> None:
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
            module = client.hub.notifications
            for name, _, _, _ in SMS_CASES:
                assert inspect.iscoroutinefunction(getattr(module, name)), name
            await module.stop_sms_campaign(id=CAMPAIGN_ID)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [
        ("POST", f"{BASE}/campaigns/{CAMPAIGN_ID}/stop"),
    ]
