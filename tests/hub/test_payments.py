from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_payments_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.payments
    assert callable(module.disable_payments)
    assert callable(module.enable_payments)
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
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_enable_payments_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.enable_payments()
    assert transport.last_request['method'] == 'GET'
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

def test_hub_payments_test_payments_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.payments.test_payments_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
