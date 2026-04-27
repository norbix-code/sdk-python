from __future__ import annotations

from typing import Any

from ..transport import Transport

class PaymentsModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disablePayments(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/disable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enablePayments(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/enable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deletePaymentsTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/payments/triggers/{triggerId}"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/triggers/{triggerId}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disablePaymentsTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/payments/triggers/{triggerId}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/triggers/{triggerId}/disable',
            method='PATCH',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enablePaymentsTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/payments/triggers/{triggerId}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/triggers/{triggerId}/enable',
            method='PATCH',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getPaymentsTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/triggers/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/triggers/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getPaymentsTriggers(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/triggers"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/triggers',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def savePaymentsTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/payments/triggers"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/triggers',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def confirmPaymentsIntegrationHumanDelivery(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/payments/integrations/confirm-human-delivery"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/integrations/confirm-human-delivery',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deletePaymentsIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/payments/integrations/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/integrations/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disablePaymentsIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/payments/integrations/{Id}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/integrations/{Id}/disable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enablePaymentsIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/payments/integrations/{Id}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/integrations/{Id}/enable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getPaymentsIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/integrations/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/integrations/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getPaymentsIntegrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/payments/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/integrations',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def savePaymentsIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/payments/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/integrations',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def testPaymentsIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/payments/integrations/test"""
        return self._transport.send(
            target='hub',
            path='/{version}/payments/integrations/test',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
