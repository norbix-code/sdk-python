# API · Database

Access with `norbix.api.database`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `find_terms` | `GET` | `/{version}/database/taxonomies/{taxonomyName}/terms` | `project` |
| `find_terms_children` | `GET` | `/{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children` | `project` |
| `find_term_tree` | `GET` | `/{version}/database/taxonomies/{taxonomyName}/terms/tree` | `project` |
| `find_taxonomy_tree` | `GET` | `/{version}/database/taxonomies/tree` | `project` |
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
| `find_merged_term_tree` | `GET` | `/{version}/database/taxonomies/{taxonomyName}/merged-tree` | `project` |
| `find_own` | `GET` | `/{version}/database/collections/{collectionName}/own` | `project` |

## Working with terms

A **taxonomy** is a named tree of **terms** (labels). A term can have one parent (a clean hierarchy) or several parents (the same item under many categories). Pick the call that matches what you want:

| I want to… | Call | Returns |
| --- | --- | --- |
| Get a taxonomy's terms as a flat list | `find_terms` | a paginated `list` of terms |
| Get only the children of one term | `find_terms_children` | a `list` of child terms (direct + multi-parent) |
| Get a taxonomy's terms as a ready-made tree | `find_term_tree` | a `tree` of nested term nodes |
| Get the taxonomy structure (e.g. Countries → Cities) | `find_taxonomy_tree` | a `tree` of taxonomy nodes |

The examples below all use one example `services` taxonomy shaped like this:

```text
Indoors
  └─ Air conditioning
       └─ Wall-mounted
Outdoors
  └─ Solar panels
```

---

### List a taxonomy's terms (flat)

**Goal:** show every term of `services` in a simple list, in display order.

```python
terms = norbix.api.database.find_terms("services")
```

```json
{
  "list": {
    "items": [
      { "id": "term_indoors",   "taxonomyName": "services", "parentId": null,           "order": 1, "name": "Indoors" },
      { "id": "term_air_con",   "taxonomyName": "services", "parentId": "term_indoors", "order": 1, "name": "Air conditioning" },
      { "id": "term_wall",      "taxonomyName": "services", "parentId": "term_air_con", "order": 1, "name": "Wall-mounted" },
      { "id": "term_outdoors",  "taxonomyName": "services", "parentId": null,           "order": 2, "name": "Outdoors" },
      { "id": "term_solar",     "taxonomyName": "services", "parentId": "term_outdoors","order": 1, "name": "Solar panels" }
    ],
    "hasMore": false, "hasPrevious": false, "startingAfter": null, "endingBefore": null
  },
  "responseStatus": { "isSuccess": true }
}
```

The list is flat — every term is one row, with its `parentId` telling you where it sits. The nesting is not built for you here (use `find_term_tree` for that).

---

### List only top-level terms (filtered)

**Goal:** show just the roots (no parent) — for the first level of a menu.

```python
terms = norbix.api.database.find_terms("services", filter='{ "parentId": null }')
```

```json
{
  "list": {
    "items": [
      { "id": "term_indoors",  "taxonomyName": "services", "parentId": null, "order": 1, "name": "Indoors" },
      { "id": "term_outdoors", "taxonomyName": "services", "parentId": null, "order": 2, "name": "Outdoors" }
    ],
    "hasMore": false, "hasPrevious": false, "startingAfter": null, "endingBefore": null
  },
  "responseStatus": { "isSuccess": true }
}
```

`filter` is an optional MongoDB filter, ANDed with the taxonomy. Use it to fetch one level at a time (lazy tree loading) or to find terms by any field.

---

### Get a term's children

**Goal:** the user expanded *Indoors* — load what is directly under it.

```python
children = norbix.api.database.find_terms_children("services", "term_indoors")
```

```json
{
  "list": {
    "items": [
      {
        "id": "term_air_con",
        "taxonomyName": "services",
        "parentId": "term_indoors",
        "order": 1,
        "name": "Air conditioning",
        "multiParents": [
          { "taxonomyId": "tax_service_types", "parentId": "term_indoors",          "name": "Indoors" },
          { "taxonomyId": "tax_service_types", "parentId": "term_energy_efficient", "name": "Energy efficient" }
        ]
      }
    ],
    "hasMore": false, "hasPrevious": false
  },
  "responseStatus": { "isSuccess": true }
}
```

