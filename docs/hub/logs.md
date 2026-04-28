# HUB · Logs

Access with `norbix.hub.logs`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disable_logging` | `GET` | `/{version}/logs/disable` | `project` |
| `enable_logging` | `GET` | `/{version}/logs/enable` | `project` |
| `delete_logging_integration` | `DELETE` | `/{version}/logs/integrations/{Id}` | `project` |
| `disable_logging_integration` | `PUT` | `/{version}/logs/integrations/{Id}/disable` | `project` |
| `enable_logging_integration` | `PUT` | `/{version}/logs/integrations/{Id}/enable` | `project` |
| `get_logging_integration` | `GET` | `/{version}/logs/integrations/{id}` | `project` |
| `get_logging_integrations` | `GET` | `/{version}/logs/integrations` | `project` |
| `save_logging_integration` | `POST` | `/{version}/logs/integrations` | `project` |
| `test_logging_integration` | `POST` | `/{version}/logs/integrations/test` | `project` |
