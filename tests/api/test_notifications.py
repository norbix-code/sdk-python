from __future__ import annotations

import asyncio
import inspect
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, NorbixApi

from ..helpers import make_client

"""Notifications on the Api: campaigns (Email, SMS, Push) and the signed-in
user's own push devices and messages.

Every one of the 44 routes is pinned by verb and fully-resolved path, and the
writes by the body (or query, for a DELETE) that reaches the wire. The route
set and the method names mirror the TypeScript Api module. Every call goes to
a capture transport, so nothing leaves the process.
"""

CAMPAIGN_ID = "camp_1"
BATCH_ID = "batch_1"
NOTIFICATION_ID = "notif_1"
TEMPLATE_ID = "tpl_1"
INTEGRATION_ID = "int_1"
DEVICE_ID = "pnd_1"
MESSAGE_ID = "ntf_1"
HASH = "signed-link-abc"

API = "/v3/notifications"

# name, verb, expected path, call
Case = tuple[str, str, str, Callable[[Any], Any]]


def _campaign_cases(channel: str, *, plural_messages: bool = False) -> list[Case]:
    """The 12 campaign routes of one channel. The gateway spells the id token
    ``{Id}`` on DELETE / stop / retry and ``{id}`` on the GETs; the resolved
    path is the same either way. Email's messages route lives under the plural
    ``/notifications/emails/``."""
    base = f"{API}/{channel}"
    messages_base = f"{API}/{channel}s" if plural_messages else base
    return [
        (f"create_{channel}_campaign", "POST", f"{base}/campaigns", lambda m: getattr(m, f"create_{channel}_campaign")()),
        (f"delete_{channel}_campaign", "DELETE", f"{base}/campaigns/{CAMPAIGN_ID}", lambda m: getattr(m, f"delete_{channel}_campaign")(CAMPAIGN_ID)),
        (f"get_{channel}_campaign", "GET", f"{base}/campaigns/{CAMPAIGN_ID}", lambda m: getattr(m, f"get_{channel}_campaign")(CAMPAIGN_ID)),
        (f"get_{channel}_campaigns", "GET", f"{base}/campaigns", lambda m: getattr(m, f"get_{channel}_campaigns")()),
        (f"get_{channel}_campaign_batches", "GET", f"{base}/campaigns/{CAMPAIGN_ID}/batches", lambda m: getattr(m, f"get_{channel}_campaign_batches")(CAMPAIGN_ID)),
        (
            f"get_{channel}_campaign_batch_notification",
            "GET",
            f"{base}/campaigns/{CAMPAIGN_ID}/batches/{BATCH_ID}/{NOTIFICATION_ID}",
            lambda m: getattr(m, f"get_{channel}_campaign_batch_notification")(CAMPAIGN_ID, BATCH_ID, NOTIFICATION_ID),
        ),
        (
            f"get_{channel}_campaign_batch_notifications",
            "GET",
            f"{base}/campaigns/{CAMPAIGN_ID}/batches/{BATCH_ID}",
            lambda m: getattr(m, f"get_{channel}_campaign_batch_notifications")(CAMPAIGN_ID, BATCH_ID),
        ),
        (f"get_{channel}_campaign_statistics", "GET", f"{base}/campaigns/{CAMPAIGN_ID}/stats", lambda m: getattr(m, f"get_{channel}_campaign_statistics")(CAMPAIGN_ID)),
        (f"preview_{channel}_notification", "GET", f"{base}/preview", lambda m: getattr(m, f"preview_{channel}_notification")(hash=HASH)),
        (
            f"retry_failed_{channel}_notifications",
            "POST",
            f"{base}/campaigns/{CAMPAIGN_ID}/retry-failed",
            lambda m: getattr(m, f"retry_failed_{channel}_notifications")(CAMPAIGN_ID, idempotency_key="retry-1"),
        ),
        (f"stop_{channel}_campaign", "POST", f"{base}/campaigns/{CAMPAIGN_ID}/stop", lambda m: getattr(m, f"stop_{channel}_campaign")(CAMPAIGN_ID)),
        (
            f"get_{channel}_campaign_messages",
            "GET",
            f"{messages_base}/campaigns/{CAMPAIGN_ID}/messages",
            lambda m: getattr(m, f"get_{channel}_campaign_messages")(CAMPAIGN_ID, campaignBatchId=BATCH_ID),
        ),
    ]


