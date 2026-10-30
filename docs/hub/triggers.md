# HUB · Triggers

Access with `norbix.hub.triggers`. This module is hand-written (not generated).

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `get_triggers_needing_attention` | `GET` | `/{version}/triggers/attention` | `project` |

Pass `triggerType` — one of `Membership`, `Schema`, `Files`, `Payments`, `Ai`.
The answer is `{"items": [{"triggerId", "triggerType", "reason", "atUtc"}, ...]}`:
the triggers of that type that need a fix, for example because their provider
integration was deleted.

```python
norbix.hub.triggers.get_triggers_needing_attention(triggerType="Schema")
```

## The trigger action

Each module saves its own triggers (`database.save_schema_trigger`,
`files.save_files_trigger`, `membership.save_membership_trigger`,
`payments.save_payments_trigger`). They all send `trigger.action`, and the
server requires `integrationId` on it — the provider that does the work. Email,
Push and SMS actions also take the optional `language` (which template language
to send) and `initiatorId` (who the send is attributed to):

```python
norbix.hub.database.save_schema_trigger(
    trigger={
        "name": "welcome",
        "isEnabled": True,
        "action": {
            "type": "Email",
            "integrationId": "int_email",
            "templateId": "tpl_123",
            "language": "de",
            "initiatorId": "user_1",
        },
    }
)
```

Everything here is asserted in `tests/hub/test_triggers.py`.

## Send to the person the event is about

A Membership trigger's Email, Push or SMS action can send to the person the
event is about (the new user, the invited address, the deleted login): set
`deliverySettings` to `{"recipientsSourceType": "TriggerSubject"}`. One
recipient per firing.

```python
norbix.hub.membership.save_membership_trigger(
    trigger={
        "type": "Membership",
        "name": "welcome the new user",
        "when": "OnRegistered",
        "isEnabled": True,
        "action": {
            "type": "Email",
            "integrationId": "int_email",
            "templateId": "tpl_123",
            "deliverySettings": {"recipientsSourceType": "TriggerSubject"},
        },
    }
)
```

- Send only `recipientsSourceType`. The subject fields (`subjectAuthId`,
  `subjectEmail`, `subjectPhone`, `subjectLanguage`) are read-only: the gateway
  fills them on the campaign the trigger starts and ignores them on a save.
- The audience exists on Membership triggers only. Any other trigger type or a
  workflow step is refused with `CM-ERRORS-TRIGGERS-020`, and a hand-made
  campaign or a scheduled task cannot use it.
- With no address, phone or device for the channel nothing is sent: the run is
  logged as skipped and the trigger shows up in
  `get_triggers_needing_attention`.

## Order and "break on failure"

When several triggers fire for the same event, they run one after the other.
Two optional fields on `trigger` decide that queue (all four save methods):

- `order` — a whole number, 0 or more. Lower runs earlier; a trigger without
  an order runs after every numbered one; equal places run by name.
- `breakOnError` — `True` stops the triggers after this one when this
  trigger's action fails. Default `False`: the others still run.

```python
norbix.hub.membership.save_membership_trigger(
    trigger={
        "type": "Membership",
        "name": "welcome first",
        "when": "OnRegistered",
        "isEnabled": True,
        "order": 1,
        "breakOnError": True,
        "action": {"type": "Email", "integrationId": "int_email", "templateId": "tpl_123"},
    }
)
```

Both come back on `get_*_trigger` and on every row of `get_*_triggers`. A
negative `order` is refused with `CM-ERRORS-TRIGGERS-008`.

