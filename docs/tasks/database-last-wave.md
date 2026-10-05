# Database last wave — Python SDK side of the gateway contract changes

## Goal

The Python SDK follows the Database contract changes now on gateway
`refactoringV2` (records, taxonomies, triggers, schemas, aggregates): fresh
DTO references, every Database method matches the gateway's routes, tests and
docs cover each change, the full suite is green, the branch is shipped.

Not in scope: typed request / response classes (the Python SDK is untyped by
design — every request field is a keyword argument that goes to the wire as
given); other modules than Database.

## Plan

1. chore(references): refresh `references/{hub,api}_dtos.py` and
   `references/{hub,api}2.dtos.ts` from the running Community Hub
   (`localhost:64964`) and Api (`localhost:64965`) built from
   `origin/refactoringV2` — done
2. feat(database): add the 6 collection-import methods the Hub serves but the
   SDK did not have (`/database/imports…`), sync and async, so every Database
   route of both hosts has a method — done
3. test(database): tests with a capture transport for every contract change
   that reaches the wire: `allRecords` on update/delete many (Hub + Api),
   rename without `renameUniqueName`, schema triggers per env (`norbix-env`
   header), the import routes, a route check of every Database method
   against the hosts' routes, and the new error codes surfacing as
   `NorbixError.error_code` — done
4. docs(database): Hub and Api database pages — bulk writes (empty filter,
   `allRecords`, own-scope bulk calls, `$` operators refused, record
   document errors, soft-deleted rows), change owner, aggregate test rights,
   schema delete blockers, `joinedCollections`, rename, schema triggers per
   env, taxonomy `dependencyRefs`, term-read rights and new error codes — done
5. Full suite (`uv run pytest`, `make typecheck`, `make lint`) green; ship
   with `nbx-ship --wait-release --cleanup` — doing

## Changes

| file | what changed | plan step # |
|---|---|---|
| `references/hub_dtos.py`, `references/hub2.dtos.ts` | refreshed from Hub `/types/python` and `/types/typescript` | 1 |
| `references/api_dtos.py`, `references/api2.dtos.ts` | refreshed from Api; the `.ts` was last taken from ServiceStack 8.30, so its diff is large | 1 |
| `src/norbix_python/hub/database.py` | `create_collection_import`, `get_collection_imports`, `get_collection_import`, `delete_collection_import`, `request_import_upload_url`, `analyze_import_file` (sync + async) | 2 |
| `tests/hub/test_database_last_wave.py` | new: request shapes for the contract changes, import routes, route check against the hosts' routes | 3 |
| `tests/api/test_database_last_wave.py` | new: `allRecords` on Api update/delete many, change owner error, `$where` refused on terms | 3 |
| `docs/hub/database.md` | import methods in the table; new sections for every contract change | 4 |
| `docs/api/database.md` | bulk writes, change owner, term reads and the new error codes | 4 |

## Findings

- The Python SDK had no method for the 6 Hub collection-import routes
  (`/database/imports`, `/imports/{Id}`, `/imports/upload-url`,
  `/imports/analyze`); `norbix-js` has them. Fixed here (step 2).
- `references/api2.dtos.ts` was a year old (ServiceStack 8.30, 2025-10-22).
  Refreshed here (step 1).
- The SDK forwards keyword arguments by their given name: `all_records=True`
  would go out as `all_records`, which the gateway does not read. The docs
  and tests use the wire name `allRecords=True`, the same way the rest of the
  SDK uses `pageSize`. Left as is (this is the SDK's documented rule).

## Rejected / moved out

- A local guard that refuses an empty filter before sending. The gateway owns
  this rule (CM-ERRORS-DATABASE-037); a copy in the SDK would drift.

## Needs you

- Nothing. The import methods are new methods (a minor release), no existing
  method changed its name, parameters or return type.

## Open questions

- None.
