from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class FilesModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disable_files(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/disable",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_files(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/enable",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_folder_files(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/folder"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/folder",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_file(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/item"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/item",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_files_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/files/triggers/{triggerId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/triggers/{triggerId}",
            method="DELETE",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_files_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/files/triggers/{triggerId}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/triggers/{triggerId}/disable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_files_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/files/triggers/{triggerId}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/triggers/{triggerId}/enable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_files_trigger(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/triggers/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/triggers/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_files_triggers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/triggers"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/triggers",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_files_trigger(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/triggers"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/triggers",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_files_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/files/integrations/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_files_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/files/integrations/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_files_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/files/integrations/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_files_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/integrations/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_files_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_files_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/integrations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_files_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/integrations/test"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/integrations/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def set_files_integration_as_default(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/files/integrations/{Id}/default"""
        return self._transport.send(
            target="hub",
            path="/{version}/files/integrations/{Id}/default",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # ------------------------------------------------------------------
    # Public file links (10b-files slice PUB). Hand-added by slice SDK-2 in
    # the shape the module generator produces.
    #
    # A file, or a whole folder, can be made readable by anyone holding a
    # link — no sign-in, no project id. The gateway mints an unguessable
    # ``nbpf_…`` id and the link is
    # ``https://<api host>/v3/files/public/nbpf_…/invoice.pdf``.
    #
    # Worth knowing before you call these:
    #   * publishing a folder is ONE record, whatever is under it;
    #   * asking twice gives the same id back;
    #   * a file cannot be made private on its own while a folder above it
    #     is public (CM-ERRORS-FILES-021) — switch the folder off instead;
    #   * the root cannot be published.
    # ------------------------------------------------------------------

    def make_file_public(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/item/public

        Makes one file readable by anyone holding its link. The file has to
        exist already. Answers with ``id`` — the ``nbpf_…`` public id.

        Keyword arguments: ``filesIntegrationId``, ``path``.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/files/item/public",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def make_file_private(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/item/private

        Takes the file's public link away; opening it afterwards gives a 404.

        Keyword arguments: ``filesIntegrationId``, ``path``.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/files/item/private",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def make_folder_public(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/folder/public

        Publishes a whole folder prefix — one record, however many files sit
        under it, at any depth. Answers with the ``nbpf_…`` id.

        Keyword arguments: ``filesIntegrationId``, ``path``.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/files/folder/public",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def make_folder_private(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/folder/private

        Takes back every link inside the folder, per-file links included.

        Keyword arguments: ``filesIntegrationId``, ``path``.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/files/folder/private",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncFilesModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def disable_files(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/disable",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_files(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/enable",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_folder_files(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/folder"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/folder",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_file(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/item"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/item",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_files_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/files/triggers/{triggerId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/triggers/{triggerId}",
            method="DELETE",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_files_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/files/triggers/{triggerId}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/triggers/{triggerId}/disable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_files_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/files/triggers/{triggerId}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/triggers/{triggerId}/enable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_files_trigger(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/triggers/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/triggers/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_files_triggers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/triggers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/triggers",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_files_trigger(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/triggers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/triggers",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_files_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/files/integrations/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_files_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/files/integrations/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_files_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/files/integrations/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_files_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/integrations/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_files_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/files/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_files_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/integrations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_files_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/integrations/test"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/integrations/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def set_files_integration_as_default(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/files/integrations/{Id}/default"""
        return await self._transport.send(
            target="hub",
            path="/{version}/files/integrations/{Id}/default",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # ------------------------------------------------------------------
    # Public file links (10b-files slice PUB). Hand-added by slice SDK-2 in
    # the shape the module generator produces.
    #
    # A file, or a whole folder, can be made readable by anyone holding a
    # link — no sign-in, no project id. The gateway mints an unguessable
    # ``nbpf_…`` id and the link is
    # ``https://<api host>/v3/files/public/nbpf_…/invoice.pdf``.
    #
    # Worth knowing before you call these:
    #   * publishing a folder is ONE record, whatever is under it;
    #   * asking twice gives the same id back;
    #   * a file cannot be made private on its own while a folder above it
    #     is public (CM-ERRORS-FILES-021) — switch the folder off instead;
    #   * the root cannot be published.
    # ------------------------------------------------------------------

    async def make_file_public(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/item/public

        Makes one file readable by anyone holding its link. The file has to
        exist already. Answers with ``id`` — the ``nbpf_…`` public id.

        Keyword arguments: ``filesIntegrationId``, ``path``.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/files/item/public",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def make_file_private(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/item/private

        Takes the file's public link away; opening it afterwards gives a 404.

        Keyword arguments: ``filesIntegrationId``, ``path``.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/files/item/private",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def make_folder_public(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/folder/public

        Publishes a whole folder prefix — one record, however many files sit
        under it, at any depth. Answers with the ``nbpf_…`` id.

        Keyword arguments: ``filesIntegrationId``, ``path``.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/files/folder/public",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def make_folder_private(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/files/folder/private

        Takes back every link inside the folder, per-file links included.

        Keyword arguments: ``filesIntegrationId``, ``path``.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/files/folder/private",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
