"""Trial limits for the Managed Service: trial availability and the waiting list.

The gateway takes the account from the signed-in session for both routes, so
every test runs on a client WITHOUT ``account_id``. Each one asserts the verb,
the fully-resolved path, the query and the body. A trial checkout in a full
region must reach the caller with ``CM-ERRORS-ACCOUNT-040``. Sync and async
clients are both covered. Nothing leaves the process.

``POST /account/trial-waitlist/intake`` has no method on purpose: only the
Norbix website's server calls it, with a shared key header.
"""
from __future__ import annotations

import asyncio
import json
from typing import Any
from urllib.parse import parse_qsl, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix, ValidationError

FULL_REGION = {
    "limitsOn": True,
    "region": "nb-eu-germany",
    "trialsOpen": False,
    "waitlistOpen": True,
    "onWaitlist": False,
    "refusal": "",
}

ADDED = {"status": "added", "message": "You are on the waiting list."}

REGION_FULL = {
    "responseStatus": {
        "isSuccess": False,
        "errors": [
            {
                "message": "Free trials in this region are full right now.",
                "errorCode": "CM-ERRORS-ACCOUNT-040",
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


def _route(request: httpx.Request) -> tuple[str, str]:
    url = urlparse(str(request.url))
    return request.method, url.path


def _query(request: httpx.Request) -> dict[str, str]:
    return dict(parse_qsl(urlparse(str(request.url)).query))


def test_get_trial_availability_sends_the_region_in_the_query_and_reads_the_answer() -> None:
    seen: list[httpx.Request] = []
    answer = _sync_client(seen, FULL_REGION).hub.account.get_trial_availability(region="nb-eu-germany")

    assert [_route(r) for r in seen] == [("GET", "/v3/account/trial-availability")]
    assert _query(seen[0]) == {"region": "nb-eu-germany"}
    assert seen[0].content == b""
    assert "norbix-account-id" not in seen[0].headers
    assert answer["trialsOpen"] is False
    assert answer["waitlistOpen"] is True
    assert answer["onWaitlist"] is False
    assert answer["limitsOn"] is True


def test_join_trial_waitlist_sends_region_consent_and_version_in_a_post_body() -> None:
    seen: list[httpx.Request] = []
    answer = _sync_client(seen, ADDED).hub.account.join_trial_waitlist(
        region="nb-eu-germany", consent=True, consentVersion="2026-11"
    )

    assert [_route(r) for r in seen] == [("POST", "/v3/account/trial-waitlist")]
    assert _query(seen[0]) == {}
    assert "norbix-account-id" not in seen[0].headers
    assert json.loads(seen[0].content) == {
        "region": "nb-eu-germany",
        "consent": True,
        "consentVersion": "2026-11",
    }
    assert answer["status"] == "added"
    assert answer["message"] == "You are on the waiting list."


def test_create_stripe_checkout_session_sends_region_without_trial_and_trial_invite() -> None:
    seen: list[httpx.Request] = []
    _sync_client(seen).hub.account.create_stripe_checkout_session(
        subscriptionType="ManagedService",
        bundle="Starter",
        billingPeriod="Monthly",
        region="nb-eu-germany",
        withoutTrial=True,
        trialInvite="invite-token-1",
    )

    assert [_route(r) for r in seen] == [("POST", "/v3/account/stripe/create-checkout-session")]
    assert json.loads(seen[0].content) == {
        "subscriptionType": "ManagedService",
        "bundle": "Starter",
        "billingPeriod": "Monthly",
        "region": "nb-eu-germany",
        "withoutTrial": True,
        "trialInvite": "invite-token-1",
    }


def test_a_trial_checkout_in_a_full_region_reaches_the_caller_with_its_code() -> None:
    seen: list[httpx.Request] = []
    with pytest.raises(ValidationError) as caught:
        _sync_client(seen, REGION_FULL, 400).hub.account.create_stripe_checkout_session(
            subscriptionType="ManagedService", bundle="Starter", billingPeriod="Monthly", region="nb-eu-germany"
        )

    err = caught.value
    assert err.http_status == 400
    assert err.error_code == "CM-ERRORS-ACCOUNT-040"


def test_async_client_has_the_same_two_methods_and_the_same_refusal() -> None:
    seen: list[httpx.Request] = []

    async def run() -> Any:
        client = _async_client(seen, FULL_REGION)
        try:
            checked = await client.hub.account.get_trial_availability(region="nb-eu-germany")
            await client.hub.account.join_trial_waitlist(
                region="nb-eu-germany", consent=True, consentVersion="2026-11"
            )
            return checked
        finally:
            await client.aclose()

    checked = asyncio.run(run())

    assert [_route(r) for r in seen] == [
        ("GET", "/v3/account/trial-availability"),
        ("POST", "/v3/account/trial-waitlist"),
    ]
    assert _query(seen[0]) == {"region": "nb-eu-germany"}
    assert json.loads(seen[1].content) == {
        "region": "nb-eu-germany",
        "consent": True,
        "consentVersion": "2026-11",
    }
    assert checked["trialsOpen"] is False
    assert checked["waitlistOpen"] is True

    async def refused() -> Any:
        client = _async_client([], REGION_FULL, 400)
        try:
            return await client.hub.account.create_stripe_checkout_session(
                subscriptionType="ManagedService", bundle="Starter", billingPeriod="Monthly"
            )
        finally:
            await client.aclose()

    with pytest.raises(ValidationError) as caught:
        asyncio.run(refused())
    assert caught.value.error_code == "CM-ERRORS-ACCOUNT-040"
