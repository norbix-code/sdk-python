# HUB · Membership

Access with `norbix.hub.membership`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disable_membership` | `GET` | `/{version}/membership/disable` | `project` |
| `enable_membership` | `GET` | `/{version}/membership/enable` | `project` |
| `delete_membership_trigger` | `DELETE` | `/{version}/membership/triggers/{triggerId}` | `project` |
| `disable_membership_trigger` | `PATCH` | `/{version}/membership/triggers/{triggerId}/disable` | `project` |
| `enable_membership_trigger` | `PATCH` | `/{version}/membership/triggers/{triggerId}/enable` | `project` |
| `get_membership_trigger` | `GET` | `/{version}/membership/triggers/{id}` | `project` |
| `get_membership_triggers` | `GET` | `/{version}/membership/triggers` | `project` |
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
