from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_hub_files_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.files
    assert callable(module.disableFiles)
    assert callable(module.enableFiles)
    assert callable(module.deleteFilesTrigger)
    assert callable(module.disableFilesTrigger)
    assert callable(module.enableFilesTrigger)
    assert callable(module.getFilesTrigger)
    assert callable(module.getFilesTriggers)
    assert callable(module.saveFilesTrigger)
    assert callable(module.deleteFilesIntegration)
    assert callable(module.disableFilesIntegration)
    assert callable(module.enableFilesIntegration)
    assert callable(module.getFilesIntegration)
    assert callable(module.getFilesIntegrations)
    assert callable(module.saveFilesIntegration)
    assert callable(module.setFilesIntegrationAsDefault)


def test_hub_files_disableFiles_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/disable') if False else {}
    client.hub.files.disableFiles(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_enableFiles_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/enable') if False else {}
    client.hub.files.enableFiles(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_deleteFilesTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/triggers/{triggerId}') if True else {}
    client.hub.files.deleteFilesTrigger(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_disableFilesTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/triggers/{triggerId}/disable') if True else {}
    client.hub.files.disableFilesTrigger(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_enableFilesTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/triggers/{triggerId}/enable') if True else {}
    client.hub.files.enableFilesTrigger(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_getFilesTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/triggers/{id}') if True else {}
    client.hub.files.getFilesTrigger(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_getFilesTriggers_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/triggers') if False else {}
    client.hub.files.getFilesTriggers(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_saveFilesTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/triggers') if False else {}
    client.hub.files.saveFilesTrigger(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_deleteFilesIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/integrations/{Id}') if True else {}
    client.hub.files.deleteFilesIntegration(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_disableFilesIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/integrations/{Id}/disable') if True else {}
    client.hub.files.disableFilesIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_enableFilesIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/integrations/{Id}/enable') if True else {}
    client.hub.files.enableFilesIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_getFilesIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/integrations/{id}') if True else {}
    client.hub.files.getFilesIntegration(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_getFilesIntegrations_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/integrations') if False else {}
    client.hub.files.getFilesIntegrations(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_saveFilesIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/integrations') if False else {}
    client.hub.files.saveFilesIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_files_setFilesIntegrationAsDefault_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/files/integrations/{Id}/default') if True else {}
    client.hub.files.setFilesIntegrationAsDefault(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
