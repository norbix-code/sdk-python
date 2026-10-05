# HUB · Database

Access with `norbix.hub.database`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disable_database` | `PUT` | `/{version}/database/disable` | `project` |
| `enable_database` | `PUT` | `/{version}/database/enable` | `project` |
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
| `get_allowed_flex_tiers` | `GET` | `/{version}/database/integrations/flex-tiers` | `project` |
| `test_database_integration` | `POST` | `/{version}/database/integrations/test` | `project` |
| `reveal_managed_flex_connection_string` | `GET` | `/{version}/database/integrations/{Id}/connection-string` | `project` |
| `get_database_taxonomy_tree` | `GET` | `/{version}/database/taxonomies/tree` | `project` |
| `get_database_merged_term_tree` | `GET` | `/{version}/database/taxonomies/{TaxonomyName}/merged-tree` | `project` |
| `get_database_taxonomy_term_tree` | `GET` | `/{version}/database/taxonomies/{TaxonomyName}/terms/tree` | `project` |
| `apply_database_schema_bundle` | `POST` | `/{version}/database/schemas/apply-bundle` | `project` |
| `get_database_schema_list_settings` | `GET` | `/{version}/database/schemas/{Id}/list-settings` | `project` |
| `update_database_schema_list_settings` | `PUT` | `/{version}/database/schemas/{Id}/list-settings` | `project` |
| `update_database_schema_embed` | `PUT` | `/{version}/database/schemas/{Id}/embed` | `project` |
| `aggregate_records` | `POST` | `/{version}/database/collections/{collectionName}/aggregate` | `project` |
| `change_record_responsibility` | `PUT` | `/{version}/database/collections/{collectionName}/{id}/responsibility` | `project` |
| `count_records` | `GET` | `/{version}/database/collections/{collectionName}/count` | `project` |
| `delete_many_records` | `DELETE` | `/{version}/database/collections/{collectionName}/many` | `project` |
| `delete_record` | `DELETE` | `/{version}/database/collections/{collectionName}/{id}` | `project` |
| `distinct_record_values` | `GET` | `/{version}/database/collections/{collectionName}/distinct` | `project` |
| `execute_records_aggregate` | `POST` | `/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute` | `project` |
| `find_records` | `GET` | `/{version}/database/collections/{collectionName}` | `project` |
| `find_one_record` | `GET` | `/{version}/database/collections/{collectionName}/{id}` | `project` |
| `get_collection_indexes` | `GET` | `/{version}/database/collections/{collectionName}/indexes` | `project` |
| `insert_many_records` | `POST` | `/{version}/database/collections/{collectionName}/many` | `project` |
| `insert_record` | `POST` | `/{version}/database/collections/{collectionName}` | `project` |
| `replace_record` | `PUT` | `/{version}/database/collections/{collectionName}/{id}/replace` | `project` |
| `seed_collection_records` | `POST` | `/{version}/database/collections/seed` | `project` |
| `update_many_records` | `PUT` | `/{version}/database/collections/{collectionName}/many` | `project` |
| `update_one_record` | `PUT` | `/{version}/database/collections/{collectionName}/{id}` | `project` |

## Working with records (Hub)

The Hub record methods are the admin side of collections: they act on every
record in the project, not only the records the caller owns (for that, use
`norbix.api.database.find_own`). Values go in as keyword arguments, the same
way as every other method in this SDK: on a `GET` they become query values, on
a write they become the JSON body. Filters, documents and updates are MongoDB
extended-JSON **strings**.

```python
products = norbix.hub.database.find_records("products", filter='{"status": "active"}', pageSize=20)
one = norbix.hub.database.find_one_record("products", "rec_1")
created = norbix.hub.database.insert_record("products", document='{"title": "Lamp", "price": 12}')
norbix.hub.database.update_one_record("products", "rec_1", update='{"$set": {"price": 10}}')
norbix.hub.database.delete_record("products", "rec_1")
total = norbix.hub.database.count_records("products", filter='{"status": "active"}')
indexes = norbix.hub.database.get_collection_indexes("products")
```

## Schemas per environment

`get_database_schemas()` returns only the schemas of one environment: the one
the client was created with (`Norbix(..., env="TEST")`, sent as the
`norbix-env` header), or `PROD` when no environment is set. Each row carries
`env` (for example `"PROD"` or `"TEST"`). To see another environment's schemas,
use a client with that `env`. The paging cursors (`startingAfter` /
`endingBefore`) are schema ids (`sch_…`); a cursor saved before the gateway
update no longer matches.

```python
test_schemas = Norbix(project_id="...", api_key="...", env="TEST").hub.database.get_database_schemas()
```

## Trees, list settings, embed and bundles

- `get_database_taxonomy_tree()` — the taxonomy structure as a tree.
- `get_database_taxonomy_term_tree("services")` — one taxonomy's terms as a tree.
- `get_database_merged_term_tree("services")` — one tree across taxonomies: the
  terms of `services` are the roots, and the terms of its child taxonomies nest
  under them.
- `get_database_schema_list_settings(id)` / `update_database_schema_list_settings(id, settings={...})`
  — how the record list shows a schema (the update replaces the whole settings object).
  Each environment keeps its own list layout: the client's `env` (the
  `norbix-env` header) picks which one you read and write.
- `update_database_schema_embed(id, ...)` — the schema's embed settings.
- `apply_database_schema_bundle(...)` — apply a bundle of schemas in one call.

The async client (`AsyncNorbix`) has the same methods; `await` them.
