# API · Notifications

Access with `norbix.api.notifications`.

Campaigns (Email, SMS, Push) and the signed-in user's own push devices and
messages, on the data API with an app key. The campaign routes are the same
gateway services the Hub serves — same paths, same bodies — so the audience
shapes documented for `norbix.hub.notifications` apply here unchanged. The
own-push routes are end-user routes: they always act on the caller's own rows.

Per channel: [Email](./email.md) · [SMS](./sms.md) · [Push](./push.md).

Every route below is asserted by verb and path in
`tests/api/test_notifications.py`.

## Email (12)

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `create_email_campaign` | `POST` | `/{version}/notifications/email/campaigns` | `project` |
| `delete_email_campaign` | `DELETE` | `/{version}/notifications/email/campaigns/{Id}` | `project` |
| `get_email_campaign` | `GET` | `/{version}/notifications/email/campaigns/{id}` | `project` |
| `get_email_campaigns` | `GET` | `/{version}/notifications/email/campaigns` | `project` |
| `get_email_campaign_batches` | `GET` | `/{version}/notifications/email/campaigns/{id}/batches` | `project` |
| `get_email_campaign_batch_notification` | `GET` | `/{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}` | `project` |
| `get_email_campaign_batch_notifications` | `GET` | `/{version}/notifications/email/campaigns/{id}/batches/{batchId}` | `project` |
| `get_email_campaign_statistics` | `GET` | `/{version}/notifications/email/campaigns/{id}/stats` | `project` |
| `preview_email_notification` | `GET` | `/{version}/notifications/email/preview` | `optional` |
| `retry_failed_email_notifications` | `POST` | `/{version}/notifications/email/campaigns/{Id}/retry-failed` | `project` |
| `stop_email_campaign` | `POST` | `/{version}/notifications/email/campaigns/{Id}/stop` | `project` |
| `get_email_campaign_messages` | `GET` | `/{version}/notifications/emails/campaigns/{campaignId}/messages` | `project` |

## SMS (12)

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `create_sms_campaign` | `POST` | `/{version}/notifications/sms/campaigns` | `project` |
| `delete_sms_campaign` | `DELETE` | `/{version}/notifications/sms/campaigns/{id}` | `project` |
| `get_sms_campaign` | `GET` | `/{version}/notifications/sms/campaigns/{id}` | `project` |
| `get_sms_campaigns` | `GET` | `/{version}/notifications/sms/campaigns` | `project` |
| `get_sms_campaign_batches` | `GET` | `/{version}/notifications/sms/campaigns/{id}/batches` | `project` |
| `get_sms_campaign_batch_notification` | `GET` | `/{version}/notifications/sms/campaigns/{id}/batches/{batchId}/{notificationId}` | `project` |
| `get_sms_campaign_batch_notifications` | `GET` | `/{version}/notifications/sms/campaigns/{id}/batches/{batchId}` | `project` |
| `get_sms_campaign_statistics` | `GET` | `/{version}/notifications/sms/campaigns/{id}/stats` | `project` |
| `preview_sms_notification` | `GET` | `/{version}/notifications/sms/preview` | `optional` |
| `retry_failed_sms_notifications` | `POST` | `/{version}/notifications/sms/campaigns/{Id}/retry-failed` | `project` |
| `stop_sms_campaign` | `POST` | `/{version}/notifications/sms/campaigns/{Id}/stop` | `project` |
| `get_sms_campaign_messages` | `GET` | `/{version}/notifications/sms/campaigns/{campaignId}/messages` | `project` |

