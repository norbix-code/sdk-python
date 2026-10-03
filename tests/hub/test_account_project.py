"""Request-shape tests for the Project-module routes of ``hub.account``.

One table drives both clients: every case is sent through the sync
``Norbix`` and the ``AsyncNorbix`` client, and the test checks the verb, the
resolved path, the JSON body and the auth / project headers.
"""
from __future__ import annotations

import asyncio
import json
from typing import Any

import httpx
import pytest

from norbix_python import AsyncNorbix, Norbix

# (method, positional args, keyword body, verb, path after /v2, expected JSON body or None)
CASES: list[tuple[str, tuple[str, ...], dict[str, Any], str, str, dict[str, Any] | None]] = [
    ("update_project_admin_url", ("pr_1",), {"url": "https://admin.example.com"}, "PATCH",
     "/account/projects/pr_1/settings/admin-url", {"url": "https://admin.example.com"}),
    ("update_project_legal_documents", ("pr_1",), {"termsMarkdown": "# Terms", "privacyMarkdown": "# Privacy"}, "PATCH",
     "/account/projects/pr_1/settings/legal", {"termsMarkdown": "# Terms", "privacyMarkdown": "# Privacy"}),
    ("update_project_expose_legal", ("pr_1",), {"exposed": True}, "PATCH",
     "/account/projects/pr_1/settings/legal/expose", {"exposed": True}),
    ("get_admin_portal_structure", ("pr_1",), {}, "GET",
     "/account/projects/pr_1/admin-portal/structure", None),
    ("assign_admin_portal_service_user", ("pr_1",), {"serviceUserId": "su_1"}, "PUT",
     "/account/projects/pr_1/settings/admin-portal/service-user", {"serviceUserId": "su_1"}),
    ("create_ai_service_user", (), {"name": "Claude Code on my laptop", "scope": {"reach": "project", "projectId": "pr_1", "rights": "read", "envs": ["TEST"]}}, "POST",
     "/account/ai/service-users", {"name": "Claude Code on my laptop", "scope": {"reach": "project", "projectId": "pr_1", "rights": "read", "envs": ["TEST"]}}),
    ("list_ai_service_users", (), {}, "GET", "/account/ai/service-users", None),
    ("rotate_ai_service_user_key", ("aisu_1",), {"revokeKeyId": "aisk_old"}, "POST",
     "/account/ai/service-users/aisu_1/keys", {"revokeKeyId": "aisk_old"}),
    ("revoke_ai_service_user_key", ("aisu_1", "aisk_1"), {}, "DELETE",
     "/account/ai/service-users/aisu_1/keys/aisk_1", None),
    ("delete_ai_service_user", ("aisu_1",), {}, "DELETE", "/account/ai/service-users/aisu_1", None),
]


def _capture(seen: list[httpx.Request]) -> Any:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    return handler


def _check(request: httpx.Request, verb: str, path: str, body: dict[str, Any] | None) -> None:
    assert request.method == verb
    assert request.url.path == "/v2" + path
    assert request.headers["authorization"] == "Bearer test-token"
    assert request.headers["x-cm-projectid"] == "test-project"
    if body is None:
        assert request.content == b""
    else:
        assert json.loads(request.content) == body


@pytest.mark.parametrize(("name", "args", "kwargs", "verb", "path", "body"), CASES, ids=[c[0] for c in CASES])
def test_sync_request_shape(
    name: str, args: tuple[str, ...], kwargs: dict[str, Any], verb: str, path: str, body: dict[str, Any] | None
) -> None:
    seen: list[httpx.Request] = []
    # No account_id: these routes take the account from the signed-in session.
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        http_client=httpx.Client(transport=httpx.MockTransport(_capture(seen))),
    )
    getattr(client.hub.account, name)(*args, **kwargs)
    assert len(seen) == 1
    _check(seen[0], verb, path, body)


@pytest.mark.parametrize(("name", "args", "kwargs", "verb", "path", "body"), CASES, ids=[c[0] for c in CASES])
def test_async_request_shape(
    name: str, args: tuple[str, ...], kwargs: dict[str, Any], verb: str, path: str, body: dict[str, Any] | None
) -> None:
    seen: list[httpx.Request] = []

    async def run() -> None:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(_capture(seen))),
        )
        try:
            await getattr(client.hub.account, name)(*args, **kwargs)
        finally:
            await client.aclose()

    asyncio.run(run())
    assert len(seen) == 1
    _check(seen[0], verb, path, body)
