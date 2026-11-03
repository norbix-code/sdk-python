# Push on the API — own devices, own messages, campaigns

[← Back to the notifications reference](./notifications.md)

`notifications.md` lists every push method with its verb, path and scope.
This page covers the seven end-user routes (the app registers its own device
and reads its own messages) and the two campaign bodies whose shape the server
picks from a discriminator inside the body.

Everything here is asserted in `tests/api/test_notifications.py`.

## Registering the app's own device

`register_own_push_device` registers (or refreshes) a push device for the
signed-in user. Two values are required:

| field | value |
|---|---|
| `provider` | who issued the token: `fcm` (Android / Firebase) or `apns` (iOS). Send the **native** device token — in an Expo app use `getDevicePushTokenAsync()`. An Expo push token (provider `expo`) is refused with `CM-ERRORS-PUSH-016`. |
| `token` | the push token, exactly as the provider gave it |

The rest describes the device and is optional: `platform` (`ios`, `android`,
`web`), `osName`, `osVersion`, `appVersion`, `deviceName`, `modelName`,
`brand`, `manufacturer`, `installationId` (a stable id the app keeps for this
installation — not the token), `locale` (`lt-LT`), `timeZone` (IANA,
`Europe/Vilnius`).

```python
device = norbix.api.notifications.register_own_push_device(
    provider="apns",
    token=native_token,
    platform="ios",
    appVersion="2.4.1",
    locale="lt-LT",
    timeZone="Europe/Vilnius",
)
device["id"]  # pnd_…
```

The same token again refreshes the device and answers the same id; a token
another user held moves to the caller. `get_own_push_devices` lists the
caller's devices, last refreshed first (`{"items": [...]}`).

## Signing out of a device

Two deletes, both of the caller's own devices only:

```python
norbix.api.notifications.delete_own_push_device("pnd_123")        # by id — another user's device is not found
norbix.api.notifications.delete_own_push_device_by_token(token=native_token)  # by token — sign-out, safe to repeat
```

`delete_own_push_device_by_token` is the sign-out call: the app does not need
to remember the device id, only the token it registered with. A DELETE carries
no body in this SDK, so `token` travels as a query value on the collection
path.

## Reading the user's own messages

`get_own_push_messages` lists the push messages sent to the caller, newest
first, paged with `pageSize` / `pageNumber`; `unreadOnly=True` keeps the
unread ones. The answer is `{"list": {"items", "totalCount", ...}}`.

```python
page = norbix.api.notifications.get_own_push_messages(unreadOnly=True, pageSize=20)
for message in page["list"]["items"]:
    norbix.api.notifications.mark_own_push_message_read(message["id"])  # ntf_…
norbix.api.notifications.mark_all_own_push_messages_read()
```

Both mark-read calls post with no body and are safe to repeat; another user's
message is not found.

## Campaigns from an app key

`create_push_campaign` and `get_push_campaign_audience_count` are the same
gateway services the Hub serves: the audience sits under `campaign["source"]`
with that audience's own fields, plus `templateId` and `integrationId` (the
push provider) — exactly as in
[HUB · Push — choosing who a campaign goes to](../hub/push.md#choosing-who-a-campaign-goes-to).
Next to `campaign` the request takes the optional `databaseIntegrationId` and
`sendNow`.

```python
count = norbix.api.notifications.get_push_campaign_audience_count(
    campaign={"source": "allUsers", "userTags": ["beta"]}
)
count["result"]["devices"]

campaign = norbix.api.notifications.create_push_campaign(
    campaign={
        "source": "devices",
        "templateId": "tpl_123",
        "integrationId": "int_push",
        "devices": [{"token": native_token, "deliveryFamily": "Ios"}],
    }
)
campaign["id"]
```

`sendNow=True` sends at once (or at a `campaignTime` sooner than the review
window). Without it a campaign created by an AI tool must be scheduled at
least 24 hours ahead for role-based / all-users / collection audiences and
1 hour ahead for direct recipient lists, or it is refused with
`CM-ERRORS-CAMPAIGNS-017`.

Reading a campaign back (`get_push_campaign`, `_batches`,
`_batch_notifications`, `_statistics`, `_messages`), stopping it and retrying
its failed recipients work as on every channel — see
[notifications.md](./notifications.md#what-is-the-same-on-every-channel).
