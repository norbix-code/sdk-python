from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import httpx

from .api import ApiNamespace
from .hub import HubNamespace
from .transport import Transport, TransportConfig

DEFAULT_BASE_URL_API = "https://api.norbix.dev"
DEFAULT_BASE_URL_HUB = "https://hub.norbix.dev"
DEFAULT_VERSION = "v2"
DEFAULT_TIMEOUT = 30.0


@dataclass
class LoginCredentials:
    userName: str
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
        resolved_project_id = project_id or os.getenv("NORBIX_PROJECT_ID")
        if not resolved_project_id:
            raise ValueError("Norbix: project_id is required or set NORBIX_PROJECT_ID.")
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

    def close(self) -> None:
        self._transport.close()

    def login(self, credentials: LoginCredentials | dict[str, Any]) -> dict[str, Any]:
        payload = credentials if isinstance(credentials, dict) else credentials.__dict__.copy()
        payload.setdefault("provider", "credentials")
        result = self._transport.send(
            target="api",
            path="/auth",
            method="POST",
            request=payload,
            scope="unauthenticated",
        )
        if isinstance(result, dict) and result.get("bearerToken"):
            self._transport._cfg.bearer_token = str(result["bearerToken"])
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