This returns **both** direct children (their `parentId` is `term_indoors`) **and** multi-parent children (terms that list `term_indoors` in `multiParents`). Parent names are already resolved, so no second lookup.

---

### Multi-parent: one product in several categories

**Goal:** in a `products` taxonomy, a *Relaxing massage oil* belongs to *For couples*, *Gift ideas*, **and** *Body care*. Listing the children of **any** of those categories returns it.

```python
children = norbix.api.database.find_terms_children("products", "term_gift_ideas")
```

```json
{
  "list": {
    "items": [
      {
        "id": "term_relaxing_oil",
        "taxonomyName": "products",
        "name": "Relaxing massage oil",
        "multiParents": [
          { "taxonomyId": "tax_categories", "parentId": "term_for_couples", "name": "For couples" },
          { "taxonomyId": "tax_categories", "parentId": "term_gift_ideas",  "name": "Gift ideas" },
          { "taxonomyId": "tax_categories", "parentId": "term_body_care",   "name": "Body care" }
        ]
      }
    ],
    "hasMore": false, "hasPrevious": false
  },
  "responseStatus": { "isSuccess": true }
}
```

One product, three category links — no duplicate listings. The same product would also come back from the children of `term_for_couples` and `term_body_care`.

---

### Get the whole term tree in one call

**Goal:** render the full `services` tree at once, already nested.

```python
tree = norbix.api.database.find_term_tree("services")
```

```json
{
  "tree": [
    {
      "id": "term_indoors",
      "name": "Indoors",
      "order": 1,
      "children": [
        {
          "id": "term_air_con",
          "name": "Air conditioning",
          "order": 1,
          "children": [
            { "id": "term_wall", "name": "Wall-mounted", "order": 1, "children": null }
          ]
        }
      ]
    },
    {
      "id": "term_outdoors",
      "name": "Outdoors",
      "order": 2,
      "children": [
        { "id": "term_solar", "name": "Solar panels", "order": 1, "children": null }
      ]
    }
  ],
  "responseStatus": { "isSuccess": true }
}
```

Roots are in `tree`; each node carries its own `children`; a leaf has `children: null`. The tree arrives ready to render — no client-side tree building.

---

### Get only a sub-tree, capped by depth

**Goal:** start from *Indoors* and go at most 2 levels deep.

```python
tree = norbix.api.database.find_term_tree(
    "services",
    root_term_id="term_indoors",
    depth=2,
)
```

```json
{
  "tree": [
    {
      "id": "term_indoors",
      "name": "Indoors",
      "order": 1,
      "children": [
        { "id": "term_air_con", "name": "Air conditioning", "order": 1, "children": null }
      ]
    }
  ],
  "responseStatus": { "isSuccess": true }
}
```

With `depth=2` you get *Indoors* (level 1) and *Air conditioning* (level 2); *Wall-mounted* (level 3) is cut off, so *Air conditioning* shows `children: null`.

---

### Get the taxonomy structure tree — without terms

**Goal:** see how taxonomies relate to each other (e.g. a `Cities` taxonomy whose parent is `Countries`), structure only.

```python
structure = norbix.api.database.find_taxonomy_tree()
```

```json
{
  "tree": [
    {
      "viewId": "txn_countries",
      "taxonomyName": "Countries",
      "taxonomySlug": "countries",
      "parentId": null,
      "children": [
        { "viewId": "txn_cities", "taxonomyName": "Cities", "taxonomySlug": "cities", "parentId": "txn_countries", "children": null, "terms": null }
      ],
      "terms": null
    }
  ],
  "responseStatus": { "isSuccess": true }
}
```

This is the **taxonomy** tree, not the term tree: nodes are taxonomies. Every `terms` is `null` because we did not ask for terms.

---

### Get the taxonomy structure tree — with terms

**Goal:** same structure, but also pull each taxonomy's terms in the same call.

```python
structure = norbix.api.database.find_taxonomy_tree(includeTerms=True)
```

