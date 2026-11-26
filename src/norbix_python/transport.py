from __future__ import annotations

import asyncio
import random
import time
from collections.abc import AsyncIterator, Callable, Iterable, Iterator
from dataclasses import dataclass, field
from typing import Any, Literal
from urllib.parse import quote, urlencode

import httpx

from .errors import NorbixError, error_from_body, retry_after_seconds_of, says_it_failed
from .project_host import project_api_base_url

HttpVerb = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
# "optional": auth is sent when the client has a token, never required — used
# by the signed notification preview links.
Scope = Literal["project", "account", "unauthenticated", "optional"]
# How to read a successful response body. "json" (the default) parses it.
# "binary" gives back the raw bytes — for an endpoint that answers with a
# file rather than a document, such as a public file link. Parsing a PDF as
# JSON quietly hands back its text instead (10b-files slice SDK-2).
# "envelope" gives back {"status", "headers", "body"} without the business
# refusal check — for a protocol endpoint whose answer headers matter, such
# as the MCP endpoint (its session id travels in a response header).
ResponseType = Literal["json", "binary", "envelope"]
Target = Literal["api", "hub"]

_IDEMPOTENT_VERBS: frozenset[str] = frozenset({"GET", "DELETE"})
# A project sign-in's JWT slides (12 hours, 30 days with rememberMe, never past
# 90 days from sign-in). Past half its window an answer carries a fresh one in
# this header; the client swaps its stored bearer token for it.
SESSION_TOKEN_HEADER = "norbix-session-token"
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
    # Accept-Language value (e.g. "lt" or "lt-LT, en;q=0.8"). No default —
    # when unset no Accept-Language header is sent.
    language: str | None = None
    base_url_api_is_default: bool = False
    base_url_hub_is_default: bool = False
    default_headers: dict[str, str] = field(default_factory=dict)
    # Called with the new token after the client swapped its stored bearer
    # token for a ``norbix-session-token`` answer header, so the app can save it.
    on_session_token: Callable[[str], None] | None = None


class Transport:
    def __init__(self, cfg: TransportConfig, client: httpx.Client | None = None) -> None:
        self._cfg = cfg
        self._client = client or httpx.Client(timeout=cfg.timeout)

    def navigation_url(
        self,
        *,
        target: Target,
        path: str,
        path_params: dict[str, Any],
        query: list[tuple[str, str | None]],
    ) -> str:
        """URL of a GET route a browser navigates to; see ``_navigation_url``."""
        return _navigation_url(self._cfg, target, path, path_params, query)

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
        language: str | None = None,
        response_type: ResponseType = "json",
        follow_redirects: bool = False,
        extra_headers: dict[str, str] | None = None,
        query: dict[str, Any] | None = None,
    ) -> Any:
        if scope == "account" and not self._cfg.account_id:
            raise NorbixError(
                message="This endpoint is account-scoped. Configure account_id on the client.",
                code="NORBIX_ACCOUNT_SCOPE_REQUIRED",
            )
        # project_id is required at construction; kept for defensive checks only.

        base_url = _api_call_base_url(self._cfg) if target == "api" else self._cfg.base_url_hub
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
        url = _with_query(url, query)
        headers = {"Accept": "application/json", **self._cfg.default_headers}

        # The stored bearer token this request sends, if it sends one. Only
        # that token is ever swapped for a fresher one (never an API key or a
        # per-call token the client does not hold).
        sent_stored_token: str | None = None
        if scope != "unauthenticated":
            token = bearer_token or self._cfg.bearer_token or self._cfg.api_key
            if not token and scope != "optional":
                raise NorbixError(
                    message="Not authenticated. Provide api_key / bearer_token or login first.",
                    code="NORBIX_NOT_AUTHENTICATED",
                )
            if token:
                headers["Authorization"] = f"Bearer {token}"
                if token == self._cfg.bearer_token:
                    sent_stored_token = token

        headers["norbix-project-id"] = self._cfg.project_id
        if self._cfg.account_id:
            headers["norbix-account-id"] = self._cfg.account_id
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
        # Language: per-call override wins over the client default. The
        # gateway reads only the standard Accept-Language header (q-values
        # honoured; project default when nothing matches). No default here —
        # the header is omitted when unset.
        resolved_language = language if language is not None else self._cfg.language
        if resolved_language:
            headers["Accept-Language"] = resolved_language
        if body is not None:
            headers["Content-Type"] = "application/json"
        # Per-call headers win over everything above (e.g. the MCP endpoint
        # needs its own Accept and its session headers).
        if extra_headers:
            headers.update(extra_headers)

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

        _take_session_token(self._cfg, sent_stored_token, response)

        if response.status_code >= 400:
            try:
                parsed: Any = response.json()
            except ValueError:
                parsed = None
            raise error_from_body(
                body=parsed,
                status=response.status_code,
                text=response.text,
                retry_after_seconds=retry_after_seconds_of(response.headers.get("retry-after")),
            )

        # An endpoint that answers with a file, not a document. Those answers
        # are not JSON, so the check below does not apply to them.
        if response_type == "binary":
            return response.content
        if response_type == "envelope":
            return _envelope(response)
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
            raise error_from_body(
                body=parsed_ok,
                status=response.status_code,
                retry_after_seconds=retry_after_seconds_of(response.headers.get("retry-after")),
            )
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

    def stream(
        self,
        *,
        target: Target,
        path: str,
        query: dict[str, Any] | None = None,
        bearer_token: str | None = None,
    ) -> Iterator[SseFrame]:
        """Open a server-sent events stream (GET) and yield its frames.

        ``path`` is the stream path (the gateway's is ``/event-stream``, without
        ``{version}``); ``query`` goes in the URL. Auth and the project / env /
        region headers are those of :meth:`send`. The read never times out —
        the stream ends when the server closes it or the caller stops
        iterating. No retry, no reconnect: a refused subscription (401 / 403 /
        404) raises the gateway's :class:`NorbixError` at once.
        """
        url, headers = _stream_request(self._cfg, target, path, query, bearer_token)
        timeout = httpx.Timeout(self._cfg.timeout, read=None)
        try:
            with self._client.stream("GET", url, headers=headers, timeout=timeout) as response:
                if response.status_code >= 400:
                    response.read()
                    raise _stream_refusal(response)
                yield from iter_sse(response.iter_lines())
        except httpx.HTTPError as exc:
            raise NorbixError(message=str(exc), code="NORBIX_NETWORK_ERROR") from exc


