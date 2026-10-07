# Database — references, nested documents, field rules

[↑ Back to docs](./README.md) · [API · Database](./api/database.md) · [API · Files](./api/files.md) · [Hub · Files](./hub/files.md)

This page covers what the schema-content contract added to the Database
module: reading references as `{ id, display }`, nested documents and arrays,
the typed schema field DTOs, files by id, and the error code each refusal
carries. The older rules (bulk writes, aggregates, term reads) stay on
[API · Database](./api/database.md#changing-many-records). Every refusal
raises a `NorbixError`; read `err.error_code` (see
[Errors](../README.md#errors)).

## Reading references — `expand_references`

A reference field (user, role, taxonomy term, record of another collection,
file) stores an id. `find`, `find_one` and `find_own` take
`expand_references=True`: every reference then reads as `{"id", "display"}` —
`display` is the value of the field the schema names as `displayField` on the
target (a user property such as `displayName`, a role's name, a term's title
or slug, a record's field, a file's name), `None` when the target is gone; a
list of them on a field that holds several ids. The default (`False` or not
given) returns the stored ids, unchanged.

The caller needs read permission on the collection **and** on every source the
published schema links to. A missing one refuses the whole read with
`CM-ERRORS-DATABASE-056`, naming the source — a permission gap never looks
like missing data.

```python
import json

from norbix_python import NorbixApi, ReferenceDisplay

norbix = NorbixApi(api_key="<api_key>", project_id="proj_123")

answer = norbix.database.find_one("articles", "rec_1", expand_references=True)
record = json.loads(answer["result"])

author = ReferenceDisplay.from_value(record["author"])   # one id
print(author.id, author.display)                         # usr_1 Jane Doe

tags = ReferenceDisplay.from_value(record["tags"])       # several ids → a list
for tag in tags:
    print(tag.id, tag.display)                           # 6651 None  ← the term is gone
```

`ReferenceDisplay` is a small pydantic model (`id: str`, `display: Any | None`)
with `from_value`, which accepts one dict, a list of dicts or `None`. The SDK
does not change the wire answer: `record["author"]` is still the plain dict.

## Nested documents and arrays

A record is stored as the JSON you send: objects (`"address": {"city":
"Vilnius"}`) and arrays of objects (`"lines": [{"sku": "A-1", "qty": 2}]`)
stay nested at any depth, and the schema is checked at every level — a broken
value names the full path (`lines[1].qty`) in `errors[0].context["FieldName"]`.

An update key may be a nested path:

| Path                  | Meaning                                                                                                    |
| --------------------- | ---------------------------------------------------------------------------------------------------------- |
| `"address.city"`      | one nested field                                                                                           |
| `"lines.0.qty"`       | the element at an index                                                                                    |
| `"lines.$[].qty"`     | every element                                                                                              |
| `"lines.$[line].qty"` | the elements `array_filters` picks — one filter document per `$[name]`, e.g. `[{"line.sku": "A-1"}]`       |

`array_filters` is a keyword option of `update_one` / `update_many`. Pass it as
a JSON string or as a list of dicts (the SDK serialises the list). A `$[name]`
without its filter, or a filter without its `$[name]`, is refused with
`CM-ERRORS-PROPERTY-002` on `ArrayFilters`. Keys that overlap (`address` and
`address.city`) are refused with `CM-ERRORS-DATABASE-014`.

```python
norbix.database.update_one(
    "orders",
    "rec_1",
    update='{"lines.$[line].qty": 3, "meta.words": 130}',
    array_filters=[{"line.sku": "A-1"}],
)
```

Filters pass through with MongoDB semantics (`{"address.city": "Vilnius"}`,
`{"lines": {"$elemMatch": {"sku": "A-1"}}}`). `sortBy` accepts a dotted path
through documents (`"address.city"`); a sort on or through a list (`lines`,
`lines.qty`, `tags`, an array position) is refused with
`CM-ERRORS-DATABASE-039` — a cursor on a list repeats or skips rows.

### Record data errors

Every refusal reads `Field '<name>' is invalid: <reason>` and carries
`FieldName` (the full path) and `Keyword` in `errors[0].context`. `-030` stays
for `required`.

| Code                     | Keyword            | Fires when                                                                                                   |
| ------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------------ |
| `CM-ERRORS-DATABASE-030` | `required`         | a required field is missing or null on insert / replace                                                      |
| `CM-ERRORS-DATABASE-039` | `type`             | wrong JSON type; one value on a multi-value field or a list on a single one; empty reference id              |
| `CM-ERRORS-DATABASE-040` | `length`           | `minLength` / `maxLength` (also per language on a translatable string); `minItems` / `maxItems`; `maxBytes`  |
| `CM-ERRORS-DATABASE-041` | `pattern`          | the string does not match `pattern`                                                                          |
| `CM-ERRORS-DATABASE-042` | `format`           | `format` email / uri / uuid; a file id that is not a UUID or `nbfl_…`; a currency code that is not 3 letters |
| `CM-ERRORS-DATABASE-043` | `range`            | `minimum` / `maximum` on integer, decimal, date, currency amount                                             |
| `CM-ERRORS-DATABASE-044` | `multipleOf`       | a decimal or currency amount off the step (`multipleOf`)                                                     |
| `CM-ERRORS-DATABASE-045` | `enum`             | value outside the enum values, the allowed currencies or the allowed geometry types                          |
| `CM-ERRORS-DATABASE-046` | `uniqueItems`      | a repeated entry in tags, a multi-value enum, file ids, several references, an array with `uniqueItems`      |
| `CM-ERRORS-DATABASE-047` | `properties`       | a currency / geolocation / nested object misses a member or carries an unknown one                           |
| `CM-ERRORS-DATABASE-048` | `coordinates`      | not a `[longitude, latitude]` pair; longitude outside -180..180 or latitude outside -90..90                  |
| `CM-ERRORS-DATABASE-049` | `translateOptions` | a translatable string is not a language → text object                                                        |
| `CM-ERRORS-DATABASE-050` | `reference`        | a user id that is not a user of the project                                                                  |
| `CM-ERRORS-DATABASE-051` | `reference`        | a role id the project does not have (a role NAME is refused — store the role id)                             |
| `CM-ERRORS-DATABASE-052` | `reference`        | a term id that is not a term of the declared taxonomy                                                        |
| `CM-ERRORS-DATABASE-053` | `reference`        | a record id that is not in the declared collection                                                           |
| `CM-ERRORS-DATABASE-054` | `reference`        | a file id none of the field's storages holds                                                                 |
| `CM-ERRORS-DATABASE-055` | `reference`        | the declared target itself cannot be read (unknown taxonomy, collection without a repository, …)             |
| `CM-ERRORS-DATABASE-056` | —                  | a read with `expand_references` by a caller without read on a linked source (the source is named)            |

Behaviour changes to know: a plain string on a translatable field is refused
(before, accepted); a duplicate tag / option / id is refused; a nested object
with an undeclared member is refused (nested forms are closed, the root stays
open); an array shorter or longer than `minItems` / `maxItems` is refused, also
for tags and files.

```python
from norbix_python import NorbixError

try:
    norbix.database.insert_one("orders", document='{"lines": [{"sku": "A-1", "qty": 0}]}')
except NorbixError as err:
    print(err.error_code)                       # CM-ERRORS-DATABASE-043
    print(err.errors[0].context["FieldName"])   # lines[0].qty
    print(err.errors[0].context["Keyword"])     # range
```

## Schema fields

`get_database_schema` returns the fields typed per kind (`$fieldType`). The
SDK hands the JSON back as it arrives; the reference DTOs are in
`references/api_dtos.py` (`JsonSchemaFieldDto` and its subclasses). New in this
contract:

- `ObjectFieldDto` (`$fieldType: object`) — a nested form: `properties`
  (the fields at the next level) and `required`.
- `ArrayFieldDto` (`array`) — a list: `items` (one field DTO, a primitive or
  an object), `minItems` / `maxItems` / `uniqueItems`.
- `JsonFieldDto` (`json`) — a free JSON value, `maxBytes`.
- `CurrencyDefaultDto` — `{ value, currency }`, the `default` of a currency
  field.
- Field rules: `default` on string / integer / decimal / boolean / date /
  currency / tags / enum; `unique` on string / integer / decimal;
  `multipleOf`, `minimum` / `maximum` on currency; `minItems` / `maxItems` on
  tags and files; `allowedFileType` / `maxSizeMb` on files; `displayField` on
  the user / role / taxonomy / collection references (the value
  `expand_references` shows).
- A taxonomy term (`TermDto`, `TermTreeDto`) carries `slug` — lower-case,
  unique inside the taxonomy, derived from the name unless sent explicitly.
  An explicit slug another term has is refused with
  `CM-ERRORS-TAXONOMIES-012`; a slug with no letter or digit with `-013`.

Schema saves that touch a display field: a collection reference whose
`displayField` is not a field of the target schema answers
`CM-ERRORS-SCHEMA-039` (the target's fields listed); a draft or rename that
would remove a field another schema shows answers `CM-ERRORS-SCHEMA-040`; a
schema delete while another schema's reference points at it answers
`CM-ERRORS-SCHEMA-041`. A nesting deeper than 5 levels is `-036`, a `default`
that breaks the field's own rules `-037`, a nested `required` naming an
undeclared field `-038`.

## Files by id

A file field stores a stable file id (the `id` an expanded reference returns;
the same id on every listing and `get_file_info`). Read that file with
`api.files.get_file_by_id(files_integration_id, id)` or
`hub.files.get_file_by_id(files_integration_id, id)`: the answer carries
`file` (resource, path), `isPublic` and `publicUrl`. An id no storage of the
integration holds answers not found. See
[API · Files](./api/files.md#reading-a-file-by-id).
