from __future__ import annotations

from typing import Any

from ..transport import Transport

class AiModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def deleteLlmIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/ai/integrations/llms/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/llms/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableLlmIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/ai/integrations/llms/{Id}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/llms/{Id}/disable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableLlmIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/ai/integrations/llms/{Id}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/llms/{Id}/enable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getLlmIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/ai/integrations/llms/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/llms/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getLlmIntegrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/ai/integrations/llms/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/llms/integrations',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveLlmIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/ai/integrations/llms/"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/llms/',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def testLlmIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/ai/integrations/llms/test"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/llms/test',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteMcpIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/ai/integrations/mcp/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/mcp/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableMcpIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/ai/integrations/mcp/{Id}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/mcp/{Id}/disable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableMcpIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/ai/integrations/mcp/{Id}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/mcp/{Id}/enable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getMcpIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/ai/integrations/mcp/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/mcp/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getMcpIntegrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/ai/integrations/mcp/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/mcp/integrations',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveMcpIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/ai/integrations/mcp/"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/mcp/',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def testMcpIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/ai/integrations/mcp/test"""
        return self._transport.send(
            target='hub',
            path='/{version}/ai/integrations/mcp/test',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
