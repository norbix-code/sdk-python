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
| `update_project_languages` | `PATCH` | `/{version}/account/projects/{projectId}/settings/languages` | `account` |
| `update_project_url` | `PATCH` | `/{version}/account/projects/{projectId}/settings/url` | `account` |
| `update_project_name` | `PATCH` | `/{version}/account/projects/{projectId}/settings/name` | `account` |
| `update_project_regions` | `PATCH` | `/{version}/account/projects/{projectId}/settings/regions` | `account` |
| `create_account` | `POST` | `/{version}/account` | `account` |
| `get_account_collaborators` | `GET` | `/{version}/account/collaborators` | `account` |
| `send_invite_to_team_member` | `POST` | `/{version}/account/team/member/invite` | `account` |
| `get_licenses` | `GET` | `/{version}/account/licenses` | `account` |
| `ask_chat` | `POST` | `/{version}/account/chat/complete` | `account` |
