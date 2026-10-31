# HUB · Notifications

Access with `norbix.hub.notifications`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `get_user_notification_preferences` | `GET` | `/{version}/notifications/user/preferences` | `project` |
| `update_user_notifications_preferences` | `PUT` | `/{version}/notifications/user/preferences` | `project` |
| `disable_email` | `PUT` | `/{version}/notifications/email/disable` | `project` |
| `get_email_disable_dependencies` | `GET` | `/{version}/notifications/email/disable-dependencies` | `project` |
| `enable_email` | `PUT` | `/{version}/notifications/email/enable` | `project` |
| `attach_file_to_template` | `POST` | `/{version}/notifications/email/templates/attachments` | `project` |
| `create_email_template` | `POST` | `/{version}/notifications/email/templates` | `project` |
| `delete_email_template` | `DELETE` | `/{version}/notifications/email/templates/{Id}` | `project` |
| `get_email_template` | `GET` | `/{version}/notifications/email/templates/{id}` | `project` |
| `get_email_templates` | `GET` | `/{version}/notifications/email/templates` | `project` |
| `get_mjml` | `POST` | `/{version}/notifications/email/templates/mjml` | `project` |
| `get_system_email_template` | `GET` | `/{version}/notifications/email/system-templates/{id}` | `project` |
| `get_system_email_templates` | `GET` | `/{version}/notifications/email/system-templates` | `project` |
| `get_email_template_available_tokens` | `GET` | `/{version}/notifications/email/templates/{id}/tokens` | `project` |
| `update_email_template` | `PUT` | `/{version}/notifications/email/templates` | `project` |
| `delete_email_signature` | `DELETE` | `/{version}/notifications/email/signatures/{id}` | `project` |
| `get_email_signature` | `GET` | `/{version}/notifications/email/signatures/{id}` | `project` |
| `get_email_signatures` | `GET` | `/{version}/notifications/email/signatures` | `project` |
| `save_email_signature` | `POST` | `/{version}/notifications/email/signatures` | `project` |
| `get_email_settings` | `GET` | `/{version}/notifications/email/settings` | `project` |
| `confirm_email_integration_human_delivery` | `POST` | `/{version}/notifications/email/integrations/confirm-human-delivery` | `project` |
| `check_email_integration_domain_health` | `POST` | `/{version}/notifications/email/integrations/domain-health` | `project` |
| `delete_email_integration` | `DELETE` | `/{version}/notifications/email/integrations/{Id}` | `project` |
| `disable_email_integration` | `PUT` | `/{version}/notifications/email/integrations/{Id}/disable` | `project` |
| `enable_email_integration` | `PUT` | `/{version}/notifications/email/integrations/{Id}/enable` | `project` |
| `get_email_integration` | `GET` | `/{version}/notifications/email/integrations/{id}` | `project` |
| `get_email_integrations` | `GET` | `/{version}/notifications/email/integrations` | `project` |
| `save_email_integration` | `POST` | `/{version}/notifications/email/integrations` | `project` |
| `set_emails_integration_as_default` | `PUT` | `/{version}/notifications/email/integrations/{Id}/default` | `project` |
| `test_email_integration` | `POST` | `/{version}/notifications/email/integrations/test` | `project` |
| `archive_email_template` | `PUT` | `/{version}/notifications/email/templates/{Id}/archive` | `project` |
| `clone_email_template` | `POST` | `/{version}/notifications/email/templates/{Id}/clone` | `project` |
| `un_archive_email_template` | `PUT` | `/{version}/notifications/email/templates/{Id}/unarchive` | `project` |
| `delete_email_footer` | `DELETE` | `/{version}/notifications/email/footers/{id}` | `project` |
| `get_email_footer` | `GET` | `/{version}/notifications/email/footers/{id}` | `project` |
| `get_email_footers` | `GET` | `/{version}/notifications/email/footers` | `project` |
| `save_email_footer` | `POST` | `/{version}/notifications/email/footers` | `project` |
| `create_email_campaign` | `POST` | `/{version}/notifications/email/campaigns` | `project` |
| `delete_email_campaign` | `DELETE` | `/{version}/notifications/email/campaigns/{Id}` | `project` |
| `stop_email_campaign` | `POST` | `/{version}/notifications/email/campaigns/{Id}/stop` | `project` |
| `retry_failed_email_notifications` | `POST` | `/{version}/notifications/email/campaigns/{Id}/retry-failed` | `project` |
| `get_email_campaign` | `GET` | `/{version}/notifications/email/campaigns/{id}` | `project` |
| `get_email_campaigns` | `GET` | `/{version}/notifications/email/campaigns` | `project` |
| `get_email_campaign_batches` | `GET` | `/{version}/notifications/email/campaigns/{id}/batches` | `project` |
| `get_email_campaign_batch_notification` | `GET` | `/{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}` | `project` |
| `get_email_campaign_batch_notifications` | `GET` | `/{version}/notifications/email/campaigns/{id}/batches/{batchId}` | `project` |
| `get_email_campaign_statistics` | `GET` | `/{version}/notifications/email/campaigns/{id}/stats` | `project` |
| `preview_email_notification` | `GET` | `/{version}/notifications/email/preview` | `optional` |
| `get_email_campaign_messages` | `GET` | `/{version}/notifications/emails/campaigns/{campaignId}/messages` | `project` |
| `disable_sms` | `PUT` | `/{version}/notifications/sms/disable` | `project` |
| `enable_sms` | `PUT` | `/{version}/notifications/sms/enable` | `project` |
| `get_sms_disable_dependencies` | `GET` | `/{version}/notifications/sms/disable-dependencies` | `project` |
| `get_sms_settings` | `GET` | `/{version}/notifications/sms/settings` | `project` |
| `get_sms_integrations` | `GET` | `/{version}/notifications/sms/integrations` | `project` |
| `save_sms_integration` | `POST` | `/{version}/notifications/sms/integrations` | `project` |
| `get_sms_integration` | `GET` | `/{version}/notifications/sms/integrations/{id}` | `project` |
| `enable_sms_integration` | `PUT` | `/{version}/notifications/sms/integrations/{Id}/enable` | `project` |
| `disable_sms_integration` | `PUT` | `/{version}/notifications/sms/integrations/{Id}/disable` | `project` |
| `set_sms_integration_as_default` | `PUT` | `/{version}/notifications/sms/integrations/{Id}/default` | `project` |
| `delete_sms_integration` | `DELETE` | `/{version}/notifications/sms/integrations/{Id}` | `project` |
| `test_sms_integration` | `POST` | `/{version}/notifications/sms/integrations/test` | `project` |
| `confirm_sms_integration_human_delivery` | `POST` | `/{version}/notifications/sms/integrations/confirm-human-delivery` | `project` |
| `get_sms_templates` | `GET` | `/{version}/notifications/sms/templates` | `project` |
| `create_sms_template` | `POST` | `/{version}/notifications/sms/templates` | `project` |
| `update_sms_template` | `PUT` | `/{version}/notifications/sms/templates` | `project` |
| `get_sms_template` | `GET` | `/{version}/notifications/sms/templates/{id}` | `project` |
| `delete_sms_template` | `DELETE` | `/{version}/notifications/sms/templates/{Id}` | `project` |
| `archive_sms_template` | `PUT` | `/{version}/notifications/sms/templates/{Id}/archive` | `project` |
| `un_archive_sms_template` | `PUT` | `/{version}/notifications/sms/templates/{Id}/unarchive` | `project` |
| `clone_sms_template` | `POST` | `/{version}/notifications/sms/templates/{Id}/clone` | `project` |
| `get_sms_message_content_tokens` | `GET` | `/{version}/notifications/sms/templates/{id}/tokens` | `project` |
| `render_sms` | `POST` | `/{version}/notifications/sms/templates/render` | `project` |
| `get_sms_campaigns` | `GET` | `/{version}/notifications/sms/campaigns` | `project` |
| `create_sms_campaign` | `POST` | `/{version}/notifications/sms/campaigns` | `project` |
| `get_sms_campaign` | `GET` | `/{version}/notifications/sms/campaigns/{id}` | `project` |
| `delete_sms_campaign` | `DELETE` | `/{version}/notifications/sms/campaigns/{id}` | `project` |
| `stop_sms_campaign` | `POST` | `/{version}/notifications/sms/campaigns/{Id}/stop` | `project` |
| `retry_failed_sms_notifications` | `POST` | `/{version}/notifications/sms/campaigns/{Id}/retry-failed` | `project` |
| `get_sms_campaign_batches` | `GET` | `/{version}/notifications/sms/campaigns/{id}/batches` | `project` |
| `get_sms_campaign_batch_notifications` | `GET` | `/{version}/notifications/sms/campaigns/{id}/batches/{batchId}` | `project` |
| `get_sms_campaign_batch_notification` | `GET` | `/{version}/notifications/sms/campaigns/{id}/batches/{batchId}/{notificationId}` | `project` |
| `get_sms_campaign_statistics` | `GET` | `/{version}/notifications/sms/campaigns/{id}/stats` | `project` |
| `get_sms_campaign_messages` | `GET` | `/{version}/notifications/sms/campaigns/{campaignId}/messages` | `project` |
| `preview_sms_notification` | `GET` | `/{version}/notifications/sms/preview` | `optional` |
| `disable_push` | `PUT` | `/{version}/notifications/push/disable` | `project` |
| `enable_push` | `PUT` | `/{version}/notifications/push/enable` | `project` |
| `archive_push_template` | `PUT` | `/{version}/notifications/push/templates/{Id}/archive` | `project` |
| `clone_push_template` | `POST` | `/{version}/notifications/push/templates/{Id}/clone` | `project` |
| `create_push_template` | `POST` | `/{version}/notifications/push/templates` | `project` |
| `delete_push_template` | `DELETE` | `/{version}/notifications/push/templates/{Id}` | `project` |
| `get_push_template` | `GET` | `/{version}/notifications/push/templates/{id}` | `project` |
| `get_push_templates` | `GET` | `/{version}/notifications/push/templates` | `project` |
| `get_push_message_content_tokens` | `GET` | `/{version}/notifications/push/templates/{id}/tokens` | `project` |
| `un_archive_push_template` | `PUT` | `/{version}/notifications/push/templates/{Id}/unarchive` | `project` |
| `update_push_template` | `PUT` | `/{version}/notifications/push/templates` | `project` |
| `confirm_push_integration_human_delivery` | `POST` | `/{version}/notifications/push/integrations/confirm-human-delivery` | `project` |
| `delete_push_integration` | `DELETE` | `/{version}/notifications/push/integrations/{Id}` | `project` |
| `disable_push_integration` | `PUT` | `/{version}/notifications/push/integrations/{Id}/disable` | `project` |
| `enable_push_integration` | `PUT` | `/{version}/notifications/push/integrations/{Id}/enable` | `project` |
| `get_push_integration` | `GET` | `/{version}/notifications/push/integrations/{id}` | `project` |
| `get_push_integrations` | `GET` | `/{version}/notifications/push/integrations` | `project` |
| `save_push_integration` | `POST` | `/{version}/notifications/push/integrations` | `project` |
| `set_push_integration_as_default` | `PUT` | `/{version}/notifications/push/integrations/{Id}/default` | `project` |
| `test_push_integration` | `POST` | `/{version}/notifications/push/integrations/test` | `project` |
| `register_device` | `POST` | `/{version}/notifications/push/devices` | `project` |
| `get_push_disable_dependencies` | `GET` | `/{version}/notifications/push/disable-dependencies` | `project` |
| `get_push_settings` | `GET` | `/{version}/notifications/push/settings` | `project` |
| `render_push` | `POST` | `/{version}/notifications/push/templates/render` | `project` |
| `create_push_campaign` | `POST` | `/{version}/notifications/push/campaigns` | `project` |
| `get_push_campaigns` | `GET` | `/{version}/notifications/push/campaigns` | `project` |
| `get_push_campaign` | `GET` | `/{version}/notifications/push/campaigns/{id}` | `project` |
| `delete_push_campaign` | `DELETE` | `/{version}/notifications/push/campaigns/{Id}` | `project` |
| `stop_push_campaign` | `POST` | `/{version}/notifications/push/campaigns/{Id}/stop` | `project` |
| `retry_failed_push_notifications` | `POST` | `/{version}/notifications/push/campaigns/{Id}/retry-failed` | `project` |
| `get_push_campaign_batches` | `GET` | `/{version}/notifications/push/campaigns/{id}/batches` | `project` |
| `get_push_campaign_batch_notifications` | `GET` | `/{version}/notifications/push/campaigns/{id}/batches/{batchId}` | `project` |
| `get_push_campaign_batch_notification` | `GET` | `/{version}/notifications/push/campaigns/{id}/batches/{batchId}/{notificationId}` | `project` |
| `get_push_campaign_statistics` | `GET` | `/{version}/notifications/push/campaigns/{id}/stats` | `project` |
| `get_push_campaign_messages` | `GET` | `/{version}/notifications/push/campaigns/{campaignId}/messages` | `project` |
| `preview_push_notification` | `GET` | `/{version}/notifications/push/preview` | `optional` |

