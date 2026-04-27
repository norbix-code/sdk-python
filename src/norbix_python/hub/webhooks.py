from __future__ import annotations

from typing import Any

from ..transport import Transport

class WebhooksModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def getWebhookIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/webhooks/integration"""
        return self._transport.send(
            target='hub',
            path='/{version}/webhooks/integration',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def revealWebhookIntegrationSecret(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/webhooks/integration/secret"""
        return self._transport.send(
            target='hub',
            path='/{version}/webhooks/integration/secret',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def rotateWebhookIntegrationSecret(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/webhooks/integration/secret/rotate"""
        return self._transport.send(
            target='hub',
            path='/{version}/webhooks/integration/secret/rotate',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateWebhookIntegrationExtraHeaders(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/webhooks/integration/extra-headers"""
        return self._transport.send(
            target='hub',
            path='/{version}/webhooks/integration/extra-headers',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableWebhookDestination(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/webhooks/destinations/{DestinationId}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/webhooks/destinations/{DestinationId}/disable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableWebhookDestination(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/webhooks/destinations/{DestinationId}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/webhooks/destinations/{DestinationId}/enable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def removeWebhookDestination(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/webhooks/destinations/{DestinationId}"""
        return self._transport.send(
            target='hub',
            path='/{version}/webhooks/destinations/{DestinationId}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveWebhookDestination(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/webhooks/destinations"""
        return self._transport.send(
            target='hub',
            path='/{version}/webhooks/destinations',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
