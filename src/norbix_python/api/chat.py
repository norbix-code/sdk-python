from __future__ import annotations

from typing import Any

from ..transport import Transport

class ChatModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def askChat(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/chat/complete"""
        return self._transport.send(
            target='api',
            path='/{version}/chat/complete',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
