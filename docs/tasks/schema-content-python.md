# schema-content-python — Python SDK follows the schema-content campaign

## Goal

The Python SDK (`norbix`, repo `norbix-code/sdk-python`) follows the gateway
contract of campaign branch `audit/schema-content` (gateway worktree
`worktrees/gateway/audit/schema-content/campaign`): `expand_references` on the
record reads with a typed `{ id, display }` helper, `array_filters` and nested
paths on the record updates, nested documents, the new schema field DTOs
(object / array / json / currency default and the field rules), `slug` on
terms, files by id, and the new error codes in the docs.

Not in scope: other SDKs, the CLI, the portal (`cloud`), gateway code, merging
(the campaign is not on `refactoringV2` yet — the pull request stays open).
The Hub record endpoints (`FindRecords`, `UpdateOneRecord`, …) are not in this
SDK today (see Findings), so `expand_references` / `array_filters` land on the
Api module only.

## Plan

1. chore(types): regenerate `references/{api,hub}_dtos.py` with `x python <file>` against the campaign hosts (Hub `:49826`, Api `:49877`) — done
2. feat(files): `get_file_by_id` on `api.files` (`GET /{version}/files/{filesIntegrationId}/by-id/{id}`) and `hub.files` (`GET /{version}/files/item/by-id`), sync + async — done
3. feat(database): keyword options `expand_references` on `find` / `find_one` / `find_own` and `array_filters` (string or list of dicts) on `update_one` / `update_many`, sync + async; `ReferenceDisplay` pydantic model with `from_value` — done
4. test(database): fake-transport tests for the options, the `{ id, display }` result, nested documents, the field DTOs, the term slug and every new error code; route tests for files by id; the two route-pinning tests read the first docstring line — done
5. docs(database): `docs/database-rules.md` (new), method pages, indexes, README — done
6. check: `uv run ruff check .`, `uv run mypy src`, `uv run pytest` — done (ruff clean; mypy clean, 38 files; pytest 1048 passed)
7. ship: `nbx-ship --no-merge` (pull request only; merge after the gateway campaign lands) — done

## Changes

| file | what changed | plan step # |
| --- | --- | --- |
| `references/api_dtos.py`, `references/hub_dtos.py` | regenerated: `ObjectFieldDto`, `ArrayFieldDto`, `JsonFieldDto`, `CurrencyDefaultDto`; `default` / `unique` / `display_field` / `multiple_of` / `minimum` / `maximum` / `min_items` / `max_items` / `allowed_file_type` / `max_size_mb` on the field DTOs; `slug` on `TermDto` / `TermTreeDto`; `expand_references` on the record reads; `array_filters` on the record updates; `GetFileByIdRequest` / `GetFileById` + `GetFileByIdResponse`; `env` on two Hub DTOs; term document descriptions (classes 221 → 227 Api, 1460 → 1466 Hub) | 1 |
| `src/norbix_python/api/files.py`, `src/norbix_python/hub/files.py` | `get_file_by_id` (sync + async), marked `HAND-WRITTEN` | 2 |
| `src/norbix_python/api/database.py` | `expand_references` / `array_filters` keyword options (sync + async), docstrings; marked `HAND-WRITTEN` | 3 |
| `src/norbix_python/models.py`, `src/norbix_python/__init__.py` | `ReferenceDisplay` (`id`, `display`, `from_value`), exported | 3 |
| `tests/api/test_database_schema_content.py` | new, 49 tests | 4 |
| `tests/test_files_routes.py`, `tests/api/test_files.py`, `tests/hub/test_files.py` | files-by-id route tests (Api path params, Hub query string) and surface asserts | 4 |
| `tests/api/test_database_last_wave.py`, `tests/hub/test_database_last_wave.py` | `_documented_routes` reads the first docstring line, so a method may carry a longer docstring | 4 |
| `docs/database-rules.md` | new: reading references, nested documents and arrays (+ error table 030–056), schema fields, files by id | 5 |
| `docs/api/database.md`, `docs/api/files.md`, `docs/hub/files.md`, `docs/hub/_index.md` (files 22 → 23; the Api index already said 10), `docs/README.md`, `README.md` | the new options and method, counts, links | 5 |

## Findings

- The Hub record endpoints (`FindRecords`, `FindOneRecord`, `UpdateOneRecord`, `UpdateManyRecords`, …) have no method in this SDK (`hub/database.py` has 41 methods, none under `/database/collections`), so the Hub side of `expandReferences` / `arrayFilters` has nowhere to land. Open — a Routine D item for the Hub Database records group.
- `scripts/generate_endpoints.py` is gitignored and not in this worktree; the new methods and options are marked `HAND-WRITTEN` so a future regeneration keeps them, as `hub/account.py` does. Open.
- `tests/*/test_database_last_wave.py` matched the whole docstring against `^VERB path$`, so any method with more than one docstring line dropped out of the route check silently. Fixed here (first line only).
- The regenerated Hub references also gain `env` on two DTOs and the richer term-document descriptions from the campaign branch — contract of earlier campaign items, not of this one. Kept (the file is generated).
- The SDK is untyped on the wire by design (runbook: "untyped SDK by design; nothing to regenerate"), so the field DTOs are typed only in `references/` — the record and schema answers stay plain dicts. `ReferenceDisplay` is the one typed helper added. Note.

## Rejected / moved out

- Merging the pull request: not in this wave (the gateway campaign is not on `refactoringV2`).
- Typed models for every new field DTO in `models.py`: the SDK hands JSON back as dicts everywhere else; adding pydantic twins for 4 of 17 field kinds would be a second, partial type system. The ServiceStack references carry the full typed shape.

## Needs you

- [ ] Merge the pull request after the gateway campaign `audit/schema-content` lands on `refactoringV2`; `get_file_by_id`, `expand_references` and `array_filters` only work against that gateway.
- [ ] Decide whether the Hub record endpoints should join this SDK (Finding 1) — today a Python caller reads and writes records through the Api module only.

## Open questions

- none
