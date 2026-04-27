from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_hub_ai_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.ai
    assert callable(module.deleteLlmIntegration)
    assert callable(module.disableLlmIntegration)
    assert callable(module.enableLlmIntegration)
    assert callable(module.getLlmIntegration)
    assert callable(module.getLlmIntegrations)
    assert callable(module.saveLlmIntegration)
    assert callable(module.testLlmIntegration)
    assert callable(module.deleteMcpIntegration)
    assert callable(module.disableMcpIntegration)
    assert callable(module.enableMcpIntegration)
    assert callable(module.getMcpIntegration)
    assert callable(module.getMcpIntegrations)
    assert callable(module.saveMcpIntegration)
    assert callable(module.testMcpIntegration)


def test_hub_ai_deleteLlmIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/llms/{Id}') if True else {}
    client.hub.ai.deleteLlmIntegration(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_disableLlmIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/llms/{Id}/disable') if True else {}
    client.hub.ai.disableLlmIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_enableLlmIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/llms/{Id}/enable') if True else {}
    client.hub.ai.enableLlmIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_getLlmIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/llms/{id}') if True else {}
    client.hub.ai.getLlmIntegration(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_getLlmIntegrations_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/llms/integrations') if False else {}
    client.hub.ai.getLlmIntegrations(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_saveLlmIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/llms/') if False else {}
    client.hub.ai.saveLlmIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_testLlmIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/llms/test') if False else {}
    client.hub.ai.testLlmIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_deleteMcpIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/mcp/{Id}') if True else {}
    client.hub.ai.deleteMcpIntegration(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_disableMcpIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/mcp/{Id}/disable') if True else {}
    client.hub.ai.disableMcpIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_enableMcpIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/mcp/{Id}/enable') if True else {}
    client.hub.ai.enableMcpIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_getMcpIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/mcp/{id}') if True else {}
    client.hub.ai.getMcpIntegration(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_getMcpIntegrations_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/mcp/integrations') if False else {}
    client.hub.ai.getMcpIntegrations(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_saveMcpIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/mcp/') if False else {}
    client.hub.ai.saveMcpIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_testMcpIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/ai/integrations/mcp/test') if False else {}
    client.hub.ai.testMcpIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
