# HUB · Code

Access with `norbix.hub.code` (and the same methods, awaited, on
`AsyncNorbix`). The Code module holds the credentials of your own cloud
(AWS Lambda, Azure Functions, Google Cloud Functions) as **Code
integrations**, lists the functions it may call, invokes them by hand, and
is what a trigger's `Code` action and a scheduler `CodeFunctionalCall` task
point at. Norbix does not host code: the function runs in your cloud and
receives one event envelope — see [Cloud functions](#cloud-functions).

Keyword arguments other than the path ids, `timeout` and `bearer_token` are
the request: the query string for `GET` / `DELETE`, the JSON body otherwise.
Integration ids look like `int_…`.

## Module and integrations

| Method | Verb | Path | Scope | Parameters go in |
| --- | --- | --- | --- | --- |
| `enable_code` | `PUT` | `/{version}/code/enable` | `project` | — |
| `disable_code` | `PUT` | `/{version}/code/disable` | `project` | — |
| `get_code_integrations` | `GET` | `/{version}/code/integrations` | `project` | query |
| `get_code_integration` | `GET` | `/{version}/code/integrations/{id}` | `project` | path: `id` |
| `save_code_integration` | `POST` | `/{version}/code/integrations` | `project` | JSON body |
| `test_code_integration` | `POST` | `/{version}/code/integrations/test` | `project` | JSON body |
| `confirm_code_integration_human_delivery` | `POST` | `/{version}/code/integrations/confirm-human-delivery` | `project` | JSON body |
| `enable_code_integration` | `PUT` | `/{version}/code/integrations/{Id}/enable` | `project` | path: `id` |
| `disable_code_integration` | `PUT` | `/{version}/code/integrations/{Id}/disable` | `project` | path: `id` |
| `delete_code_integration` | `DELETE` | `/{version}/code/integrations/{Id}` | `project` | path: `id` |

## Marketplace

The 28 routes of the gateway contract `Code.Marketplace.md` §14: the catalog
of listings, the installed connections (integration ids look like `int_…`),
their secrets and token mappings, and the functions added on a connection
(`func_…`). Every method, its verb, path, query and body are asserted in
`tests/hub/test_code.py`, for the sync and the async client.

| Method | Verb | Path | Scope | Parameters go in |
| --- | --- | --- | --- | --- |
| `get_marketplace_listings` | `GET` | `/{version}/code/marketplace/listings` | `project` | query: `categories`, `transports`, `search`, `officialOnly`, `tags` |
| `get_marketplace_listing_function_tokens` | `GET` | `/{version}/code/marketplace/listings/{ListingViewId}/functions/{FunctionKey}/tokens` | `project` | path: `listing_view_id`, `function_key` |
| `get_marketplace_integrations` | `GET` | `/{version}/code/marketplace/integrations` | `project` | — |
| `get_marketplace_integration` | `GET` | `/{version}/code/marketplace/integrations/{IntegrationViewId}` | `project` | path: `integration_view_id` |
| `save_marketplace_integration` | `POST` | `/{version}/code/marketplace/integrations` | `project` | JSON body: `integration`, `secrets` |
| `delete_marketplace_integration` | `DELETE` | `/{version}/code/marketplace/integrations/{IntegrationViewId}` | `project` | path: `integration_view_id` |
| `enable_marketplace_integration` | `POST` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/enable` | `project` | path: `integration_view_id` |
| `disable_marketplace_integration` | `POST` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/disable` | `project` | path: `integration_view_id` |
| `get_marketplace_functions` | `GET` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/functions` | `project` | path: `integration_view_id` |
| `get_marketplace_function` | `GET` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}` | `project` | path: `integration_view_id`, `function_view_id` |
| `save_marketplace_function` | `POST` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/functions` | `project` | path: `integration_view_id`; JSON body: `function` |
| `delete_marketplace_function` | `DELETE` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}` | `project` | path: `integration_view_id`, `function_view_id` |
| `enable_marketplace_function` | `POST` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/enable` | `project` | path: `integration_view_id`, `function_view_id` |
| `disable_marketplace_function` | `POST` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/disable` | `project` | path: `integration_view_id`, `function_view_id` |
| `get_marketplace_function_tokens` | `GET` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/tokens` | `project` | path: `integration_view_id`, `function_view_id` |
| `invoke_marketplace_function` | `POST` | `/{version}/code/marketplace/functions/{FunctionViewId}/invoke` | `project` | path: `function_view_id`; JSON body: `payload` |
| `get_marketplace_listing` | `GET` | `/{version}/code/marketplace/listings/{ListingViewId}` | `project` | path: `listing_view_id` |
| `test_marketplace_integration` | `POST` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/test` | `project` | path: `integration_view_id` |
| `get_marketplace_integration_tools` | `GET` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/tools` | `project` | path: `integration_view_id`; returns the stored MCP tool catalog (`tools`, `listedAt`, `catalogHash`, `truncated`) |
| `get_marketplace_integration_access` | `GET` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/access` | `project` | path: `integration_view_id`; returns the access matrix (`roles`, `packages`, `tools`, `functions`) |
| `set_marketplace_integration_role_access` | `PUT` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/access/roles` | `project` | path: `integration_view_id`; JSON body: `roleId`, `package` (`None`, `Viewer`, `FunctionsOnly`, `ReadOnly`, `FullAccess`), `manage`; returns the role id |
| `save_marketplace_integration_custom_access` | `POST` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/access/roles/custom` | `project` | path: `integration_view_id`; JSON body: `roleId`, `basePackage`, `tools`, `functions`, `manage`, `newPolicyForThisRoleOnly`; returns `policyId`, `created`, `usedByRoles` |
| `start_marketplace_integration_sign_in` | `POST` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/oauth/start` | `project` | path: `integration_view_id`; returns `authorizeUrl` (open it in a browser), `redirectUrl`, `expiresAt` |
| `replace_marketplace_integration_secrets` | `PUT` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/secrets` | `project` | path: `integration_view_id`; JSON body: `secrets` |
| `reveal_marketplace_integration_secrets` | `POST` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/secrets/reveal` | `project` | path: `integration_view_id` |
| `set_marketplace_integration_token_mappings` | `PUT` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/token-mappings` | `project` | path: `integration_view_id`; JSON body: `tokenMappings` |
| `get_marketplace_function_catalog` | `GET` | `/{version}/code/marketplace/integrations/{IntegrationViewId}/catalog` | `project` | path: `integration_view_id` |
| `get_marketplace_function_runs` | `GET` | `/{version}/code/marketplace/functions/runs` | `project` | query: exactly one of `functionId` / `triggerId` / `taskId`, `limit` (1–50, default 20); newest first |

```python
listings = norbix.hub.code.get_marketplace_listings(search="slack")
runs = norbix.hub.code.get_marketplace_function_runs(triggerId="trg_…", limit=5)
result = norbix.hub.code.invoke_marketplace_function("func_…", payload={"text": "Order shipped"})
```

### Marketplace function runs and their details

Each call of a marketplace function is one run row: an invoke (user, API key,
AI), a trigger run or a scheduler fire. `functionId` lists every source of one
function (up to 50 kept); `triggerId` / `taskId` list the runs one trigger or
task started (20 kept). A row carries `status` (`ok` / `failed` / `skipped`,
`None` on rows written before the field existed), `durationMs`, `source`
(`user`, `api-key`, `ai`, `trigger`, `scheduler`), `event`, `correlationId`
and `hasDetails`.

The input, steps and response of a run are written to the project log under
the row's `correlationId`, only while the environment's Norbix Logging is on —
then `hasDetails` is `True`. Read them with the logs route; its query field is
`targetCorrelationId`:

```python
runs = norbix.hub.code.get_marketplace_function_runs(functionId="func_…", limit=10)
for run in runs.get("runs", []):
    if not run.get("hasDetails"):
        continue  # logs were off for this run
    details = norbix.hub.logs.get_logs_by_correlation_id(targetCorrelationId=run["correlationId"])
    # details["items"]: marketplace:run:started → marketplace:run:step … → completed | failed | skipped
```

## Cloud functions

The five routes of the gateway contract `Code.Functions.md` (§3.3, §3.4,
§5.1). Every method, its verb, path, query and body are asserted in
`tests/hub/test_code.py`, for the sync and the async client.

| Method | Verb | Path | Scope | Parameters go in |
| --- | --- | --- | --- | --- |
| `get_code_functions` | `GET` | `/{version}/code/functions` | `project` | query: `integrationId` (required), `prefix`, `tag` (`key` or `key=value`), `pageSize`, `startingAfter`, `endingBefore` |
| `get_code_function_qualifiers` | `GET` | `/{version}/code/functions/qualifiers` | `project` | query: `integrationId`, `functionId` |
| `invoke_code_function` | `POST` | `/{version}/code/functions/invoke` | `project` | JSON body: `functionRef` `{integrationId, functionId, qualifier?}`, `payload?`, `invocationType` (`Sync` / `Async`), `runAsUserId?`, `config?` |
| `get_code_function_event_sample` | `GET` | `/{version}/code/functions/event-sample` | `project` | query: `source` (`database` · `membership` · `files` · `payments` · `ai` · `scheduler` · `manual`, any case), `event?`, `schemaId?` |
| `get_code_function_runs` | `GET` | `/{version}/code/functions/runs` | `project` | query: exactly one of `triggerId` / `taskId`, `limit` (1–50, default 20); the last runs, newest first; each run carries `input` — the scrubbed envelope a Fake-provider run received |

```python
integration_id = "int_6rBACnEaxQ0x1jTiHtAuWV"
functions = norbix.hub.code.get_code_functions(integrationId=integration_id, prefix="orders-")
qualifiers = norbix.hub.code.get_code_function_qualifiers(integrationId=integration_id, functionId="orders-on-update")
result = norbix.hub.code.invoke_code_function(
    functionRef={"integrationId": integration_id, "functionId": "orders-on-update", "qualifier": "prod"},
    payload={"orderId": "6ac54a59212c29912eaddd81", "dryRun": True},
    invocationType="Sync",
)
sample = norbix.hub.code.get_code_function_event_sample(source="database", event="database.record.updated")
runs = norbix.hub.code.get_code_function_runs(triggerId="trg_…", limit=5)
```

`get_code_functions` is a live listing from the provider (no Norbix-side
state), paged in memory on the function id. An Azure integration cannot list
(`CM-ERRORS-CODE-010`) — type the function name instead. `invoke_code_function`
answers `{statusCode, output, durationMs, requestId?, logs?}`; `output` is the
function's body as JSON when it parses, else the raw text. `runs` is the last
20 (up to 50) runs of one trigger or task, newest first:
`{firedAt, event, source, succeeded, statusCode?, durationMs?, error?, requestId?}`.

### The event envelope — `parse_function_event`

Inside the function, the SDK reads the envelope Norbix sent
(`CodeFunctionEventDto`, one shape for every source) and gives you a client
that acts as the run-as user:

```python
import json

from norbix_python import Norbix, parse_function_event


def handler(raw, _context):                       # AWS Lambda; Azure / Google pass the body the same way
    event = parse_function_event(raw)             # str, bytes or the decoded dict; raises on specVersion != "1"
    if event.event != "database.record.updated":
        return {"ok": True}

    change = event.as_database_record_change()    # .old / .new as dicts, None when absent
    old, new = change.old or {}, change.new or {}
    if old.get("status") != new.get("status") and new.get("status") == "processing":
        norbix = Norbix(**event.client_options())  # project, env, region, hub / api urls, the run-as token
        norbix.api.database.insert_one(
            "order_events",
            document=json.dumps({"orderId": new["_id"], "status": "processing", "eventId": event.event_id}),
        )
    return {"ok": True}
```

| On the event | What it is |
| --- | --- |
| `event`, `event_id`, `id`, `source`, `created_on`, `spec_version` | the envelope header; `event` is the handler key (`database.record.updated`, `scheduler.task.fired`, `manual.invoke`, …), `source` one of `database` · `membership` · `files` · `payments` · `ai` · `scheduler` · `manual` |
| `context` | `project_id`, `account_id`, `environment`, `region`, `hub_url`, `api_url`, `echo_url`, `trigger_id` / `task_id`, `correlation_id`, `caller` (`user_id`, `email`, `kind` — data, never authority), `run_as` (`user_id`, `access_token` valid 15 minutes, `expires_at`) |
| `as_database_record_change()` | `collection`, `schema_id`, `schema_version`, `record_id`, `old`, `new`, `truncated`, `old_ref` / `new_ref` (over 200 KB the documents are left out and the refs say where to fetch them) |
| `as_user_change()` | `user_id`, `old`, `new` |
| `as_file_change()` | `old` (delete), `new` (upload), `path` |
| `as_payment()` | `integration_id`, `provider`, `provider_event_id`, `event_name`, `status`, `amount_minor`, `currency`, `external_ids`, `occurred_on`, `received_on` |
| `as_scheduled_task()` | `task_id`, `name`, `fired_at` |
| `as_ai_usage()` | `payload`, `target_user_id` |
| `payload()` | the caller's JSON on a manual invoke, or a scheduler task's static payload; `None` when there is none |
| `config` | the developer's JSON bound at fire time; `None` when the action has none |
| `client_options()` | the `Norbix` / `AsyncNorbix` keyword arguments: `project_id`, `account_id`, `env`, `region`, `bearer_token`, `base_url_hub`, `base_url_api` |
| `raw` | the decoded envelope, for anything else |

A view of a slot the event does not carry (a file event asked for a record
change) raises `NorbixFunctionEventError`, as does a payload that is not an
object or not `specVersion` `"1"`. Timestamps stay ISO-8601 strings. Every
sample source, the refusals and the client built from an event are asserted
in `tests/test_functions.py`. A sample envelope for a local run comes from
`get_code_function_event_sample`.
