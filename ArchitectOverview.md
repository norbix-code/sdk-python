# Architect Overview — norbix-python SDK

> Author role: Python Architect (20+ years).
> Scope: developer UX of the Python SDK — how config is initiated, how the library feels when imported and used in real scripts.
> Reviewed paths: `src/norbix_python/__init__.py`, `src/norbix_python/client.py`, `src/norbix_python/transport.py`, `src/norbix_python/errors.py`, `src/norbix_python/api/*.py`, `src/norbix_python/hub/*.py`, `tests/*.py`, `pyproject.toml`, `README.md`.

---

## Suggestions list (sorted by impact)

### Naming and Python idioms

1. **Method names are camelCase, not snake_case.** `findOne`, `getDatabaseSchemas`, `deleteMany` look like JavaScript / C#. Python community uses `find_one`, `get_database_schemas`, `delete_many`. PyMongo, boto3, requests, stripe, openai — all use snake_case. This is the single biggest UX issue.
2. **`LoginCredentials` fields use camelCase (`userName`).** Should be `user_name` with a serialization alias for the wire format.
3. **Module class names like `DatabaseModule` are noisy.** `Database`, `Files`, `Ai` is enough. Users do not write these names anyway.

### API ergonomics — the "import and use" feeling

4. **Every method takes one big `dict[str, Any]`.** No autocomplete, no type hints, no IDE help. User cannot tell which keys are path parameters, which are query, which are body.
   - Now: `db.findOne({"collectionName": "orders", "id": "123"})`
   - Better: `db.find_one("orders", id="123")` or `db.collection("orders").find_one("123")`
5. **No fluent / resource-oriented API.** Best Python SDKs feel like: `s3.objects("bucket").list()`, `db["orders"].find_one(id)`. Norbix forces you to build a dict every call.
6. **Return type is always `Any`.** README itself shows the pain:
   ```python
   items = response.get("results", []) if isinstance(response, dict) else []
   ```
   This is a code smell. Return Pydantic models or at minimum `TypedDict`.
7. **No `download()` / `upload()` / `execute()` style methods.** The `db.FindAll()`, `files.Download()`, `code.Execute()` style is missing. `hub/files.py` only has trigger and integration management (`enableFiles`, `saveFilesIntegration`). There is no real file upload / download / list. There is no `code.execute()` module at all.

### Configuration / initialization UX

8. **Env variables are supported (good).** `NORBIX_PROJECT_ID`, `NORBIX_API_KEY`, etc. are read in `src/norbix_python/client.py` lines 42–54. This part is solid.
9. **No `.env` auto-loading.** Most modern SDKs (or their docs) suggest `python-dotenv`. The README does not mention it.
10. **No global / default client pattern.** OpenAI and stripe let you do `stripe.api_key = "..."` then `stripe.Customer.list()`. Norbix forces explicit `Norbix(...)` every time. For scripts, a module-level client is friendlier.
11. **`project_id` always required.** Even for endpoints that don't need it (`/auth`). This forces users to set it before login is even possible, which is strange.
12. **API key and bearer token are mixed under one `Authorization: Bearer` header** (`transport.py` line 74). Most APIs use `Authorization: ApiKey ...` or a separate header for API keys. Mixing them is unclear and risky.

### Architecture / safety

13. **Path parameters are extracted from the request dict by string matching** (`_build_url_and_body`, `transport.py` lines 115–144). This is "magic" — caller does not know which keys vanish from the body. Case-insensitive lookup (`_lookup_case_insensitive`, lines 147–154) makes it worse: `id` and `Id` collide silently.
14. **Private attribute mutation.** `client.py` line 81 does `self._transport._cfg.bearer_token = str(...)` — touching a private field. The `set_bearer_token()` method already exists (line 87) but `login()` does not use it. Inconsistent.
15. **`NorbixError` is a `@dataclass` AND an `Exception`.** This works in Python 3.10+ but is fragile — `Exception.__init__` is bypassed. A normal class with `__init__` calling `super().__init__(message)` is safer.
16. **No `__enter__` / `__exit__`** on `Norbix`. Should support `with Norbix(...) as client:` so the underlying `httpx.Client` is closed automatically.
17. **No async client.** `httpx` already gives you `AsyncClient`. Modern Python SDKs ship `AsyncNorbix` for free.
18. **No retries, no backoff, no rate-limit handling.** Stripe's SDK retries idempotent calls automatically.
19. **No pagination helper.** `find()` returns `{"results": [...]}` but the user has to handle `skip`/`take` themselves. An iterator (`for order in db.orders.iter_all()`) is the standard.

### Tests / docs

20. **Only 3 tests in `tests/test_client.py`.** Coverage of modules (`database`, `files`, `ai`) is zero. The boilerplate of every method is identical — one parametrized test would cover all of them.
21. **README example uses `getCurrentUser({})`** but this method is not in `src/norbix_python/api/membership.py`. Either the doc is stale or the method is missing.
22. **`per-file-ignores` in `pyproject.toml`** (lines 47–50) disables `E501` and `I001` for all generated modules. This hides real issues. Generated code should still be linted.

