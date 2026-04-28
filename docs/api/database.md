# API · Database

Access with `norbix.api.database`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `find_terms` | `GET` | `/{version}/database/taxonomies/{taxonomyName}/terms` | `project` |
| `find_terms_children` | `GET` | `/{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children` | `project` |
| `get_database_schema` | `GET` | `/{version}/database/schemas/{id}` | `project` |
| `get_database_schemas` | `GET` | `/{version}/database/schemas` | `project` |
| `aggregate` | `POST` | `/{version}/database/collections/{collectionName}/aggregate` | `project` |
| `change_responsibility` | `PUT` | `/{version}/database/collections/{collectionName}/{id}/responsibility` | `project` |
| `count` | `GET` | `/{version}/database/collections/{collectionName}/count` | `project` |
| `delete_many` | `DELETE` | `/{version}/database/collections/{collectionName}/many` | `project` |
| `delete_one` | `DELETE` | `/{version}/database/collections/{collectionName}/{id}` | `project` |
| `distinct` | `GET` | `/{version}/database/collections/{collectionName}/distinct` | `project` |
| `execute_aggregate` | `POST` | `/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute` | `project` |
| `find` | `GET` | `/{version}/database/collections/{collectionName}` | `project` |
| `find_one` | `GET` | `/{version}/database/collections/{collectionName}/{id}` | `project` |
| `insert_many` | `POST` | `/{version}/database/collections/{collectionName}/many` | `project` |
| `insert_one` | `POST` | `/{version}/database/collections/{collectionName}` | `project` |
| `replace_one` | `PUT` | `/{version}/database/collections/{collectionName}/{id}/replace` | `project` |
| `update_many` | `PUT` | `/{version}/database/collections/{collectionName}/many` | `project` |
| `update_one` | `PUT` | `/{version}/database/collections/{collectionName}/{id}` | `project` |
