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
```

```python
norbix = NorbixApi()  # reads from environment when values omitted
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
