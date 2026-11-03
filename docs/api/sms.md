# SMS on the API — campaigns from an app key

[← Back to the notifications reference](./notifications.md)

`notifications.md` lists every SMS method with its verb, path and scope.
`create_sms_campaign` takes a body whose shape the server picks from a value
inside that body, which the signature cannot show. This page covers that body.

Everything here is asserted in `tests/api/test_notifications.py`. The route
is the same gateway service the Hub serves, so
`norbix.hub.notifications.create_sms_campaign` reads exactly the same body —
the full audience table is in
[HUB · SMS — choosing who a campaign goes to](../hub/sms.md#choosing-who-a-campaign-goes-to).

## Choosing who a campaign goes to

Unlike Email and Push, the SMS request is **flat** — no `campaign` wrapper.
`deliveryType` picks the audience and the one settings object that matches it
repeats the audience name in `recipientsSourceType`:

| audience | `deliveryType` | settings key |
|---|---|---|
| everyone in the project subscribed to SMS | `AllUsers` | `allUsers` |
| a named list of project members | `SpecifiedUsers` | `specifiedUsers` |
| the account owner and team members | `AccountUsers` | `accountUsers` |
| rows of a database collection | `Collection` | `collection` |
| raw phone numbers | `PhoneNumbers` | `phoneNumbers` |

`templateId` and `integrationId` (the SMS provider) are top level. The
provider `integrationId` is a different field from `databaseIntegrationId`
(the database that holds a `Collection` audience), so both sit side by side;
`language` and `initiatorId` are optional.

```python
campaign = norbix.api.notifications.create_sms_campaign(
    templateId="tpl_123",
    integrationId="int_sms",
    deliveryType="PhoneNumbers",
    phoneNumbers={"recipientsSourceType": "PhoneNumbers", "phoneNumbers": ["+37060000000"]},
)
campaign["id"]
```

Send `deliveryType` as the name, not a number — the server reads it as a
string.

## Reading the messages of a campaign

`get_sms_campaign_messages("camp_1", campaignBatchId=...)` needs the batch id
from `get_sms_campaign_batches`; the gateway refuses the call without it. Each
row carries the delivery state (`state`, `attempts[]`, `deliveryEvents[]`)
documented in
[HUB · Notifications — delivery state](../hub/notifications.md#delivery-state-on-a-notification-row).

## Stopping, retrying, previewing

Stopping (`stop_sms_campaign("camp_1")`, no body), retrying the failed
recipients (`retry_failed_sms_notifications("camp_1", idempotency_key=...)`)
and the signed-link preview (`preview_sms_notification(hash=...)`, no sign-in
needed) work as on every channel — see
[notifications.md](./notifications.md#what-is-the-same-on-every-channel).
