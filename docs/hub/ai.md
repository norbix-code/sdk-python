# HUB · Ai

Access with `norbix.hub.ai`.

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