EMAIL_CASES: list[Case] = _campaign_cases("email", plural_messages=True)

SMS_CASES: list[Case] = _campaign_cases("sms")

PUSH_CASES: list[Case] = _campaign_cases("push") + [
    ("get_push_campaign_audience_count", "POST", f"{API}/push/campaigns/audience-count", lambda m: m.get_push_campaign_audience_count()),
    # own devices and messages — end-user routes, always the caller's own rows
    ("register_own_push_device", "POST", f"{API}/push/devices", lambda m: m.register_own_push_device(provider="fcm", token="tok_1")),
    ("get_own_push_devices", "GET", f"{API}/push/devices", lambda m: m.get_own_push_devices()),
    ("delete_own_push_device", "DELETE", f"{API}/push/devices/{DEVICE_ID}", lambda m: m.delete_own_push_device(DEVICE_ID)),
    ("delete_own_push_device_by_token", "DELETE", f"{API}/push/devices", lambda m: m.delete_own_push_device_by_token(token="tok_1")),
    ("get_own_push_messages", "GET", f"{API}/push/messages", lambda m: m.get_own_push_messages()),
    ("mark_own_push_message_read", "POST", f"{API}/push/messages/{MESSAGE_ID}/read", lambda m: m.mark_own_push_message_read(MESSAGE_ID)),
    ("mark_all_own_push_messages_read", "POST", f"{API}/push/messages/read", lambda m: m.mark_all_own_push_messages_read()),
]

ALL_CASES: list[Case] = EMAIL_CASES + SMS_CASES + PUSH_CASES


@pytest.mark.parametrize(("name", "verb", "path", "call"), ALL_CASES, ids=[case[0] for case in ALL_CASES])
def test_api_notifications_endpoint_hits_the_expected_route(
    name: str, verb: str, path: str, call: Callable[[Any], Any]
) -> None:
    # The client carries an account id; project-scoped routes ignore it.
    client, transport = make_client(account_id="acct_1")
    call(client.api.notifications)

    assert transport.last_request is not None
    assert transport.last_request["method"] == verb
    assert urlparse(transport.last_request["url"]).path == path, (
        f"{name}: got {transport.last_request['url']}, expected the path {path}"
    )
    assert transport.last_request["url"].startswith("https://api.")


def test_api_notifications_surface_size() -> None:
    """12 Email, 12 SMS and 20 Push routes — 44, as the TypeScript Api module.
    A new route changes a count here, so it cannot arrive untested."""
    assert len(EMAIL_CASES) == 12
    assert len(SMS_CASES) == 12
    assert len(PUSH_CASES) == 20
    assert len({case[0] for case in ALL_CASES}) == 44


def test_api_notifications_call_sends_auth_and_project_headers() -> None:
    client, transport = make_client()
    client.api.notifications.get_own_push_devices()

    assert transport.last_request is not None
    headers = transport.last_request["headers"]
    assert headers["authorization"] == "Bearer test-token"
    assert headers["norbix-project-id"] == "test-project"


def test_api_split_client_has_the_notifications_module() -> None:
    api = NorbixApi(project_id="p1", api_key="k1")
    try:
        assert callable(api.notifications.create_email_campaign)
        assert callable(api.notifications.register_own_push_device)
    finally:
        api.close()


# ---------------------------------------------------------------- campaigns


