from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from norbix_python import AsyncNorbix

from ..helpers import make_client

"""Scheduler coverage.

Every scheduler method, sync and async: the verb, the fully-resolved path, and
where each parameter goes — the route token in the path, list filters in the
query string, the save request in the JSON body. Source of truth: gateway
Hub.Scheduler/*.cs [Route]. Every call goes to a capture transport, so nothing
leaves the process.
"""

TASK_ID = "tsk_1"
INITIATOR_USER_ID = "usr_1"
EMAIL_TEMPLATE_ID = "etpl_1"

BASE = "/v3/scheduler"

# A complete save request: the initiator, the schedule, and an email campaign
# task sent to all users. EmailCampaign is the only task type the gateway runs.
SAVE_REQUEST: dict[str, Any] = {
    "initiatorUserId": INITIATOR_USER_ID,
    "name": "Weekly digest",
    "cron": "0 9 * * 1",
    "isEnabled": True,
    "stopOnError": False,
    "task": {
        "type": "EmailCampaign",
        "campaign": {"source": "AllUsers", "templateId": EMAIL_TEMPLATE_ID},
    },
}

# name, verb, expected path, expected query (None: none), expected body (None: none), call
SchedulerCase = tuple[str, str, str, dict[str, list[str]] | None, dict[str, Any] | None, Callable[[Any], Any]]

SCHEDULER_CASES: list[SchedulerCase] = [
    # module — PUT since the gateway moved them off GET
    ("enable_scheduler", "PUT", f"{BASE}/enable", None, None, lambda m: m.enable_scheduler()),
    ("disable_scheduler", "PUT", f"{BASE}/disable", None, None, lambda m: m.disable_scheduler()),
    # tasks
    (
        "get_scheduler_tasks",
        "GET",
        f"{BASE}/tasks",
        {"pageSize": ["10"], "type": ["EmailCampaign"]},
        None,
        lambda m: m.get_scheduler_tasks(pageSize=10, type="EmailCampaign"),
    ),
    (
        "get_scheduler_task",
        "GET",
        f"{BASE}/tasks/{TASK_ID}",
        None,
        None,
        lambda m: m.get_scheduler_task(id=TASK_ID),
    ),
    (
        "save_scheduler_task",
        "POST",
        f"{BASE}/tasks",
        None,
        SAVE_REQUEST,
        lambda m: m.save_scheduler_task(**SAVE_REQUEST),
    ),
    (
        "enable_scheduler_task",
        "PUT",
        f"{BASE}/tasks/{TASK_ID}/enable",
        None,
        None,
        lambda m: m.enable_scheduler_task(id=TASK_ID),
    ),
    (
        "disable_scheduler_task",
        "PUT",
        f"{BASE}/tasks/{TASK_ID}/disable",
        None,
        None,
        lambda m: m.disable_scheduler_task(id=TASK_ID),
    ),
    (
        "delete_scheduler_task",
        "DELETE",
        f"{BASE}/tasks/{TASK_ID}",
        None,
        None,
        lambda m: m.delete_scheduler_task(id=TASK_ID),
    ),
]


def _assert_request(
    name: str,
    method: str,
    url: str,
    body: str,
    verb: str,
    path: str,
    query: dict[str, list[str]] | None,
    expected_body: dict[str, Any] | None,
) -> None:
    parsed = urlparse(url)
    assert method == verb, f"{name}: verb {method}, expected {verb}"
    assert parsed.path == path, f"{name}: got {url}, expected the path {path}"
    assert parse_qs(parsed.query) == (query or {}), f"{name}: query {parsed.query!r}"
    if expected_body is None:
        assert body == "", f"{name}: expected no body, got {body!r}"
    else:
        assert json.loads(body) == expected_body, f"{name}: body {body}"


@pytest.mark.parametrize(
    ("name", "verb", "path", "query", "body", "call"),
    SCHEDULER_CASES,
    ids=[case[0] for case in SCHEDULER_CASES],
)
def test_scheduler_endpoint_hits_the_expected_route(
    name: str,
    verb: str,
    path: str,
    query: dict[str, list[str]] | None,
    body: dict[str, Any] | None,
    call: Callable[[Any], Any],
) -> None:
    client, transport = make_client()
    call(client.hub.scheduler)

    assert transport.last_request is not None
    _assert_request(
        name,
        transport.last_request["method"],
        transport.last_request["url"],
        transport.last_request["body"],
        verb,
        path,
        query,
        body,
    )


def test_async_scheduler_endpoints_hit_the_same_routes() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    async def run() -> None:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        try:
            for _, _, _, _, _, call in SCHEDULER_CASES:
                await call(client.hub.scheduler)
        finally:
            await client.aclose()

    asyncio.run(run())

    assert len(seen) == len(SCHEDULER_CASES)
    for request, (name, verb, path, query, body, _) in zip(seen, SCHEDULER_CASES, strict=True):
        _assert_request(name, request.method, str(request.url), request.content.decode("utf-8"), verb, path, query, body)


def test_scheduler_surface_size() -> None:
    """8 scheduler routes in the gateway. A new one changes this count, so it cannot arrive untested."""
    assert len(SCHEDULER_CASES) == 8
    assert len({case[0] for case in SCHEDULER_CASES}) == 8


def test_save_scheduler_task_sends_the_email_campaign_task() -> None:
    client, transport = make_client()
    client.hub.scheduler.save_scheduler_task(**SAVE_REQUEST)

    assert transport.last_request is not None
    sent = json.loads(transport.last_request["body"])
    # The discriminator reaches the wire as the name; the campaign is nested under task.
    assert sent["task"] == {
        "type": "EmailCampaign",
        "campaign": {"source": "AllUsers", "templateId": EMAIL_TEMPLATE_ID},
    }
    assert sent["initiatorUserId"] == INITIATOR_USER_ID
    assert sent["stopOnError"] is False


def test_save_scheduler_task_sends_the_task_id_in_the_body_on_update() -> None:
    client, transport = make_client()
    client.hub.scheduler.save_scheduler_task(taskId=TASK_ID, **SAVE_REQUEST)

    assert transport.last_request is not None
    assert urlparse(transport.last_request["url"]).path == f"{BASE}/tasks"
    assert json.loads(transport.last_request["body"]) == {"taskId": TASK_ID, **SAVE_REQUEST}
