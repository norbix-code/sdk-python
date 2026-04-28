from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_logs_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.logs
    assert callable(module.disable_logging)
    assert callable(module.enable_logging)
    assert callable(module.delete_logging_integration)
    assert callable(module.disable_logging_integration)
    assert callable(module.enable_logging_integration)
    assert callable(module.get_logging_integration)
    assert callable(module.get_logging_integrations)
    assert callable(module.save_logging_integration)
    assert callable(module.test_logging_integration)


def test_hub_logs_disable_logging_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.disable_logging()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_enable_logging_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.enable_logging()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_delete_logging_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.delete_logging_integration(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_disable_logging_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.disable_logging_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_enable_logging_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.enable_logging_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_get_logging_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.get_logging_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_get_logging_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.get_logging_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_save_logging_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.save_logging_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_test_logging_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.test_logging_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
