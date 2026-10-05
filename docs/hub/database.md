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
| `create_collection_import` | `POST` | `/{version}/database/imports` | `project` |
| `get_collection_imports` | `GET` | `/{version}/database/imports` | `project` |
| `get_collection_import` | `GET` | `/{version}/database/imports/{Id}` | `project` |
| `delete_collection_import` | `DELETE` | `/{version}/database/imports/{Id}` | `project` |
| `request_import_upload_url` | `POST` | `/{version}/database/imports/upload-url` | `project` |
| `analyze_import_file` | `POST` | `/{version}/database/imports/analyze` | `project` |
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
norbix.hub.database.update_one_record("products", "rec_1", update='{"price": 10}')
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

## Changing many records

`update_many_records` and `delete_many_records` change every record that
matches `filter`. An empty filter (`'{}'`) matches **every** record of the
collection, so the gateway refuses it with `CM-ERRORS-DATABASE-037` unless
you also send `allRecords=True`. For `update_many_records` a missing filter
counts as `'{}'`.

```python
# Only the matching records:
norbix.hub.database.update_many_records("products", filter='{"status": "draft"}', update='{"status": "live"}')
# Every record — the flag says you mean it:
norbix.hub.database.delete_many_records("products", filter="{}", allRecords=True)
```

Pass the flag with its wire name, `allRecords` (the SDK sends keyword
arguments as given; on `update_many_records` it goes in the JSON body, on
`delete_many_records` in the query). The marketplace built-ins `db.update` and
`db.delete` take the same flag as the `allRecords` argument.

Other rules for record writes:

- **Who may call the bulk methods.** A caller with only own-record rights
  (`createAsUser`, `updateOwn`, `deleteOwn`) may now call `insert_many_records`,
  `update_many_records` and `delete_many_records`. The call changes only the
  caller's own records (before, it was refused with 403).
- **No `$` operators in an update.** `update_one_record` / `update_many_records`
  take the new values as a plain document. An update with `$inc`, `$set` and
  the like is refused with `CM-ERRORS-DATABASE-035` (before, MongoDB failed
  at run time).
- **A broken record document** on insert one, insert many or replace is
  refused with `CM-ERRORS-DATABASE-036` "Invalid record document" (before,
  `005` "Invalid filter document"). For insert many,
  `err.errors[0].context["Index"]` is the position of the bad document.
- **Soft-deleted records are not found.** Update, replace and change owner
  no longer match a soft-deleted record: it answers "not found", and a bulk
  update skips it.
- **Change owner** (`change_record_responsibility`) refuses a new owner who is
  not a user of the project in the request environment, with
  `CM-ERRORS-MEMBERSHIP-USERS-012`.

## Aggregates

- `get_database_aggregate(id)` returns `joinedCollections`: the schemas the
  pipeline joins (`$lookup` / `$graphLookup` / `$unionWith`), next to the
  start `schemaId`. The aggregate list rows do not carry it.
- `save_database_aggregate(...)` refuses `$out`, `$merge`, `$where`,
  `$function` and `$accumulator` (`CM-ERRORS-DATABASE-031`) and a join it
  cannot follow (`034`); a pipeline that does not parse is refused with
  `CM-ERRORS-AGGREGATES-002`.
- A pipeline (run, test or saved-and-executed) that joins a collection the
  caller cannot read is refused with `033`; a join to a name that is not a
  schema in the request environment with `032`.
- `test_database_aggregate(...)` needs `database:create` **or**
  `database:update` on `database:aggregate:{schemaId}`, plus read. A caller
  with read rights only gets 403.

## Schemas: rename and delete

- `rename_database_schema(id, title="...")` sends only the new title. The old
  `renameUniqueName` switch is gone: a name that another schema in the same
  environment already uses is always refused with `CM-ERRORS-SCHEMA-002`
  ("Two schemas cannot share one collection"); the error context carries
  `SchemaName`. The schema name is the MongoDB collection name, so two schemas
  can never share it.
