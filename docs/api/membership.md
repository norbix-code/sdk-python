# API · Membership

Access with `norbix.api.membership`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `block_user` | `PATCH` | `/{version}/membership/auth/block` | `project` |
| `save_system_user_with_permissions` | `POST` | `/{version}/membership/auth/register/service` | `project` |
| `save_guest_user` | `POST` | `/{version}/membership/auth/register/guest` | `project` |
| `save_user_name_user` | `POST` | `/{version}/membership/auth/register/user-name` | `project` |
| `save_email_user` | `POST` | `/{version}/membership/auth/register/email` | `project` |
| `save_phone_user` | `POST` | `/{version}/membership/auth/register/phone` | `project` |
| `save_phone_user_name_with_permissions` | `POST` | `/{version}/membership/auth/register/phone-with-permissions` | `project` |
| `save_email_user_name_with_permissions` | `POST` | `/{version}/membership/auth/register/email-with-permissions` | `project` |
| `save_user_name_with_permissions` | `POST` | `/{version}/membership/auth/register/user-name-with-permissions` | `project` |
| `delete_user` | `DELETE` | `/{version}/membership/auth` | `project` |
| `get_user` | `GET` | `/{version}/membership/auth/{id}` | `project` |
| `get_users` | `GET` | `/{version}/membership/auth` | `project` |
| `get_user_preferences` | `GET` | `/{version}/membership/auth/{id}/preferences` | `project` |
| `invite_user` | `POST` | `/{version}/membership/auth/invite` | `project` |
| `assign_role_permissions` | `PUT` | `/{version}/membership/auth/assign-roles` | `project` |
| `unblock_user` | `PATCH` | `/{version}/membership/auth/unblock` | `project` |
| `update_user` | `PUT` | `/{version}/membership/auth` | `project` |
| `update_user_preferences` | `PUT` | `/{version}/membership/auth/{id}/preferences` | `project` |
| `confirm_email_verification` | `POST` | `/{version}/membership/userauth/email/confirm-verification` | `project` |
| `start_email_verification` | `POST` | `/{version}/membership/userauth/email/start-verification` | `project` |
| `has_passkey` | `POST` | `/{version}/membership/userauth/has-passkey` | `project` |
| `passkey_logout` | `POST` | `/{version}/membership/userauth/logout` | `project` |
| `passkey_authentication_options` | `POST` | `/{version}/membership/userauth/passkey/authentication-options` | `project` |
| `passkey_registration_options` | `POST` | `/{version}/membership/userauth/passkey/registration-options` | `project` |
| `verify_passkey_authentication` | `POST` | `/{version}/membership/userauth/passkey/verify-authentication` | `project` |
| `verify_passkey_registration` | `POST` | `/{version}/membership/userauth/passkey/verify-registration` | `project` |
| `list_passkeys` | `GET` | `/{version}/membership/userauth/passkeys` | `project` |
| `rename_passkey` | `POST` | `/{version}/membership/userauth/passkeys/{CredentialId}/rename` | `project` |
| `revoke_passkey` | `POST` | `/{version}/membership/userauth/passkeys/{CredentialId}/revoke` | `project` |
| `consume_magic_link` | `POST` | `/{version}/membership/userauth/recovery/magic-link/consume` | `project` |
| `request_magic_link` | `POST` | `/{version}/membership/userauth/recovery/magic-link/request` | `project` |
| `use_recovery_code` | `POST` | `/{version}/membership/userauth/recovery/use-code` | `project` |
| `refresh_passkey_token` | `POST` | `/{version}/membership/userauth/token/refresh` | `project` |
| `start_link_identity` | `POST` | `/{version}/membership/auth/{UserId}/link-identity/start` | `project` |
| `link_identity` | `POST` | `/{version}/membership/auth/{UserId}/link-identity` | `project` |
| `exchange_social_sign_in_code` | `POST` | `/{version}/membership/auth/social/{Provider}/exchange` | `unauthenticated` |
| `social_sign_in_url` | — | builds `GET /{version}/membership/auth/social/{provider}?projectId=…` (a URL, not a call) | — |
| `change_password` | `POST` | `/{version}/membership/userauth/password/change` | `project` |
| `request_password_reset` | `POST` | `/{version}/membership/userauth/password/reset/request` | `project` |
| `confirm_password_reset` | `POST` | `/{version}/membership/userauth/password/reset/confirm` | `project` |
| `map_auth_to_user` | `POST` | `/{version}/membership/users/{userId}/map-auth` | `project` |
| `set_contact_roles` | `PUT` | `/{version}/membership/users/{userId}/roles` | `project` |
| `grant_contact_consent` | `POST` | `/{version}/membership/users/{contactId}/marketing-state/{channel}/consent` | `project` |
| `unsubscribe_contact` | `POST` | `/{version}/membership/users/{contactId}/marketing-state/{channel}/unsubscribe` | `project` |
| `set_contact_tag_subscription` | `PUT` | `/{version}/membership/users/{contactId}/marketing-state/{commChannel}/{channel}/tags/{tag}` | `project` |
| `get_all_contacts` | `GET` | `/{version}/membership/users` | `project` |
| `create_contact` | `POST` | `/{version}/membership/users` | `project` |
| `merge_contacts` | `POST` | `/{version}/membership/users/merge` | `project` |
| `repair_contact_roles` | `POST` | `/{version}/membership/users/repair-roles` | `project` |
| `get_contact` | `GET` | `/{version}/membership/users/{contactId}` | `project` |
| `update_contact` | `PATCH` | `/{version}/membership/users/{contactId}` | `project` |
| `delete_contact` | `DELETE` | `/{version}/membership/users/{contactId}` | `project` |
| `add_contact_identity` | `POST` | `/{version}/membership/users/{contactId}/identities` | `project` |
| `remove_contact_identity` | `DELETE` | `/{version}/membership/users/{contactId}/identities/{authId}` | `project` |
| `promote_contact_identity` | `POST` | `/{version}/membership/users/{contactId}/identities/{authId}/promote` | `project` |
| `clear_contact_bounce` | `POST` | `/{version}/membership/users/{contactId}/marketing-state/{channel}/clear-bounce` | `project` |
| `set_user_ai_plan` | `PUT` | `/{version}/membership/users/{userId}/ai-plan` | `project` |
| `finish_invitation` | `POST` | `/{version}/membership/auth/invitation/finish` | `optional` |
| `send_test_password_reset` | `POST` | `/{version}/membership/userauth/password/reset/test` | `project` |