class AsyncTransport:
    def __init__(self, cfg: TransportConfig, client: httpx.AsyncClient | None = None) -> None:
        self._cfg = cfg
        self._client = client or httpx.AsyncClient(timeout=cfg.timeout)

    def navigation_url(
        self,
        *,
        target: Target,
        path: str,
        path_params: dict[str, Any],
        query: list[tuple[str, str | None]],
    ) -> str:
        """URL of a GET route a browser navigates to; see ``_navigation_url``."""
        return _navigation_url(self._cfg, target, path, path_params, query)

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
        language: str | None = None,
        response_type: ResponseType = "json",
        follow_redirects: bool = False,
        extra_headers: dict[str, str] | None = None,
        query: dict[str, Any] | None = None,
    ) -> Any:
        if scope == "account" and not self._cfg.account_id:
            raise NorbixError(
                message="This endpoint is account-scoped. Configure account_id on the client.",
                code="NORBIX_ACCOUNT_SCOPE_REQUIRED",
            )
        # project_id is required at construction; kept for defensive checks only.

        base_url = _api_call_base_url(self._cfg) if target == "api" else self._cfg.base_url_hub
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
        url = _with_query(url, query)
        headers = {"Accept": "application/json", **self._cfg.default_headers}

        # The stored bearer token this request sends, if it sends one. Only
        # that token is ever swapped for a fresher one (never an API key or a
        # per-call token the client does not hold).
        sent_stored_token: str | None = None
        if scope != "unauthenticated":
            token = bearer_token or self._cfg.bearer_token or self._cfg.api_key
            if not token and scope != "optional":
                raise NorbixError(
                    message="Not authenticated. Provide api_key / bearer_token or login first.",
                    code="NORBIX_NOT_AUTHENTICATED",
                )
            if token:
                headers["Authorization"] = f"Bearer {token}"
                if token == self._cfg.bearer_token:
                    sent_stored_token = token

        headers["norbix-project-id"] = self._cfg.project_id
        if self._cfg.account_id:
            headers["norbix-account-id"] = self._cfg.account_id
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
        # Language: per-call override wins over the client default. The
        # gateway reads only the standard Accept-Language header (q-values
        # honoured; project default when nothing matches). No default here —
        # the header is omitted when unset.
        resolved_language = language if language is not None else self._cfg.language
        if resolved_language:
            headers["Accept-Language"] = resolved_language
        if body is not None:
            headers["Content-Type"] = "application/json"
        # Per-call headers win over everything above (e.g. the MCP endpoint
        # needs its own Accept and its session headers).
        if extra_headers:
            headers.update(extra_headers)

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

        _take_session_token(self._cfg, sent_stored_token, response)

        if response.status_code >= 400:
            try:
                parsed: Any = response.json()
            except ValueError:
                parsed = None
            raise error_from_body(
                body=parsed,
                status=response.status_code,
                text=response.text,
                retry_after_seconds=retry_after_seconds_of(response.headers.get("retry-after")),
            )

        # An endpoint that answers with a file, not a document. Those answers
        # are not JSON, so the check below does not apply to them.
        if response_type == "binary":
            return response.content
        if response_type == "envelope":
            return _envelope(response)
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
            raise error_from_body(
                body=parsed_ok,
                status=response.status_code,
                retry_after_seconds=retry_after_seconds_of(response.headers.get("retry-after")),
            )
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

    async def stream(
        self,
        *,
        target: Target,
        path: str,
        query: dict[str, Any] | None = None,
        bearer_token: str | None = None,
    ) -> AsyncIterator[SseFrame]:
        """Async twin of :meth:`Transport.stream`."""
        url, headers = _stream_request(self._cfg, target, path, query, bearer_token)
        timeout = httpx.Timeout(self._cfg.timeout, read=None)
        try:
            stream = self._client.stream("GET", url, headers=headers, timeout=timeout)
            async with stream as response:
                if response.status_code >= 400:
                    await response.aread()
                    raise _stream_refusal(response)
                parser = _SseParser()
                async for line in response.aiter_lines():
                    frame = parser.feed(line)
                    if frame is not None:
                        yield frame
        except httpx.HTTPError as exc:
            raise NorbixError(message=str(exc), code="NORBIX_NETWORK_ERROR") from exc

