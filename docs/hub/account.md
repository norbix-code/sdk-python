# HUB · Account

Access with `norbix.hub.account`.

Every method here needs only a key or a bearer token (scope `project`): the
gateway takes the account from the signed-in session, or from the project id
in the path, and never reads the `X-CM-AccountId` header. Four routes are
public on the gateway and need no token and no `account_id` at all (scope
`unauthenticated`, no `Authorization` header is sent): sign-up
(`create_account`), accepting an invitation
(`create_team_member_from_invitation`), the region list (`get_account_regions`,
also `norbix.hub.regions.list`) and `verify_account`, which takes the account
id once, in the request: `verify_account(accountId="acc_456", token="...")`.
Sync and async clients behave the same. Tests:
`tests/hub/test_account_token_only.py`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `get_account_profile` | `GET` | `/{version}/account/profile` | `project` |
| `update_account_profile` | `PUT` | `/{version}/account/profile` | `project` |
| `resend_account_verification_token` | `GET` | `/{version}/account/verify/resend` | `project` |
| `get_account_status` | `GET` | `/{version}/account/status` | `project` |
| `create_stripe_checkout_session` | `POST` | `/{version}/account/stripe/create-checkout-session` | `project` |
| `get_stripe_billing_portal_url` | `POST` | `/{version}/account/stripe/get-portal-url` | `project` |
| `create_team_member_from_invitation` | `POST` | `/{version}/account/team/member` | `unauthenticated` |
| `verify_account` | `GET` | `/{version}/account/verify` | `unauthenticated` |
| `delete_notifications_group` | `DELETE` | `/{version}/account/projects/{projectId}/notifications/settings/group` | `project` |
| `delete_notifications_tag` | `DELETE` | `/{version}/account/projects/{projectId}/notifications/settings/tag` | `project` |
| `remove_tag_from_notifications_group` | `DELETE` | `/{version}/account/projects/{projectId}/notifications/settings/group/tag` | `project` |
| `save_notifications_group` | `POST` | `/{version}/account/projects/{projectId}/notifications/settings/group` | `project` |
| `save_notifications_tag` | `POST` | `/{version}/account/projects/{projectId}/notifications/settings/tag` | `project` |
| `create_project` | `POST` | `/{version}/account/projects` | `project` |
| `delete_project` | `DELETE` | `/{version}/account/projects/{projectId}` | `project` |
| `get_project` | `GET` | `/{version}/account/projects/{projectId}` | `project` |
| `get_projects` | `GET` | `/{version}/account/projects` | `project` |
| `get_account_regions` | `GET` | `/{version}/account/regions` | `unauthenticated` |
| `get_project_tokens` | `GET` | `/{version}/account/projects/{projectId}/tokens` | `project` |
| `update_project_accent_color` | `PATCH` | `/{version}/account/projects/{projectId}/settings/accent-color` | `project` |
| `update_project_icon` | `PATCH` | `/{version}/account/projects/{projectId}/settings/icon` | `project` |
| `update_project_logo` | `PATCH` | `/{version}/account/projects/{projectId}/settings/logo` | `project` |
| `update_project_main_color` | `PATCH` | `/{version}/account/projects/{projectId}/settings/main-color` | `project` |
| `update_project_allowed_origins` | `PATCH` | `/{version}/account/projects/{projectId}/settings/origins` | `project` |
| `update_project_default_language` | `PATCH` | `/{version}/account/projects/{projectId}/settings/default-language` | `project` |
| `update_project_description` | `PATCH` | `/{version}/account/projects/{projectId}/settings/description` | `project` |
| `disable_project` | `PATCH` | `/{version}/account/projects/{projectId}/disable` | `project` |
| `enable_project` | `PATCH` | `/{version}/account/projects/{projectId}/enable` | `project` |
| `check_project_languages` | `POST` | `/{version}/account/projects/{projectId}/settings/languages/check` | `project` |
| `update_project_languages` | `PATCH` | `/{version}/account/projects/{projectId}/settings/languages` | `project` |
| `update_project_url` | `PATCH` | `/{version}/account/projects/{projectId}/settings/url` | `project` |
| `update_project_name` | `PATCH` | `/{version}/account/projects/{projectId}/settings/name` | `project` |
| `update_project_regions` | `PATCH` | `/{version}/account/projects/{projectId}/settings/regions` | `project` |
| `create_account` | `POST` | `/{version}/account` | `unauthenticated` |
| `get_account_collaborators` | `GET` | `/{version}/account/collaborators` | `project` |
| `get_my_account_user_profile` | `GET` | `/{version}/account/me` | `project` |
| `update_my_account_user_phone` | `PUT` | `/{version}/account/me/phone` | `project` |
| `send_invite_to_team_member` | `POST` | `/{version}/account/team/member/invite` | `project` |
| `get_licenses` | `GET` | `/{version}/account/licenses` | `project` |
| `get_project_ai_settings` | `GET` | `/{version}/account/projects/{projectId}/ai/settings` | `project` |
| `update_project_ai_settings` | `PUT` | `/{version}/account/projects/{projectId}/ai/settings` | `project` |
| `create_project_ai_assistant` | `POST` | `/{version}/account/projects/{projectId}/ai/assistants` | `project` |
| `update_project_ai_assistant` | `PUT` | `/{version}/account/projects/{projectId}/ai/assistants/{assistantId}` | `project` |
| `delete_project_ai_assistant` | `DELETE` | `/{version}/account/projects/{projectId}/ai/assistants/{assistantId}` | `project` |
| `get_project_ai_usage` | `GET` | `/{version}/account/projects/{projectId}/ai/usage` | `project` |
| `set_admin_portal_enabled` | `PUT` | `/{version}/account/projects/{projectId}/admin-portal/enabled` | `project` |
| `update_project_admin_url` | `PATCH` | `/{version}/account/projects/{projectId}/settings/admin-url` | `project` |
| `update_project_legal_documents` | `PATCH` | `/{version}/account/projects/{projectId}/settings/legal` | `project` |
| `update_project_expose_legal` | `PATCH` | `/{version}/account/projects/{projectId}/settings/legal/expose` | `project` |
| `update_project_expose_brand` | `PATCH` | `/{version}/account/projects/{projectId}/settings/brand/expose` | `project` |
| `update_project_expose_auth` | `PATCH` | `/{version}/account/projects/{projectId}/settings/auth/expose` | `project` |
| `get_admin_portal_structure` | `GET` | `/{version}/account/projects/{projectId}/admin-portal/structure` | `project` |
| `assign_admin_portal_service_user` | `PUT` | `/{version}/account/projects/{projectId}/settings/admin-portal/service-user` | `project` |
| `create_ai_service_user` | `POST` | `/{version}/account/ai/service-users` | `project` |
| `list_ai_service_users` | `GET` | `/{version}/account/ai/service-users` | `project` |
| `rotate_ai_service_user_key` | `POST` | `/{version}/account/ai/service-users/{Id}/keys` | `project` |
| `revoke_ai_service_user_key` | `DELETE` | `/{version}/account/ai/service-users/{Id}/keys/{KeyId}` | `project` |
| `delete_ai_service_user` | `DELETE` | `/{version}/account/ai/service-users/{Id}` | `project` |
| `mcp` | `POST` | `/{version}/account/mcp` | `project` |
| `mcp_stream` | `GET` | `/{version}/account/mcp` | `project` |
| `mcp_end_session` | `DELETE` | `/{version}/account/mcp` | `project` |

