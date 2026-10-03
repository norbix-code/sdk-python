# HUB · Email

Access with `norbix.hub.email`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `one_click_unsubscribe` | `POST` | `/{version}/email/one-click-unsubscribe` | `optional` |
| `get_email_preferences_by_link` | `GET` | `/{version}/email/preferences` | `optional` |

`get_email_preferences_by_link(token=...)` reads the marketing e-mail preferences of the
person a signed unsubscribe link belongs to. The signed token is the key: it works on a
client with no API key or bearer token (scope `optional` — a token is sent only when the
client has one).

Both methods are public links: `one_click_unsubscribe` is also sent without credentials
when the client has none.
