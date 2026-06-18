from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class ResourcesModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def resolve_resources(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/resources/resolve"""
        return self._transport.send(
            target="hub",
            path="/{version}/resources/resolve",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncResourcesModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def resolve_resources(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/resources/resolve"""
        return await self._transport.send(
            target="hub",
            path="/{version}/resources/resolve",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
