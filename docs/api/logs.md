# API · Logs

Access with `norbix.api.logs`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `write_logs` | `POST` | `/{version}/logs` | `project` |

Write your app's own log entries. Send 1–100 entries in one call. They are
queued: the call returns at once with `{"accepted": n}`. Read them back on the
Hub with `norbix.hub.logs.get_logs` / `get_log` (see [HUB · Logs](../hub/logs.md)).

Each entry:

| Field | Required | Rule |
| --- | --- | --- |
| `title` | yes | ≤ 200 characters |
| `level` | no | `"information"`, `"warning"` or `"error"` |
| `message` | no | ≤ 8000 characters |
| `eventCode` | no | a-z, 0-9, `_ . : -`, ≤ 64; stored as `app:<code>` |
| `correlationId` | no | letters, digits, `_ -`, ≤ 64 |
| `timestamp` | no | ISO-8601 UTC string, at most 7 days old and 5 minutes ahead |
| `meta` | no | string → string map, ≤ 20 keys |

`projectId` is optional; the client's project is used when it is left out.

```python
from datetime import datetime, timezone

result = norbix.api.logs.write_logs(entries=[
    {
        "level": "error",
        "title": "Checkout failed",
        "message": "card declined",
        "eventCode": "checkout.failed",
        "correlationId": request_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "meta": {"orderId": order_id},
    },
])
print(result["accepted"])
```

`timestamp` must be a string: pass `datetime.isoformat()`, not the `datetime`
itself.

## Refusals

| HTTP | Error | When |
| --- | --- | --- |
| 400 | `ValidationError` | an entry breaks a rule above |
| 400 | `ValidationError`, `CM-ERRORS-LOGGING-002` | the Logs module is off for the project |
| 429 | `RateLimitError`, `CM-ERRORS-LOGGING-003` | the project's per-minute quota is used up |

The SDK does not retry `write_logs` (it is a POST). On a 429 the gateway sends
a `Retry-After` header with the seconds to wait; the SDK puts it on the error as
`retry_after_seconds` (`None` when the header is absent or unreadable):

```python
from norbix_python import RateLimitError

try:
    norbix.api.logs.write_logs(entries=entries)
except RateLimitError as exc:
    time.sleep(exc.retry_after_seconds or 60)  # then send the entries again
```
