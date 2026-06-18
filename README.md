# norbix-python

[![CI](https://github.com/norbix-dev/norbix-python/actions/workflows/ci.yml/badge.svg)](https://github.com/norbix-dev/norbix-python/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/norbix.svg)](https://pypi.org/project/norbix/)
[![Python](https://img.shields.io/badge/python-%3E=3.10-blue)](https://python.org)
[![License](https://img.shields.io/pypi/l/norbix.svg)](./LICENSE)

Official Python SDK for [Norbix](https://norbix.dev).
Use split clients with flat module access:

- `NorbixApi` for API scope (`client.database`, `client.membership`, ...)
- `NorbixHub` for Hub scope (`client.database`, `client.account`, ...)

## Install

```bash
uv add norbix
```

Optional: load `.env` in apps with `python-dotenv` (`load_dotenv()` before constructing `Norbix()`).

## Quickstart

```python
from norbix_python import NorbixApi

# Service mode
norbix = NorbixApi(api_key="<api_key>", project_id="proj_123")

norbix.database.find("orders", take=20, skip=0, orderBy=[{"field": "createdAt", "direction": "desc"}])
```

```python
# User mode
from norbix_python import LoginCredentials, NorbixApi

norbix = NorbixApi(project_id="proj_123")
norbix.login(LoginCredentials(user_name="alice@team.io", password="secret"))
norbix.database.find("orders", take=10)
```

### Async client

```python
from norbix_python import AsyncNorbix

async def main() -> None:
    async with AsyncNorbix(api_key="...", project_id="proj_123") as client:
        await client.api.echo.echo()

# asyncio.run(main())
```

## Real-world examples

### 1) List recent orders (API scope)

```python
from norbix_python import DatabaseFindResult, NorbixApi, NorbixError

norbix = NorbixApi(api_key="sk_live_xxx", project_id="proj_123")

try:
    raw = norbix.database.find("orders", take=20, skip=0, orderBy=[{"field": "createdAt", "direction": "desc"}])
    typed = DatabaseFindResult.model_validate(raw) if isinstance(raw, dict) else DatabaseFindResult()
    items = typed.results
    print(f"Fetched {len(items)} orders")
except NorbixError as exc:
    print(exc.code, exc.status, exc.message)
```

### 2) Login as user and load profile

```python
from norbix_python import LoginCredentials, NorbixApi

norbix = NorbixApi(project_id="proj_123")

auth = norbix.login(LoginCredentials(user_name="alice@team.io", password="secret"))
print("Logged in, token prefix:", str(auth.get("bearerToken", ""))[:16])

users = norbix.membership.get_users()
print("Users response:", users)
```

### 3) Account-scoped Hub call (requires account_id)

```python
from norbix_python import NorbixHub

norbix = NorbixHub(
    api_key="sk_live_xxx",
    project_id="proj_123",
    account_id="acc_456",  # required for account-scoped endpoints
)

account = norbix.account.get_account_profile()
print(account)
```

## Breaking changes (recent major-style refresh)

- Methods use **snake_case** (`find_one`, `get_database_schemas`) instead of camelCase.
- Path parameters are **positional or keyword** arguments (for example `find("orders", ...)`,
  `find_one("orders", id)`). Remaining query/body fields are passed as keyword args.
- Use **typed errors** where helpful: `AuthenticationError`, `NotFoundError`, `RateLimitError`,
  `ValidationError` (all subclass `NorbixError`).

## Authentication

- API key: set `api_key` or `NORBIX_API_KEY`
- JWT bearer: set `bearer_token`, `NORBIX_BEARER_TOKEN`, or call `norbix.login(...)`
- If both are configured, bearer token wins
- If neither is configured, SDK raises `NORBIX_NOT_AUTHENTICATED`

API keys and JWTs are sent as `Authorization: Bearer ...` (document your backend expectations).

## Configuration from environment

```bash
NORBIX_API_KEY=sk_live_...
NORBIX_PROJECT_ID=proj_123
NORBIX_ACCOUNT_ID=acc_456
NORBIX_API_URL=https://api.norbix.ai
NORBIX_HUB_URL=https://hub.norbix.ai
NORBIX_REGION=nb-eu-germany
```

```python
norbix = NorbixApi()  # reads from environment when values omitted
```

## Multi-region support

Norbix can run a project in one or more regions (region codes like
`nb-eu-germany`). The SDK has **no default region**: when no region is
configured, no region header is sent and the standard base URLs are used.

### Selecting a region

Resolution order: explicit `region=` on the client → `NORBIX_REGION`
environment variable → unset (no header).

```python
from norbix_python import Norbix

norbix = Norbix(api_key="sk_live_xxx", project_id="proj_123", region="nb-eu-germany")
```

`region=` is accepted by all clients: `Norbix`, `NorbixApi`, `NorbixHub`,
and `AsyncNorbix`. Every request then carries the `nb-region` header.

### Switching at runtime

```python
norbix.set_region("nb-eu-germany")   # subsequent requests target this region
norbix.get_region()                  # "nb-eu-germany"
norbix.set_region(None)              # clear — no nb-region header is sent
```

Available on the sync clients and `AsyncNorbix` alike.

### Per-call override (header only)

The `client.hub.regions` methods accept a per-call `region=` that overrides
the client default **for that request's `nb-region` header only** — the
request URL is never changed by a per-call region:

```python
norbix.hub.regions.list(region="nb-us-east")
```

### Regional base URLs

When a region is set and you are using the SDK-default base URLs
(`https://api.norbix.ai` / `https://hub.norbix.ai`), the SDK prefixes the
region as a subdomain:

```text
region="nb-eu-germany"  →  https://nb-eu-germany.api.norbix.ai
                           https://nb-eu-germany.hub.norbix.ai
```

Custom base URLs (`base_url_api=`, `base_url_hub=`, `NORBIX_API_URL`,
`NORBIX_HUB_URL`) are **never rewritten** — self-hosted and custom
deployments are unaffected; the `nb-region` header is still sent when a
region is configured.

### Managing regions (Hub, account scope)

These endpoints require `account_id` (see
[Project vs account scope](#project-vs-account-scope)).

```python
from norbix_python import NorbixHub

norbix = NorbixHub(api_key="sk_live_xxx", project_id="proj_123", account_id="acc_456")

# Regions available to the account.
# Response shape: {"items": [{"id": ..., "continent": ..., "name": ...}, ...]}
# where "id" is the region code (e.g. "nb-eu-germany").
regions = norbix.regions.list()

# Update the regions a project runs in (omitted fields are left unchanged)
norbix.regions.update_project_regions(
    "proj_123",
    primary_region="nb-eu-germany",
    additional_regions=["nb-us-east"],
)

# Pin a new project to regions at creation time
norbix.account.create_project(
    name="my-project",
    primary_region="nb-eu-germany",
    additional_regions=["nb-us-east"],
)
```

With the combined client the same modules live under `client.hub`
(`norbix.hub.regions.list()`, `norbix.hub.account.create_project(...)`).

### Async

```python
from norbix_python import AsyncNorbix

async def main() -> None:
    async with AsyncNorbix(
        api_key="sk_live_xxx",
        project_id="proj_123",
        account_id="acc_456",
        region="nb-eu-germany",
    ) as client:
        regions = await client.hub.regions.list()
        await client.hub.regions.update_project_regions(
            "proj_123",
            primary_region="nb-eu-germany",
            region="nb-us-east",  # per-call header override
        )
        client.set_region(None)  # clear at runtime
```

## Project vs account scope

- `project_id` is required (set explicitly or via env).
- `account_id` is optional
- Account-scoped Hub methods raise `NORBIX_ACCOUNT_SCOPE_REQUIRED` if `account_id` is not configured

## SDK maintenance

Regenerate API and Hub modules from DTO stubs:

```bash
uv run python scripts/generate_endpoints.py
```

This refreshes `src/norbix_python/api/`, `hub/`, matching tests under `tests/api` and `tests/hub`, and docs under `docs/`.

## Development

```bash
uv sync
uv run ruff check .
uv run mypy src
uv run pytest
```

## Releases

Pushes to `main`, `next`, and `beta` run
[python-semantic-release](https://python-semantic-release.readthedocs.io/)
and publish to PyPI.

## License

MIT
