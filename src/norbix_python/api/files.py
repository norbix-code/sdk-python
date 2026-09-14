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

    # ------------------------------------------------------------------
    # The public file link (10b-files slice PUB). Hand-added by slice SDK-2.
    # ------------------------------------------------------------------

    def get_public_file(self, public_id: str, name: str, *, timeout: float | None = None, **request: Any) -> Any:
        """GET /{version}/files/public/{publicId}/{name}

        The gateway declares the route as /{version}/files/public/{PublicId}/{Name*} —
        written out here exactly as the gateway spells it, so the SDK coverage
        matrix can see that the two agree (knowledge.md K23).

        Reads a file somebody made public.

        **No sign-in and no project id.** The SDK deliberately sends no
        ``Authorization`` header for this call, even when the client is signed
        in: the link has to work in an e-mail, in an ``<img src>``, or in a
        browser on a stranger's phone. The unguessable ``nbpf_…`` id is the
        whole credential.

        Gives back the file's raw ``bytes``. When the storage provider signs
        its own links (Amazon S3, Azure Blob, Google Cloud Storage) the gateway
        answers 302 and this call follows the redirect, so the bytes come from
        the provider and never pass through Norbix.

        ``name`` is the file's name for a file link, or the path inside the
        folder for a folder link (``2026/q1/report.pdf``); its slashes stay
        slashes.

        Every miss is the same plain 404 — an unknown id, a name that does not
        match, a file made private again, a file gone from storage. A more
        precise answer would tell a stranger the file is there.
        """
        return self._transport.send(
            target="api",
            path="/{version}/files/public/{publicId}/{name}",
            method="GET",
            path_params={"publicId": public_id, "name": name},
            request=request,
            scope="unauthenticated",
            timeout=timeout,
            response_type="binary",
            follow_redirects=True,
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

    # ------------------------------------------------------------------
    # The public file link (10b-files slice PUB). Hand-added by slice SDK-2.
    # ------------------------------------------------------------------

    async def get_public_file(self, public_id: str, name: str, *, timeout: float | None = None, **request: Any) -> Any:
        """GET /{version}/files/public/{publicId}/{name}

        The gateway declares the route as /{version}/files/public/{PublicId}/{Name*} —
        written out here exactly as the gateway spells it, so the SDK coverage
        matrix can see that the two agree (knowledge.md K23).

        Reads a file somebody made public.

        **No sign-in and no project id.** The SDK deliberately sends no
        ``Authorization`` header for this call, even when the client is signed
        in: the link has to work in an e-mail, in an ``<img src>``, or in a
        browser on a stranger's phone. The unguessable ``nbpf_…`` id is the
        whole credential.

        Gives back the file's raw ``bytes``. When the storage provider signs
        its own links (Amazon S3, Azure Blob, Google Cloud Storage) the gateway
        answers 302 and this call follows the redirect, so the bytes come from
        the provider and never pass through Norbix.

        ``name`` is the file's name for a file link, or the path inside the
        folder for a folder link (``2026/q1/report.pdf``); its slashes stay
        slashes.

        Every miss is the same plain 404 — an unknown id, a name that does not
        match, a file made private again, a file gone from storage. A more
        precise answer would tell a stranger the file is there.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/files/public/{publicId}/{name}",
            method="GET",
            path_params={"publicId": public_id, "name": name},
            request=request,
            scope="unauthenticated",
            timeout=timeout,
            response_type="binary",
            follow_redirects=True,
        )