## Social sign-in and link identity

Project users can sign in with Google, Apple, Microsoft, GitHub, Facebook, X or
Okta. The project's enabled providers are in the public config
(`norbix.api.public.get_public_project_config(...)` → `auth.socialSignIn`:
`provider`, `displayName`, `startPath`).

```python
m = norbix.api.membership

# 1. PKCE: keep the verifier (memory on a device, the session on a server); only the challenge travels.
pkce = create_pkce_pair()
# Send the browser (on a phone: the system browser) here. Not a call: it redirects.
url = m.social_sign_in_url(
    "google", return_url="https://app.example.com/oauth/callback", code_challenge=pkce.code_challenge
)

# 2. The return page gets ?code=…&provider=google (or ?error=…). Trade the code within 2 minutes:
token = m.exchange_social_sign_in_code("google", code=code, codeVerifier=pkce.code_verifier)
# token["bearerToken"]: the project JWT (14 days, no refresh token)

# Link another provider to the signed-in user (yourself only):
link_pkce = create_pkce_pair()
start = m.start_link_identity(
    "usr_…", provider="github", returnUrl="https://app.example.com/settings", codeChallenge=link_pkce.code_challenge
)
# send the browser to start["authorizeUrl"]; it comes back with ?intent=link&code=…
m.link_identity("usr_…", code=link_code, codeVerifier=link_pkce.code_verifier)
```

- `social_sign_in_url(provider, mode=..., return_url=..., code_challenge=...)` puts the project id
  and a non-PROD env in the query, because a navigation sends no headers. The
  start and the provider callback have no call method.
- `exchange_social_sign_in_code` sends no credentials, even when the client
  has a key or a JWT: the gateway refuses an old token on any route, and the
  exchange is how a user signs in again.
- `link_identity` now takes `code` (the link code); `provider` /
  `providerToken` are gone.
- PKCE (S256) is optional but strongly recommended: `create_pkce_pair()` (from
  `norbix_python`) gives `code_verifier` and `code_challenge` (32 random
  bytes, base64url). A code started with a challenge needs its verifier; a
  verifier for a code started without one is refused too.
- Refusals: `CM-ERRORS-MEMBERSHIP-051` (code used, expired or unknown), `-055`
  (409, the provider account belongs to another user), `-056` (403, not
  yourself), `-058` (PKCE: `context.Reason` `verifier_missing`,
  `verifier_wrong` or `challenge_missing`; the code is used up — start
  again), `-059` (the challenge is not a 43-character S256). A refused
  `returnUrl` sends the browser to the mode's failure page with
  `error=return_url_not_allowed`.

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
