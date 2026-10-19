"""Payment orders and checkout on the Api (project scope).

A payment order is what a buyer pays for: lines priced in minor units, a
merchant reference and a price version. Create it, start a provider checkout
(Montonio, …) and send the buyer to ``checkout["paymentUrl"]``. A verified
provider callback moves the order on; a destination or Code function hears it
as ``payments.order.paid`` / ``…refunded`` / ``…expired`` (see
``NorbixWebhookEvents.Payments`` and ``FunctionEvent.as_payment_order``).
"""

from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class PaymentsModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def create_payment_order(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/payments/orders

        Create a payment order for a buyer: ``buyerUserId``, ``merchantReference``,
        ``currency``, ``priceVersion``, ``lines`` (each ``sku``, ``title``,
        ``quantity``, ``unitAmountMinor``), optional ``idempotencyKey`` and
        ``metadata`` (a string map). Gives back ``{"id": "ord_…"}``; the same body
        with the same ``idempotencyKey`` gives back the same id.
        """
        return self._transport.send(
            target="api",
            path="/{version}/payments/orders",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_payment_order(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/payments/orders/{Id}

        One payment order by its id (``ord_…``). Gives back ``{"item": order}``
        (lines, totals, status, checkouts, ``settledMinor``, ``refundedMinor``, …).
        """
        return self._transport.send(
            target="api",
            path="/{version}/payments/orders/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_payment_orders(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/payments/orders

        The payment orders of the project, filtered by the optional
        ``buyerUserId``, ``merchantReference`` and ``status`` (query). Gives back
        ``{"list": {"items": [...], ...}}``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/payments/orders",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def start_payment_checkout(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/payments/orders/{Id}/checkout

        Start (or reuse) the provider checkout of an order: ``integrationId``,
        ``returnUrl``, optional ``method``, ``preferredCountry`` and
        ``preferredProvider``. Gives back ``checkout`` (``paymentUrl`` to send the
        buyer to, ``expiresAtUtc``, …), ``reused`` (an open checkout was handed
        back) and the ``order``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/payments/orders/{Id}/checkout",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncPaymentsModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create_payment_order(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/payments/orders

        Create a payment order for a buyer: ``buyerUserId``, ``merchantReference``,
        ``currency``, ``priceVersion``, ``lines`` (each ``sku``, ``title``,
        ``quantity``, ``unitAmountMinor``), optional ``idempotencyKey`` and
        ``metadata`` (a string map). Gives back ``{"id": "ord_…"}``; the same body
        with the same ``idempotencyKey`` gives back the same id.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/payments/orders",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_payment_order(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/payments/orders/{Id}

        One payment order by its id (``ord_…``). Gives back ``{"item": order}``
        (lines, totals, status, checkouts, ``settledMinor``, ``refundedMinor``, …).
        """
        return await self._transport.send(
            target="api",
            path="/{version}/payments/orders/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_payment_orders(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/payments/orders

        The payment orders of the project, filtered by the optional
        ``buyerUserId``, ``merchantReference`` and ``status`` (query). Gives back
        ``{"list": {"items": [...], ...}}``.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/payments/orders",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def start_payment_checkout(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/payments/orders/{Id}/checkout

        Start (or reuse) the provider checkout of an order: ``integrationId``,
        ``returnUrl``, optional ``method``, ``preferredCountry`` and
        ``preferredProvider``. Gives back ``checkout`` (``paymentUrl`` to send the
        buyer to, ``expiresAtUtc``, …), ``reused`` (an open checkout was handed
        back) and the ``order``.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/payments/orders/{Id}/checkout",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
