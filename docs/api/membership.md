# API · Membership

Access with `norbix.api.membership`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `block_user` | `PATCH` | `/{version}/membership/users/block` | `project` |
| `save_system_user_with_permissions` | `POST` | `/{version}/membership/users/register/service` | `project` |
| `save_guest_user` | `POST` | `/{version}/membership/users/register/guest` | `project` |
| `save_user_name_user` | `POST` | `/{version}/membership/users/register/user-name` | `project` |
| `save_email_user` | `POST` | `/{version}/membership/users/register/email` | `project` |
| `save_phone_user` | `POST` | `/{version}/membership/users/register/phone` | `project` |
| `save_phone_user_name_with_permissions` | `POST` | `/{version}/membership/users/register/phone-with-permissions` | `project` |
| `save_email_user_name_with_permissions` | `POST` | `/{version}/membership/users/register/email-with-permissions` | `project` |
| `save_user_name_with_permissions` | `POST` | `/{version}/membership/users/register/user-name-with-permissions` | `project` |
| `delete_user` | `DELETE` | `/{version}/membership/users` | `project` |
| `get_user` | `GET` | `/{version}/membership/users/{id}` | `project` |
| `get_users` | `GET` | `/{version}/membership/users` | `project` |
| `get_user_preferences` | `GET` | `/{version}/membership/users/{id}/preferences` | `project` |
| `invite_user` | `POST` | `/{version}/membership/users/invite` | `project` |
| `assign_role_permissions` | `PUT` | `/{version}/membership/users/assign-roles` | `project` |
| `unblock_user` | `PATCH` | `/{version}/membership/users/unblock` | `project` |
| `update_user` | `PUT` | `/{version}/membership/users` | `project` |
| `update_user_preferences` | `PUT` | `/{version}/membership/users/{id}/preferences` | `project` |
