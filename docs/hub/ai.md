# HUB · Ai

Access with `norbix.hub.ai`.

The LLM and MCP integration routes are covered by
`tests/hub/test_ai_cluster_routes.py` (host, verb, exact path, query and body,
sync and async). The MCP routes are deprecated: the gateway still serves them,
but `save_mcp_integration` is always refused (`CM-ERRORS-MARKETPLACE-030`) and
stores nothing — MCP servers are connected in the Code Marketplace now.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `delete_llm_integration` | `DELETE` | `/{version}/ai/integrations/llms/{Id}` | `project` |
| `disable_llm_integration` | `PUT` | `/{version}/ai/integrations/llms/{Id}/disable` | `project` |
| `enable_llm_integration` | `PUT` | `/{version}/ai/integrations/llms/{Id}/enable` | `project` |
| `get_llm_integration` | `GET` | `/{version}/ai/integrations/llms/{id}` | `project` |
| `get_llm_integrations` | `GET` | `/{version}/ai/integrations/llms/integrations` | `project` |
| `save_llm_integration` | `POST` | `/{version}/ai/integrations/llms/` | `project` |
| `test_llm_integration` | `POST` | `/{version}/ai/integrations/llms/test` | `project` |
| `delete_mcp_integration` | `DELETE` | `/{version}/ai/integrations/mcp/{Id}` | `project` |
| `disable_mcp_integration` | `PUT` | `/{version}/ai/integrations/mcp/{Id}/disable` | `project` |
| `enable_mcp_integration` | `PUT` | `/{version}/ai/integrations/mcp/{Id}/enable` | `project` |
| `get_mcp_integration` | `GET` | `/{version}/ai/integrations/mcp/{id}` | `project` |
| `get_mcp_integrations` | `GET` | `/{version}/ai/integrations/mcp/integrations` | `project` |
| `save_mcp_integration` | `POST` | `/{version}/ai/integrations/mcp/` | `project` |
| `test_mcp_integration` | `POST` | `/{version}/ai/integrations/mcp/test` | `project` |
| `get_embedding_integrations` | `GET` | `/{version}/ai/integrations/embeddings` | `project` |
| `save_embedding_integration` | `POST` | `/{version}/ai/integrations/embeddings` | `project` |
| `get_embedding_integration` | `GET` | `/{version}/ai/integrations/embeddings/{Id}` | `project` |
| `delete_embedding_integration` | `DELETE` | `/{version}/ai/integrations/embeddings/{Id}` | `project` |
| `test_embedding_integration` | `POST` | `/{version}/ai/integrations/embeddings/{Id}/test` | `project` |
| `set_llm_integration_as_default` | `PUT` | `/{version}/ai/integrations/llms/{Id}/default` | `project` |

## AI triggers

A trigger on an AI project event: `"type": "Ai"`, `"when"` one of
`OnCreditsWarning`, `OnCreditsExhausted` (the project's AI credits),
`OnQuotaWarning`, `OnQuotaExhausted` (a user's AI plan quota), and any trigger
action. Every route is asserted in `tests/hub/test_ai.py`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `save_ai_project_trigger` | `POST` | `/{version}/ai/triggers` | `project` |
| `get_ai_project_triggers` | `GET` | `/{version}/ai/triggers` | `project` |
| `get_ai_project_trigger(id)` | `GET` | `/{version}/ai/triggers/{id}` | `project` |
| `enable_ai_project_trigger(trigger_id)` | `PATCH` | `/{version}/ai/triggers/{triggerId}/enable` | `project` |
| `disable_ai_project_trigger(trigger_id)` | `PATCH` | `/{version}/ai/triggers/{triggerId}/disable` | `project` |
| `delete_ai_project_trigger(trigger_id)` | `DELETE` | `/{version}/ai/triggers/{triggerId}` | `project` |

```python
norbix.hub.ai.save_ai_project_trigger(
    trigger={
        "type": "Ai", "name": "Credits running out", "when": "OnCreditsWarning",
        "action": {"type": "Email", "integrationId": "int_mail", "templateId": "tpl_credits"},
    }
)
```
