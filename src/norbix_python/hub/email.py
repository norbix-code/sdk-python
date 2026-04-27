from __future__ import annotations

from typing import Any

from ..transport import Transport

class EmailModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def oneClickUnsubscribe(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/email/one-click-unsubscribe"""
        return self._transport.send(
            target='hub',
            path='/{version}/email/one-click-unsubscribe',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
