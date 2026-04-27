from __future__ import annotations

from typing import Any

import httpx

from norbix_python import Norbix


class CaptureTransport(httpx.BaseTransport):
    def __init__(self) -> None:
        self.last_request: dict[str, Any] | None = None

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self.last_request = {
            "method": request.method,
            "url": str(request.url),
            "headers": dict(request.headers),
            "body": request.content.decode("utf-8") if request.content else "",
        }
        return httpx.Response(200, json={})


def make_client(account_id: str | None = None) -> tuple[Norbix, CaptureTransport]:
    transport = CaptureTransport()
    http_client = httpx.Client(transport=transport)
    client = Norbix(
        project_id="test-project",
        bearer_token="test-token",
        account_id=account_id,
        http_client=http_client,
    )
    return client, transport


def stub_request_for_path(path: str) -> dict[str, str]:
    out: dict[str, str] = {}
    idx = 0
    while True:
        start = path.find("{", idx)
        end = path.find("}", start + 1)
        if start < 0 or end < 0:
            break
        token = path[start + 1 : end]
        if token != "version":
            out[token] = f"stub-{token}"
        idx = end + 1
    return out
