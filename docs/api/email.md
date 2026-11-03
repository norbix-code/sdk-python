# Email on the API — campaigns from an app key

[← Back to the notifications reference](./notifications.md)

`notifications.md` lists every email method with its verb, path and scope.
`create_email_campaign` takes a body whose shape the server picks from a
discriminator inside that body, which the signature cannot show. This page
covers that body, plus the one route whose path is easy to get wrong.

Everything here is asserted in `tests/api/test_notifications.py`. The route
is the same gateway service the Hub serves, so
`norbix.hub.notifications.create_email_campaign` reads exactly the same body.

## Choosing who a campaign goes to

`create_email_campaign` reads the audience from `campaign["source"]`. Send
that field plus the audience's own fields (source of truth: gateway
`Hub.Emails.Campaigns/Campaigns/Create.EmailTo*.cs`):

| audience | `source` | own fields |
|---|---|---|
| everyone in the project | `allUsers` | `rolesNames`, `userTags` (both optional filters) |
| a named list of project users | `specifiedUsers` | `userRecipients`, optional `userCc`, `userBcc`, `singleEmailStrategy` |
| a named list of account users | `accountUsers` | `userRecipients`, optional `userCc`, `userBcc`, `singleEmailStrategy` |
| rows of a database collection | `collection` | `schemaName`, `fields` (the record fields that hold the recipient), `fieldType` (`User` or `Email`), optional `roleNames`, `languages` |
| raw e-mail addresses | `email` | `recipients`, optional `recipientsCc`, `recipientsBcc`, `singleEmailStrategy` |

Every audience also takes `templateId` and `integrationId` (both required —
`integrationId` is the email provider, from the Hub's
`get_email_integrations`), and the optional `validationIntegrationId`,
`language`, `initiatorId`, `notes`, `campaignTime` (Unix seconds) and
`mappedTokens`. `singleEmailStrategy=True` puts every recipient on one
message instead of one message per recipient. Note the spelling:
`rolesNames` on `allUsers`, but `roleNames` on `collection` — the gateway
names them differently.

Next to `campaign` the request takes `databaseIntegrationId` (the database
that holds a `collection` audience) and `sendNow`:

```python
campaign = norbix.api.notifications.create_email_campaign(
    campaign={
        "source": "email",
        "templateId": "tpl_123",
        "integrationId": "int_email",
        "recipients": ["anna@example.com"],
    },
    sendNow=True,
)
campaign["id"]
```

Send `source` as the name, not a number — the server reads it as a string.
`sendNow=True` sends at once (or at a `campaignTime` sooner than the review
window). Without it a campaign created by an AI tool must be scheduled at
least 24 hours ahead for role-based / all-users / collection audiences and
1 hour ahead for direct recipient lists, or it is refused with
`CM-ERRORS-CAMPAIGNS-017`.

## Reading the messages of a campaign

`get_email_campaign_messages` is the one email route under the **plural**
`/notifications/emails/` prefix; the SDK carries that for you. The gateway
requires `campaignBatchId` (from `get_email_campaign_batches`):

```python
batches = norbix.api.notifications.get_email_campaign_batches("camp_1")
page = norbix.api.notifications.get_email_campaign_messages(
    "camp_1", campaignBatchId=batches["list"]["items"][0]["id"], pageSize=50
)
```

Each row carries the delivery state (`state`, `attempts[]`,
`deliveryEvents[]`) documented in
[HUB · Notifications — delivery state](../hub/notifications.md#delivery-state-on-a-notification-row).

## Stopping, retrying, previewing

Stopping (`stop_email_campaign("camp_1")`, no body), retrying the failed
recipients (`retry_failed_email_notifications("camp_1", idempotency_key=...)`)
and the signed-link preview (`preview_email_notification(hash=...)`, no
sign-in needed) work as on every channel — see
[notifications.md](./notifications.md#what-is-the-same-on-every-channel).
