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

## The delivery envelope: `id` and `eventId`

Each delivery POSTs `{ id, eventId, event, createdOn, accountId, projectId,
triggerId, data }` to the destination.

- `id` — one per delivery. A retry of the same delivery keeps its `id`.
- `eventId` — one per change. Every delivery made for one record change (the
  plain webhook delivery and each schema Webhook-trigger delivery) carries the
  same `eventId`. When the publisher has no shared event id (Files,
  Membership, Payments, AI triggers) it equals `id`.

A destination that is subscribed to the event **and** targeted by a schema
Webhook trigger gets **two** deliveries for one change: one with `triggerId`
null, one with `triggerId` set — two `id`s, one `eventId`. De-duplicate on
`eventId` (fall back to `id` for older gateways that do not send it). The
receiver in `norbix_python.webhooks` does this fallback for you
(`event.event_id`); see [the webhook receiver](../webhooks-receiver.md).