def _take_session_token(
    cfg: TransportConfig, sent_stored_token: str | None, response: httpx.Response
) -> None:
    """Swap the stored bearer token for the answer's ``norbix-session-token``.

    Only when the request sent the stored bearer token and that token is still
    the stored one (a sign-out or another call may have changed it meanwhile).
    An empty header value is ignored. API-key calls never swap.
    """
    if not sent_stored_token:
        return
    fresh = (response.headers.get(SESSION_TOKEN_HEADER) or "").strip()
    if not fresh or fresh == sent_stored_token or cfg.bearer_token != sent_stored_token:
        return
    cfg.bearer_token = fresh
    if cfg.on_session_token is not None:
        cfg.on_session_token(fresh)


def _api_call_base_url(cfg: TransportConfig) -> str:
    """Where an API call goes: the project's own host wherever the address serves one.

    ``project_api_base_url`` decides it from ``cfg.base_url_api`` — built in or
    supplied by the caller — and the project id at the time of the call, so
    the host and the ``norbix-project-id`` header always name the same project
    (``https://pr-<32 hex>.api.norbix.ai`` on norbix.ai, with no region label:
    the project's DNS record already points at its region).
    """
    return project_api_base_url(cfg.base_url_api, cfg.project_id).project


def _navigation_url(
    cfg: TransportConfig,
    target: Target,
    path: str,
    path_params: dict[str, Any],
    query: list[tuple[str, str | None]],
) -> str:
    """The full URL of a GET route a browser navigates to (a link or a redirect, not a call).

    A navigation carries no headers, so the project id and a non-PROD env go
    into the query (``?projectId=…&env=…``), followed by ``query`` in order;
    ``None`` values are left out. Path values are percent-encoded.

    The link stays on the shared API host, never the project's own one: the
    gateway's social sign-in callback comes back to the shared host, and its
    nonce cookie is host-only. A template or a pasted project host loses its
    label (``https://{projectHostLabel}.api.customer.com`` → ``https://api.customer.com``).
    """
    base_url = (
        project_api_base_url(cfg.base_url_api, cfg.project_id).shared
        if target == "api"
        else cfg.base_url_hub
    )
    version = cfg.api_version if target == "api" else cfg.hub_version
    url, _ = _build_url_and_body(
        base_url=base_url,
        path=path,
        version=version,
        method="GET",
        path_params={k: quote(str(v), safe="") for k, v in path_params.items()},
        request={},
    )
    pairs: list[tuple[str, str | None]] = [("projectId", cfg.project_id or None)]
    if cfg.env and cfg.env != "PROD":
        pairs.append(("env", cfg.env))
    pairs.extend(query)
    encoded = "&".join(
        f"{quote(k, safe='')}={quote(v, safe='')}" for k, v in pairs if v is not None
    )
    return f"{url}?{encoded}" if encoded else url


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