## Your account user and the team

`get_my_account_user_profile`, `update_my_account_user_phone` and
`get_account_collaborators` act on the signed-in account user and their
account. The gateway takes the account from the session, so they need only a
key or a bearer token — no `account_id`. Sync and async clients have the same
methods. Tests: `tests/hub/test_account_me.py`.

The phone (E.164 format, `+` and the country code; an empty value clears it)
is the number "Account users" SMS campaigns send to (see
[sms.md](./sms.md#choosing-who-a-campaign-goes-to)):

```python
norbix.hub.account.update_my_account_user_phone(phone="+37060000000")
me = norbix.hub.account.get_my_account_user_profile()
print(me["item"]["generalInfo"]["phone"])
```

The team list pages with flat fields — `pageSize` (default 20),
`startingAfter`, `endingBefore` — and `projectId` (without
`includeAccountOwner`) narrows it to one project's collaborators:

```python
team = norbix.hub.account.get_account_collaborators(projectId="proj_123", pageSize=50)
```

## The developer MCP endpoint

`mcp`, `mcp_stream` and `mcp_end_session` speak MCP Streamable HTTP
(revision 2025-11-25). They give back `{"status", "sessionId", "body", "events"}`:
`sessionId` is read from the `Mcp-Session-Id` answer header of `initialize`
and must be passed as `session_id` on every later call; `body` is the JSON-RPC
answer; `events` holds the messages of an SSE answer (a streamed `tools/call`,
or the `mcp_stream` server stream). `mcp_stream` does not stream: it returns
when the server closes the stream or `timeout` runs out.

```python
init = norbix.hub.account.mcp({"jsonrpc": "2.0", "id": 1, "method": "initialize",
                               "params": {"protocolVersion": "2025-11-25", "capabilities": {},
                                          "clientInfo": {"name": "my-agent", "version": "1.0"}}})
sid = init["sessionId"]
norbix.hub.account.mcp({"jsonrpc": "2.0", "method": "notifications/initialized"}, session_id=sid)
tools = norbix.hub.account.mcp({"jsonrpc": "2.0", "id": 2, "method": "tools/list"}, session_id=sid)
norbix.hub.account.mcp_end_session(sid)
```

An AI service user key (`nbsu_…`, from `create_ai_service_user` or
`rotate_ai_service_user_key`) works as the client's `api_key` / `bearer_token`
and narrows the tools the agent sees to the service user's scope.
