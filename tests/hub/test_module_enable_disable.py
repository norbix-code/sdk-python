"""Every module's enable / disable call uses PUT (gateway change on refactoringV2).

The gateway moved the 18 module switches from GET to PUT. GET still answers
for a while (hidden, deprecated, logs a WARN), but the SDK must send PUT.
Both the sync and the async client are checked.
"""

from __future__ import annotations

import asyncio

import httpx
import pytest

from norbix_python import AsyncNorbix

from ..helpers import make_client

# (module attribute, method name, path after /v3)
CASES = [
    ("database", "enable_database", "/database/enable"),
    ("database", "disable_database", "/database/disable"),
    ("files", "enable_files", "/files/enable"),
    ("files", "disable_files", "/files/disable"),
    ("notifications", "enable_push", "/notifications/push/enable"),
    ("notifications", "disable_push", "/notifications/push/disable"),
    ("notifications", "enable_sms", "/notifications/sms/enable"),
    ("notifications", "disable_sms", "/notifications/sms/disable"),
    ("notifications", "enable_email", "/notifications/email/enable"),
    ("notifications", "disable_email", "/notifications/email/disable"),
    ("payments", "enable_payments", "/payments/enable"),
    ("payments", "disable_payments", "/payments/disable"),
    ("logs", "enable_logging", "/logs/enable"),
    ("logs", "disable_logging", "/logs/disable"),
    ("membership", "enable_membership", "/membership/enable"),
    ("membership", "disable_membership", "/membership/disable"),
    ("code", "enable_code", "/code/enable"),
    ("code", "disable_code", "/code/disable"),
]


@pytest.mark.parametrize(("module", "method", "path"), CASES, ids=[c[1] for c in CASES])
def test_sync_module_switch_uses_put(module: str, method: str, path: str) -> None:
    client, transport = make_client()
    getattr(getattr(client.hub, module), method)()
    assert transport.last_request is not None
    sent = httpx.URL(transport.last_request["url"])
    assert (transport.last_request["method"], sent.path) == ("PUT", "/v3" + path)


@pytest.mark.parametrize(("module", "method", "path"), CASES, ids=[c[1] for c in CASES])
def test_async_module_switch_uses_put(module: str, method: str, path: str) -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    async def run() -> None:
        async with AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        ) as client:
            await getattr(getattr(client.hub, module), method)()

    asyncio.run(run())
    assert [(r.method, r.url.path) for r in seen] == [("PUT", "/v3" + path)]