def _with_query(url: str, query: dict[str, Any] | None) -> str:
    """Append query parameters that always go in the URL, whatever the verb."""
    if not query:
        return url
    pairs = [(k, _stringify(v)) for k, v in query.items() if v is not None]
    if not pairs:
        return url
    return f"{url}{'&' if '?' in url else '?'}{urlencode(pairs)}"


def _envelope(response: httpx.Response) -> dict[str, Any]:
    """Status, headers (lower-case names) and body (parsed JSON, else text, else None)."""
    body: Any = None
    if response.content:
        try:
            body = response.json()
        except ValueError:
            body = response.text
    return {
        "status": response.status_code,
        "headers": {k.lower(): v for k, v in response.headers.items()},
        "body": body,
    }


def _to_iterable(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    return [value]


def _stringify(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


@dataclass
class SseFrame:
    """One server-sent events frame: ``event`` ("message" when the frame has
    none), the ``data`` lines joined with "\n", and the last ``id`` seen."""

    event: str
    data: str
    id: str | None = None


class _SseParser:
    """SSE framing: ``event:``, ``data:`` (several are joined), ``id:``, ``:``
    comments (heartbeats) and the blank line that ends a frame."""

    def __init__(self) -> None:
        self._event = "message"
        self._data: list[str] = []
        self._id: str | None = None

    def feed(self, line: str) -> SseFrame | None:
        line = line.rstrip("\r")
        if line == "":
            frame = None
            if self._data or self._event != "message":
                frame = SseFrame(event=self._event, data="\n".join(self._data), id=self._id)
            self._event, self._data = "message", []
            return frame
        if line.startswith(":"):
            return None
        field_name, _, value = line.partition(":")
        if value.startswith(" "):
            value = value[1:]
        if field_name == "event":
            self._event = value
        elif field_name == "data":
            self._data.append(value)
        elif field_name == "id":
            self._id = value
        return None


def iter_sse(lines: Iterable[str]) -> Iterator[SseFrame]:
    """Parse SSE lines into frames (see :class:`_SseParser`)."""
    parser = _SseParser()
    for line in lines:
        frame = parser.feed(line)
        if frame is not None:
            yield frame


def _stream_request(
    cfg: TransportConfig,
    target: Target,
    path: str,
    query: dict[str, Any] | None,
    bearer_token: str | None,
) -> tuple[str, dict[str, str]]:
    base_url = _api_call_base_url(cfg) if target == "api" else cfg.base_url_hub
    version = cfg.api_version if target == "api" else cfg.hub_version
    url, _ = _build_url_and_body(
        base_url=base_url,
        path=path,
        version=version,
        method="GET",
        path_params={},
        request=query or {},
    )
    headers = {"Accept": "text/event-stream", "Cache-Control": "no-cache", **cfg.default_headers}
    token = bearer_token or cfg.bearer_token or cfg.api_key
    if not token:
        raise NorbixError(
            message="Not authenticated. Provide api_key / bearer_token or login first.",
            code="NORBIX_NOT_AUTHENTICATED",
        )
    headers["Authorization"] = f"Bearer {token}"
    headers["norbix-project-id"] = cfg.project_id
    if cfg.account_id:
        headers["norbix-account-id"] = cfg.account_id
    if cfg.env and cfg.env != "PROD":
        headers["norbix-env"] = cfg.env
    if cfg.region:
        headers["nb-region"] = cfg.region
    return url, headers


def _stream_refusal(response: httpx.Response) -> NorbixError:
    try:
        parsed: Any = response.json()
    except ValueError:
        parsed = None
    return error_from_body(body=parsed, status=response.status_code, text=response.text)
