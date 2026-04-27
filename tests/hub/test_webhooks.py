from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_hub_webhooks_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.webhooks
    assert callable(module.getWebhookIntegration)
    assert callable(module.revealWebhookIntegrationSecret)
    assert callable(module.rotateWebhookIntegrationSecret)
    assert callable(module.updateWebhookIntegrationExtraHeaders)
    assert callable(module.disableWebhookDestination)
    assert callable(module.enableWebhookDestination)
    assert callable(module.removeWebhookDestination)
    assert callable(module.saveWebhookDestination)


def test_hub_webhooks_getWebhookIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/webhooks/integration') if False else {}
    client.hub.webhooks.getWebhookIntegration(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_revealWebhookIntegrationSecret_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/webhooks/integration/secret') if False else {}
    client.hub.webhooks.revealWebhookIntegrationSecret(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_rotateWebhookIntegrationSecret_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/webhooks/integration/secret/rotate') if False else {}
    client.hub.webhooks.rotateWebhookIntegrationSecret(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_updateWebhookIntegrationExtraHeaders_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/webhooks/integration/extra-headers') if False else {}
    client.hub.webhooks.updateWebhookIntegrationExtraHeaders(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_disableWebhookDestination_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/webhooks/destinations/{DestinationId}/disable') if True else {}
    client.hub.webhooks.disableWebhookDestination(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_enableWebhookDestination_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/webhooks/destinations/{DestinationId}/enable') if True else {}
    client.hub.webhooks.enableWebhookDestination(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_removeWebhookDestination_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/webhooks/destinations/{DestinationId}') if True else {}
    client.hub.webhooks.removeWebhookDestination(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_saveWebhookDestination_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/webhooks/destinations') if False else {}
    client.hub.webhooks.saveWebhookDestination(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
