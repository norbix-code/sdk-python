from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

class InternalModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def internals_type_gen(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /internal/_typegen"""
        return self._transport.send(
            target="hub",
            path="/internal/_typegen",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncInternalModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def internals_type_gen(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /internal/_typegen"""
        return await self._transport.send(
            target="hub",
            path="/internal/_typegen",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
