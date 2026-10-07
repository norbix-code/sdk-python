from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_ai_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.ai
    assert callable(module.delete_llm_integration)
    assert callable(module.disable_llm_integration)
    assert callable(module.enable_llm_integration)
    assert callable(module.get_llm_integration)
    assert callable(module.get_llm_integrations)
    assert callable(module.save_llm_integration)
    assert callable(module.test_llm_integration)
    assert callable(module.delete_mcp_integration)
    assert callable(module.disable_mcp_integration)
    assert callable(module.enable_mcp_integration)
    assert callable(module.get_mcp_integration)
    assert callable(module.get_mcp_integrations)
    assert callable(module.save_mcp_integration)
    assert callable(module.test_mcp_integration)


def test_hub_ai_delete_llm_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.delete_llm_integration(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_disable_llm_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.disable_llm_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_enable_llm_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.enable_llm_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_get_llm_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_llm_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_get_llm_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_llm_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_save_llm_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.save_llm_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_test_llm_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.test_llm_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_delete_mcp_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.delete_mcp_integration(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_disable_mcp_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.disable_mcp_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_enable_mcp_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.enable_mcp_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_get_mcp_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_mcp_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_get_mcp_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_mcp_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_save_mcp_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.save_mcp_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_test_mcp_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.test_mcp_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_ai_wave3_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.ai
    assert callable(module.get_embedding_integrations)
    assert callable(module.save_embedding_integration)
    assert callable(module.get_embedding_integration)
    assert callable(module.delete_embedding_integration)
    assert callable(module.test_embedding_integration)
    assert callable(module.set_llm_integration_as_default)


def test_hub_ai_get_embedding_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_embedding_integrations()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request['url'].endswith('/v3/ai/integrations/embeddings')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_hub_ai_save_embedding_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.save_embedding_integration()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request['url'].endswith('/v3/ai/integrations/embeddings')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_hub_ai_get_embedding_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_embedding_integration(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request['url'].endswith('/v3/ai/integrations/embeddings/stub-Id')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_hub_ai_delete_embedding_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.delete_embedding_integration(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request['url'].endswith('/v3/ai/integrations/embeddings/stub-Id')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_hub_ai_test_embedding_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.test_embedding_integration(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request['url'].endswith('/v3/ai/integrations/embeddings/stub-Id/test')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_hub_ai_set_llm_integration_as_default_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.set_llm_integration_as_default(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request['url'].endswith('/v3/ai/integrations/llms/stub-Id/default')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'

