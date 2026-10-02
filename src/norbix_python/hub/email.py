from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class EmailModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def one_click_unsubscribe(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/email/one-click-unsubscribe

        Public: the signed link in the e-mail is the key, so no credentials are
        needed. Auth is still sent when the client has a token.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/email/one-click-unsubscribe",
            method="POST",
            path_params={},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_preferences_by_link(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/email/preferences

        Reads the marketing e-mail preferences of the person a signed unsubscribe link
        belongs to. Opens with the link alone: pass ``token=...`` and no credentials are
        needed. Auth is still sent when the client has a token.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/email/preferences",
            method="GET",
            path_params={},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncEmailModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def one_click_unsubscribe(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/email/one-click-unsubscribe

        Public: the signed link in the e-mail is the key, so no credentials are
        needed. Auth is still sent when the client has a token.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/email/one-click-unsubscribe",
            method="POST",
            path_params={},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_preferences_by_link(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/email/preferences

        Reads the marketing e-mail preferences of the person a signed unsubscribe link
        belongs to. Opens with the link alone: pass ``token=...`` and no credentials are
        needed. Auth is still sent when the client has a token.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/email/preferences",
            method="GET",
            path_params={},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )
