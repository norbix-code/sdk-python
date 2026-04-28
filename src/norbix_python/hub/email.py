from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

class EmailModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def one_click_unsubscribe(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/email/one-click-unsubscribe"""
        return self._transport.send(
            target="hub",
            path="/{version}/email/one-click-unsubscribe",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncEmailModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def one_click_unsubscribe(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/email/one-click-unsubscribe"""
        return await self._transport.send(
            target="hub",
            path="/{version}/email/one-click-unsubscribe",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