Every method above has an async twin on `client.hub.notifications` when the
client is an `AsyncNorbix`. See [push.md](./push.md) for how to pick a push
campaign audience and a push provider, and [sms.md](./sms.md) for the same two
choices on an SMS campaign.

## Cloning a template

`clone_email_template`, `clone_sms_template` and `clone_push_template` copy a
template and answer the new copy's id, so you can open or edit the copy
without listing the templates again:

```python
copy = client.hub.notifications.clone_email_template(id="tpl_welcome")
client.hub.notifications.get_email_template(id=copy["id"])
```

## Retrying failed recipients

`retry_failed_email_notifications`, `retry_failed_sms_notifications` and
`retry_failed_push_notifications` send a campaign's failed recipients again
(route `…/campaigns/{id}/retry-failed`). Only recipients whose last attempt
failed are sent; the ones that were accepted stay untouched. The campaign id
is positional and `idempotency_key` (at most 64 characters) is required — the
same key on the same campaign replays the first answer instead of selecting
again, so a retried call after a timeout never sends twice:

```python
answer = client.hub.notifications.retry_failed_email_notifications(
    "camp_1",
    idempotency_key="camp_1-retry-2026-10-26",
    categories=["Transient"],
)
answer["selected"]   # recipients queued again
answer["skipped"]    # {reason: count} — why the others were left out
answer["replayed"]   # True when this key was already used: the first answer, nothing new sent
```