```json
{
  "tree": [
    {
      "viewId": "txn_countries",
      "taxonomyName": "Countries",
      "taxonomySlug": "countries",
      "parentId": null,
      "terms": [
        { "id": "term_lt", "name": "Lithuania", "order": 1, "children": null },
        { "id": "term_lv", "name": "Latvia",    "order": 2, "children": null }
      ],
      "children": [
        {
          "viewId": "txn_cities",
          "taxonomyName": "Cities",
          "taxonomySlug": "cities",
          "parentId": "txn_countries",
          "terms": [
            { "id": "term_vilnius", "name": "Vilnius", "order": 1, "children": null },
            { "id": "term_kaunas",  "name": "Kaunas",  "order": 2, "children": null }
          ],
          "children": null
        }
      ]
    }
  ],
  "responseStatus": { "isSuccess": true }
}
```

Now each taxonomy node's `terms` holds that taxonomy's full term tree (same shape as `find_term_tree`) — *Countries* carries its countries, *Cities* carries its cities.

> Every term-reading call also accepts an optional `databaseIntegrationId` to target a non-default database.

---

### Records the caller owns

**Goal:** list only the records of `products` that the signed-in user is
responsible for.

```python
mine = norbix.api.database.find_own("products", pageSize=20)
```

### A taxonomy's merged term tree

**Goal:** get one tree across taxonomies: the terms of `services` are the
roots, and the terms of its child taxonomies nest under them.

```python
tree = norbix.api.database.find_merged_term_tree("services")
```

---

## Changing many records

`update_many` and `delete_many` change every record that matches `filter`. An
empty filter (`'{}'`) matches **every** record of the collection, so the
gateway refuses it with `CM-ERRORS-DATABASE-037` unless you also send
`allRecords=True`. For `update_many` a missing filter counts as `'{}'`.

```python
norbix.api.database.update_many("products", filter='{"status": "draft"}', update='{"status": "live"}')
norbix.api.database.delete_many("products", filter="{}", allRecords=True)  # every record
```

Pass the flag with its wire name, `allRecords` (the SDK sends keyword
arguments as given).

- **Own-record rights are enough.** A caller with only `createAsUser`,
  `updateOwn` or `deleteOwn` may call `insert_many`, `update_many` and
  `delete_many`; the call changes only the caller's own records (before, it
  was refused with 403).
- **No `$` operators in an update.** `update_one` / `update_many` take the new
  values as a plain document (`'{"price": 10}'`). `$inc`, `$set` and the like
  are refused with `CM-ERRORS-DATABASE-035`.
- **A broken record document** on `insert_one`, `insert_many` or `replace_one`
  is refused with `CM-ERRORS-DATABASE-036` "Invalid record document" (before,
  `005`). For `insert_many`, `err.errors[0].context["Index"]` is the position
  of the bad document.
- **Soft-deleted records are not found** by update, replace and change owner;
  a bulk update skips them.
- **Change owner** (`change_responsibility`) refuses a new owner who is not a
  user of the project in the request environment, with
  `CM-ERRORS-MEMBERSHIP-USERS-012`.

```python
from norbix_python import NorbixError

try:
    norbix.api.database.delete_many("products", filter="{}")
except NorbixError as err:
    assert err.error_code == "CM-ERRORS-DATABASE-037"
```

## Term reads: rights and errors

- Term reads by taxonomy name (`find_terms`, `find_terms_children`,
  `find_term_tree`, `find_merged_term_tree`) check `database:read` on
  `database:term:{taxonomy id}`. The merged tree checks it on every nested
  taxonomy too.
- `find_terms` and `find_terms_children` refuse `$where`, `$function` and
  `$accumulator` in `filter` with `CM-ERRORS-DATABASE-031`.
- `CM-ERRORS-TAXONOMIES-010`: the taxonomy name is unknown (the merged tree
  used to answer `-003`).
- `CM-ERRORS-TAXONOMIES-011`: the term tree has more than 5000 terms (whole
  taxonomy, merged tree, `find_taxonomy_tree(includeTerms=True)`).
- `CM-ERRORS-TAXONOMIES-005`: a taxonomy name longer than 40 characters.
- `find_taxonomy_tree(includeTerms=True)` fails when reading the terms fails.
  Before, it returned the taxonomies without terms.

## Aggregates

`aggregate` and `execute_aggregate` refuse a pipeline that joins a collection
the caller cannot read (`CM-ERRORS-DATABASE-033`), a name that is not a schema
in the request environment (`032`), or a join into another database (`034`).
`execute_aggregate` also needs `database:read` on the collection, and refuses
a saved `$out` / `$merge` / JavaScript stage (`031`).
