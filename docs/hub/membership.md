# HUB · Membership

Access with `norbix.hub.membership`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disable_membership` | `PUT` | `/{version}/membership/disable` | `project` |
| `enable_membership` | `PUT` | `/{version}/membership/enable` | `project` |
| `delete_membership_trigger` | `DELETE` | `/{version}/membership/triggers/{triggerId}` | `project` |
| `disable_membership_trigger` | `PATCH` | `/{version}/membership/triggers/{triggerId}/disable` | `project` |
| `enable_membership_trigger` | `PATCH` | `/{version}/membership/triggers/{triggerId}/enable` | `project` |
| `get_membership_trigger` | `GET` | `/{version}/membership/triggers/{id}` | `project` |
| `get_membership_triggers` | `GET` | `/{version}/membership/triggers` | `project` |
| `get_execution_identities` | `GET` | `/{version}/membership/execution-identities` | `project` |
| `create_execution_identity` | `POST` | `/{version}/membership/execution-identities` | `project` |
| `save_membership_trigger` | `POST` | `/{version}/membership/triggers` | `project` |
| `create_role` | `POST` | `/{version}/membership/roles` | `project` |
| `delete_role` | `DELETE` | `/{version}/membership/roles` | `project` |
| `get_role` | `GET` | `/{version}/membership/roles/{Id}` | `project` |
| `get_roles` | `GET` | `/{version}/membership/roles` | `project` |
| `update_role_policies` | `PATCH` | `/{version}/membership/roles` | `project` |
| `create_policy` | `POST` | `/{version}/membership/policies` | `project` |
| `delete_policy` | `DELETE` | `/{version}/membership/policies` | `project` |
| `get_policy` | `GET` | `/{version}/membership/policies/{Id}` | `project` |
| `get_policies` | `GET` | `/{version}/membership/policies` | `project` |
| `update_policy` | `PUT` | `/{version}/membership/policies` | `project` |
| `delete_membership_integration` | `DELETE` | `/{version}/membership/integrations/{Id}` | `project` |
| `disable_membership_integration` | `PUT` | `/{version}/membership/integrations/{Id}/disable` | `project` |
| `enable_membership_integration` | `PUT` | `/{version}/membership/integrations/{Id}/enable` | `project` |
| `get_membership_integration` | `GET` | `/{version}/membership/integrations/{id}` | `project` |
| `get_membership_integrations` | `GET` | `/{version}/membership/integrations` | `project` |
| `save_membership_integration` | `POST` | `/{version}/membership/integrations` | `project` |
| `set_membership_integration_as_default` | `PUT` | `/{version}/membership/integrations/{Id}/default` | `project` |
| `get_passkey_settings` | `GET` | `/{version}/membership/passkey/settings` | `project` |
| `save_passkey_settings` | `POST` | `/{version}/membership/passkey/settings` | `project` |
| `get_policy_options` | `GET` | `/{version}/membership/policies/new/options` | `project` |
| `create_contact` | `POST` | `/{version}/membership/users` | `project` |
| `get_all_contacts` | `GET` | `/{version}/membership/users` | `project` |
| `get_contact` | `GET` | `/{version}/membership/users/{contactId}` | `project` |
| `delete_contact` | `DELETE` | `/{version}/membership/users/{contactId}` | `project` |
| `merge_contacts` | `POST` | `/{version}/membership/users/merge` | `project` |
| `add_contact_identity` | `POST` | `/{version}/membership/users/{contactId}/identities` | `project` |
| `remove_contact_identity` | `DELETE` | `/{version}/membership/users/{contactId}/identities/{authId}` | `project` |
| `promote_contact_identity` | `POST` | `/{version}/membership/users/{contactId}/identities/{authId}/promote` | `project` |
| `update_authentication_settings` | `PUT` | `/{version}/membership/authentication` | `project` |
| `update_password_complexity` | `PUT` | `/{version}/membership/authorization/password-complexity` | `project` |
| `import_users` | `POST` | `/{version}/membership/users/import` | `project` |
| `repair_login_project_ids` | `POST` | `/{version}/membership/users/repair-logins` | `project` |
| `get_authentication_settings` | `GET` | `/{version}/membership/authentication` | `project` |
| `get_authorization_settings` | `GET` | `/{version}/membership/authorization` | `project` |
| `update_authorization_settings` | `PUT` | `/{version}/membership/authorization` | `project` |
| `list_service_user_api_keys` | `GET` | `/{version}/membership/users/{Id}/api-keys` | `project` |
| `issue_service_user_api_key` | `POST` | `/{version}/membership/users/{Id}/api-keys` | `project` |
| `delete_service_user_api_key` | `DELETE` | `/{version}/membership/users/{Id}/api-keys/{KeyId}` | `project` |
| `repair_contact_roles` | `POST` | `/{version}/membership/users/repair-roles` | `project` |
| `update_contact` | `PATCH` | `/{version}/membership/users/{contactId}` | `project` |
| `clear_contact_bounce` | `POST` | `/{version}/membership/users/{contactId}/marketing-state/{channel}/clear-bounce` | `project` |
| `set_user_ai_plan` | `PUT` | `/{version}/membership/users/{userId}/ai-plan` | `project` |

## Service-user API keys

`issue_service_user_api_key(user_id, name="ci", scopes=["database:read"], expiresInDays=30)`
issues a key for a service user; the key text is in the answer once. `list_service_user_api_keys(user_id)`
lists the keys (without their text) and `delete_service_user_api_key(user_id, key_id)` deletes one.

## Contacts on both hosts

The contact routes (`/membership/users…`) are served by the Hub and by the API host. The same methods
live on `norbix.hub.membership` and `norbix.api.membership`; a project API key calls the API host.
`import_users` and `repair_login_project_ids` are Hub only.

`get_policy_options` calls `GET /{version}/membership/policies/new/options`, a route the gateway no
longer serves (its source is commented out): it answers 404. It is kept so no caller breaks.
