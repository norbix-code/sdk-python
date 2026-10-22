from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_payments_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.payments
    assert callable(module.disable_payments)
    assert callable(module.enable_payments)
    assert callable(module.get_payments_webhook_log)
    assert callable(module.delete_payments_trigger)
    assert callable(module.disable_payments_trigger)
    assert callable(module.enable_payments_trigger)
    assert callable(module.get_payments_trigger)
    assert callable(module.get_payments_triggers)
    assert callable(module.save_payments_trigger)
    assert callable(module.confirm_payments_integration_human_delivery)
    assert callable(module.delete_payments_integration)
    assert callable(module.disable_payments_integration)
    assert callable(module.enable_payments_integration)
    assert callable(module.get_payments_integration)
    assert callable(module.get_payments_integrations)
    assert callable(module.save_payments_integration)
    assert callable(module.test_payments_integration)


def test_hub_payments_disable_payments_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.disable_payments()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_enable_payments_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.enable_payments()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_delete_payments_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.delete_payments_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_disable_payments_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.disable_payments_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_enable_payments_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.enable_payments_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_get_payments_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.get_payments_trigger(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_get_payments_triggers_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.get_payments_triggers()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_save_payments_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.save_payments_trigger()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_confirm_payments_integration_human_delivery_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.confirm_payments_integration_human_delivery()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_delete_payments_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.delete_payments_integration(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_disable_payments_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.disable_payments_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_enable_payments_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.enable_payments_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_get_payments_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.get_payments_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_get_payments_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.get_payments_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_save_payments_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.save_payments_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_save_montonio_integration_leaves_out_unset_is_sandbox() -> None:
    # Owner 2026-10-22: isSandbox is optional; empty = true (sandbox) on the gateway.
    # The SDK must not fill in a default, or an unset field would become live mode.
    import json

    client, transport = make_client(account_id=None)
    client.hub.payments.save_payments_integration(
        integration={"provider": "Montonio", "accessKey": "ak_test", "secretKey": "sk_test"},
    )
    assert transport.last_request is not None
    body = json.loads(transport.last_request['body'])
    assert body == {"integration": {"provider": "Montonio", "accessKey": "ak_test", "secretKey": "sk_test"}}
    assert "isSandbox" not in body["integration"]

def test_hub_payments_test_payments_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.test_payments_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_payments_get_payments_webhook_log_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.get_payments_webhook_log(integration_id="int_stripe", limit=20)
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert '/payments/webhooks/log' in transport.last_request['url']
    assert 'integration_id=int_stripe' in transport.last_request['url'] or 'integrationId=int_stripe' in transport.last_request['url']


def test_async_hub_payments_get_payments_webhook_log_hits_the_route() -> None:
    import asyncio
    from urllib.parse import parse_qs, urlparse

    import httpx

    from norbix_python import AsyncNorbix

    seen: list[httpx.Request] = []
    log = {"list": [{"integrationId": "int_stripe", "eventName": "payment_intent.succeeded", "statusCode": 200}]}

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json=log)

    async def run() -> object:
        client = AsyncNorbix(
            project_id='test-project',
            bearer_token='test-token',
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        try:
            return await client.hub.payments.get_payments_webhook_log(integration_id="int_stripe", limit=20)
        finally:
            await client.aclose()

    assert asyncio.run(run()) == log
    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [('GET', '/v3/payments/webhooks/log')]
    assert parse_qs(urlparse(str(seen[0].url)).query).get('limit') == ['20']
