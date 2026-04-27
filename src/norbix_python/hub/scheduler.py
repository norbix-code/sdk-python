from __future__ import annotations

from typing import Any

from ..transport import Transport

class SchedulerModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disableScheduler(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/scheduler/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/scheduler/disable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableScheduler(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/scheduler/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/scheduler/enable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteSchedulerTask(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/scheduler/tasks/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/scheduler/tasks/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableSchedulerTask(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/scheduler/tasks/{Id}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/scheduler/tasks/{Id}/disable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableSchedulerTask(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/scheduler/tasks/{Id}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/scheduler/tasks/{Id}/enable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getSchedulerTask(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/scheduler/tasks/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/scheduler/tasks/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getSchedulerTasks(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/scheduler/tasks"""
        return self._transport.send(
            target='hub',
            path='/{version}/scheduler/tasks',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveSchedulerTask(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/scheduler/tasks"""
        return self._transport.send(
            target='hub',
            path='/{version}/scheduler/tasks',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