def test_create_email_campaign_sends_the_campaign_wrapper() -> None:
    # Same gateway service as the Hub: the campaign sits under `campaign`,
    # `databaseIntegrationId` and `sendNow` next to it.
    client, transport = make_client()
    client.api.notifications.create_email_campaign(
        campaign={"templateId": TEMPLATE_ID, "integrationId": INTEGRATION_ID, "source": "allUsers"},
        databaseIntegrationId="db_1",
        sendNow=True,
    )

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert json.loads(transport.last_request["body"]) == {
        "campaign": {"templateId": TEMPLATE_ID, "integrationId": INTEGRATION_ID, "source": "allUsers"},
        "databaseIntegrationId": "db_1",
        "sendNow": True,
    }


def test_create_push_campaign_sends_the_campaign_wrapper() -> None:
    client, transport = make_client()
    client.api.notifications.create_push_campaign(
        campaign={"source": "devices", "templateId": TEMPLATE_ID, "integrationId": INTEGRATION_ID, "devices": [{"token": "tok_1", "deliveryFamily": "Ios"}]},
    )

    assert transport.last_request is not None
    assert json.loads(transport.last_request["body"]) == {
        "campaign": {"source": "devices", "templateId": TEMPLATE_ID, "integrationId": INTEGRATION_ID, "devices": [{"token": "tok_1", "deliveryFamily": "Ios"}]},
    }


def test_create_sms_campaign_is_flat_with_the_provider_id_top_level() -> None:
    # SMS has no `campaign` wrapper: `deliveryType` picks the settings key, and
    # the provider `integrationId` sits next to (not inside) `databaseIntegrationId`.
    client, transport = make_client()
    client.api.notifications.create_sms_campaign(
        templateId=TEMPLATE_ID,
        integrationId=INTEGRATION_ID,
        databaseIntegrationId="db_1",
        deliveryType="PhoneNumbers",
        phoneNumbers={"recipientsSourceType": "PhoneNumbers", "phoneNumbers": ["+37060000000"]},
    )

    assert transport.last_request is not None
    assert json.loads(transport.last_request["body"]) == {
        "templateId": TEMPLATE_ID,
        "integrationId": INTEGRATION_ID,
        "databaseIntegrationId": "db_1",
        "deliveryType": "PhoneNumbers",
        "phoneNumbers": {"recipientsSourceType": "PhoneNumbers", "phoneNumbers": ["+37060000000"]},
    }


def test_get_push_campaign_audience_count_sends_the_audience_under_campaign() -> None:
    client, transport = make_client()
    client.api.notifications.get_push_campaign_audience_count(
        campaign={"source": "allUsers", "userTags": ["beta"]},
        databaseIntegrationId="db_1",
    )

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert json.loads(transport.last_request["body"]) == {
        "campaign": {"source": "allUsers", "userTags": ["beta"]},
        "databaseIntegrationId": "db_1",
    }


@pytest.mark.parametrize("channel", ["email", "sms", "push"])
def test_stop_campaign_fills_the_route_token_and_sends_no_body(channel: str) -> None:
    client, transport = make_client()
    getattr(client.api.notifications, f"stop_{channel}_campaign")(CAMPAIGN_ID)

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert urlparse(transport.last_request["url"]).path == f"{API}/{channel}/campaigns/{CAMPAIGN_ID}/stop"
    assert transport.last_request["body"] == ""


@pytest.mark.parametrize("channel", ["email", "sms", "push"])
def test_retry_failed_sends_only_the_key_when_nothing_else_is_set(channel: str) -> None:
    client, transport = make_client()
    getattr(client.api.notifications, f"retry_failed_{channel}_notifications")(CAMPAIGN_ID, idempotency_key="retry-1")

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert urlparse(transport.last_request["url"]).path == f"{API}/{channel}/campaigns/{CAMPAIGN_ID}/retry-failed"
    assert json.loads(transport.last_request["body"]) == {"idempotencyKey": "retry-1"}


