from __future__ import annotations

import json

from urllib.parse import urlparse

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
    assert callable(module.delete_ai_project_trigger)
    assert callable(module.disable_ai_project_trigger)
    assert callable(module.enable_ai_project_trigger)
    assert callable(module.get_ai_project_trigger)
    assert callable(module.get_ai_project_triggers)
    assert callable(module.save_ai_project_trigger)


def test_hub_ai_delete_llm_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.delete_llm_integration(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'DELETE'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/llms/stub-Id'

def test_hub_ai_disable_llm_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.disable_llm_integration(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PUT'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/llms/stub-Id/disable'

def test_hub_ai_enable_llm_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.enable_llm_integration(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PUT'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/llms/stub-Id/enable'

def test_hub_ai_get_llm_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_llm_integration(id="stub-id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/llms/stub-id'

def test_hub_ai_get_llm_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_llm_integrations()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/llms/integrations'

def test_hub_ai_save_llm_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.save_llm_integration()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/llms/'

def test_hub_ai_test_llm_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.test_llm_integration()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/llms/test'

def test_hub_ai_delete_mcp_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.delete_mcp_integration(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'DELETE'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/mcp/stub-Id'

def test_hub_ai_disable_mcp_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.disable_mcp_integration(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PUT'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/mcp/stub-Id/disable'

def test_hub_ai_enable_mcp_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.enable_mcp_integration(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PUT'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/mcp/stub-Id/enable'

def test_hub_ai_get_mcp_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_mcp_integration(id="stub-id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/mcp/stub-id'

def test_hub_ai_get_mcp_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_mcp_integrations()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/mcp/integrations'

def test_hub_ai_save_mcp_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.save_mcp_integration()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/mcp/'

def test_hub_ai_test_mcp_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.test_mcp_integration()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/integrations/mcp/test'

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
    assert transport.last_request['headers']['norbix-project-id'] == 'test-project'


def test_hub_ai_save_embedding_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.save_embedding_integration()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request['url'].endswith('/v3/ai/integrations/embeddings')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['norbix-project-id'] == 'test-project'


def test_hub_ai_get_embedding_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_embedding_integration(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request['url'].endswith('/v3/ai/integrations/embeddings/stub-Id')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['norbix-project-id'] == 'test-project'


def test_hub_ai_delete_embedding_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.delete_embedding_integration(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request['url'].endswith('/v3/ai/integrations/embeddings/stub-Id')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['norbix-project-id'] == 'test-project'


def test_hub_ai_test_embedding_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.test_embedding_integration(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request['url'].endswith('/v3/ai/integrations/embeddings/stub-Id/test')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['norbix-project-id'] == 'test-project'


def test_hub_ai_set_llm_integration_as_default_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.set_llm_integration_as_default(id="stub-Id")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request['url'].endswith('/v3/ai/integrations/llms/stub-Id/default')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['norbix-project-id'] == 'test-project'


# AI triggers (credits and quota events): the six routes, verb, exact path and
# where the request goes. Nothing leaves the process.

def test_hub_ai_delete_ai_project_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.delete_ai_project_trigger(trigger_id="trg_1")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'DELETE'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/triggers/trg_1'
    assert transport.last_request['body'] == ''

def test_hub_ai_disable_ai_project_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.disable_ai_project_trigger(trigger_id="trg_1")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PATCH'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/triggers/trg_1/disable'
    assert transport.last_request['body'] == ''

def test_hub_ai_enable_ai_project_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.enable_ai_project_trigger(trigger_id="trg_1")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PATCH'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/triggers/trg_1/enable'
    assert transport.last_request['body'] == ''

def test_hub_ai_get_ai_project_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_ai_project_trigger(id="trg_1")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/triggers/trg_1'
    assert transport.last_request['body'] == ''

def test_hub_ai_get_ai_project_triggers_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.ai.get_ai_project_triggers()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/triggers'
    assert transport.last_request['body'] == ''

def test_hub_ai_save_ai_project_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    trigger = {"type": "Ai", "name": "Credits running out", "when": "OnCreditsWarning", "action": {"type": "Email", "integrationId": "int_1"}}
    client.hub.ai.save_ai_project_trigger(trigger=trigger)
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert urlparse(transport.last_request['url']).path == '/v3/ai/triggers'
    assert json.loads(transport.last_request['body']) == {"trigger": trigger}
