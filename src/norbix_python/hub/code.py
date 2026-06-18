from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class CodeModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disable_code(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/disable",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_code(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/enable",
            method="GET",
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

    def set_code_integration_as_default(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/integrations/{Id}/default"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/integrations/{Id}/default",
            method="PUT",
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

    def get_marketplace_bindings(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_marketplace_function_binding(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_marketplace_function_binding(self, integration_view_id: str, binding_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}",
            method="DELETE",
            path_params={"IntegrationViewId": integration_view_id, "BindingViewId": binding_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_binding(self, integration_view_id: str, binding_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id, "BindingViewId": binding_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_marketplace_function_binding(self, integration_view_id: str, binding_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/disable",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id, "BindingViewId": binding_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_marketplace_function_binding(self, integration_view_id: str, binding_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/enable",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id, "BindingViewId": binding_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def invoke_marketplace_function_binding(self, integration_view_id: str, binding_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/invoke"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/invoke",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id, "BindingViewId": binding_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_marketplace_binding_tokens(self, integration_view_id: str, binding_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/tokens"""
        return self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/tokens",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id, "BindingViewId": binding_view_id},
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

    def get_marketplace_function_catalog(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
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


class AsyncCodeModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def disable_code(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/disable",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_code(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/enable",
            method="GET",
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

    async def set_code_integration_as_default(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/code/integrations/{Id}/default"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/integrations/{Id}/default",
            method="PUT",
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

    async def get_marketplace_bindings(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_marketplace_function_binding(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_marketplace_function_binding(self, integration_view_id: str, binding_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}",
            method="DELETE",
            path_params={"IntegrationViewId": integration_view_id, "BindingViewId": binding_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_binding(self, integration_view_id: str, binding_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id, "BindingViewId": binding_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_marketplace_function_binding(self, integration_view_id: str, binding_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/disable",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id, "BindingViewId": binding_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_marketplace_function_binding(self, integration_view_id: str, binding_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/enable",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id, "BindingViewId": binding_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def invoke_marketplace_function_binding(self, integration_view_id: str, binding_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/invoke"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/invoke",
            method="POST",
            path_params={"IntegrationViewId": integration_view_id, "BindingViewId": binding_view_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_marketplace_binding_tokens(self, integration_view_id: str, binding_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/tokens"""
        return await self._transport.send(
            target="hub",
            path="/{version}/code/marketplace/integrations/{IntegrationViewId}/bindings/{BindingViewId}/tokens",
            method="GET",
            path_params={"IntegrationViewId": integration_view_id, "BindingViewId": binding_view_id},
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

    async def get_marketplace_function_catalog(self, integration_view_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
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
