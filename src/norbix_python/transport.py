from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal
from urllib.parse import urlencode

import httpx

from .errors import NorbixError

HttpVerb = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
Scope = Literal["project", "account", "unauthenticated"]
Target = Literal["api", "hub"]


@dataclass
class TransportConfig:
    api_key: str | None
    bearer_token: str | None
    project_id: str
    account_id: str | None
    base_url_api: str
    base_url_hub: str
    api_version: str
    hub_version: str
    timeout: float
    default_headers: dict[str, str] = field(default_factory=dict)


class Transport:
    def __init__(self, cfg: TransportConfig, client: httpx.Client | None = None) -> None:
        self._cfg = cfg
        self._client = client or httpx.Client(timeout=cfg.timeout)

    def close(self) -> None:
        self._client.close()

    def send(
        self,
        *,
        target: Target,
        path: str,
        method: HttpVerb,
        request: dict[str, Any] | None = None,
        scope: Scope = "project",
        timeout: float | None = None,
        bearer_token: str | None = None,
    ) -> Any:
        if scope == "account" and not self._cfg.account_id:
            raise NorbixError(
                message="This endpoint is account-scoped. Configure account_id on the client.",
                code="NORBIX_ACCOUNT_SCOPE_REQUIRED",
            )

        base_url = self._cfg.base_url_api if target == "api" else self._cfg.base_url_hub
        version = self._cfg.api_version if target == "api" else self._cfg.hub_version
        req = request or {}
        url, body = _build_url_and_body(
            base_url=base_url,
            path=path,
            version=version,
            method=method,
            request=req,
        )
        headers = {"Accept": "application/json", **self._cfg.default_headers}

        if scope != "unauthenticated":
            token = bearer_token or self._cfg.bearer_token or self._cfg.api_key
            if not token:
                raise NorbixError(
                    message="Not authenticated. Provide api_key / bearer_token or login first.",
                    code="NORBIX_NOT_AUTHENTICATED",
                )
            headers["Authorization"] = f"Bearer {token}"

        headers["X-CM-ProjectId"] = self._cfg.project_id
        if self._cfg.account_id:
            headers["X-CM-AccountId"] = self._cfg.account_id
        if body is not None:
            headers["Content-Type"] = "application/json"

        try:
            response = self._client.request(
                method=method,
                url=url,
                headers=headers,
                json=body,
                timeout=timeout or self._cfg.timeout,
            )
        except httpx.HTTPError as exc:
            raise NorbixError(message=str(exc), code="NORBIX_NETWORK_ERROR") from exc

        if response.status_code >= 400:
            data: dict[str, Any]
            try:
                parsed = response.json()
                data = parsed if isinstance(parsed, dict) else {}
            except ValueError:
                data = {}
            raise NorbixError(
                message=data.get("message", response.text or "Request failed"),
                status=response.status_code,
                code=data.get("errorCode", f"HTTP_{response.status_code}"),
                details=data,
            )

        if response.status_code == 204 or not response.content:
            return None
        try:
            return response.json()
        except ValueError:
            return response.text


def _build_url_and_body(
    *, base_url: str, path: str, version: str, method: HttpVerb, request: dict[str, Any]
) -> tuple[str, dict[str, Any] | None]:
    normalized = path.replace("{version}", version)
    consumed: set[str] = set()

    while True:
        start = normalized.find("{")
        end = normalized.find("}", start + 1)
        if start < 0 or end < 0:
            break
        token = normalized[start + 1 : end]
        value, key = _lookup_case_insensitive(request, token)
        if value is None:
            raise NorbixError(
                message=f"Missing path parameter '{token}' for path {path}",
                code="NORBIX_MISSING_PATH_PARAM",
            )
        consumed.add(key)
        normalized = normalized[:start] + str(value) + normalized[end + 1 :]

    remaining = {k: v for k, v in request.items() if k not in consumed and v is not None}
    url = f"{base_url.rstrip('/')}/{normalized.lstrip('/')}"
    if method in {"GET", "DELETE"}:
        query = urlencode(
            [(k, _stringify(v)) for k, v in remaining.items() for v in _to_iterable(v)],
            doseq=True,
        )
        return (f"{url}?{query}" if query else url, None)
    return (url, remaining if remaining else None)


def _lookup_case_insensitive(values: dict[str, Any], key: str) -> tuple[Any | None, str]:
    if key in values:
        return values[key], key
    lower_key = key.lower()
    for current_key, current_value in values.items():
        if current_key.lower() == lower_key:
            return current_value, current_key
    return None, key


def _to_iterable(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    return [value]


def _stringify(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)
