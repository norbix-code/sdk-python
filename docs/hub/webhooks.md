# HUB · Webhooks

Access with `norbix.hub.webhooks`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `getWebhookIntegration` | `GET` | `/{version}/webhooks/integration` | `project` |
| `revealWebhookIntegrationSecret` | `GET` | `/{version}/webhooks/integration/secret` | `project` |
| `rotateWebhookIntegrationSecret` | `POST` | `/{version}/webhooks/integration/secret/rotate` | `project` |
| `updateWebhookIntegrationExtraHeaders` | `PUT` | `/{version}/webhooks/integration/extra-headers` | `project` |
| `disableWebhookDestination` | `PUT` | `/{version}/webhooks/destinations/{DestinationId}/disable` | `project` |
| `enableWebhookDestination` | `PUT` | `/{version}/webhooks/destinations/{DestinationId}/enable` | `project` |
| `removeWebhookDestination` | `DELETE` | `/{version}/webhooks/destinations/{DestinationId}` | `project` |
| `saveWebhookDestination` | `POST` | `/{version}/webhooks/destinations` | `project` |
