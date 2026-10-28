from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class IntegrationsModule:
    """Helpers shared by every module's integrations (files, email, code, ...)."""

    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_keyless_integration_setup(
        self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any
    ) -> Any:
        """GET /{version}/integrations/keyless/setup

        What a developer needs before saving a keyless cloud integration.
        Request: ``module`` (files, email or code), ``cloud`` (azure, aws or
        google), optional ``integrationId`` (an existing integration).
        Answer: ``integrationId`` (save with it), ``env``, ``module``, ``cloud``,
        ``issuer``, ``subject``, ``audience``, ``available`` (with
        ``unavailableReason`` when false) and the cloud setup ``script``.
        ``templates``: ready CloudFormation / Bicep / Terraform files for this
        integration (a list of ``{"kind", "fileName", "content"}``).
        """
        return self._transport.send(
            target="hub",
            path="/{version}/integrations/keyless/setup",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncIntegrationsModule:
    """Helpers shared by every module's integrations (files, email, code, ...)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_keyless_integration_setup(
        self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any
    ) -> Any:
        """GET /{version}/integrations/keyless/setup — see ``IntegrationsModule.get_keyless_integration_setup``."""
        return await self._transport.send(
            target="hub",
            path="/{version}/integrations/keyless/setup",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
