# HUB · Membership

Access with `norbix.hub.membership`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disableMembership` | `GET` | `/{version}/membership/disable` | `project` |
| `enableMembership` | `GET` | `/{version}/membership/enable` | `project` |
| `deleteMembershipTrigger` | `DELETE` | `/{version}/membership/triggers/{triggerId}` | `project` |
| `disableMembershipTrigger` | `PATCH` | `/{version}/membership/triggers/{triggerId}/disable` | `project` |
| `enableMembershipTrigger` | `PATCH` | `/{version}/membership/triggers/{triggerId}/enable` | `project` |
| `getMembershipTrigger` | `GET` | `/{version}/membership/triggers/{id}` | `project` |
| `getMembershipTriggers` | `GET` | `/{version}/membership/triggers` | `project` |
| `saveMembershipTrigger` | `POST` | `/{version}/membership/triggers` | `project` |
| `createRole` | `POST` | `/{version}/membership/roles` | `project` |
| `deleteRole` | `DELETE` | `/{version}/membership/roles` | `project` |
| `getRole` | `GET` | `/{version}/membership/roles/{Id}` | `project` |
| `getRoles` | `GET` | `/{version}/membership/roles` | `project` |
| `updateRolePolicies` | `PATCH` | `/{version}/membership/roles` | `project` |
| `createPolicy` | `POST` | `/{version}/membership/policies` | `project` |
| `deletePolicy` | `DELETE` | `/{version}/membership/policies` | `project` |
| `getPolicy` | `GET` | `/{version}/membership/policies/{Id}` | `project` |
| `getPolicies` | `GET` | `/{version}/membership/policies` | `project` |
| `updatePolicy` | `PUT` | `/{version}/membership/policies` | `project` |
| `deleteMembershipIntegration` | `DELETE` | `/{version}/membership/integrations/{Id}` | `project` |
| `disableMembershipIntegration` | `PUT` | `/{version}/membership/integrations/{Id}/disable` | `project` |
| `enableMembershipIntegration` | `PUT` | `/{version}/membership/integrations/{Id}/enable` | `project` |
| `getMembershipIntegration` | `GET` | `/{version}/membership/integrations/{id}` | `project` |
| `getMembershipIntegrations` | `GET` | `/{version}/membership/integrations` | `project` |
| `saveMembershipIntegration` | `POST` | `/{version}/membership/integrations` | `project` |
| `setMembershipIntegrationAsDefault` | `PUT` | `/{version}/membership/integrations/{Id}/default` | `project` |
