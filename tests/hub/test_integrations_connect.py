"""Quick connect (one-click OAuth) of a payments integration.

The five routes of Hub.Payments/Integrations/Connect/QuickConnect.cs a program
calls: the shared providers and targets reads on ``hub.integrations`` and
start / complete / disconnect on ``hub.payments``. A fake httpx transport only:
no gateway and no provider are contacted.
"""

from __future__ import annotations

import asyncio
import json
from urllib.parse import parse_qs, urlparse

import httpx

from norbix_python import AsyncNorbix

from ..helpers import make_client

CONNECT = "qc_1"
ID = "int_1"


def _sent(transport):  # type: ignore[no-untyped-def]
    sent = transport.last_request
    assert sent is not None
    url = urlparse(sent["url"])
    body = json.loads(sent["body"]) if sent["body"] else None
    return sent["method"], url.path, parse_qs(url.query), body


def test_get_quick_connect_providers_sends_the_module_filter_in_the_query() -> None:
    client, transport = make_client()
    client.hub.integrations.get_quick_connect_providers(module="payments")
    assert _sent(transport) == ("GET", "/v3/integrations/connect/providers", {"module": ["payments"]}, None)


def test_get_quick_connect_providers_without_a_filter_sends_no_query() -> None:
    client, transport = make_client()
    client.hub.integrations.get_quick_connect_providers()
    assert _sent(transport) == ("GET", "/v3/integrations/connect/providers", {}, None)


def test_get_integration_connect_targets_puts_the_connect_id_in_the_path() -> None:
    client, transport = make_client()
    client.hub.integrations.get_integration_connect_targets(CONNECT)
    assert _sent(transport) == ("GET", f"/v3/integrations/connect/{CONNECT}/targets", {}, None)


def test_start_payments_integration_connect_sends_the_request_in_the_body() -> None:
    client, transport = make_client()
    client.hub.payments.start_payments_integration_connect(
        provider="woocommerce",
        integrationName="Shop",
        mode="test",
        input={"storeUrl": "https://shop.example.com"},
        integrationId=ID,
    )
    method, path, query, body = _sent(transport)
    assert (method, path, query) == ("POST", "/v3/payments/integrations/connect/start", {})
    assert body == {
        "provider": "woocommerce",
        "integrationName": "Shop",
        "mode": "test",
        "input": {"storeUrl": "https://shop.example.com"},
        "integrationId": ID,
    }


def test_complete_payments_integration_connect_puts_the_connect_id_in_the_path_and_the_target_in_the_body() -> None:
    client, transport = make_client()
    client.hub.payments.complete_payments_integration_connect(CONNECT, targetId="shop_42", isEnabled=True)
    assert _sent(transport) == (
        "POST",
        f"/v3/payments/integrations/connect/{CONNECT}/complete",
        {},
        {"targetId": "shop_42", "isEnabled": True},
    )


def test_disconnect_payments_integration_connect_puts_the_id_in_the_path() -> None:
    client, transport = make_client()
    client.hub.payments.disconnect_payments_integration_connect(ID)
    method, path, query, _ = _sent(transport)
    assert (method, path, query) == ("POST", f"/v3/payments/integrations/{ID}/connect/disconnect", {})


def test_async_quick_connect_hits_the_same_routes_and_returns_the_answers() -> None:
    seen: list[httpx.Request] = []
    answers = iter(
        [
            {"providers": [{"module": "payments", "provider": "woocommerce", "available": True}]},
            {"authorizeUrl": "https://shop.example.com/wc-auth", "connectId": CONNECT},
            {"connectId": CONNECT, "targets": [{"id": "shop_42", "name": "Main shop"}]},
            {"id": "int_new"},
            {"wasConnected": True, "providerAnswered": False},
        ]
    )

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json=next(answers))

    async def run() -> list[object]:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        try:
            providers = await client.hub.integrations.get_quick_connect_providers(module="payments")
            started = await client.hub.payments.start_payments_integration_connect(
                provider="woocommerce", integrationName="Shop"
            )
            targets = await client.hub.integrations.get_integration_connect_targets(started["connectId"])
            saved = await client.hub.payments.complete_payments_integration_connect(
                started["connectId"], targetId=targets["targets"][0]["id"], isEnabled=True
            )
            ended = await client.hub.payments.disconnect_payments_integration_connect(saved["id"])
            return [providers, started, targets, saved, ended]
        finally:
            await client.aclose()

    providers, started, targets, saved, ended = asyncio.run(run())
    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [
        ("GET", "/v3/integrations/connect/providers"),
        ("POST", "/v3/payments/integrations/connect/start"),
        ("GET", f"/v3/integrations/connect/{CONNECT}/targets"),
        ("POST", f"/v3/payments/integrations/connect/{CONNECT}/complete"),
        ("POST", "/v3/payments/integrations/int_new/connect/disconnect"),
    ]
    assert providers["providers"][0]["provider"] == "woocommerce"
    assert started["connectId"] == CONNECT
    assert targets["targets"][0]["id"] == "shop_42"
    assert saved == {"id": "int_new"}
    assert ended == {"wasConnected": True, "providerAnswered": False}