@pytest.mark.parametrize("channel", ["email", "sms", "push"])
def test_retry_failed_sends_every_option_under_its_wire_name(channel: str) -> None:
    client, transport = make_client()
    getattr(client.api.notifications, f"retry_failed_{channel}_notifications")(
        CAMPAIGN_ID,
        idempotency_key="retry-1",
        notification_ids=[NOTIFICATION_ID],
        include_ambiguous=False,
        categories=["Transient"],
        database_integration_id="db_1",
    )

    assert transport.last_request is not None
    assert json.loads(transport.last_request["body"]) == {
        "idempotencyKey": "retry-1",
        "notificationIds": [NOTIFICATION_ID],
        "includeAmbiguous": False,
        "categories": ["Transient"],
        "databaseIntegrationId": "db_1",
    }


@pytest.mark.parametrize("channel", ["email", "sms", "push"])
def test_get_campaigns_sends_its_filters_as_query_values(channel: str) -> None:
    client, transport = make_client()
    getattr(client.api.notifications, f"get_{channel}_campaigns")(templateId=TEMPLATE_ID, pageSize=10, pageNumber=0)

    assert transport.last_request is not None
    url = urlparse(transport.last_request["url"])
    assert url.path == f"{API}/{channel}/campaigns"
    assert parse_qs(url.query) == {"templateId": [TEMPLATE_ID], "pageSize": ["10"], "pageNumber": ["0"]}


def test_get_email_campaign_messages_uses_the_plural_route_and_the_batch_query() -> None:
    # The gateway requires `campaignBatchId` for the messages of a campaign.
    client, transport = make_client()
    client.api.notifications.get_email_campaign_messages(CAMPAIGN_ID, campaignBatchId=BATCH_ID, pageSize=20)

    assert transport.last_request is not None
    url = urlparse(transport.last_request["url"])
    assert url.path == f"{API}/emails/campaigns/{CAMPAIGN_ID}/messages"
    assert parse_qs(url.query) == {"campaignBatchId": [BATCH_ID], "pageSize": ["20"]}


# ---------------------------------------------------------------- preview (signed link)


@pytest.fixture
def _no_env_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("NORBIX_API_KEY", raising=False)
    monkeypatch.delenv("NORBIX_BEARER_TOKEN", raising=False)


@pytest.mark.usefixtures("_no_env_credentials")
@pytest.mark.parametrize("channel", ["email", "sms", "push"])
def test_preview_with_signed_link_needs_no_sign_in(channel: str) -> None:
    # The hash is the key: a client with no API key and no bearer token still
    # sends the request, with no Authorization header.
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    client = Norbix(project_id="test-project", http_client=httpx.Client(transport=httpx.MockTransport(handler)))
    getattr(client.api.notifications, f"preview_{channel}_notification")(hash=HASH)

    assert len(seen) == 1
    url = urlparse(str(seen[0].url))
    assert seen[0].method == "GET"
    assert url.path == f"{API}/{channel}/preview"
    assert parse_qs(url.query) == {"hash": [HASH]}
    assert "Authorization" not in seen[0].headers


# ---------------------------------------------------------------- own push


def test_register_own_push_device_sends_the_provider_and_the_token() -> None:
    # gateway Api.Notifications/OwnPush.cs: `provider` (fcm | apns) and `token`
    # are required; the rest describes the device.
    client, transport = make_client()
    client.api.notifications.register_own_push_device(
        provider="apns",
        token="tok_1",
        platform="ios",
        osName="iOS",
        osVersion="18.1",
        appVersion="2.4.1",
        deviceName="Anna's iPhone",
        modelName="iPhone 15",
        installationId="inst_1",
        locale="lt-LT",
        timeZone="Europe/Vilnius",
    )

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert urlparse(transport.last_request["url"]).path == f"{API}/push/devices"
    assert json.loads(transport.last_request["body"]) == {
        "provider": "apns",
        "token": "tok_1",
        "platform": "ios",
        "osName": "iOS",
        "osVersion": "18.1",
        "appVersion": "2.4.1",
        "deviceName": "Anna's iPhone",
        "modelName": "iPhone 15",
        "installationId": "inst_1",
        "locale": "lt-LT",
        "timeZone": "Europe/Vilnius",
    }


