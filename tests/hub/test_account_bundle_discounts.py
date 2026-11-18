"""Discount codes for the Managed Service bundle.

The gateway takes the account from the signed-in session for both routes, so
every test runs on a client WITHOUT ``account_id``. Each one asserts the verb,
the fully-resolved path and the body. A refused code must reach the caller
with its error code and the ``reason`` from the error context. Sync and async
clients are both covered. Nothing leaves the process.
"""
from __future__ import annotations

import asyncio
import json
from typing import Any
from urllib.parse import urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, ValidationError

DISCOUNT = {
    "discount": {
        "code": "LAUNCH20",
        "percentOff": 20,
        "amountOff": 0,
        "currency": "usd",
        "months": 3,
        "endsAt": None,
    }
}

ALREADY_USED = {
    "responseStatus": {
        "isSuccess": False,
        "errors": [
            {
                "message": "This discount code was already used by this account.",
                "errorCode": "CM-ERRORS-ACCOUNT-027",
                "context": {"reason": "already_used"},
            }
        ],
    }
}


def _handler(seen: list[httpx.Request], answer: Any, status: int = 200) -> Any:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(status, json=answer if answer is not None else {})

    return handler


def _sync_client(seen: list[httpx.Request], answer: Any = None, status: int = 200) -> Norbix:
    return Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=httpx.MockTransport(_handler(seen, answer, status))),
    )


def _async_client(seen: list[httpx.Request], answer: Any = None, status: int = 200) -> AsyncNorbix:
    return AsyncNorbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(_handler(seen, answer, status))),
    )


def _route(request: httpx.Request) -> tuple[str, str, str]:
    url = urlparse(str(request.url))
    return request.method, url.path, url.query


def test_check_bundle_discount_sends_code_bundle_and_period_and_reads_the_discount() -> None:
    seen: list[httpx.Request] = []
    answer = _sync_client(seen, DISCOUNT).hub.account.check_bundle_discount(
        code="LAUNCH20", bundle="Growth", billingPeriod="Monthly"
    )

    assert [_route(r) for r in seen] == [("POST", "/v3/account/stripe/discount/check", "")]
    assert "norbix-account-id" not in seen[0].headers
    assert json.loads(seen[0].content) == {
        "code": "LAUNCH20",
        "bundle": "Growth",
        "billingPeriod": "Monthly",
    }
    assert answer["discount"]["percentOff"] == 20
    assert answer["discount"]["months"] == 3
    assert answer["discount"]["endsAt"] is None


def test_apply_bundle_discount_sends_the_code_in_a_post_body() -> None:
    seen: list[httpx.Request] = []
    _sync_client(seen).hub.account.apply_bundle_discount(code="LAUNCH20")

    assert [_route(r) for r in seen] == [("POST", "/v3/account/stripe/discount", "")]
    assert "norbix-account-id" not in seen[0].headers
    assert json.loads(seen[0].content) == {"code": "LAUNCH20"}


def test_create_stripe_checkout_session_sends_the_discount_code() -> None:
    seen: list[httpx.Request] = []
    _sync_client(seen).hub.account.create_stripe_checkout_session(
        subscriptionType="ManagedService", bundle="Starter", billingPeriod="Monthly", discountCode="LAUNCH20"
    )

    assert [_route(r) for r in seen] == [("POST", "/v3/account/stripe/create-checkout-session", "")]
    assert json.loads(seen[0].content) == {
        "subscriptionType": "ManagedService",
        "bundle": "Starter",
        "billingPeriod": "Monthly",
        "discountCode": "LAUNCH20",
    }


def test_a_refused_code_reaches_the_caller_with_its_code_and_reason() -> None:
    seen: list[httpx.Request] = []
    with pytest.raises(ValidationError) as caught:
        _sync_client(seen, ALREADY_USED, 400).hub.account.apply_bundle_discount(code="LAUNCH20")

    err = caught.value
    assert err.http_status == 400
    assert err.error_code == "CM-ERRORS-ACCOUNT-027"
    assert err.context == {"reason": "already_used"}
    assert err.errors[0].context["reason"] == "already_used"


def test_async_client_has_the_same_two_methods_and_the_same_refusal() -> None:
    seen: list[httpx.Request] = []

    async def run() -> Any:
        client = _async_client(seen, DISCOUNT)
        try:
            checked = await client.hub.account.check_bundle_discount(code="LAUNCH20")
            await client.hub.account.apply_bundle_discount(code="LAUNCH20")
            return checked
        finally:
            await client.aclose()

    checked = asyncio.run(run())

    assert [_route(r) for r in seen] == [
        ("POST", "/v3/account/stripe/discount/check", ""),
        ("POST", "/v3/account/stripe/discount", ""),
    ]
    assert json.loads(seen[0].content) == {"code": "LAUNCH20"}
    assert json.loads(seen[1].content) == {"code": "LAUNCH20"}
    assert checked["discount"]["code"] == "LAUNCH20"

    async def refused() -> Any:
        client = _async_client([], ALREADY_USED, 400)
        try:
            return await client.hub.account.check_bundle_discount(code="LAUNCH20")
        finally:
            await client.aclose()

    with pytest.raises(ValidationError) as caught:
        asyncio.run(refused())
    assert caught.value.error_code == "CM-ERRORS-ACCOUNT-027"
    assert caught.value.context == {"reason": "already_used"}
