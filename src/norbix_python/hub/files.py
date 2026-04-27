from __future__ import annotations

from typing import Any

from ..transport import Transport

class FilesModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disableFiles(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/files/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/disable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableFiles(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/files/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/enable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteFilesTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/files/triggers/{triggerId}"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/triggers/{triggerId}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableFilesTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/files/triggers/{triggerId}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/triggers/{triggerId}/disable',
            method='PATCH',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableFilesTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/files/triggers/{triggerId}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/triggers/{triggerId}/enable',
            method='PATCH',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getFilesTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/files/triggers/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/triggers/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getFilesTriggers(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/files/triggers"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/triggers',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveFilesTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/files/triggers"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/triggers',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteFilesIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/files/integrations/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/integrations/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableFilesIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/files/integrations/{Id}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/integrations/{Id}/disable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableFilesIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/files/integrations/{Id}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/integrations/{Id}/enable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getFilesIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/files/integrations/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/integrations/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getFilesIntegrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/files/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/integrations',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveFilesIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/files/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/integrations',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def setFilesIntegrationAsDefault(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/files/integrations/{Id}/default"""
        return self._transport.send(
            target='hub',
            path='/{version}/files/integrations/{Id}/default',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
