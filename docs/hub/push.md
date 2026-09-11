# Push — choosing an audience and a provider

[← Back to the notifications reference](./notifications.md)

`notifications.md` lists every push method with its verb, path and scope. Two
of them take a body whose shape the server picks from a discriminator inside
that body, which the signature cannot show. This page covers those two.

Everything here is asserted in `tests/hub/test_push.py`.

## Choosing who a campaign goes to

`create_push_campaign` reads the audience from `campaign["source"]`. Send that
field plus the audience's own fields:

| audience | `source` | own fields |
|---|---|---|
| everyone in the project | `allUsers` | `rolesNames`, `userTags` (both optional filters) |
| a named list of project users | `specifiedUsers` | `userRecipients` |
| a named list of account users | `accountUsers` | `userRecipients` |
| rows of a database collection | `collection` | `schemaName`, `fields`, `fieldType` |
| raw device tokens | `devices` | `devices` |

```python
client.hub.notifications.create_push_campaign(
    campaign={
        "source": "allUsers",
        "templateId": "tpl_123",
        "userTags": ["beta"],
    }
)
```

Send `source` as the name, not a number — the server reads it as a string.

## Choosing a push provider

`save_push_integration` works the same way, with `integration["provider"]`:

| provider | `provider` value |
|---|---|
| Fake (sandbox, never sends) | `Fake` |
| Android / Firebase | `AndroidFirebase` |
| Apple APNs | `AppleApns` |
| Chrome extension | `CodeMashChromePlugin` |
| Chrome web | `ChromeWeb` |
| Edge web | `EdgeWeb` |
| Firefox web | `FirefoxWeb` |
| Safari | `SafariPush` |

```python
client.hub.notifications.save_push_integration(
    integration={"provider": "Fake", "integrationName": "sandbox", "isEnabled": True}
)
```

Use `Fake` in tests and local development. It accepts a send and contacts no
push service, so nothing reaches a real device.

## Known gaps

| what | why |
|---|---|
| `check_integration_availability` and the CodeMash-app test call | they point at gateway routes that are commented out, so they are not callable. |
| `get_push_campaign_message` | the gateway route declares an `{id}` token that no request field matches, so the endpoint is unreliable until that is fixed. |
