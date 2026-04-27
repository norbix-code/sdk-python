from __future__ import annotations

from typing import Any

from ..transport import Transport

class InternalModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def internalsTypeGen(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /internal/_typegen"""
        return self._transport.send(
            target='hub',
            path='/internal/_typegen',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
