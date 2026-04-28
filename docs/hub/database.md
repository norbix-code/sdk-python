# HUB · Database

Access with `norbix.hub.database`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disable_database` | `GET` | `/{version}/database/disable` | `project` |
| `enable_database` | `GET` | `/{version}/database/enable` | `project` |
| `delete_schema_trigger` | `DELETE` | `/{version}/database/schemas/triggers/{triggerId}` | `project` |
| `disable_schema_trigger` | `PATCH` | `/{version}/database/schemas/triggers/{triggerId}/disable` | `project` |
| `enable_schema_trigger` | `PATCH` | `/{version}/database/schemas/triggers/{triggerId}/enable` | `project` |
| `get_schema_trigger` | `GET` | `/{version}/database/schemas/triggers/{id}` | `project` |
| `get_schema_triggers` | `GET` | `/{version}/database/schemas/triggers` | `project` |
| `save_schema_trigger` | `POST` | `/{version}/database/schemas/triggers` | `project` |
| `delete_database_taxonomy` | `DELETE` | `/{version}/database/taxonomies/{Id}` | `project` |
| `get_database_taxonomy` | `GET` | `/{version}/database/taxonomies/{id}` | `project` |
| `get_database_taxonomies` | `GET` | `/{version}/database/taxonomies` | `project` |
| `save_database_taxonomy` | `POST` | `/{version}/database/taxonomies` | `project` |
| `delete_database_taxonomy_term` | `DELETE` | `/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}` | `project` |
| `delete_many_database_taxonomy_terms` | `DELETE` | `/{version}/database/taxonomies/{TaxonomyId}/terms/many` | `project` |
| `get_database_taxonomy_term` | `GET` | `/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}` | `project` |
| `save_database_taxonomy_term` | `POST` | `/{version}/database/taxonomies/{TaxonomyId}/terms` | `project` |
| `update_database_taxonomy_term` | `PUT` | `/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}` | `project` |
| `delete_database_schema` | `DELETE` | `/{version}/database/schemas/{Id}` | `project` |
| `discard_database_schema_draft` | `DELETE` | `/{version}/database/schemas/{Id}/draft` | `project` |
| `get_database_schema` | `GET` | `/{version}/database/schemas/{id}` | `project` |
| `get_database_schemas` | `GET` | `/{version}/database/schemas` | `project` |
| `get_database_schema_draft` | `GET` | `/{version}/database/schemas/{Id}/draft` | `project` |
| `get_database_schema_version_diff` | `GET` | `/{version}/database/schemas/{Id}/versions/diff` | `project` |
| `get_database_schema_versions` | `GET` | `/{version}/database/schemas/{Id}/versions` | `project` |
| `publish_database_schema` | `POST` | `/{version}/database/schemas/{Id}/publish` | `project` |
| `rename_database_schema` | `PUT` | `/{version}/database/schemas/{Id}/rename` | `project` |
| `save_database_schema` | `POST` | `/{version}/database/schemas` | `project` |
| `update_database_schema_draft` | `PUT` | `/{version}/database/schemas/{Id}/draft` | `project` |
| `update_database_schema_settings` | `PUT` | `/{version}/database/schemas/{Id}/settings` | `project` |
| `delete_database_integration` | `DELETE` | `/{version}/database/integrations/{Id}` | `project` |
| `disable_database_integration` | `PUT` | `/{version}/database/integrations/{Id}/disable` | `project` |
| `enable_database_integration` | `PUT` | `/{version}/database/integrations/{Id}/enable` | `project` |
| `get_database_integration` | `GET` | `/{version}/database/integrations/{id}` | `project` |
| `get_database_integrations` | `GET` | `/{version}/database/integrations` | `project` |
| `save_database_integration` | `POST` | `/{version}/database/integrations` | `project` |
| `set_database_integration_as_default` | `PUT` | `/{version}/database/integrations/{Id}/default` | `project` |
| `delete_database_aggregate` | `DELETE` | `/{version}/database/aggregates/{Id}` | `project` |
| `get_database_aggregate` | `GET` | `/{version}/database/aggregates/{Id}` | `project` |
| `get_database_aggregates` | `GET` | `/{version}/database/aggregates` | `project` |
| `save_database_aggregate` | `POST` | `/{version}/database/aggregates` | `project` |
| `test_database_aggregate` | `POST` | `/{version}/database/aggregates/test` | `project` |
