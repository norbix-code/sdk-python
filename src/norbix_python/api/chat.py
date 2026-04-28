from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

class ChatModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def ask_chat(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/chat/complete"""
        return self._transport.send(
            target="api",
            path="/{version}/chat/complete",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncChatModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def ask_chat(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/chat/complete"""
        return await self._transport.send(
            target="api",
            path="/{version}/chat/complete",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
