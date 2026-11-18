# API · Public

Access with `norbix.api.public` (or `client.public` on `NorbixApi`).

These routes need **no sign-in**: the gateway does not authenticate them, and
the SDK sends no `Authorization` header even when the client has a token.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `get_public_project_config` | `GET` | `/{version}/public/projects/{ProjectId}/config` | `unauthenticated` |
| `get_public_project_legal` | `GET` | `/{version}/public/projects/{ProjectId}/legal/{Kind}` | `unauthenticated` |
| `get_public_project_brand_asset` | `GET` | `/{version}/public/projects/{ProjectId}/brand/{Kind}` | `unauthenticated` |

`get_public_project_legal` takes `kind` = `"terms"` or `"privacy"` and gives
back `{kind, title, body, available}` (Markdown in `body`). `available` is
`False` until the project turns the legal pages on with
`norbix.hub.account.update_project_expose_legal(project_id, exposed=True)`.

`get_public_project_brand_asset` takes `kind` = `"logo"` or `"icon"` and gives
back the image `bytes` (the address `get_public_project_config` hands out as
`branding.logoUrl` / `iconUrl`). It answers only while the project exposes its
brand; every miss is a plain 404. A logo kept in a cloud bucket answers 302 to
a signed link, and the call follows it.