- `delete_database_schema(id)` is also refused while a saved aggregate starts
  from the schema or joins it: `CM-ERRORS-SCHEMA-018`. The message names the
  aggregates; `err.errors[0].context` has `BlockerAggregateIds` and
  `BlockerAggregateNames`. (A schema that a trigger uses is refused with
  `CM-ERRORS-SCHEMA-017`, `BlockerTriggerIds`.)
- `save_database_schema(viewId=...)` with an id that is not a schema of the
  request environment answers "schema not found".
- `update_database_schema_list_settings(...)` refusals all use
  `CM-ERRORS-SCHEMA-034`; the context's `Rule` says which rule failed.
- `apply_database_schema_bundle(...)`: a refused step keeps its own error code
  and context.

## Database integrations per environment

`get_database_integrations()` lists only the integrations of the client's
environment (`PROD` when no `env` is set); each row has `env`. A saved
integration has `isSystemOwned` (read only). Saving into an environment the
project does not have is refused. An integration whose secret is empty in the
request environment answers `CM-ERRORS-DATABASE-038`.

## Schema triggers per environment

Schema triggers are kept per environment. Every schema-trigger call works on
the client's environment (the `norbix-env` header; `PROD` when none is set):

- `get_schema_triggers()` lists only that environment's triggers; each row
  has `env`.
- `get_schema_trigger(id)` returns `env`, and `schemaId` is now the owning
  schema's id (`sch_…`). Before, it wrongly held the trigger's own id
  (`trg_…`).
- `enable_schema_trigger`, `disable_schema_trigger` and `delete_schema_trigger`
  act on the copy in that environment. No copy there answers
  `CM-ERRORS-TRIGGERS-002` (not found).
- `save_schema_trigger(id=..., schemaId=...)` with the id of a trigger that
  belongs to another schema answers `CM-ERRORS-TRIGGERS-002`.

```python
test = Norbix(project_id="...", api_key="...", env="TEST")
test.hub.database.disable_schema_trigger("trg_1")  # the TEST copy only
```

## Taxonomies

- `get_database_taxonomies()` rows have `dependencyRefs` in place of the old
  `dependencyNames`: one `{"id": ..., "name": ...}` pair per entry of
  `dependencies`, in the same order. A dependency that no longer exists keeps
  its place with `"name": None`.

  ```python
  for row in norbix.hub.database.get_database_taxonomies()["list"]["items"]:
      names = [ref["name"] or f"(deleted {ref['id']})" for ref in row.get("dependencyRefs") or []]
  ```

- `save_database_taxonomy(viewId=...)` with the id of an existing taxonomy is
  an update and needs `database:update` on `database:taxonomy:{viewId}`.
  Without `viewId` (or with an unknown one) it is a create and needs
  `database:create`. An update replaces the whole taxonomy: send every field
  you want to keep.
- Term reads by taxonomy name (term tree, merged tree) check
  `database:read` on `database:term:{taxonomy id}`; the merged tree checks it
  on every nested taxonomy too.
- `get_database_taxonomy_tree(includeTerms=True)` now fails when reading the
  terms fails. Before, it returned the taxonomies without terms.
- Errors on term reads: `CM-ERRORS-TAXONOMIES-010` the taxonomy name is
  unknown (the merged tree used to answer `-003`); `-011` the term tree has
  more than 5000 terms (whole taxonomy, merged tree, `includeTerms`); `-005`
  a taxonomy name longer than 40 characters.

## Collection imports

Import CSV rows into a collection: ask for an upload URL, upload the file,
analyze it, then create the import and follow it.

```python
target = norbix.hub.database.request_import_upload_url(fileName="products.csv")["result"]
httpx.put(target["url"], content=csv_bytes, headers={"Content-Type": target["contentType"]})
preview = norbix.hub.database.analyze_import_file(file=target["file"], hasHeader=True)
created = norbix.hub.database.create_collection_import(file=target["file"], schemaId="sch_1", hasHeader=True)
status = norbix.hub.database.get_collection_import(created["id"])
imports = norbix.hub.database.get_collection_imports()
norbix.hub.database.delete_collection_import(created["id"])
```

The request fields are listed under `RequestImportUploadUrlRequest`,
`AnalyzeImportFileRequest` and `CreateCollectionImport` in
`references/hub_dtos.py`.

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
