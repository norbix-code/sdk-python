from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

class PaymentsModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disable_payments(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/disable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_payments(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/enable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_payments_trigger(self, trigger_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/payments/triggers/{triggerId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/triggers/{triggerId}",
            method="DELETE",
            path_params={"triggerId": trigger_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_payments_trigger(self, trigger_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/payments/triggers/{triggerId}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/triggers/{triggerId}/disable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_payments_trigger(self, trigger_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/payments/triggers/{triggerId}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/triggers/{triggerId}/enable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_payments_trigger(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/triggers/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/triggers/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_payments_triggers(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/triggers"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/triggers",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_payments_trigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/payments/triggers"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/triggers",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def confirm_payments_integration_human_delivery(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/payments/integrations/confirm-human-delivery"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/integrations/confirm-human-delivery",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_payments_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/payments/integrations/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_payments_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/payments/integrations/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_payments_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/payments/integrations/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_payments_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/integrations/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_payments_integrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/integrations",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_payments_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/payments/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/integrations",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_payments_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/payments/integrations/test"""
        return self._transport.send(
            target="hub",
            path="/{version}/payments/integrations/test",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncPaymentsModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def disable_payments(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/disable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_payments(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/enable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_payments_trigger(self, trigger_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/payments/triggers/{triggerId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/triggers/{triggerId}",
            method="DELETE",
            path_params={"triggerId": trigger_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_payments_trigger(self, trigger_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/payments/triggers/{triggerId}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/triggers/{triggerId}/disable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_payments_trigger(self, trigger_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/payments/triggers/{triggerId}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/triggers/{triggerId}/enable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_payments_trigger(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/triggers/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/triggers/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_payments_triggers(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/triggers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/triggers",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_payments_trigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/payments/triggers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/triggers",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def confirm_payments_integration_human_delivery(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/payments/integrations/confirm-human-delivery"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/integrations/confirm-human-delivery",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_payments_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/payments/integrations/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_payments_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/payments/integrations/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_payments_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/payments/integrations/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_payments_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/integrations/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_payments_integrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/integrations",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_payments_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/payments/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/integrations",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_payments_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/payments/integrations/test"""
        return await self._transport.send(
            target="hub",
            path="/{version}/payments/integrations/test",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
