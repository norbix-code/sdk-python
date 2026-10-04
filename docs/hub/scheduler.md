# HUB · Scheduler

Access with `norbix.hub.scheduler` (and the same methods, awaited, on
`AsyncNorbix`). The scheduler runs a task on a cron schedule.

| Method | Verb | Path | Scope | Parameters go in |
| --- | --- | --- | --- | --- |
| `enable_scheduler` | `PUT` | `/{version}/scheduler/enable` | `project` | — |
| `disable_scheduler` | `PUT` | `/{version}/scheduler/disable` | `project` | — |
| `get_scheduler_tasks` | `GET` | `/{version}/scheduler/tasks` | `project` | query: `pageSize`, `startingAfter`, `endingBefore`, `type`, `enabled` |
| `get_scheduler_task` | `GET` | `/{version}/scheduler/tasks/{id}` | `project` | path: `id` |
| `save_scheduler_task` | `POST` | `/{version}/scheduler/tasks` | `project` | JSON body (see below) |
| `enable_scheduler_task` | `PUT` | `/{version}/scheduler/tasks/{Id}/enable` | `project` | path: `id` |
| `disable_scheduler_task` | `PUT` | `/{version}/scheduler/tasks/{Id}/disable` | `project` | path: `id` |
| `delete_scheduler_task` | `DELETE` | `/{version}/scheduler/tasks/{Id}` | `project` | path: `id` |

Keyword arguments other than `id`, `timeout` and `bearer_token` are the
request: the query string for `GET` / `DELETE`, the JSON body otherwise. Task
ids look like `tsk_…`. Every method, its path, its query and its body are
asserted in `tests/hub/test_scheduler.py`, for the sync and the async client.

> **Module enable / disable are `PUT`.** Versions up to 3.5 sent `GET`; the
> gateway now answers only `PUT` on `/scheduler/enable` and
> `/scheduler/disable`, so the call from an older SDK fails. Upgrade the SDK.

## Turn the module on

```python
norbix.hub.scheduler.enable_scheduler()
```

## Save a task (create or update)

**Only `EmailCampaign` tasks run today.** `PushCampaign`, `SmsCampaign`,
`CodeFunctionalCall` and `WebhookCall` exist in the gateway's type list, but
it refuses them on save.

The body:

| field | required | meaning |
| --- | --- | --- |
| `initiatorUserId` | yes | the user the task runs as (`usr_…`): you, or a service user of this project |
| `name` | yes | display name |
| `cron` | yes | exactly **5 fields** (minute hour day-of-month month day-of-week), evaluated in **UTC** — `"0 9 * * 1"` is every Monday 09:00 UTC |
| `isEnabled` | yes | start enabled or not |
| `stopOnError` | yes | disable the task after a failed run |
| `task` | yes | what to run (below) |
| `taskId` | on update | the `tsk_…` id to update; leave it out to create |
| `description` | no | notes |

`task` is a dict:

| field | required | meaning |
| --- | --- | --- |
| `type` | yes | `"EmailCampaign"` — the name, as a string |
| `campaign` | yes | the email campaign to send: the same body the email campaign endpoints take — `source`, `templateId`, and the audience fields of that source |
| `databaseIntegrationId` | no | the database integration the campaign reads from |

`campaign["source"]` picks the audience: `AllUsers` (optional `rolesNames`,
`userTags`), `SpecifiedUsers` (`userRecipients`), `AccountUsers`
(`userRecipients`), `Email`, `Collection`. Every source also takes the optional
`integrationId`, `language`, `notes` and `mappedTokens`.

```python
saved = norbix.hub.scheduler.save_scheduler_task(
    initiatorUserId="usr_123",
    name="Weekly digest",
    cron="0 9 * * 1",  # Mondays 09:00 UTC
    isEnabled=True,
    stopOnError=False,
    task={
        "type": "EmailCampaign",
        "campaign": {
            "source": "AllUsers",
            "templateId": "etpl_123",
        },
    },
)
task_id = saved["id"]  # tsk_…
```

This goes on the wire as:

```json
{
  "initiatorUserId": "usr_123",
  "name": "Weekly digest",
  "cron": "0 9 * * 1",
  "isEnabled": true,
  "stopOnError": false,
  "task": {
    "type": "EmailCampaign",
    "campaign": { "source": "AllUsers", "templateId": "etpl_123" }
  }
}
```

To update, send the same body with `taskId="tsk_…"`.

## Read tasks

```python
page = norbix.hub.scheduler.get_scheduler_tasks(pageSize=20, type="EmailCampaign", enabled=True)
for row in page["list"]["items"]:
    print(row["taskId"], row["name"], row["cron"], row["isEnabled"])

one = norbix.hub.scheduler.get_scheduler_task(id="tsk_123")
# one["item"]["payloadJson"] holds the saved task body as JSON.
```

## Pause, resume, delete

```python
norbix.hub.scheduler.disable_scheduler_task(id="tsk_123")
norbix.hub.scheduler.enable_scheduler_task(id="tsk_123")
norbix.hub.scheduler.delete_scheduler_task(id="tsk_123")
```

## Async

```python
async with AsyncNorbix(project_id="proj_123", api_key="sk_...") as norbix:
    body = {
        "initiatorUserId": "usr_123",
        "name": "Weekly digest",
        "cron": "0 9 * * 1",
        "isEnabled": True,
        "stopOnError": False,
        "task": {"type": "EmailCampaign", "campaign": {"source": "AllUsers", "templateId": "etpl_123"}},
    }
    saved = await norbix.hub.scheduler.save_scheduler_task(**body)
```
