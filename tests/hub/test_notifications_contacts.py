from __future__ import annotations

import asyncio
from collections.abc import Callable
from pathlib import Path
from typing import Any

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

"""Contacts moved from /notifications/contacts to /membership/users.

The gateway answers 404 on the old path. The deprecated notifications contact
methods keep their names and call the membership routes; consent and
unsubscribe are served by the API host only. Every call goes to a mock
transport, so nothing leaves the process.
"""

API = "https://api.test"
HUB = "https://hub.test"

# name, host, method, path, call
ContactCase = tuple[str, str, str, str, Callable[[Any], Any]]

CONTACT_CASES: list[ContactCase] = [
    ("get_all_contacts", HUB, "GET", "/v2/membership/users", lambda m: m.get_all_contacts()),
    ("create_contact", HUB, "POST", "/v2/membership/users", lambda m: m.create_contact()),
    ("merge_contacts", HUB, "POST", "/v2/membership/users/merge", lambda m: m.merge_contacts()),
    ("delete_contact", HUB, "DELETE", "/v2/membership/users/ct_1", lambda m: m.delete_contact("ct_1")),
    ("get_contact", HUB, "GET", "/v2/membership/users/ct_1", lambda m: m.get_contact("ct_1")),
    (
        "add_contact_identity",
        HUB,
        "POST",
        "/v2/membership/users/ct_1/identities",
        lambda m: m.add_contact_identity("ct_1"),
    ),
    (
        "remove_contact_identity",
        HUB,
        "DELETE",
        "/v2/membership/users/ct_1/identities/usr_1",
        lambda m: m.remove_contact_identity("ct_1", identity_id="usr_1"),
    ),
    (
        "promote_contact_identity",
        HUB,
        "POST",
        "/v2/membership/users/ct_1/identities/usr_1/promote",
        lambda m: m.promote_contact_identity("ct_1", identity_id="usr_1"),
    ),
    (
        "grant_contact_consent",
        API,
        "POST",
        "/v2/membership/users/ct_1/marketing-state/Email/consent",
        lambda m: m.grant_contact_consent("ct_1", "Email"),
    ),
    (
        "unsubscribe_contact",
        API,
        "POST",
        "/v2/membership/users/ct_1/marketing-state/Email/unsubscribe",
        lambda m: m.unsubscribe_contact("ct_1", "Email"),
    ),
]

CLIENT_ARGS: dict[str, Any] = {
    "project_id": "test-project",
    "api_key": "key_1",
    "base_url_api": API,
    "base_url_hub": HUB,
    "api_version": "v2",
    "hub_version": "v2",
}


def _capture(seen: list[httpx.Request]) -> Callable[[httpx.Request], httpx.Response]:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    return handler


def _assert_request(request: httpx.Request, host: str, method: str, path: str) -> None:
    assert f"{request.url.scheme}://{request.url.host}" == host
    assert request.method == method
    assert request.url.path == path


def test_no_module_calls_the_old_contacts_route() -> None:
    src = Path(__file__).resolve().parents[2] / "src" / "norbix_python"
    offenders = [str(f) for f in src.rglob("*.py") if "/notifications/contacts" in f.read_text()]
    assert offenders == []


@pytest.mark.parametrize("name, host, method, path, call", CONTACT_CASES, ids=[c[0] for c in CONTACT_CASES])
def test_notifications_contact_methods_call_membership_routes(
    name: str, host: str, method: str, path: str, call: Callable[[Any], Any]
) -> None:
    seen: list[httpx.Request] = []
    client = Norbix(**CLIENT_ARGS, http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))))

    call(client.hub.notifications)

    assert len(seen) == 1
    _assert_request(seen[0], host, method, path)


@pytest.mark.parametrize("name, host, method, path, call", CONTACT_CASES, ids=[c[0] for c in CONTACT_CASES])
def test_async_notifications_contact_methods_call_membership_routes(
    name: str, host: str, method: str, path: str, call: Callable[[Any], Any]
) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(
            **CLIENT_ARGS, http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen)))
        )
        try:
            await call(client.hub.notifications)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == 1
    _assert_request(seen[0], host, method, path)
