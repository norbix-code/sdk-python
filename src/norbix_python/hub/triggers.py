from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

# HAND-WRITTEN module: scripts/generate_endpoints.py (gitignored, not in the
# repo) did not produce it. Keep it — and its registration in hub/__init__.py —
# when the hub modules are regenerated.


class TriggersModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_triggers_needing_attention(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/triggers/attention

        Lists the triggers of one type that need attention (for example, a
        trigger whose provider integration is gone). Pass ``triggerType=...``
        (Membership, Schema, Files, Payments or Ai). Response: ``{"items": [...]}``.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/triggers/attention",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncTriggersModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_triggers_needing_attention(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/triggers/attention

        Lists the triggers of one type that need attention (for example, a
        trigger whose provider integration is gone). Pass ``triggerType=...``
        (Membership, Schema, Files, Payments or Ai). Response: ``{"items": [...]}``.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/triggers/attention",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
