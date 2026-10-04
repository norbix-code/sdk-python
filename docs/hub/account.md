# HUB · Account

Access with `norbix.hub.account`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `get_account_profile` | `GET` | `/{version}/account/profile` | `account` |
| `update_account_profile` | `PUT` | `/{version}/account/profile` | `account` |
| `resend_account_verification_token` | `GET` | `/{version}/account/verify/resend` | `account` |
| `get_account_status` | `GET` | `/{version}/account/status` | `account` |
| `create_stripe_checkout_session` | `POST` | `/{version}/account/stripe/create-checkout-session` | `account` |
| `get_stripe_billing_portal_url` | `POST` | `/{version}/account/stripe/get-portal-url` | `account` |
| `create_team_member_from_invitation` | `POST` | `/{version}/account/team/member` | `account` |
| `verify_account` | `GET` | `/{version}/account/verify` | `account` |
| `delete_notifications_group` | `DELETE` | `/{version}/account/projects/{projectId}/notifications/settings/group` | `account` |
| `delete_notifications_tag` | `DELETE` | `/{version}/account/projects/{projectId}/notifications/settings/tag` | `account` |
| `remove_tag_from_notifications_group` | `DELETE` | `/{version}/account/projects/{projectId}/notifications/settings/group/tag` | `account` |
| `save_notifications_group` | `POST` | `/{version}/account/projects/{projectId}/notifications/settings/group` | `account` |
| `save_notifications_tag` | `POST` | `/{version}/account/projects/{projectId}/notifications/settings/tag` | `account` |
| `create_project` | `POST` | `/{version}/account/projects` | `account` |
| `delete_project` | `DELETE` | `/{version}/account/projects/{projectId}` | `account` |
| `get_project` | `GET` | `/{version}/account/projects/{projectId}` | `account` |
| `get_projects` | `GET` | `/{version}/account/projects` | `account` |
| `get_account_regions` | `GET` | `/{version}/account/regions` | `account` |
| `get_project_tokens` | `GET` | `/{version}/account/projects/{projectId}/tokens` | `account` |
| `update_project_accent_color` | `PATCH` | `/{version}/account/projects/{projectId}/settings/accent-color` | `account` |
| `update_project_icon` | `PATCH` | `/{version}/account/projects/{projectId}/settings/icon` | `account` |
| `update_project_logo` | `PATCH` | `/{version}/account/projects/{projectId}/settings/logo` | `account` |
| `update_project_main_color` | `PATCH` | `/{version}/account/projects/{projectId}/settings/main-color` | `account` |
| `update_project_allowed_origins` | `PATCH` | `/{version}/account/projects/{projectId}/settings/origins` | `account` |
| `update_project_default_language` | `PATCH` | `/{version}/account/projects/{projectId}/settings/default-language` | `account` |
| `update_project_description` | `PATCH` | `/{version}/account/projects/{projectId}/settings/description` | `account` |
| `disable_project` | `PATCH` | `/{version}/account/projects/{projectId}/disable` | `account` |
| `enable_project` | `PATCH` | `/{version}/account/projects/{projectId}/enable` | `account` |
| `check_project_languages` | `POST` | `/{version}/account/projects/{projectId}/settings/languages/check` | `account` |
| `update_project_languages` | `PATCH` | `/{version}/account/projects/{projectId}/settings/languages` | `account` |
| `update_project_url` | `PATCH` | `/{version}/account/projects/{projectId}/settings/url` | `account` |
| `update_project_name` | `PATCH` | `/{version}/account/projects/{projectId}/settings/name` | `account` |
| `update_project_regions` | `PATCH` | `/{version}/account/projects/{projectId}/settings/regions` | `account` |
| `create_account` | `POST` | `/{version}/account` | `account` |
| `get_account_collaborators` | `GET` | `/{version}/account/collaborators` | `account` |
| `send_invite_to_team_member` | `POST` | `/{version}/account/team/member/invite` | `account` |
| `get_licenses` | `GET` | `/{version}/account/licenses` | `account` |
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