def test_delete_own_push_device_by_token_sends_the_token_as_a_query_value() -> None:
    # A DELETE carries no body in this SDK: the token travels in the query, on
    # the collection path (no id).
    client, transport = make_client()
    client.api.notifications.delete_own_push_device_by_token(token="tok_1")

    assert transport.last_request is not None
    assert transport.last_request["method"] == "DELETE"
    url = urlparse(transport.last_request["url"])
    assert url.path == f"{API}/push/devices"
    assert parse_qs(url.query) == {"token": ["tok_1"]}
    assert transport.last_request["body"] == ""


def test_delete_own_push_device_fills_the_route_token() -> None:
    client, transport = make_client()
    client.api.notifications.delete_own_push_device(DEVICE_ID)

    assert transport.last_request is not None
    assert transport.last_request["method"] == "DELETE"
    url = urlparse(transport.last_request["url"])
    assert url.path == f"{API}/push/devices/{DEVICE_ID}"
    assert url.query == ""


def test_get_own_push_messages_sends_unread_only_and_paging_as_query_values() -> None:
    client, transport = make_client()
    client.api.notifications.get_own_push_messages(unreadOnly=True, pageSize=20, pageNumber=0)

    assert transport.last_request is not None
    url = urlparse(transport.last_request["url"])
    assert url.path == f"{API}/push/messages"
    assert parse_qs(url.query) == {"unreadOnly": ["true"], "pageSize": ["20"], "pageNumber": ["0"]}


@pytest.mark.parametrize(
    ("name", "path", "call"),
    [
        ("mark_own_push_message_read", f"{API}/push/messages/{MESSAGE_ID}/read", lambda m: m.mark_own_push_message_read(MESSAGE_ID)),
        ("mark_all_own_push_messages_read", f"{API}/push/messages/read", lambda m: m.mark_all_own_push_messages_read()),
    ],
    ids=["one", "all"],
)
def test_mark_read_posts_with_no_body(name: str, path: str, call: Callable[[Any], Any]) -> None:
    client, transport = make_client()
    call(client.api.notifications)

    assert transport.last_request is not None
    assert transport.last_request["method"] == "POST"
    assert urlparse(transport.last_request["url"]).path == path
    assert transport.last_request["body"] == ""


# ---------------------------------------------------------------- async twin


def test_async_module_exposes_the_same_notifications_surface() -> None:
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
            module = client.api.notifications
            for name, _, _, _ in ALL_CASES:
                assert inspect.iscoroutinefunction(getattr(module, name)), name
            await module.register_own_push_device(provider="fcm", token="tok_1")
            await module.stop_push_campaign(CAMPAIGN_ID)
            await module.retry_failed_email_notifications(CAMPAIGN_ID, idempotency_key="retry-1")
            await module.delete_own_push_device_by_token(token="tok_1")
        finally:
            await client.aclose()

    asyncio.run(run())

    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [
        ("POST", f"{API}/push/devices"),
        ("POST", f"{API}/push/campaigns/{CAMPAIGN_ID}/stop"),
        ("POST", f"{API}/email/campaigns/{CAMPAIGN_ID}/retry-failed"),
        ("DELETE", f"{API}/push/devices"),
    ]
    assert json.loads(seen[0].content) == {"provider": "fcm", "token": "tok_1"}
    assert json.loads(seen[2].content) == {"idempotencyKey": "retry-1"}
    assert parse_qs(urlparse(str(seen[3].url)).query) == {"token": ["tok_1"]}
