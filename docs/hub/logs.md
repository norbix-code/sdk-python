# HUB · Logs

Access with `norbix.hub.logs`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disableLogging` | `GET` | `/{version}/logs/disable` | `project` |
| `enableLogging` | `GET` | `/{version}/logs/enable` | `project` |
| `deleteLoggingIntegration` | `DELETE` | `/{version}/logs/integrations/{Id}` | `project` |
| `disableLoggingIntegration` | `PUT` | `/{version}/logs/integrations/{Id}/disable` | `project` |
| `enableLoggingIntegration` | `PUT` | `/{version}/logs/integrations/{Id}/enable` | `project` |
| `getLoggingIntegration` | `GET` | `/{version}/logs/integrations/{id}` | `project` |
| `getLoggingIntegrations` | `GET` | `/{version}/logs/integrations` | `project` |
| `saveLoggingIntegration` | `POST` | `/{version}/logs/integrations` | `project` |
| `testLoggingIntegration` | `POST` | `/{version}/logs/integrations/test` | `project` |
