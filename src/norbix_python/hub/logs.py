from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

class LogsModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disable_logging(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/logs/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/disable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_logging(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/logs/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/enable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_logging_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/logs/integrations/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_logging_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/logs/integrations/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_logging_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/logs/integrations/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_logging_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/logs/integrations/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_logging_integrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/logs/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_logging_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/logs/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_logging_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/logs/integrations/test"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/test",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncLogsModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def disable_logging(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/logs/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/disable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_logging(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/logs/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/enable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_logging_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/logs/integrations/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_logging_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/logs/integrations/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_logging_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/logs/integrations/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_logging_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/logs/integrations/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_logging_integrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/logs/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_logging_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/logs/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_logging_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/logs/integrations/test"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/test",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
