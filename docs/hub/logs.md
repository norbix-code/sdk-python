# HUB · Logs

Access with `norbix.hub.logs`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disable_logging` | `PUT` | `/{version}/logs/disable` | `project` |
| `enable_logging` | `PUT` | `/{version}/logs/enable` | `project` |
| `get_logs` | `GET` | `/{version}/logs` | `project` |
| `get_log` | `GET` | `/{version}/logs/{Id}` | `project` |
| `get_logs_by_correlation_id` | `GET` | `/{version}/logs/audit` | `project` |
| `clean_logs` | `POST` | `/{version}/logs/clean` | `project` |
| `get_log_settings` | `GET` | `/{version}/logs/settings` | `project` |
| `save_log_settings` | `POST` | `/{version}/logs/settings` | `project` |
| `delete_logging_integration` | `DELETE` | `/{version}/logs/integrations/{Id}` | `project` |
| `disable_logging_integration` | `PUT` | `/{version}/logs/integrations/{Id}/disable` | `project` |
| `enable_logging_integration` | `PUT` | `/{version}/logs/integrations/{Id}/enable` | `project` |
| `get_logging_integration` | `GET` | `/{version}/logs/integrations/{id}` | `project` |
| `get_logging_integrations` | `GET` | `/{version}/logs/integrations` | `project` |
| `save_logging_integration` | `POST` | `/{version}/logs/integrations` | `project` |
| `test_logging_integration` | `POST` | `/{version}/logs/integrations/test` | `project` |

Your app writes its own entries on the Api with `norbix.api.logs.write_logs`
(see [API · Logs](../api/logs.md)).

## Reading logs

`get_logs` takes the optional filters `level`, `module`, `logCorrelationId`,
`eventCode`, `search`, `metaKey` / `metaValue`, `fromUtc` / `toUtc` and the
cursor paging fields `pageSize`, `startingAfter`, `endingBefore`. An entry your
app wrote with `eventCode="order.paid"` is stored as `app:order.paid`.

```python
page = norbix.hub.logs.get_logs(level="error", eventCode="app:checkout.failed", pageSize=50)
for entry in page["list"]["items"]:
    print(entry["id"], entry["title"])

one = norbix.hub.logs.get_log(page["list"]["items"][0]["id"])["item"]

settings = norbix.hub.logs.get_log_settings()
norbix.hub.logs.save_log_settings(skipHttpBodyMeta=True)

norbix.hub.logs.clean_logs()  # deletes every entry stored in Norbix Logging
```

## Logging integrations

An integration sends the project's logs on to Datadog, AWS CloudWatch or
MongoDB. **After you save an integration, call `test_logging_integration`.
Nothing is delivered to an integration until its last test passed.**

```python
saved = norbix.hub.logs.save_logging_integration(**datadog_or_cloudwatch_or_mongodb_request)
norbix.hub.logs.test_logging_integration(integrationId=saved["id"])
```
