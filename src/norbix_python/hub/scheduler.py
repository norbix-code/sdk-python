from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

class SchedulerModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disable_scheduler(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/scheduler/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/scheduler/disable",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_scheduler(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/scheduler/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/scheduler/enable",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_scheduler_task(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/scheduler/tasks/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/scheduler/tasks/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_scheduler_task(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/scheduler/tasks/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/scheduler/tasks/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_scheduler_task(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/scheduler/tasks/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/scheduler/tasks/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_scheduler_task(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/scheduler/tasks/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/scheduler/tasks/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_scheduler_tasks(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/scheduler/tasks"""
        return self._transport.send(
            target="hub",
            path="/{version}/scheduler/tasks",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_scheduler_task(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/scheduler/tasks"""
        return self._transport.send(
            target="hub",
            path="/{version}/scheduler/tasks",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncSchedulerModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def disable_scheduler(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/scheduler/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/scheduler/disable",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_scheduler(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/scheduler/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/scheduler/enable",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_scheduler_task(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/scheduler/tasks/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/scheduler/tasks/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_scheduler_task(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/scheduler/tasks/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/scheduler/tasks/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_scheduler_task(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/scheduler/tasks/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/scheduler/tasks/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_scheduler_task(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/scheduler/tasks/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/scheduler/tasks/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_scheduler_tasks(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/scheduler/tasks"""
        return await self._transport.send(
            target="hub",
            path="/{version}/scheduler/tasks",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_scheduler_task(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/scheduler/tasks"""
        return await self._transport.send(
            target="hub",
            path="/{version}/scheduler/tasks",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
