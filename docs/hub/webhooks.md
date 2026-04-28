# HUB · Webhooks

Access with `norbix.hub.webhooks`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `get_webhook_integration` | `GET` | `/{version}/webhooks/integration` | `project` |
| `reveal_webhook_integration_secret` | `GET` | `/{version}/webhooks/integration/secret` | `project` |
| `rotate_webhook_integration_secret` | `POST` | `/{version}/webhooks/integration/secret/rotate` | `project` |
| `update_webhook_integration_extra_headers` | `PUT` | `/{version}/webhooks/integration/extra-headers` | `project` |
| `disable_webhook_destination` | `PUT` | `/{version}/webhooks/destinations/{DestinationId}/disable` | `project` |
| `enable_webhook_destination` | `PUT` | `/{version}/webhooks/destinations/{DestinationId}/enable` | `project` |
| `remove_webhook_destination` | `DELETE` | `/{version}/webhooks/destinations/{DestinationId}` | `project` |
| `save_webhook_destination` | `POST` | `/{version}/webhooks/destinations` | `project` |
