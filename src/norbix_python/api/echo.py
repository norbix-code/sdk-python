from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

class EchoModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def echo(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/echo"""
        return self._transport.send(
            target="api",
            path="/{version}/echo",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncEchoModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def echo(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/echo"""
        return await self._transport.send(
            target="api",
            path="/{version}/echo",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
