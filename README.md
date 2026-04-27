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

## Quickstart

```python
from norbix_python import Norbix

# Service mode
norbix = Norbix(api_key="<api_key>", project_id="proj_123")

norbix.api.database.find({"collectionName": "orders"})
norbix.hub.database.getDatabaseSchemas()
```

```python
# User mode
norbix = Norbix(project_id="proj_123")
norbix.login({"userName": "alice@team.io", "password": "secret"})
norbix.api.database.find({"collectionName": "orders"})
```

## Real-world examples

### 1) List recent orders (API scope)

```python
from norbix_python import Norbix, NorbixError

norbix = Norbix(api_key="sk_live_xxx", project_id="proj_123")

try:
    response = norbix.api.database.find(
        {
            "collectionName": "orders",
            "take": 20,
            "skip": 0,
            "orderBy": [{"field": "createdAt", "direction": "desc"}],
        }
    )
    items = response.get("results", []) if isinstance(response, dict) else []
    print(f"Fetched {len(items)} orders")
except NorbixError as exc:
    print(exc.code, exc.status, exc.message)
```

### 2) Login as user and load profile

```python
from norbix_python import LoginCredentials, Norbix

norbix = Norbix(project_id="proj_123")

auth = norbix.login(LoginCredentials(userName="alice@team.io", password="secret"))
print("Logged in, token prefix:", str(auth.get("bearerToken", ""))[:16])

me = norbix.api.membership.getCurrentUser({})
print("Current user payload:", me)
```

### 3) Account-scoped Hub call (requires account_id)

```python
from norbix_python import Norbix

norbix = Norbix(
    api_key="sk_live_xxx",
    project_id="proj_123",
    account_id="acc_456",  # required for account-scoped endpoints
)

account = norbix.hub.account.getAccount({})
print(account)
```

## Authentication

- API key: set `api_key` or `NORBIX_API_KEY`
- JWT bearer: set `bearer_token`, `NORBIX_BEARER_TOKEN`, or call `norbix.login(...)`
- If both are configured, bearer token wins
- If neither is configured, SDK raises `NORBIX_NOT_AUTHENTICATED`

## Configuration from environment

```bash
NORBIX_API_KEY=sk_live_...
NORBIX_PROJECT_ID=proj_123
NORBIX_ACCOUNT_ID=acc_456
NORBIX_API_URL=https://api.norbix.dev
NORBIX_HUB_URL=https://hub.norbix.dev
```

```python
norbix = Norbix()  # reads from environment
```

## Project vs account scope

- `project_id` is required
- `account_id` is optional
- Account-scoped Hub methods raise `NORBIX_ACCOUNT_SCOPE_REQUIRED` if `account_id` is not configured

## Generated references

Like the TypeScript SDK, this package is generated from ServiceStack references.

- `uv run python scripts/sync_types.py` generates `references/*_dtos.py` using `x python <url>`
- `uv run python scripts/sync_types.py --update-only` updates existing `*_dtos.py` files in place
- `uv run python scripts/generate_endpoints.py` regenerates modules, tests, and docs

Install `x` if needed:

```bash
dotnet tool install --global x
```

## Development

```bash
uv sync
uv run ruff check .
uv run mypy src
uv run pytest
uv run python scripts/generate_endpoints.py
```

## Releases

Pushes to `main`, `next`, and `beta` run
[python-semantic-release](https://python-semantic-release.readthedocs.io/)
and publish to PyPI.

## License

MIT
