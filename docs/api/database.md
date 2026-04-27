# API · Database

Access with `norbix.api.database`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `findTerms` | `GET` | `/{version}/database/taxonomies/{taxonomyName}/terms` | `project` |
| `findTermsChildren` | `GET` | `/{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children` | `project` |
| `getDatabaseSchema` | `GET` | `/{version}/database/schemas/{id}` | `project` |
| `getDatabaseSchemas` | `GET` | `/{version}/database/schemas` | `project` |
| `aggregate` | `POST` | `/{version}/database/collections/{collectionName}/aggregate` | `project` |
| `changeResponsibility` | `PUT` | `/{version}/database/collections/{collectionName}/{id}/responsibility` | `project` |
| `count` | `GET` | `/{version}/database/collections/{collectionName}/count` | `project` |
| `deleteMany` | `DELETE` | `/{version}/database/collections/{collectionName}/many` | `project` |
| `deleteOne` | `DELETE` | `/{version}/database/collections/{collectionName}/{id}` | `project` |
| `distinct` | `GET` | `/{version}/database/collections/{collectionName}/distinct` | `project` |
| `executeAggregate` | `POST` | `/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute` | `project` |
| `find` | `GET` | `/{version}/database/collections/{collectionName}` | `project` |
| `findOne` | `GET` | `/{version}/database/collections/{collectionName}/{id}` | `project` |
| `insertMany` | `POST` | `/{version}/database/collections/{collectionName}/many` | `project` |
| `insertOne` | `POST` | `/{version}/database/collections/{collectionName}` | `project` |
| `replaceOne` | `PUT` | `/{version}/database/collections/{collectionName}/{id}/replace` | `project` |
| `updateMany` | `PUT` | `/{version}/database/collections/{collectionName}/many` | `project` |
| `updateOne` | `PUT` | `/{version}/database/collections/{collectionName}/{id}` | `project` |
