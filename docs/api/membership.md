# API · Membership

Access with `norbix.api.membership`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `blockUser` | `PATCH` | `/{version}/membership/users/block` | `project` |
| `saveSystemUserWithPermissions` | `POST` | `/{version}/membership/users/register/service` | `project` |
| `saveGuestUser` | `POST` | `/{version}/membership/users/register/guest` | `project` |
| `saveUserNameUser` | `POST` | `/{version}/membership/users/register/user-name` | `project` |
| `saveEmailUser` | `POST` | `/{version}/membership/users/register/email` | `project` |
| `savePhoneUser` | `POST` | `/{version}/membership/users/register/phone` | `project` |
| `savePhoneUserNameWithPermissions` | `POST` | `/{version}/membership/users/register/phone-with-permissions` | `project` |
| `saveEmailUserNameWithPermissions` | `POST` | `/{version}/membership/users/register/email-with-permissions` | `project` |
| `saveUserNameWithPermissions` | `POST` | `/{version}/membership/users/register/user-name-with-permissions` | `project` |
| `deleteUser` | `DELETE` | `/{version}/membership/users` | `project` |
| `getUser` | `GET` | `/{version}/membership/users/{id}` | `project` |
| `getUsers` | `GET` | `/{version}/membership/users` | `project` |
| `getUserPreferences` | `GET` | `/{version}/membership/users/{id}/preferences` | `project` |
| `inviteUser` | `POST` | `/{version}/membership/users/invite` | `project` |
| `assignRolePermissions` | `PUT` | `/{version}/membership/users/assign-roles` | `project` |
| `unblockUser` | `PATCH` | `/{version}/membership/users/unblock` | `project` |
| `updateUser` | `PUT` | `/{version}/membership/users` | `project` |
| `updateUserPreferences` | `PUT` | `/{version}/membership/users/{id}/preferences` | `project` |