The optional narrowing values travel under their wire names and are not sent
when unset:

| keyword | wire name | what it does |
|---|---|---|
| `notification_ids` | `notificationIds` | only these rows of the campaign |
| `categories` | `categories` | only these failure kinds: `Transient`, `Permanent`, `Unknown` |
| `include_ambiguous` | `includeAmbiguous` | also take rows whose provider answer never said whether the message went out; the answer then carries `warning`, the text that a duplicate may be sent |
| `database_integration_id` | `databaseIntegrationId` | the database integration id, the same value `create_sms_campaign` takes (different from the provider `integrationId`) |

The answer is `{"retryRequestId", "selected", "skipped": {reason: count},
"replayed", "warning"?}`. Besides the reasons for rows left out, `skipped` can
carry `optedOut`, `compliance`, `undeliverable`: the people the send gates stopped during the
retry. Those keys are added to the stored answer later and are part of `selected`.

## Delivery state on a notification row

The rows of `get_*_campaign_batch_notifications`,
`get_*_campaign_batch_notification` and `get_*_campaign_messages` carry the
delivery state of each recipient (dicts, as everything in this SDK):

- `state` — `Pending`, `Sending`, `Retrying`, `Accepted`, `Failed`, `Blocked`
  or `Cancelled`, and `stateChangedAt`.
