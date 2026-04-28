from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_webhooks_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.webhooks
    assert callable(module.get_webhook_integration)
    assert callable(module.reveal_webhook_integration_secret)
    assert callable(module.rotate_webhook_integration_secret)
    assert callable(module.update_webhook_integration_extra_headers)
    assert callable(module.disable_webhook_destination)
    assert callable(module.enable_webhook_destination)
    assert callable(module.remove_webhook_destination)
    assert callable(module.save_webhook_destination)


def test_hub_webhooks_get_webhook_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.webhooks.get_webhook_integration({})
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_reveal_webhook_integration_secret_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.webhooks.reveal_webhook_integration_secret({})
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_rotate_webhook_integration_secret_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.webhooks.rotate_webhook_integration_secret({})
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_update_webhook_integration_extra_headers_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.webhooks.update_webhook_integration_extra_headers({})
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_disable_webhook_destination_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.webhooks.disable_webhook_destination(destination_id="stub-DestinationId")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_enable_webhook_destination_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.webhooks.enable_webhook_destination(destination_id="stub-DestinationId")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_remove_webhook_destination_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.webhooks.remove_webhook_destination(destination_id="stub-DestinationId")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_webhooks_save_webhook_destination_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.webhooks.save_webhook_destination({})
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
