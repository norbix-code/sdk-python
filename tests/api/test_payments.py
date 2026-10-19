from __future__ import annotations

import asyncio
import json
from urllib.parse import parse_qs, urlparse

import httpx

from norbix_python import AsyncNorbix

from ..helpers import make_client


def test_api_payments_module_surface() -> None:
    client, _ = make_client()
    module = client.api.payments
    assert callable(module.create_payment_order)
    assert callable(module.get_payment_order)
    assert callable(module.get_payment_orders)
    assert callable(module.start_payment_checkout)


def test_api_payments_create_payment_order_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.payments.create_payment_order(
        buyerUserId="usr_1",
        merchantReference="ad-1042-promo-1",
        idempotencyKey="idem-key-1",
        currency="EUR",
        priceVersion="v1",
        lines=[{"sku": "star-day", "quantity": 21, "unitAmountMinor": 30}],
        metadata={"adId": "ad_1042"},
    )
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert urlparse(transport.last_request['url']).path == '/v3/payments/orders'
    body = json.loads(transport.last_request['body'])
    assert body['buyerUserId'] == 'usr_1'
    assert body['idempotencyKey'] == 'idem-key-1'
    assert body['lines'] == [{"sku": "star-day", "quantity": 21, "unitAmountMinor": 30}]
    assert body['metadata'] == {"adId": "ad_1042"}


def test_api_payments_get_payment_order_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.payments.get_payment_order("ord_1")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert urlparse(transport.last_request['url']).path == '/v3/payments/orders/ord_1'
    assert transport.last_request['body'] == ''


def test_api_payments_get_payment_orders_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.payments.get_payment_orders(buyerUserId="usr_1", merchantReference="ad-1042", status="Paid")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    url = urlparse(transport.last_request['url'])
    assert url.path == '/v3/payments/orders'
    assert parse_qs(url.query) == {"buyerUserId": ["usr_1"], "merchantReference": ["ad-1042"], "status": ["Paid"]}


def test_api_payments_start_payment_checkout_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.payments.start_payment_checkout(
        "ord_1",
        integrationId="int_montonio",
        returnUrl="https://shop.example.test/return",
        preferredCountry="LT",
    )
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert urlparse(transport.last_request['url']).path == '/v3/payments/orders/ord_1/checkout'
    body = json.loads(transport.last_request['body'])
    assert body == {
        "integrationId": "int_montonio",
        "returnUrl": "https://shop.example.test/return",
        "preferredCountry": "LT",
    }


def test_async_api_payments_hit_the_routes() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"id": "ord_1"})

    async def run() -> None:
        client = AsyncNorbix(
            project_id='test-project',
            bearer_token='test-token',
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        try:
            await client.api.payments.create_payment_order(buyerUserId="usr_1", currency="EUR")
            await client.api.payments.get_payment_order("ord_1")
            await client.api.payments.get_payment_orders(status="Paid")
            await client.api.payments.start_payment_checkout("ord_1", integrationId="int_1", returnUrl="https://x.test")
        finally:
            await client.aclose()

    asyncio.run(run())
    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [
        ('POST', '/v3/payments/orders'),
        ('GET', '/v3/payments/orders/ord_1'),
        ('GET', '/v3/payments/orders'),
        ('POST', '/v3/payments/orders/ord_1/checkout'),
    ]
