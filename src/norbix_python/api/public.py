"""Public project pages served by the API host — no sign-in.

The API-host twin of the TypeScript SDK's ``src/api/public.ts``.
"""
from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class PublicModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_public_project_config(self, project_id: str, *, timeout: float | None = None, **request: Any) -> Any:
        """GET /{version}/public/projects/{ProjectId}/config

        The project's public, non-sensitive config — what an Admin Portal or a
        sign-in page needs before anyone signs in: ``displayName``, the
        Admin Portal switch, the brand block (when the project exposes its
        brand), social providers, passkey, and sign-in methods with the
        password policy (only when the project exposes them).

        **No sign-in.** The gateway does not authenticate this route, and the
        SDK sends no ``Authorization`` header even when the client has one.
        An unknown project gives back an empty config, not an error.
        Request DTO: GetPublicProjectConfig.
        """
        return self._transport.send(
            target="api",
            path="/{version}/public/projects/{ProjectId}/config",
            method="GET",
            path_params={"ProjectId": project_id},
            request=request,
            scope="unauthenticated",
            timeout=timeout,
        )

    def get_public_project_legal(self, project_id: str, kind: str, *, timeout: float | None = None, **request: Any) -> Any:
        """GET /{version}/public/projects/{ProjectId}/legal/{Kind}

        The project's public legal document: ``kind`` is ``"terms"`` or
        ``"privacy"``. Gives back ``{kind, title, body, available}`` with the
        Markdown in ``body``. ``available`` is ``False`` when the project has
        not turned the legal pages on (``hub.account.update_project_expose_legal``),
        has not written that document, or does not exist — the answer does
        not say which.

        **No sign-in**, same as ``get_public_project_config``.
        Request DTO: GetPublicProjectLegal.
        """
        return self._transport.send(
            target="api",
            path="/{version}/public/projects/{ProjectId}/legal/{Kind}",
            method="GET",
            path_params={"ProjectId": project_id, "Kind": kind},
            request=request,
            scope="unauthenticated",
            timeout=timeout,
        )


class AsyncPublicModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_public_project_config(self, project_id: str, *, timeout: float | None = None, **request: Any) -> Any:
        """GET /{version}/public/projects/{ProjectId}/config

        The project's public, non-sensitive config — what an Admin Portal or a
        sign-in page needs before anyone signs in: ``displayName``, the
        Admin Portal switch, the brand block (when the project exposes its
        brand), social providers, passkey, and sign-in methods with the
        password policy (only when the project exposes them).

        **No sign-in.** The gateway does not authenticate this route, and the
        SDK sends no ``Authorization`` header even when the client has one.
        An unknown project gives back an empty config, not an error.
        Request DTO: GetPublicProjectConfig.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/public/projects/{ProjectId}/config",
            method="GET",
            path_params={"ProjectId": project_id},
            request=request,
            scope="unauthenticated",
            timeout=timeout,
        )

    async def get_public_project_legal(self, project_id: str, kind: str, *, timeout: float | None = None, **request: Any) -> Any:
        """GET /{version}/public/projects/{ProjectId}/legal/{Kind}

        The project's public legal document: ``kind`` is ``"terms"`` or
        ``"privacy"``. Gives back ``{kind, title, body, available}`` with the
        Markdown in ``body``. ``available`` is ``False`` when the project has
        not turned the legal pages on (``hub.account.update_project_expose_legal``),
        has not written that document, or does not exist — the answer does
        not say which.

        **No sign-in**, same as ``get_public_project_config``.
        Request DTO: GetPublicProjectLegal.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/public/projects/{ProjectId}/legal/{Kind}",
            method="GET",
            path_params={"ProjectId": project_id, "Kind": kind},
            request=request,
            scope="unauthenticated",
            timeout=timeout,
        )
