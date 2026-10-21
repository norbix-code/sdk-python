from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class LogsModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disable_logging(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/logs/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/disable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_logging(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/logs/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/enable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_logging_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/logs/integrations/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_logging_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/logs/integrations/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_logging_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/logs/integrations/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_logging_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/logs/integrations/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_logging_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/logs/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_logging_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/logs/integrations

        Save (create or update) a logging integration — Datadog, AWS
        CloudWatch or MongoDB. Gives back ``{"id": ...}``. Then call
        ``test_logging_integration``: nothing is delivered until a test passed.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_logging_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/logs/integrations/test

        Test a logging integration: ``integrationId``. Call it after every
        ``save_logging_integration`` — nothing is delivered to an integration
        until its last test passed.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_logs_by_correlation_id(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/logs/audit"""
        return self._transport.send(
            target="hub",
            path="/{version}/logs/audit",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_logs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/logs

        The project's log entries, filtered by the optional
        ``level``, ``module``, ``logCorrelationId``, ``eventCode``, ``search``,
        ``metaKey`` / ``metaValue``, ``fromUtc`` / ``toUtc`` and the cursor
        paging fields ``pageSize``, ``startingAfter``, ``endingBefore`` (query). Gives back ``{"list": {"items": [...], ...}}``.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/logs",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_log(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/logs/{Id}

        One log entry by its id. Gives back ``{"item": entry}``.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/logs/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def clean_logs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/logs/clean

        Delete every log entry stored in the project's Norbix Logging integration.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/logs/clean",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_log_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/logs/settings

        The project's log flags: ``skipCloudDashboardLogs``, ``skipHttpBodyMeta``,
        ``aiChatLoggingEnabled`` and ``hasNorbixLogging``.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/logs/settings",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_log_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/logs/settings

        Change the project's log flags: ``skipCloudDashboardLogs``,
        ``skipHttpBodyMeta``, ``aiChatLoggingEnabled`` (each optional; a flag
        left out keeps its value).
        """
        return self._transport.send(
            target="hub",
            path="/{version}/logs/settings",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncLogsModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def disable_logging(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/logs/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/disable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_logging(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/logs/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/enable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_logging_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/logs/integrations/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_logging_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/logs/integrations/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_logging_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/logs/integrations/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_logging_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/logs/integrations/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_logging_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/logs/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_logging_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/logs/integrations

        Save (create or update) a logging integration — Datadog, AWS
        CloudWatch or MongoDB. Gives back ``{"id": ...}``. Then call
        ``test_logging_integration``: nothing is delivered until a test passed.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_logging_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/logs/integrations/test

        Test a logging integration: ``integrationId``. Call it after every
        ``save_logging_integration`` — nothing is delivered to an integration
        until its last test passed.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/integrations/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_logs_by_correlation_id(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/logs/audit"""
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/audit",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_logs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/logs

        The project's log entries, filtered by the optional
        ``level``, ``module``, ``logCorrelationId``, ``eventCode``, ``search``,
        ``metaKey`` / ``metaValue``, ``fromUtc`` / ``toUtc`` and the cursor
        paging fields ``pageSize``, ``startingAfter``, ``endingBefore`` (query). Gives back ``{"list": {"items": [...], ...}}``.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/logs",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_log(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/logs/{Id}

        One log entry by its id. Gives back ``{"item": entry}``.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def clean_logs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/logs/clean

        Delete every log entry stored in the project's Norbix Logging integration.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/clean",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_log_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/logs/settings

        The project's log flags: ``skipCloudDashboardLogs``, ``skipHttpBodyMeta``,
        ``aiChatLoggingEnabled`` and ``hasNorbixLogging``.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/settings",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_log_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/logs/settings

        Change the project's log flags: ``skipCloudDashboardLogs``,
        ``skipHttpBodyMeta``, ``aiChatLoggingEnabled`` (each optional; a flag
        left out keeps its value).
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/logs/settings",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
