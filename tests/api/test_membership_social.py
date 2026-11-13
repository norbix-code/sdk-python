from __future__ import annotations

import asyncio
from typing import Any
from urllib.parse import parse_qs, urlsplit

from norbix_python import AsyncNorbix, Norbix

"""The social sign-in start URL: ``client.api.membership.social_sign_in_url``.

The start route answers a redirect to the provider, so it is a URL the browser
navigates to, not a call. A navigation carries no headers: the project id and a
non-PROD env go in the query. Nothing is sent.
"""

ARGS: dict[str, Any] = {
    "project_id": "pr_1",
    "api_key": "key_1",
    "base_url_api": "https://api.test",
    "base_url_hub": "https://hub.test",
    "api_version": "v3",
    "hub_version": "v3",
}


def test_url_carries_the_project_id_and_no_env_for_prod() -> None:
    url = Norbix(**ARGS).api.membership.social_sign_in_url("google")
    assert url == "https://api.test/v3/membership/auth/social/google?projectId=pr_1"


def test_url_encodes_mode_and_return_url() -> None:
    url = Norbix(**ARGS).api.membership.social_sign_in_url(
        "github",
        mode="Admin portal & app",
        return_url="https://app.example.com/oauth/callback?next=/a b&x=1",
    )
    assert url == (
        "https://api.test/v3/membership/auth/social/github?projectId=pr_1"
        "&mode=Admin%20portal%20%26%20app"
        "&returnUrl=https%3A%2F%2Fapp.example.com%2Foauth%2Fcallback%3Fnext%3D%2Fa%20b%26x%3D1"
    )
    query = parse_qs(urlsplit(url).query)
    assert query["mode"] == ["Admin portal & app"]
    assert query["returnUrl"] == ["https://app.example.com/oauth/callback?next=/a b&x=1"]


def test_url_puts_a_non_prod_env_in_the_query() -> None:
    url = Norbix(**ARGS, env="TEST").api.membership.social_sign_in_url("okta")
    assert url == "https://api.test/v3/membership/auth/social/okta?projectId=pr_1&env=TEST"


def test_url_escapes_the_provider() -> None:
    url = Norbix(**ARGS).api.membership.social_sign_in_url("a/b")
    assert url == "https://api.test/v3/membership/auth/social/a%2Fb?projectId=pr_1"


def test_async_client_builds_the_same_url() -> None:
    async def run() -> str:
        client = AsyncNorbix(**ARGS)
        try:
            return client.api.membership.social_sign_in_url("google", return_url="https://app.test/cb")
        finally:
            await client.aclose()

    assert asyncio.run(run()) == (
        "https://api.test/v3/membership/auth/social/google?projectId=pr_1&returnUrl=https%3A%2F%2Fapp.test%2Fcb"
    )
