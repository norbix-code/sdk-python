from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

class WebhooksModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_webhook_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/webhooks/integration"""
        return self._transport.send(
            target="hub",
            path="/{version}/webhooks/integration",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def reveal_webhook_integration_secret(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/webhooks/integration/secret"""
        return self._transport.send(
            target="hub",
            path="/{version}/webhooks/integration/secret",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def rotate_webhook_integration_secret(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/webhooks/integration/secret/rotate"""
        return self._transport.send(
            target="hub",
            path="/{version}/webhooks/integration/secret/rotate",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_webhook_integration_extra_headers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/webhooks/integration/extra-headers"""
        return self._transport.send(
            target="hub",
            path="/{version}/webhooks/integration/extra-headers",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_webhook_destination(self, destination_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/webhooks/destinations/{DestinationId}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/webhooks/destinations/{DestinationId}/disable",
            method="PUT",
            path_params={"DestinationId": destination_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_webhook_destination(self, destination_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/webhooks/destinations/{DestinationId}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/webhooks/destinations/{DestinationId}/enable",
            method="PUT",
            path_params={"DestinationId": destination_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def remove_webhook_destination(self, destination_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/webhooks/destinations/{DestinationId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/webhooks/destinations/{DestinationId}",
            method="DELETE",
            path_params={"DestinationId": destination_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_webhook_destination(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/webhooks/destinations"""
        return self._transport.send(
            target="hub",
            path="/{version}/webhooks/destinations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncWebhooksModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_webhook_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/webhooks/integration"""
        return await self._transport.send(
            target="hub",
            path="/{version}/webhooks/integration",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def reveal_webhook_integration_secret(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/webhooks/integration/secret"""
        return await self._transport.send(
            target="hub",
            path="/{version}/webhooks/integration/secret",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def rotate_webhook_integration_secret(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/webhooks/integration/secret/rotate"""
        return await self._transport.send(
            target="hub",
            path="/{version}/webhooks/integration/secret/rotate",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_webhook_integration_extra_headers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/webhooks/integration/extra-headers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/webhooks/integration/extra-headers",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_webhook_destination(self, destination_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/webhooks/destinations/{DestinationId}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/webhooks/destinations/{DestinationId}/disable",
            method="PUT",
            path_params={"DestinationId": destination_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_webhook_destination(self, destination_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/webhooks/destinations/{DestinationId}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/webhooks/destinations/{DestinationId}/enable",
            method="PUT",
            path_params={"DestinationId": destination_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def remove_webhook_destination(self, destination_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/webhooks/destinations/{DestinationId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/webhooks/destinations/{DestinationId}",
            method="DELETE",
            path_params={"DestinationId": destination_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_webhook_destination(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/webhooks/destinations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/webhooks/destinations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
