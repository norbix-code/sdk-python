from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class IntegrationsModule:
    """Helpers shared by every module's integrations: keyless cloud setup, quick connect, saved secrets."""

    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_keyless_integration_setup(
        self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any
    ) -> Any:
        """GET /{version}/integrations/keyless/setup

        What a developer needs before saving a keyless cloud integration.
        Request: ``module`` (files, email, code, logs, push, payments or
        database), ``cloud`` (azure, aws, google — or atlas for the database
        module, MongoDB Atlas M10+; logs: aws or azure; push and payments:
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

    def get_quick_connect_providers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/integrations/connect/providers — the providers that can quick-connect (one-click OAuth) on this install.

        Request: optional ``module`` (e.g. ``payments``; empty = every module). Answer: ``providers``, each with
        ``module``, ``provider``, ``available``, ``requiredInputs`` (e.g. storeUrl), ``modes`` (test / live) and
        ``redirectUrl``. Read it before ``payments.start_payments_integration_connect``."""
        return self._transport.send(
            target="hub",
            path="/{version}/integrations/connect/providers",
            method="GET",
            path_params={},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_integration_connect_targets(self, connect_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/integrations/connect/{ConnectId}/targets — the accounts a quick connect may finish with.

        Once the person approved on the provider's page: ``targets`` (``id``, ``name``, ``detail``) plus
        ``connectId``, ``module``, ``provider``, ``integrationName``, ``accountName``. Pick one and finish with
        ``payments.complete_payments_integration_connect``."""
        return self._transport.send(
            target="hub",
            path="/{version}/integrations/connect/{ConnectId}/targets",
            method="GET",
            path_params={"ConnectId": connect_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


    def get_integration_secrets(
        self, integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any
    ) -> Any:
        """GET /{version}/integrations/{IntegrationId}/secrets — which secrets of an integration are saved.

        Works for an integration of any module. Answer: ``result``, a list of ``{"key", "field", "isSet",
        "isOptional"}`` — never a value or any part of one. ``field`` is the save request property that fills
        the key. Empty for keyless and Norbix-owned integrations and for MCP, Marketplace and Webhook
        integrations. Request: optional ``env``."""
        return self._transport.send(
            target="hub",
            path="/{version}/integrations/{IntegrationId}/secrets",
            method="GET",
            path_params={"IntegrationId": integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def remove_integration_secrets(
        self,
        integration_id: str,
        keys: list[str],
        *,
        timeout: float | None = None,
        bearer_token: str | None = None,
        **request: Any,
    ) -> Any:
        """POST /{version}/integrations/{IntegrationId}/secrets/remove — remove optional secrets.

        ``keys`` as ``get_integration_secrets`` lists them. A key the integration needs is refused with
        ``CM-ERRORS-SECRETS-012`` (400) and nothing is written. Request: optional ``env``. Answer: ``id``."""
        return self._transport.send(
            target="hub",
            path="/{version}/integrations/{IntegrationId}/secrets/remove",
            method="POST",
            path_params={"IntegrationId": integration_id},
            request={**request, "keys": list(keys)},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

class AsyncIntegrationsModule:
    """Helpers shared by every module's integrations: keyless cloud setup, quick connect, saved secrets."""

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

    async def get_quick_connect_providers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/integrations/connect/providers — the providers that can quick-connect (one-click OAuth) on this install.

        Request: optional ``module`` (e.g. ``payments``; empty = every module). Answer: ``providers``, each with
        ``module``, ``provider``, ``available``, ``requiredInputs`` (e.g. storeUrl), ``modes`` (test / live) and
        ``redirectUrl``. Read it before ``payments.start_payments_integration_connect``."""
        return await self._transport.send(
            target="hub",
            path="/{version}/integrations/connect/providers",
            method="GET",
            path_params={},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_integration_connect_targets(self, connect_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/integrations/connect/{ConnectId}/targets — the accounts a quick connect may finish with.

        Once the person approved on the provider's page: ``targets`` (``id``, ``name``, ``detail``) plus
        ``connectId``, ``module``, ``provider``, ``integrationName``, ``accountName``. Pick one and finish with
        ``payments.complete_payments_integration_connect``."""
        return await self._transport.send(
            target="hub",
            path="/{version}/integrations/connect/{ConnectId}/targets",
            method="GET",
            path_params={"ConnectId": connect_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_integration_secrets(
        self, integration_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any
    ) -> Any:
        """GET /{version}/integrations/{IntegrationId}/secrets — see ``IntegrationsModule.get_integration_secrets``."""
        return await self._transport.send(
            target="hub",
            path="/{version}/integrations/{IntegrationId}/secrets",
            method="GET",
            path_params={"IntegrationId": integration_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def remove_integration_secrets(
        self,
        integration_id: str,
        keys: list[str],
        *,
        timeout: float | None = None,
        bearer_token: str | None = None,
        **request: Any,
    ) -> Any:
        """POST /{version}/integrations/{IntegrationId}/secrets/remove — see ``IntegrationsModule.remove_integration_secrets``."""
        return await self._transport.send(
            target="hub",
            path="/{version}/integrations/{IntegrationId}/secrets/remove",
            method="POST",
            path_params={"IntegrationId": integration_id},
            request={**request, "keys": list(keys)},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
