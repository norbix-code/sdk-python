from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class FilesModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def delete_file_api(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/files/{filesIntegrationId}"""
        return self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}",
            method="DELETE",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def list_files(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/{filesIntegrationId}"""
        return self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}",
            method="GET",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_many_files_api(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/files/{filesIntegrationId}/bulk"""
        return self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}/bulk",
            method="DELETE",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def commit_upload(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/{filesIntegrationId}/commit"""
        return self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}/commit",
            method="POST",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def download_file_api(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/{filesIntegrationId}/download"""
        return self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}/download",
            method="GET",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_file_info(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/{filesIntegrationId}/info"""
        return self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}/info",
            method="GET",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_signed_url(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/{filesIntegrationId}/sign"""
        return self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}/sign",
            method="GET",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def request_upload_url(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/{filesIntegrationId}/upload-url"""
        return self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}/upload-url",
            method="POST",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncFilesModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def delete_file_api(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/files/{filesIntegrationId}"""
        return await self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}",
            method="DELETE",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def list_files(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/{filesIntegrationId}"""
        return await self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}",
            method="GET",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_many_files_api(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/files/{filesIntegrationId}/bulk"""
        return await self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}/bulk",
            method="DELETE",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def commit_upload(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/{filesIntegrationId}/commit"""
        return await self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}/commit",
            method="POST",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def download_file_api(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/{filesIntegrationId}/download"""
        return await self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}/download",
            method="GET",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_file_info(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/{filesIntegrationId}/info"""
        return await self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}/info",
            method="GET",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_signed_url(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/{filesIntegrationId}/sign"""
        return await self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}/sign",
            method="GET",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def request_upload_url(self, files_integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/{filesIntegrationId}/upload-url"""
        return await self._transport.send(
            target="api",
            path="/{version}/files/{filesIntegrationId}/upload-url",
            method="POST",
            path_params={"filesIntegrationId": files_integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
