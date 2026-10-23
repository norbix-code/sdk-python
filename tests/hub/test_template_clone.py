"""Template clone answers the new copy's id.

The gateway's clone requests (email, SMS and push templates) answer an
``IdResponse``: ``{"id": "<new template id>"}``. The SDK hands that answer to
the caller unchanged. Every call goes to a fake transport; no server is
contacted.
"""

from __future__ import annotations

import asyncio
from typing import Any

import httpx

from norbix_python import AsyncNorbix, Norbix

SOURCE_ID = "tpl_source"
COPY_ID = "tpl_copy"


def _answering(seen: list[httpx.Request]) -> Norbix:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"id": COPY_ID})

    return Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )


def _assert_clone(seen: list[httpx.Request], channel: str, answer: Any) -> None:
    assert answer == {"id": COPY_ID}
    assert len(seen) == 1
    assert seen[0].method == "POST"
    assert seen[0].url.path == f"/v3/notifications/{channel}/templates/{SOURCE_ID}/clone"


def test_clone_email_template_returns_the_copy_id() -> None:
    seen: list[httpx.Request] = []
    answer = _answering(seen).hub.notifications.clone_email_template(id=SOURCE_ID)
    _assert_clone(seen, "email", answer)


def test_clone_sms_template_returns_the_copy_id() -> None:
    seen: list[httpx.Request] = []
    answer = _answering(seen).hub.notifications.clone_sms_template(id=SOURCE_ID)
    _assert_clone(seen, "sms", answer)


def test_clone_push_template_returns_the_copy_id() -> None:
    seen: list[httpx.Request] = []
    answer = _answering(seen).hub.notifications.clone_push_template(id=SOURCE_ID)
    _assert_clone(seen, "push", answer)


def test_async_clone_returns_the_copy_id() -> None:
    seen: list[httpx.Request] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"id": COPY_ID})

    async def run() -> Any:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        return await client.hub.notifications.clone_email_template(id=SOURCE_ID)

    _assert_clone(seen, "email", asyncio.run(run()))
