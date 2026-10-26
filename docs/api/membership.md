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
| `change_password` | `POST` | `/{version}/membership/userauth/password/change` | `project` |
| `request_password_reset` | `POST` | `/{version}/membership/userauth/password/reset/request` | `project` |
| `confirm_password_reset` | `POST` | `/{version}/membership/userauth/password/reset/confirm` | `project` |

## Credential version

Every user carries a `credentialVersion`, a number that moves when the
password changes. `change_password` and `confirm_password_reset` answer
`{"authId", "credentialVersion"}`; `get_user` / `get_users` read it on each
user; and `norbix.login(...)` keeps the whole sign-in answer, so
`auth["meta"]["credentialVersion"]` is the version the token was issued for.

A token issued before the change is refused with HTTP 401 and the error code
`CM-ERRORS-MEMBERSHIP-USERS-050` ("credentials changed, sign in again"). The
SDK raises it as an `AuthenticationError` (every 401 is one); switch on
`error_code` to tell it from a plain expired token and sign in again:

```python
from norbix_python import AuthenticationError, LoginCredentials

try:
    norbix.api.membership.get_user(id="usr_1")
except AuthenticationError as exc:
    if exc.error_code == "CM-ERRORS-MEMBERSHIP-USERS-050":
        norbix.login(LoginCredentials(user_name="alice@team.io", password="…"))  # a fresh token
    else:
        raise
```
