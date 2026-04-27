# HUB · Database

Access with `norbix.hub.database`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disableDatabase` | `GET` | `/{version}/database/disable` | `project` |
| `enableDatabase` | `GET` | `/{version}/database/enable` | `project` |
| `deleteSchemaTrigger` | `DELETE` | `/{version}/database/schemas/triggers/{triggerId}` | `project` |
| `disableSchemaTrigger` | `PATCH` | `/{version}/database/schemas/triggers/{triggerId}/disable` | `project` |
| `enableSchemaTrigger` | `PATCH` | `/{version}/database/schemas/triggers/{triggerId}/enable` | `project` |
| `getSchemaTrigger` | `GET` | `/{version}/database/schemas/triggers/{id}` | `project` |
| `getSchemaTriggers` | `GET` | `/{version}/database/schemas/triggers` | `project` |
| `saveSchemaTrigger` | `POST` | `/{version}/database/schemas/triggers` | `project` |
| `deleteDatabaseTaxonomy` | `DELETE` | `/{version}/database/taxonomies/{Id}` | `project` |
| `getDatabaseTaxonomy` | `GET` | `/{version}/database/taxonomies/{id}` | `project` |
| `getDatabaseTaxonomies` | `GET` | `/{version}/database/taxonomies` | `project` |
| `saveDatabaseTaxonomy` | `POST` | `/{version}/database/taxonomies` | `project` |
| `deleteDatabaseTaxonomyTerm` | `DELETE` | `/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}` | `project` |
| `deleteManyDatabaseTaxonomyTerms` | `DELETE` | `/{version}/database/taxonomies/{TaxonomyId}/terms/many` | `project` |
| `getDatabaseTaxonomyTerm` | `GET` | `/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}` | `project` |
| `saveDatabaseTaxonomyTerm` | `POST` | `/{version}/database/taxonomies/{TaxonomyId}/terms` | `project` |
| `updateDatabaseTaxonomyTerm` | `PUT` | `/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}` | `project` |
| `deleteDatabaseSchema` | `DELETE` | `/{version}/database/schemas/{Id}` | `project` |
| `discardDatabaseSchemaDraft` | `DELETE` | `/{version}/database/schemas/{Id}/draft` | `project` |
| `getDatabaseSchema` | `GET` | `/{version}/database/schemas/{id}` | `project` |
| `getDatabaseSchemas` | `GET` | `/{version}/database/schemas` | `project` |
| `getDatabaseSchemaDraft` | `GET` | `/{version}/database/schemas/{Id}/draft` | `project` |
| `getDatabaseSchemaVersionDiff` | `GET` | `/{version}/database/schemas/{Id}/versions/diff` | `project` |
| `getDatabaseSchemaVersions` | `GET` | `/{version}/database/schemas/{Id}/versions` | `project` |
| `publishDatabaseSchema` | `POST` | `/{version}/database/schemas/{Id}/publish` | `project` |
| `renameDatabaseSchema` | `PUT` | `/{version}/database/schemas/{Id}/rename` | `project` |
| `saveDatabaseSchema` | `POST` | `/{version}/database/schemas` | `project` |
| `updateDatabaseSchemaDraft` | `PUT` | `/{version}/database/schemas/{Id}/draft` | `project` |
| `updateDatabaseSchemaSettings` | `PUT` | `/{version}/database/schemas/{Id}/settings` | `project` |
| `deleteDatabaseIntegration` | `DELETE` | `/{version}/database/integrations/{Id}` | `project` |
| `disableDatabaseIntegration` | `PUT` | `/{version}/database/integrations/{Id}/disable` | `project` |
| `enableDatabaseIntegration` | `PUT` | `/{version}/database/integrations/{Id}/enable` | `project` |
| `getDatabaseIntegration` | `GET` | `/{version}/database/integrations/{id}` | `project` |
| `getDatabaseIntegrations` | `GET` | `/{version}/database/integrations` | `project` |
| `saveDatabaseIntegration` | `POST` | `/{version}/database/integrations` | `project` |
| `setDatabaseIntegrationAsDefault` | `PUT` | `/{version}/database/integrations/{Id}/default` | `project` |
| `deleteDatabaseAggregate` | `DELETE` | `/{version}/database/aggregates/{Id}` | `project` |
| `getDatabaseAggregate` | `GET` | `/{version}/database/aggregates/{Id}` | `project` |
| `getDatabaseAggregates` | `GET` | `/{version}/database/aggregates` | `project` |
| `saveDatabaseAggregate` | `POST` | `/{version}/database/aggregates` | `project` |
| `testDatabaseAggregate` | `POST` | `/{version}/database/aggregates/test` | `project` |
