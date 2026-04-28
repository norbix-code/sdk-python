from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any

import httpx

if TYPE_CHECKING:
    from .facade.database import Collection
from pydantic import BaseModel, ConfigDict, Field

from .api import ApiNamespace
from .hub import HubNamespace
from .transport import AsyncTransport, Transport, TransportConfig

DEFAULT_BASE_URL_API = "https://api.norbix.dev"
DEFAULT_BASE_URL_HUB = "https://hub.norbix.dev"
DEFAULT_VERSION = "v2"
DEFAULT_TIMEOUT = 30.0


class LoginCredentials(BaseModel):
    """Login payload; serializes to camelCase keys expected by the API."""

    model_config = ConfigDict(populate_by_name=True)

    user_name: str = Field(alias="userName")
    password: str
    provider: str = "credentials"


class Norbix:
    def __init__(
        self,
        *,
        project_id: str | None = None,
        api_key: str | None = None,
        bearer_token: str | None = None,
        account_id: str | None = None,
        base_url_api: str | None = None,
        base_url_hub: str | None = None,
        api_version: str | None = None,
        hub_version: str | None = None,
        timeout: float | None = None,
        default_headers: dict[str, str] | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        resolved_project_id = (
            project_id if project_id is not None else os.getenv("NORBIX_PROJECT_ID") or None
        )
        resolved_base_url_api = base_url_api or os.getenv("NORBIX_API_URL") or DEFAULT_BASE_URL_API
        resolved_base_url_hub = base_url_hub or os.getenv("NORBIX_HUB_URL") or DEFAULT_BASE_URL_HUB
        resolved_api_version = api_version or os.getenv("NORBIX_API_VERSION") or DEFAULT_VERSION
        resolved_hub_version = hub_version or os.getenv("NORBIX_HUB_VERSION") or DEFAULT_VERSION

        cfg = TransportConfig(
            api_key=api_key or os.getenv("NORBIX_API_KEY"),
            bearer_token=bearer_token or os.getenv("NORBIX_BEARER_TOKEN"),
            project_id=resolved_project_id,
            account_id=account_id or os.getenv("NORBIX_ACCOUNT_ID"),
            base_url_api=resolved_base_url_api,
            base_url_hub=resolved_base_url_hub,
            api_version=resolved_api_version,
            hub_version=resolved_hub_version,
            timeout=timeout or DEFAULT_TIMEOUT,
            default_headers=default_headers or {},
        )

        self._transport = Transport(cfg=cfg, client=http_client)
        self.api = ApiNamespace(self._transport)
        self.hub = HubNamespace(self._transport)

    def collection(self, name: str) -> Collection:
        from .facade.database import Collection as CollectionFacade

        return CollectionFacade(self, name)

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> Norbix:
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def login(self, credentials: LoginCredentials | dict[str, Any]) -> dict[str, Any]:
        if isinstance(credentials, LoginCredentials):
            payload = credentials.model_dump(by_alias=True, exclude_none=True)
        else:
            payload = dict(credentials)
        payload.setdefault("provider", "credentials")
        result = self._transport.send(
            target="api",
            path="/auth",
            method="POST",
            path_params={},
            request=payload,
            scope="unauthenticated",
        )
        if isinstance(result, dict) and result.get("bearerToken"):
            self.set_bearer_token(str(result["bearerToken"]))
        return result if isinstance(result, dict) else {}

    def logout(self) -> None:
        self._transport._cfg.bearer_token = None

    def set_bearer_token(self, token: str | None) -> None:
        self._transport._cfg.bearer_token = token

    def set_api_key(self, api_key: str | None) -> None:
        self._transport._cfg.api_key = api_key

    def set_scope(self, *, project_id: str, account_id: str | None = None) -> None:
        self._transport._cfg.project_id = project_id
        self._transport._cfg.account_id = account_id

    def is_authenticated(self) -> bool:
        return bool(self._transport._cfg.bearer_token or self._transport._cfg.api_key)


class AsyncNorbix:
    """Async client using ``httpx.AsyncClient`` (same scopes as :class:`Norbix`)."""

    def __init__(
        self,
        *,
        project_id: str | None = None,
        api_key: str | None = None,
        bearer_token: str | None = None,
        account_id: str | None = None,
        base_url_api: str | None = None,
        base_url_hub: str | None = None,
        api_version: str | None = None,
        hub_version: str | None = None,
        timeout: float | None = None,
        default_headers: dict[str, str] | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        resolved_project_id = (
            project_id if project_id is not None else os.getenv("NORBIX_PROJECT_ID") or None
        )
        resolved_base_url_api = base_url_api or os.getenv("NORBIX_API_URL") or DEFAULT_BASE_URL_API
        resolved_base_url_hub = base_url_hub or os.getenv("NORBIX_HUB_URL") or DEFAULT_BASE_URL_HUB
        resolved_api_version = api_version or os.getenv("NORBIX_API_VERSION") or DEFAULT_VERSION
        resolved_hub_version = hub_version or os.getenv("NORBIX_HUB_VERSION") or DEFAULT_VERSION

        cfg = TransportConfig(
            api_key=api_key or os.getenv("NORBIX_API_KEY"),
            bearer_token=bearer_token or os.getenv("NORBIX_BEARER_TOKEN"),
            project_id=resolved_project_id,
            account_id=account_id or os.getenv("NORBIX_ACCOUNT_ID"),
            base_url_api=resolved_base_url_api,
            base_url_hub=resolved_base_url_hub,
            api_version=resolved_api_version,
            hub_version=resolved_hub_version,
            timeout=timeout or DEFAULT_TIMEOUT,
            default_headers=default_headers or {},
        )

        self._transport = AsyncTransport(cfg=cfg, client=http_client)
        from .api import AsyncApiNamespace
        from .hub import AsyncHubNamespace

        self.api = AsyncApiNamespace(self._transport)
        self.hub = AsyncHubNamespace(self._transport)

    async def aclose(self) -> None:
        await self._transport.aclose()

    async def __aenter__(self) -> AsyncNorbix:
        return self

    async def __aexit__(self, *_exc: object) -> None:
        await self.aclose()

    async def login(self, credentials: LoginCredentials | dict[str, Any]) -> dict[str, Any]:
        if isinstance(credentials, LoginCredentials):
            payload = credentials.model_dump(by_alias=True, exclude_none=True)
        else:
            payload = dict(credentials)
        payload.setdefault("provider", "credentials")
        result = await self._transport.send(
            target="api",
            path="/auth",
            method="POST",
            path_params={},
            request=payload,
            scope="unauthenticated",
        )
        if isinstance(result, dict) and result.get("bearerToken"):
            self.set_bearer_token(str(result["bearerToken"]))
        return result if isinstance(result, dict) else {}

    def set_bearer_token(self, token: str | None) -> None:
        self._transport._cfg.bearer_token = token

    def set_api_key(self, api_key: str | None) -> None:
        self._transport._cfg.api_key = api_key

    def is_authenticated(self) -> bool:
        return bool(self._transport._cfg.bearer_token or self._transport._cfg.api_key)
