# API · Public

Access with `norbix.api.public` (or `client.public` on `NorbixApi`).

These routes need **no sign-in**: the gateway does not authenticate them, and
the SDK sends no `Authorization` header even when the client has a token.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `get_public_project_config` | `GET` | `/{version}/public/projects/{ProjectId}/config` | `unauthenticated` |
| `get_public_project_legal` | `GET` | `/{version}/public/projects/{ProjectId}/legal/{Kind}` | `unauthenticated` |

`get_public_project_legal` takes `kind` = `"terms"` or `"privacy"` and gives
back `{kind, title, body, available}` (Markdown in `body`). `available` is
`False` until the project turns the legal pages on with
`norbix.hub.account.update_project_expose_legal(project_id, exposed=True)`.
