# HUB · Files

Access with `norbix.hub.files`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disableFiles` | `GET` | `/{version}/files/disable` | `project` |
| `enableFiles` | `GET` | `/{version}/files/enable` | `project` |
| `deleteFilesTrigger` | `DELETE` | `/{version}/files/triggers/{triggerId}` | `project` |
| `disableFilesTrigger` | `PATCH` | `/{version}/files/triggers/{triggerId}/disable` | `project` |
| `enableFilesTrigger` | `PATCH` | `/{version}/files/triggers/{triggerId}/enable` | `project` |
| `getFilesTrigger` | `GET` | `/{version}/files/triggers/{id}` | `project` |
| `getFilesTriggers` | `GET` | `/{version}/files/triggers` | `project` |
| `saveFilesTrigger` | `POST` | `/{version}/files/triggers` | `project` |
| `deleteFilesIntegration` | `DELETE` | `/{version}/files/integrations/{Id}` | `project` |
| `disableFilesIntegration` | `PUT` | `/{version}/files/integrations/{Id}/disable` | `project` |
| `enableFilesIntegration` | `PUT` | `/{version}/files/integrations/{Id}/enable` | `project` |
| `getFilesIntegration` | `GET` | `/{version}/files/integrations/{id}` | `project` |
| `getFilesIntegrations` | `GET` | `/{version}/files/integrations` | `project` |
| `saveFilesIntegration` | `POST` | `/{version}/files/integrations` | `project` |
| `setFilesIntegrationAsDefault` | `PUT` | `/{version}/files/integrations/{Id}/default` | `project` |
