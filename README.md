# norbix-python

[![CI](https://github.com/norbix-dev/norbix-python/actions/workflows/ci.yml/badge.svg)](https://github.com/norbix-dev/norbix-python/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/norbix-python.svg)](https://pypi.org/project/norbix-python/)
[![Python](https://img.shields.io/badge/python-%3E=3.10-blue)](https://python.org)
[![License](https://img.shields.io/pypi/l/norbix-python.svg)](./LICENSE)

Official Python SDK for [Norbix](https://norbix.dev). One client wraps both the
**API** (project-scoped data) and **Hub** (project/account configuration).

## Install

```bash
uv add norbix-python
```

Optional: load `.env` in apps with `python-dotenv` (`load_dotenv()` before constructing `Norbix()`).

## Quickstart

```python
from norbix_python import Norbix

# Service mode
norbix = Norbix(api_key="<api_key>", project_id="proj_123")

norbix.api.database.find(
    "orders",
    request={
        "take": 20,
        "skip": 0,
        "orderBy": [{"field": "createdAt", "direction": "desc"}],
    },
)
norbix.hub.database.get_database_schemas({})
```

```python
# User mode (project_id optional until you call project-scoped endpoints)
from norbix_python import LoginCredentials, Norbix

norbix = Norbix()
norbix.login(LoginCredentials(user_name="alice@team.io", password="secret"))
norbix.set_scope(project_id="proj_123")
norbix.api.database.find("orders", request={"take": 10})
```

### Convenience wrapper (collection-oriented)

```python
from norbix_python import Norbix

norbix = Norbix(api_key="...", project_id="proj_123")
orders = norbix.collection("orders").find_all(
    take=20,
    order_by=[{"field": "createdAt", "direction": "desc"}],
)
```

### Async client

```python
from norbix_python import AsyncNorbix

async def main() -> None:
    async with AsyncNorbix(api_key="...", project_id="proj_123") as client:
        await client.api.echo.echo({})

# asyncio.run(main())
```

### Module-level default client

```python
import norbix_python as nb

nb.configure(api_key="...", project_id="proj_123")
nb.get_client().api.echo.echo({})
```

## Real-world examples

### 1) List recent orders (API scope)

```python
from norbix_python import DatabaseFindResult, Norbix, NorbixError

norbix = Norbix(api_key="sk_live_xxx", project_id="proj_123")

try:
    raw = norbix.api.database.find(
        "orders",
        request={
            "take": 20,
            "skip": 0,
            "orderBy": [{"field": "createdAt", "direction": "desc"}],
        },
    )
    typed = DatabaseFindResult.model_validate(raw) if isinstance(raw, dict) else DatabaseFindResult()
    items = typed.results
    print(f"Fetched {len(items)} orders")
except NorbixError as exc:
    print(exc.code, exc.status, exc.message)
```

### 2) Login as user and load profile

```python
from norbix_python import LoginCredentials, Norbix

norbix = Norbix(project_id="proj_123")

auth = norbix.login(LoginCredentials(user_name="alice@team.io", password="secret"))
print("Logged in, token prefix:", str(auth.get("bearerToken", ""))[:16])

users = norbix.api.membership.get_users({})
print("Users response:", users)
```

### 3) Account-scoped Hub call (requires account_id)

```python
from norbix_python import Norbix

norbix = Norbix(
    api_key="sk_live_xxx",
    project_id="proj_123",
    account_id="acc_456",  # required for account-scoped endpoints
)

account = norbix.hub.account.get_account_profile({})
print(account)
```

## Breaking changes (recent major-style refresh)

- Methods use **snake_case** (`find_one`, `get_database_schemas`) instead of camelCase.
- Path parameters are **positional or keyword** arguments (for example `find("orders", ...)`,
  `find_one("orders", id)`). Remaining query/body fields go in `request={...}`.
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
NORBIX_API_URL=https://api.norbix.dev
NORBIX_HUB_URL=https://hub.norbix.dev
```

```python
norbix = Norbix()  # reads from environment when values omitted
```

## Project vs account scope

- `project_id` is required for **project**- and **account**-scoped endpoints (set explicitly or via env).
- You may construct `Norbix()` without `project_id` for **login-only** flows; set `project_id` before other calls (for example `set_scope(project_id=...)`).
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