- `attempts[]` — one per send: `attemptId`, `number`, `startedAt`,
  `finishedAt`, `outcome` (`Accepted` | `Failed` | `Blocked`), `category` (`Unknown` |
  `Transient` | `Permanent` | `Ambiguous`), `statusCode`, `errorCode`,
  `message`, `providerRef`, `retryAfterSeconds`, `exhausted`, `nextRetryAt`,
  `correlationId`, `trigger` (`Initial` | `AutoRetry` | `ManualRetry`) and, for
  a manual retry, the `retryRequestId` the retry call answered.
- `deliveryEvents[]` — what the provider reported after acceptance:
  `eventId`, `outcome` (`Delivered` | `Bounced` | `Complained` | `Rejected` |
  `Deferred`), `at`, `provider`, `providerRef`, `reason`; the row's
  `deliveryOutcome` and `deliveryOutcomeRank` summarise them.

`get_*_campaign_statistics` also counts `failedRetryable` (failed rows a retry
would select) and `cancelled`.

## Delivery events from the provider

`deliveryEvents[]` fills only when the provider integration reports back.
`save_email_integration` / `save_sms_integration` take, inside `integration`:

| provider | `provider` value | delivery-event fields |
|---|---|---|
| Amazon SES | `AwsSes` | `deliveryEventsEnabled`, `snsTopicArn` |
| SendGrid | `SendGrid` | `deliveryEventsEnabled`, `eventWebhookPublicKey` |
| Azure Communication Services (email) | `azureCommunication` | `endpoint`, `accessKey`, optional `deliveryEventsEnabled`, `eventGridKey` |
| Twilio (SMS) | `Twilio` | `deliveryEventsEnabled`, `statusCallbackUrl` |

`get_email_integration` / `get_sms_integration` read the same fields back. The
provider's callback routes are the gateway's own public webhooks, not SDK
methods.
