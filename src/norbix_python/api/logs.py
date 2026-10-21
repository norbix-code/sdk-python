"""Write your app's own log entries on the Api (project scope).

``write_logs`` sends 1–100 entries in one call. They are queued and the call
returns at once with ``{"accepted": n}``; read them back on the Hub with
``hub.logs.get_logs`` / ``get_log`` (an entry's ``eventCode`` is stored as
``app:<code>``).
"""

from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class LogsModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def write_logs(
        self,
        *,
        entries: list[dict[str, Any]],
        timeout: float | None = None,
        bearer_token: str | None = None,
        **request: Any,
    ) -> Any:
        """POST /{version}/logs

        Write 1–100 log entries. Each entry: ``title`` (required, ≤200),
        ``level`` (``"information"`` / ``"warning"`` / ``"error"``),
        ``message`` (≤8000), ``eventCode`` (a-z 0-9 ``_ . : -``, ≤64),
        ``correlationId`` (letters, digits, ``_ -``, ≤64), ``timestamp`` (an
        ISO-8601 UTC string, ≤7 days old, ≤5 minutes ahead) and ``meta`` (a
        string map, ≤20 keys). Optional ``projectId``. Gives back
        ``{"accepted": n}``.

        Raises ``ValidationError`` (400) for a broken entry or
        ``CM-ERRORS-LOGGING-002`` when the Logs module is off, and
        ``RateLimitError`` (429, ``CM-ERRORS-LOGGING-003``) when the project's
        per-minute quota is used up — its ``retry_after_seconds`` says how many
        seconds to wait. The call is not retried.
        """
        return self._transport.send(
            target="api",
            path="/{version}/logs",
            method="POST",
            path_params={},
            request={"entries": entries, **request},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncLogsModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def write_logs(
        self,
        *,
        entries: list[dict[str, Any]],
        timeout: float | None = None,
        bearer_token: str | None = None,
        **request: Any,
    ) -> Any:
        """POST /{version}/logs — see :meth:`LogsModule.write_logs`."""
        return await self._transport.send(
            target="api",
            path="/{version}/logs",
            method="POST",
            path_params={},
            request={"entries": entries, **request},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
