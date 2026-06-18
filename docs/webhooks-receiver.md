# Webhook receiver (`norbix_python.webhooks`)

Handle **inbound** Norbix webhook deliveries at your HTTP endpoint. This is the
subscriber side — distinct from `client.hub.webhooks`, which configures
destinations via the Hub API.

## Quick start

```python
from norbix_python.webhooks import (
    NorbixWebhookReceiver,
    NorbixWebhookEvents,
    NORBIX_WEBHOOK_EVENT_NAMES,
    UserDto,
    WebhookEvent,
)

# No arguments → reads NORBIX_WEBHOOK_SIGNING_SECRET (and friends) from env.
receiver = NorbixWebhookReceiver()


# Register as a decorator — the first arg IS the payload, the second is metadata.
@receiver.on(NorbixWebhookEvents.Membership.USER_REGISTERED)
def on_registered(user: UserDto, event: WebhookEvent) -> None:
    print(user.email or user.user_name, event.metadata.user)


# ...or as a plain method call.
receiver.on(NorbixWebhookEvents.Database.RECORD_INSERTED, on_record)

# One raw logger for every event — runs in addition to any `on` handler.
receiver.on_all(NORBIX_WEBHOOK_EVENT_NAMES, lambda envelope, ctx: print(envelope.event))

# In your web framework (Flask/FastAPI/Django), pass the raw body + headers:
result = receiver.handle(raw_body=body, headers=request.headers)
```

`AsyncNorbixWebhookReceiver` is the async twin — same API, `await receiver.handle(...)`,
and handlers may be `async def`.

## Configuration

`NorbixWebhookReceiver(...)` reads these env vars; any argument you pass overrides
the env var.

| Env var | Argument | Default |
|---------|----------|---------|
| `NORBIX_WEBHOOK_SIGNING_SECRET` | `secret` | — (verify skipped if unset) |
| `NORBIX_WEBHOOK_TOLERANCE_SECONDS` | `tolerance_seconds` | `300` |
| `NORBIX_PROJECT_ID` | `project_id` (guard) | — |
| `NORBIX_ACCOUNT_ID` | `account_id` (guard) | — |

When `project_id` / `account_id` are set, a delivery whose envelope does not
match raises `NorbixWebhookSignatureError`.

## Payloads — `from`/`to` only when you must compare

The payload differs by trigger kind. Create, delete, and single-property state
flips give the **entity directly**; only an arbitrary mutation gives a
`Mutation` (`from_` / `to`). Batch events give a list.

| Event | Kind | Handler payload |
|-------|------|-----------------|
| `membership.user.registered` | entity | `UserDto` |
| `membership.user.verified` / `blocked` / `reactivated` | entity (state flip) | `UserDto` |
| `membership.user.deleted` | entity | `UserDto` |
| `membership.user.updated` | mutation | `Mutation[UserDto]` (`.from_`, `.to`) |
| `database.record.inserted` / `deleted` | entity | the document (`dict`) |
| `database.record.updated` / `replaced` | mutation | `Mutation` of documents |
| `database.records.inserted` | batch | `list` of documents |
| `files.file.uploaded` | entity | `FileResourceRef` |

Wrapper identifiers (entity id, schema, record ids) are lifted onto
`event.metadata` (`event.metadata.user`, `.schema`, `.record`, `.records`).

```python
@receiver.on(NorbixWebhookEvents.Membership.USER_UPDATED)
def on_updated(change, event):           # change: Mutation[UserDto]
    if change.from_.email != change.to.email:
        ...  # email changed
```

> Python note: `from` is a keyword, so the mutation field is `from_` (its JSON
> alias is still `from`).

## Signature verification

Norbix signs each delivery with `X-Norbix-Signature: sha256=<hex>` over
`"<timestamp>.<rawBody>"`. Configure the project signing secret
(`client.hub.webhooks.reveal_webhook_integration_secret()`) or set
`NORBIX_WEBHOOK_SIGNING_SECRET`. With no secret configured, verification is
skipped and `result.verified` is `None`.

## API

| Export | Description |
|--------|-------------|
| `NorbixWebhookReceiver` | Sync receiver — `.on`, `.on_all`, `.handle()` |
| `AsyncNorbixWebhookReceiver` | Async twin (`await .handle()`) |
| `NorbixWebhookEvents` | Named event constants |
| `NORBIX_WEBHOOK_EVENT_NAMES` | Closed catalog of event names |
| `UserDto`, `FileResourceRef`, `Mutation`, `UserMutation` | Payload models |
| `WebhookEvent`, `WebhookContext`, `WebhookEnvelope` | Metadata / raw models |
| `verify_signature`, `compute_signature`, `parse_webhook_headers` | Low-level helpers |
| `normalize_webhook` | Envelope → `(payload, metadata)` |

Errors: `NorbixWebhookSignatureError`, `NorbixWebhookParseError`
(both extend `NorbixWebhookError` → `NorbixError`).
```
