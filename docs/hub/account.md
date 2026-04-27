# HUB · Account

Access with `norbix.hub.account`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `getAccountProfile` | `GET` | `/{version}/account/profile` | `account` |
| `updateAccountProfile` | `PUT` | `/{version}/account/profile` | `account` |
| `resendAccountVerificationToken` | `GET` | `/{version}/account/verify/resend` | `account` |
| `getAccountStatus` | `GET` | `/{version}/account/status` | `account` |
| `createStripeCheckoutSession` | `POST` | `/{version}/account/stripe/create-checkout-session` | `account` |
| `getStripeBillingPortalUrl` | `POST` | `/{version}/account/stripe/get-portal-url` | `account` |
| `createTeamMemberFromInvitation` | `POST` | `/{version}/account/team/member` | `account` |
| `verifyAccount` | `GET` | `/{version}/account/verify` | `account` |
| `deleteNotificationsGroup` | `DELETE` | `/{version}/account/projects/{projectId}/notifications/settings/group` | `account` |
| `deleteNotificationsTag` | `DELETE` | `/{version}/account/projects/{projectId}/notifications/settings/tag` | `account` |
| `removeTagFromNotificationsGroup` | `DELETE` | `/{version}/account/projects/{projectId}/notifications/settings/group/tag` | `account` |
| `saveNotificationsGroup` | `POST` | `/{version}/account/projects/{projectId}/notifications/settings/group` | `account` |
| `saveNotificationsTag` | `POST` | `/{version}/account/projects/{projectId}/notifications/settings/tag` | `account` |
| `createProject` | `POST` | `/{version}/account/projects` | `account` |
| `deleteProject` | `DELETE` | `/{version}/account/projects/{projectId}` | `account` |
| `getProject` | `GET` | `/{version}/account/projects/{projectId}` | `account` |
| `getProjects` | `GET` | `/{version}/account/projects` | `account` |
| `getAccountRegions` | `GET` | `/{version}/account/regions` | `account` |
| `getProjectTokens` | `GET` | `/{version}/account/projects/{projectId}/tokens` | `account` |
| `updateProjectAccentColor` | `PATCH` | `/{version}/account/projects/{projectId}/settings/accent-color` | `account` |
| `updateProjectIcon` | `PATCH` | `/{version}/account/projects/{projectId}/settings/icon` | `account` |
| `updateProjectLogo` | `PATCH` | `/{version}/account/projects/{projectId}/settings/logo` | `account` |
| `updateProjectMainColor` | `PATCH` | `/{version}/account/projects/{projectId}/settings/main-color` | `account` |
| `updateProjectAllowedOrigins` | `PATCH` | `/{version}/account/projects/{projectId}/settings/origins` | `account` |
| `updateProjectDefaultLanguage` | `PATCH` | `/{version}/account/projects/{projectId}/settings/default-language` | `account` |
| `updateProjectDescription` | `PATCH` | `/{version}/account/projects/{projectId}/settings/description` | `account` |
| `disableProject` | `PATCH` | `/{version}/account/projects/{projectId}/disable` | `account` |
| `enableProject` | `PATCH` | `/{version}/account/projects/{projectId}/enable` | `account` |
| `updateProjectLanguages` | `PATCH` | `/{version}/account/projects/{projectId}/settings/languages` | `account` |
| `updateProjectUrl` | `PATCH` | `/{version}/account/projects/{projectId}/settings/url` | `account` |
| `updateProjectName` | `PATCH` | `/{version}/account/projects/{projectId}/settings/name` | `account` |
| `updateProjectRegions` | `PATCH` | `/{version}/account/projects/{projectId}/settings/regions` | `account` |
| `createAccount` | `POST` | `/{version}/account` | `account` |
| `getAccountCollaborators` | `GET` | `/{version}/account/collaborators` | `account` |
| `sendInviteToTeamMember` | `POST` | `/{version}/account/team/member/invite` | `account` |
| `getLicenses` | `GET` | `/{version}/account/licenses` | `account` |
| `askChat` | `POST` | `/{version}/account/chat/complete` | `account` |
