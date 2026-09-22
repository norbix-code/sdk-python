from __future__ import annotations

import asyncio
import random
import time
from dataclasses import dataclass, field
from typing import Any, Literal
from urllib.parse import urlencode

import httpx

from .errors import NorbixError, error_from_body, says_it_failed

HttpVerb = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
Scope = Literal["project", "account", "unauthenticated"]
# How to read a successful response body. "json" (the default) parses it.
# "binary" gives back the raw bytes — for an endpoint that answers with a
# file rather than a document, such as a public file link. Parsing a PDF as
# JSON quietly hands back its text instead (10b-files slice SDK-2).
ResponseType = Literal["json", "binary"]
Target = Literal["api", "hub"]

_IDEMPOTENT_VERBS: frozenset[str] = frozenset({"GET", "DELETE"})
_DEFAULT_MAX_RETRIES = 3


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
    env: str = "PROD"
    region: str | None = None
    base_url_api_is_default: bool = False
    base_url_hub_is_default: bool = False
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
        path_params: dict[str, Any] | None = None,
        request: dict[str, Any] | None = None,
        scope: Scope = "project",
        timeout: float | None = None,
        bearer_token: str | None = None,
        env: str | None = None,
        region: str | None = None,
        response_type: ResponseType = "json",
        follow_redirects: bool = False,
    ) -> Any:
        if scope == "account" and not self._cfg.account_id:
            raise NorbixError(
                message="This endpoint is account-scoped. Configure account_id on the client.",
                code="NORBIX_ACCOUNT_SCOPE_REQUIRED",
            )
        # project_id is required at construction; kept for defensive checks only.

        base_url = self._cfg.base_url_api if target == "api" else self._cfg.base_url_hub
        version = self._cfg.api_version if target == "api" else self._cfg.hub_version
        params = path_params or {}
        req = request or {}
        url, body = _build_url_and_body(
            base_url=base_url,
            path=path,
            version=version,
            method=method,
            path_params=params,
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
        # Environment selector: per-call override wins over the client default.
        # "PROD" is the backend default, so the header is omitted for it.
        resolved_env = env if env is not None else self._cfg.env
        if resolved_env and resolved_env != "PROD":
            headers["norbix-env"] = resolved_env
        # Region selector: per-call override wins over the client default.
        # There is no default region — the header is omitted when unset.
        resolved_region = region if region is not None else self._cfg.region
        if resolved_region:
            headers["nb-region"] = resolved_region
        if body is not None:
            headers["Content-Type"] = "application/json"

        try:
            response = self._request_with_retries(
                method=method,
                url=url,
                headers=headers,
                json=body,
                timeout=timeout or self._cfg.timeout,
                follow_redirects=follow_redirects,
            )
        except httpx.HTTPError as exc:
            raise NorbixError(message=str(exc), code="NORBIX_NETWORK_ERROR") from exc

        if response.status_code >= 400:
            try:
                parsed: Any = response.json()
            except ValueError:
                parsed = None
            raise error_from_body(
                body=parsed,
                status=response.status_code,
                text=response.text,
            )

        # An endpoint that answers with a file, not a document. Those answers
        # are not JSON, so the check below does not apply to them.
        if response_type == "binary":
            return response.content
        if response.status_code == 204 or not response.content:
            return None
        try:
            parsed_ok: Any = response.json()
        except ValueError:
            return response.text

        # A 2xx does not mean the call worked: the gateway answers a business
        # refusal with HTTP 200 and responseStatus.isSuccess = False, and that
        # is a failure the caller must see (10b-files, issue #67).
        if says_it_failed(parsed_ok):
            raise error_from_body(body=parsed_ok, status=response.status_code)
        return parsed_ok

    def _request_with_retries(
        self,
        *,
        method: HttpVerb,
        url: str,
        headers: dict[str, str],
        json: dict[str, Any] | None,
        timeout: float,
        follow_redirects: bool = False,
    ) -> httpx.Response:
        attempt = 0
        last_response: httpx.Response | None = None
        while attempt < _DEFAULT_MAX_RETRIES:
            response = self._client.request(
                method=method,
                url=url,
                headers=headers,
                json=json,
                timeout=timeout,
                follow_redirects=follow_redirects,
            )
            last_response = response
            if response.status_code < 400:
                return response
            if response.status_code < 500 and response.status_code != 429:
                return response
            if method not in _IDEMPOTENT_VERBS:
                return response
            attempt += 1
            if attempt >= _DEFAULT_MAX_RETRIES:
                break
            delay = 0.25 * (2 ** (attempt - 1)) + random.random() * 0.1
            time.sleep(delay)
        assert last_response is not None
        return last_response


class AsyncTransport:
    def __init__(self, cfg: TransportConfig, client: httpx.AsyncClient | None = None) -> None:
        self._cfg = cfg
        self._client = client or httpx.AsyncClient(timeout=cfg.timeout)

    async def aclose(self) -> None:
        await self._client.aclose()

    async def send(
        self,
        *,
        target: Target,
        path: str,
        method: HttpVerb,
        path_params: dict[str, Any] | None = None,
        request: dict[str, Any] | None = None,
        scope: Scope = "project",
        timeout: float | None = None,
        bearer_token: str | None = None,
        env: str | None = None,
        region: str | None = None,
        response_type: ResponseType = "json",
        follow_redirects: bool = False,
    ) -> Any:
        if scope == "account" and not self._cfg.account_id:
            raise NorbixError(
                message="This endpoint is account-scoped. Configure account_id on the client.",
                code="NORBIX_ACCOUNT_SCOPE_REQUIRED",
            )
        # project_id is required at construction; kept for defensive checks only.

        base_url = self._cfg.base_url_api if target == "api" else self._cfg.base_url_hub
        version = self._cfg.api_version if target == "api" else self._cfg.hub_version
        params = path_params or {}
        req = request or {}
        url, body = _build_url_and_body(
            base_url=base_url,
            path=path,
            version=version,
            method=method,
            path_params=params,
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
        # Environment selector: per-call override wins over the client default.
        # "PROD" is the backend default, so the header is omitted for it.
        resolved_env = env if env is not None else self._cfg.env
        if resolved_env and resolved_env != "PROD":
            headers["norbix-env"] = resolved_env
        # Region selector: per-call override wins over the client default.
        # There is no default region — the header is omitted when unset.
        resolved_region = region if region is not None else self._cfg.region
        if resolved_region:
            headers["nb-region"] = resolved_region
        if body is not None:
            headers["Content-Type"] = "application/json"

        try:
            response = await self._request_with_retries(
                method=method,
                url=url,
                headers=headers,
                json=body,
                timeout=timeout or self._cfg.timeout,
                follow_redirects=follow_redirects,
            )
        except httpx.HTTPError as exc:
            raise NorbixError(message=str(exc), code="NORBIX_NETWORK_ERROR") from exc

        if response.status_code >= 400:
            try:
                parsed: Any = response.json()
            except ValueError:
                parsed = None
            raise error_from_body(
                body=parsed,
                status=response.status_code,
                text=response.text,
            )

        # An endpoint that answers with a file, not a document. Those answers
        # are not JSON, so the check below does not apply to them.
        if response_type == "binary":
            return response.content
        if response.status_code == 204 or not response.content:
            return None
        try:
            parsed_ok: Any = response.json()
        except ValueError:
            return response.text

        # A 2xx does not mean the call worked: the gateway answers a business
        # refusal with HTTP 200 and responseStatus.isSuccess = False, and that
        # is a failure the caller must see (10b-files, issue #67).
        if says_it_failed(parsed_ok):
            raise error_from_body(body=parsed_ok, status=response.status_code)
        return parsed_ok

    async def _request_with_retries(
        self,
        *,
        method: HttpVerb,
        url: str,
        headers: dict[str, str],
        json: dict[str, Any] | None,
        timeout: float,
        follow_redirects: bool = False,
    ) -> httpx.Response:
        attempt = 0
        last_response: httpx.Response | None = None
        while attempt < _DEFAULT_MAX_RETRIES:
            response = await self._client.request(
                method=method,
                url=url,
                headers=headers,
                json=json,
                timeout=timeout,
                follow_redirects=follow_redirects,
            )
            last_response = response
            if response.status_code < 400:
                return response
            if response.status_code < 500 and response.status_code != 429:
                return response
            if method not in _IDEMPOTENT_VERBS:
                return response
            attempt += 1
            if attempt >= _DEFAULT_MAX_RETRIES:
                break
            delay = 0.25 * (2 ** (attempt - 1)) + random.random() * 0.1
            await asyncio.sleep(delay)
        assert last_response is not None
        return last_response


def _build_url_and_body(
    *,
    base_url: str,
    path: str,
    version: str,
    method: HttpVerb,
    path_params: dict[str, Any],
    request: dict[str, Any],
) -> tuple[str, dict[str, Any] | None]:
    normalized = path.replace("{version}", version)
    consumed: set[str] = set()

    while True:
        start = normalized.find("{")
        end = normalized.find("}", start + 1)
        if start < 0 or end < 0:
            break
        token = normalized[start + 1 : end]
        if token not in path_params:
            raise NorbixError(
                message=f"Missing path parameter '{token}' for path {path}",
                code="NORBIX_MISSING_PATH_PARAM",
            )
        value = path_params[token]
        consumed.add(token)
        normalized = normalized[:start] + str(value) + normalized[end + 1 :]

    remaining = {k: v for k, v in request.items() if v is not None}
    url = f"{base_url.rstrip('/')}/{normalized.lstrip('/')}"
    if method in {"GET", "DELETE"}:
        query = urlencode(
            [(k, _stringify(v)) for k, v in remaining.items() for v in _to_iterable(v)],
            doseq=True,
        )
        return (f"{url}?{query}" if query else url, None)
    return (url, remaining if remaining else None)


def _to_iterable(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    return [value]


def _stringify(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)