## Push (20)

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `create_push_campaign` | `POST` | `/{version}/notifications/push/campaigns` | `project` |
| `delete_push_campaign` | `DELETE` | `/{version}/notifications/push/campaigns/{Id}` | `project` |
| `get_push_campaign` | `GET` | `/{version}/notifications/push/campaigns/{id}` | `project` |
| `get_push_campaigns` | `GET` | `/{version}/notifications/push/campaigns` | `project` |
| `get_push_campaign_batches` | `GET` | `/{version}/notifications/push/campaigns/{id}/batches` | `project` |
| `get_push_campaign_batch_notification` | `GET` | `/{version}/notifications/push/campaigns/{id}/batches/{batchId}/{notificationId}` | `project` |
| `get_push_campaign_batch_notifications` | `GET` | `/{version}/notifications/push/campaigns/{id}/batches/{batchId}` | `project` |
| `get_push_campaign_statistics` | `GET` | `/{version}/notifications/push/campaigns/{id}/stats` | `project` |
| `preview_push_notification` | `GET` | `/{version}/notifications/push/preview` | `optional` |
| `retry_failed_push_notifications` | `POST` | `/{version}/notifications/push/campaigns/{Id}/retry-failed` | `project` |
| `stop_push_campaign` | `POST` | `/{version}/notifications/push/campaigns/{Id}/stop` | `project` |
| `get_push_campaign_messages` | `GET` | `/{version}/notifications/push/campaigns/{campaignId}/messages` | `project` |
| `get_push_campaign_audience_count` | `POST` | `/{version}/notifications/push/campaigns/audience-count` | `project` |
| `register_own_push_device` | `POST` | `/{version}/notifications/push/devices` | `project` |
| `get_own_push_devices` | `GET` | `/{version}/notifications/push/devices` | `project` |
| `delete_own_push_device` | `DELETE` | `/{version}/notifications/push/devices/{Id}` | `project` |
| `delete_own_push_device_by_token` | `DELETE` | `/{version}/notifications/push/devices` | `project` |
| `get_own_push_messages` | `GET` | `/{version}/notifications/push/messages` | `project` |
| `mark_own_push_message_read` | `POST` | `/{version}/notifications/push/messages/{Id}/read` | `project` |
| `mark_all_own_push_messages_read` | `POST` | `/{version}/notifications/push/messages/read` | `project` |

## What is the same on every channel

- **Path ids are positional**: `get_email_campaign("camp_1")`,
  `get_sms_campaign_batch_notification("camp_1", "batch_1", "notif_1")`,
  `get_push_campaign_messages("camp_1", campaignBatchId="batch_1")`. Every
  other value is a keyword under its wire name and travels as the body (POST)
  or the query (GET, DELETE).
- **`get_*_campaigns`** filters (all optional): `templateId`, `from` / `to`
  (Unix seconds), `pageSize`, `pageNumber`, `databaseIntegrationId`; Email and
  SMS also take `campaignId`, Email also `emailAddress`.
- **`get_*_campaign_messages`** needs `campaignBatchId` (from
  `get_*_campaign_batches`); the gateway refuses the call without it. Email's
  route sits under the plural `/notifications/emails/`; SMS and Push are
  singular.
- **`stop_*_campaign`** posts with no body: the campaign stops at its next
  batch, batches already sent stay sent.
- **`retry_failed_*_notifications`** takes the campaign id positionally and a
  required `idempotency_key`; the narrowing options (`notification_ids`,
  `categories`, `include_ambiguous`, `database_integration_id`) travel under
  their wire names and are not sent when unset. Same contract as the Hub:
  see [HUB · Notifications — retrying failed recipients](../hub/notifications.md#retrying-failed-recipients).
- **`preview_*_notification`** opens with a signed link alone
  (`hash=...`), with no API key and no bearer token (scope `optional` — auth
  is sent only when the client has a token). A signed-in member can pass
  `projectId` + `notificationId` instead.
- The delivery state on a notification row (`state`, `attempts[]`,
  `deliveryEvents[]`) is the same as on the Hub: see
  [HUB · Notifications — delivery state](../hub/notifications.md#delivery-state-on-a-notification-row).

Not here: the notification inbox (`/notifications/inbox/*`, the bell) — four
Api routes the SDK does not wrap yet.
