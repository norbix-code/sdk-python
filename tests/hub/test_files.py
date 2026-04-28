from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_files_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.files
    assert callable(module.disable_files)
    assert callable(module.enable_files)
    assert callable(module.delete_files_trigger)
    assert callable(module.disable_files_trigger)
    assert callable(module.enable_files_trigger)
    assert callable(module.get_files_trigger)
    assert callable(module.get_files_triggers)
    assert callable(module.save_files_trigger)
    assert callable(module.delete_files_integration)
    assert callable(module.disable_files_integration)
    assert callable(module.enable_files_integration)
    assert callable(module.get_files_integration)
    assert callable(module.get_files_integrations)
    assert callable(module.save_files_integration)
    assert callable(module.set_files_integration_as_default)


def test_hub_files_disable_files_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.disable_files()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_enable_files_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.enable_files()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_delete_files_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.delete_files_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_disable_files_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.disable_files_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_enable_files_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.enable_files_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_get_files_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.get_files_trigger(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_get_files_triggers_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.get_files_triggers()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_save_files_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.save_files_trigger()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_delete_files_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.delete_files_integration(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_disable_files_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.disable_files_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_enable_files_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.enable_files_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_get_files_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.get_files_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_get_files_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.get_files_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_save_files_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.save_files_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_set_files_integration_as_default_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.files.set_files_integration_as_default(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
