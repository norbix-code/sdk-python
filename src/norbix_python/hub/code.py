from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class CodeModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disable_code(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/disable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_code(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/enable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_code_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/integrations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def confirm_code_integration_human_delivery(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/integrations/confirm-human-delivery"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/integrations/confirm-human-delivery",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_code_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/integrations/test"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/integrations/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_code_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/code/integrations/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_code_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/integrations/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_code_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/integrations/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/integrations/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_listings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/listings"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/listings",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_listing_function_tokens(self, listing_view_id: str, function_key: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/listings/{ListingViewId}/functions/{FunctionKey}/tokens"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/listings/{ListingViewId}/functions/{FunctionKey}/tokens",
            method="GET",
            path_params={"ListingViewId": listing_view_id, "FunctionKey": function_key},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_integration(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_marketplace_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_marketplace_integration(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/code/marketplace/integrations/{IntegrationViewId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}",
            method="DELETE",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_marketplace_integration(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/enable",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_marketplace_integration(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/disable",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_functions(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/functions"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_function(self, integration_view_id: str, function_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id, "FunctionViewId": function_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_marketplace_function(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/functions"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_marketplace_function(self, integration_view_id: str, function_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}",
            method="DELETE",
            path_params={"IntegrationViewId": integration_view_id, "FunctionViewId": function_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_marketplace_function(self, integration_view_id: str, function_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/enable",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id, "FunctionViewId": function_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_marketplace_function(self, integration_view_id: str, function_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/disable",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id, "FunctionViewId": function_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_function_tokens(self, integration_view_id: str, function_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/tokens"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/tokens",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id, "FunctionViewId": function_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def invoke_marketplace_function(self, function_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/functions/{FunctionViewId}/invoke"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/functions/{FunctionViewId}/invoke",
            method="POST",
            path_params={"FunctionViewId": function_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_listing(self, listing_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/listings/{ListingViewId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/listings/{ListingViewId}",
            method="GET",
            path_params={"ListingViewId": listing_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_marketplace_integration(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/test"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/test",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_integration_tools(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/tools — the stored MCP tool catalog of a connection."""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/tools",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_integration_access(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/access — the access matrix of a connection: roles, packages, tools and functions."""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/access",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def set_marketplace_integration_role_access(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/marketplace/integrations/{IntegrationViewId}/access/roles — give a role one package (None, Viewer, FunctionsOnly, ReadOnly, FullAccess) and the Manage flag; body `roleId`, `package`, `manage`."""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/access/roles",
            method="PUT",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_marketplace_integration_custom_access(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/access/roles/custom — a custom access policy of the connection for one role; body `roleId`, `basePackage`, `tools`, `functions`, `manage`, `newPolicyForThisRoleOnly`."""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/access/roles/custom",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def start_marketplace_integration_sign_in(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/oauth/start — start the OAuth sign-in of an MCP connection; returns `authorizeUrl` (open it in a browser), `redirectUrl`, `expiresAt`."""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/oauth/start",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def sign_out_marketplace_integration(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/oauth/sign-out — sign an MCP connection out of OAuth; returns `wasSignedIn` and `revoke` (`Revoked`, `NoRevocationEndpoint`, `Failed` or None)."""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/oauth/sign-out",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def replace_marketplace_integration_secrets(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/marketplace/integrations/{IntegrationViewId}/secrets"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/secrets",
            method="PUT",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def reveal_marketplace_integration_secrets(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/secrets/reveal"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/secrets/reveal",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def set_marketplace_integration_token_mappings(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/marketplace/integrations/{IntegrationViewId}/token-mappings"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/token-mappings",
            method="PUT",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_function_catalog(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/catalog"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/catalog",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_function_runs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/functions/runs"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/functions/runs",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_functions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/functions"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/functions",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_function_qualifiers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/functions/qualifiers"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/functions/qualifiers",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def invoke_code_function(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/functions/invoke"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/functions/invoke",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_function_event_sample(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/functions/event-sample"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/functions/event-sample",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_function_runs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/functions/runs"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/functions/runs",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncCodeModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def disable_code(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/disable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_code(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/enable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_code_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/integrations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def confirm_code_integration_human_delivery(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/integrations/confirm-human-delivery"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/integrations/confirm-human-delivery",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_code_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/integrations/test"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/integrations/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_code_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/code/integrations/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_code_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/integrations/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_code_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/integrations/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/integrations/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_listings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/listings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/listings",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_listing_function_tokens(self, listing_view_id: str, function_key: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/listings/{ListingViewId}/functions/{FunctionKey}/tokens"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/listings/{ListingViewId}/functions/{FunctionKey}/tokens",
            method="GET",
            path_params={"ListingViewId": listing_view_id, "FunctionKey": function_key},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_integration(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_marketplace_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_marketplace_integration(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/code/marketplace/integrations/{IntegrationViewId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}",
            method="DELETE",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_marketplace_integration(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/enable",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_marketplace_integration(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/disable",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_functions(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/functions"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_function(self, integration_view_id: str, function_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id, "FunctionViewId": function_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_marketplace_function(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/functions"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_marketplace_function(self, integration_view_id: str, function_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}",
            method="DELETE",
            path_params={"IntegrationViewId": integration_view_id, "FunctionViewId": function_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_marketplace_function(self, integration_view_id: str, function_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/enable",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id, "FunctionViewId": function_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_marketplace_function(self, integration_view_id: str, function_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/disable",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id, "FunctionViewId": function_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_function_tokens(self, integration_view_id: str, function_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/tokens"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/tokens",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id, "FunctionViewId": function_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def invoke_marketplace_function(self, function_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/functions/{FunctionViewId}/invoke"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/functions/{FunctionViewId}/invoke",
            method="POST",
            path_params={"FunctionViewId": function_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_listing(self, listing_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/listings/{ListingViewId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/listings/{ListingViewId}",
            method="GET",
            path_params={"ListingViewId": listing_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_marketplace_integration(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/test"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/test",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_integration_tools(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/tools — the stored MCP tool catalog of a connection."""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/tools",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_integration_access(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/access — the access matrix of a connection: roles, packages, tools and functions."""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/access",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def set_marketplace_integration_role_access(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/marketplace/integrations/{IntegrationViewId}/access/roles — give a role one package (None, Viewer, FunctionsOnly, ReadOnly, FullAccess) and the Manage flag; body `roleId`, `package`, `manage`."""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/access/roles",
            method="PUT",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_marketplace_integration_custom_access(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/access/roles/custom — a custom access policy of the connection for one role; body `roleId`, `basePackage`, `tools`, `functions`, `manage`, `newPolicyForThisRoleOnly`."""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/access/roles/custom",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def start_marketplace_integration_sign_in(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/oauth/start — start the OAuth sign-in of an MCP connection; returns `authorizeUrl` (open it in a browser), `redirectUrl`, `expiresAt`."""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/oauth/start",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def sign_out_marketplace_integration(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/oauth/sign-out — sign an MCP connection out of OAuth; returns `wasSignedIn` and `revoke` (`Revoked`, `NoRevocationEndpoint`, `Failed` or None)."""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/oauth/sign-out",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def replace_marketplace_integration_secrets(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/marketplace/integrations/{IntegrationViewId}/secrets"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/secrets",
            method="PUT",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def reveal_marketplace_integration_secrets(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/secrets/reveal"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/secrets/reveal",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def set_marketplace_integration_token_mappings(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/marketplace/integrations/{IntegrationViewId}/token-mappings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/token-mappings",
            method="PUT",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_function_catalog(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/catalog"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/catalog",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_function_runs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/functions/runs"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/functions/runs",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_functions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/functions"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/functions",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_function_qualifiers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/functions/qualifiers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/functions/qualifiers",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def invoke_code_function(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/functions/invoke"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/functions/invoke",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_function_event_sample(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/functions/event-sample"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/functions/event-sample",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_function_runs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/functions/runs"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/functions/runs",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
