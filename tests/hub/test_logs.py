from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_hub_logs_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.logs
    assert callable(module.disableLogging)
    assert callable(module.enableLogging)
    assert callable(module.deleteLoggingIntegration)
    assert callable(module.disableLoggingIntegration)
    assert callable(module.enableLoggingIntegration)
    assert callable(module.getLoggingIntegration)
    assert callable(module.getLoggingIntegrations)
    assert callable(module.saveLoggingIntegration)
    assert callable(module.testLoggingIntegration)


def test_hub_logs_disableLogging_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/logs/disable') if False else {}
    client.hub.logs.disableLogging(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_enableLogging_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/logs/enable') if False else {}
    client.hub.logs.enableLogging(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_deleteLoggingIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/logs/integrations/{Id}') if True else {}
    client.hub.logs.deleteLoggingIntegration(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_disableLoggingIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/logs/integrations/{Id}/disable') if True else {}
    client.hub.logs.disableLoggingIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_enableLoggingIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/logs/integrations/{Id}/enable') if True else {}
    client.hub.logs.enableLoggingIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_getLoggingIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/logs/integrations/{id}') if True else {}
    client.hub.logs.getLoggingIntegration(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_getLoggingIntegrations_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/logs/integrations') if False else {}
    client.hub.logs.getLoggingIntegrations(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_saveLoggingIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/logs/integrations') if False else {}
    client.hub.logs.saveLoggingIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_testLoggingIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/logs/integrations/test') if False else {}
    client.hub.logs.testLoggingIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
