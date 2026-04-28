# HUB · Payments

Access with `norbix.hub.payments`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disable_payments` | `GET` | `/{version}/payments/disable` | `project` |
| `enable_payments` | `GET` | `/{version}/payments/enable` | `project` |
| `delete_payments_trigger` | `DELETE` | `/{version}/payments/triggers/{triggerId}` | `project` |
| `disable_payments_trigger` | `PATCH` | `/{version}/payments/triggers/{triggerId}/disable` | `project` |
| `enable_payments_trigger` | `PATCH` | `/{version}/payments/triggers/{triggerId}/enable` | `project` |
| `get_payments_trigger` | `GET` | `/{version}/payments/triggers/{id}` | `project` |
| `get_payments_triggers` | `GET` | `/{version}/payments/triggers` | `project` |
| `save_payments_trigger` | `POST` | `/{version}/payments/triggers` | `project` |
| `confirm_payments_integration_human_delivery` | `POST` | `/{version}/payments/integrations/confirm-human-delivery` | `project` |
| `delete_payments_integration` | `DELETE` | `/{version}/payments/integrations/{Id}` | `project` |
| `disable_payments_integration` | `PUT` | `/{version}/payments/integrations/{Id}/disable` | `project` |
| `enable_payments_integration` | `PUT` | `/{version}/payments/integrations/{Id}/enable` | `project` |
| `get_payments_integration` | `GET` | `/{version}/payments/integrations/{id}` | `project` |
| `get_payments_integrations` | `GET` | `/{version}/payments/integrations` | `project` |
| `save_payments_integration` | `POST` | `/{version}/payments/integrations` | `project` |
| `test_payments_integration` | `POST` | `/{version}/payments/integrations/test` | `project` |
