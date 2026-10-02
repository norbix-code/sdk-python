# SMS — choosing an audience and a provider

[← Back to the notifications reference](./notifications.md)

`notifications.md` lists every SMS method with its verb, path and scope. Two of
them take a body whose shape the server picks from a value inside that body,
which the signature cannot show. This page covers those two, plus the three
calls whose required values are not obvious from the route.

Everything here is asserted in `tests/hub/test_sms.py`.

## Choosing who a campaign goes to

`create_sms_campaign` reads the audience from `deliveryType` and then the one
settings object that matches it. The request is flat (no `campaign` wrapper),
and the settings object repeats the audience name in `recipientsSourceType`:

| audience | `deliveryType` | settings key | own fields |
|---|---|---|---|
| everyone in the project subscribed to SMS | `AllUsers` | `allUsers` | `rolesNames`, `userTags` (both optional filters) |
| a named list of project members | `SpecifiedUsers` | `specifiedUsers` | `recipients` (member ids) |
| rows of a database collection | `Collection` | `collection` | `schemaName`, `fields` (the record fields that hold the recipient), `fieldType` (`User` or `Email`), optional `roleNames`, `languages` |
| raw phone numbers | `PhoneNumbers` | `phoneNumbers` | `phoneNumbers` (international format, `+370…`) |

Every settings object also takes `campaignTime` (Unix seconds, UTC — set a
future time so the campaign can be reviewed in the dashboard first), and the
optional `mappedTokens` and `respectTimeZoneSettings`. The request itself takes
`templateId` (required), and the optional `language` and `databaseIntegrationId`.
Note the spelling: `rolesNames` on `allUsers`, but `roleNames` on `collection` —
the gateway names them differently.

```python
client.hub.notifications.create_sms_campaign(
    templateId="tpl_123",
    deliveryType="PhoneNumbers",
    phoneNumbers={
        "recipientsSourceType": "PhoneNumbers",
        "phoneNumbers": ["+37060000000"],
        "campaignTime": 1_900_000_000,
    },
)
```

Send `deliveryType` as the name, not a number — the server reads it as a
string. The generated enum also lists `AccountUsers`; the create request has no
settings object for it, so the gateway refuses it.

A scheduled campaign can be cancelled with `stop_sms_campaign(id=...)`; it posts
to `…/campaigns/{id}/stop` with no body.

## Choosing an SMS provider

`save_sms_integration` works the same way, with `integration["provider"]`:

| provider | `provider` value | own fields |
|---|---|---|
| Fake (sandbox, never sends) | `Fake` | none |
| Twilio | `Twilio` | `accountSid`, `fromPhoneNumber`, `authToken` |
| Vonage | `Vonage` | `apiKey`, `fromSender`, `apiSecret` |
| Plivo | `Plivo` | `authId`, `fromPhoneNumber`, `authToken` |
| Telnyx | `Telnyx` | `messagingProfileId`, `fromPhoneNumber`, `apiKey` |
| Bird | `Bird` | `originator`, `region`, `apiKey` |
| Telesign | `Telesign` | `customerId`, `fromSender`, `apiKey` |
| Sinch | `Sinch` | `servicePlanId`, `fromPhoneNumber`, `apiKey`, `apiSecret` |

`integrationName` and `isEnabled` are optional; send `integrationId` to update
an existing one. The Fake provider takes no field at all — this is the whole
request, and the server builds the rest (one Fake per project):

```python
client.hub.notifications.save_sms_integration(integration={"provider": "Fake"})
```

## Rendering a template without sending

`render_sms` runs the Razor template and returns the bound text, or the list of
tokens it could not resolve. Tokens are Razor only (`@Model.FirstName`):

```python
rendered = client.hub.notifications.render_sms(
    code="Hi @Model.FirstName",
    tokens=[{"key": "FirstName", "value": "Ada"}],
    isForPreview=True,
)
```

## Reading one message of a campaign

Use `get_sms_campaign_batch_notification` with the campaign id, the batch id
and the notification id (route `…/campaigns/{id}/batches/{batchId}/{notificationId}`):

```python
message = client.hub.notifications.get_sms_campaign_batch_notification(
    id="camp_1",
    batch_id="batch_1",
    notification_id="notif_1",
)
```

Get the ids from `get_sms_campaigns`, `get_sms_campaign_batches` and
`get_sms_campaign_batch_notifications`. The older `get_sms_campaign_message`
(`…/campaigns/{campaignId}/messages/{notificationId}`) was removed together
with its gateway route.

## Preview with a signed link

`preview_sms_notification(hash=...)` opens with the signed link alone — no API
key and no sign-in are needed (scope `optional`). See the README section
"Preview a notification with its signed link".