---

## Summary

The SDK is a thin, generated wrapper over the HTTP API. The transport layer (`src/norbix_python/transport.py`) is clean and the env-variable support in `src/norbix_python/client.py` (lines 42–54) is well done. The **biggest weakness is developer UX** — the SDK feels like a TypeScript library translated to Python rather than a Python library. A senior Python developer using this for the first time will not feel "at home".

### Where it hurts most — config initiation

The env-variable story is fine, but the constructor surface in `src/norbix_python/client.py` (lines 27–65) is wide (10+ parameters). A user who only wants `Norbix()` from `.env` is fine, but a user who wants explicit credentials has to pass several keyword arguments. Splitting into `Norbix.from_env()` and `Norbix(api_key=..., project_id=...)` would clarify intent. Adding a top-level helper like:

```python
import norbix
norbix.configure(api_key="sk_live_...", project_id="proj_123")
norbix.db.find_all("orders")
```

would match the OpenAI / stripe style users expect.

### Where it hurts most — calling style

The request style `db.FindAll()`, `files.Download()`, `code.Execute()` is not possible today.

Today (from `README.md` lines 46–53):

```python
response = norbix.api.database.find(
    {"collectionName": "orders", "take": 20, "skip": 0,
     "orderBy": [{"field": "createdAt", "direction": "desc"}]}
)
items = response.get("results", []) if isinstance(response, dict) else []
```

What it should look like (PyMongo / stripe style):

```python
orders = norbix.db("orders").find_all(take=20, order_by="-createdAt")
for order in orders:
    print(order.id)
```

The current style is caused by `src/norbix_python/api/database.py` lines 143–153 where `find` accepts only a dict and returns `Any`. The dict-only signature comes from the code generator. To fix this without rewriting the generator, add a thin **hand-written facade layer** on top of the generated modules — for example `src/norbix_python/db.py` exposing `Collection.find_all()`, `find_one()`, `insert_one()` with typed kwargs, calling the generated `database.find(...)` underneath.

### File operations are missing

`src/norbix_python/hub/files.py` only manages triggers and integrations (`enableFiles`, `saveFilesIntegration`, lines 23–177). There is no `upload()`, `download()`, `list()`, `delete_object()`. If the backend supports file storage, the SDK is not exposing it. If it does not, then the module name `files` is misleading.

### Path parameter handling is magical

`transport.py` lines 121–134 walks the URL template and pulls keys from the request dict — case-insensitive (`_lookup_case_insensitive`, lines 147–154). The user has no way to tell from the method signature `database.findOne(request)` which dict keys are path parameters (`collectionName`, `id`) and which are body. Promote them to explicit positional arguments in the generated code:

```python
def find_one(self, collection_name: str, id: str, *, timeout: float | None = None) -> Any:
    ...
```

### Auth state is leaky

`client.py` line 81 writes directly to `self._transport._cfg.bearer_token` — bypassing `set_bearer_token()` (line 87) which exists for exactly this. Replace with `self.set_bearer_token(str(result["bearerToken"]))`. Also, `transport.py` line 74 sends `api_key` as `Authorization: Bearer ...` together with JWT tokens — most APIs separate these. Add a clear header strategy.

### Errors swallow detail

`NorbixError` (`src/norbix_python/errors.py`) is a `@dataclass(Exception)`. It works but is fragile. Convert to a normal exception class with `super().__init__(message)`, keep `code`, `status`, `details` as attributes, and add subclasses (`AuthenticationError`, `RateLimitError`, `NotFoundError`, `ValidationError`) so users can write:

```python
try:
    norbix.db.find_one("orders", id="123")
except NotFoundError:
    ...
except RateLimitError:
    ...
```

like in stripe and openai SDKs.

### Quality of the plan / generation pipeline

The architecture (one `Transport` + one module per resource + namespaces `api` / `hub`) is reasonable and extendable. The `pyproject.toml` is professional — `ruff`, `mypy --strict`, `pytest`, semantic-release. But `tool.ruff.lint.per-file-ignores` (lines 47–50) silences linting for the generated modules — that hides bugs in the very code most users will read.

---

## Top 5 actions, in order

1. **Rename methods to snake_case in the generator.** This alone removes 80% of the "this feels foreign" feeling.
2. **Promote path parameters to explicit function arguments.** Stop reading them out of the request dict.
3. **Add a hand-written facade** for the most-used resources: `db.collection("orders").find_all()`, `files.upload(path)`, etc. — backed by the generated code.
4. **Return typed objects (Pydantic v2 models)**, since you already require Python 3.10+. Stop returning `Any`.
5. **Add `__enter__`/`__exit__`, an `AsyncNorbix`, and basic retries on idempotent verbs.**

If you do these five, the SDK will feel like a first-class Python library and not a generated transport.
