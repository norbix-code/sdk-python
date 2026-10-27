from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport
from ..workflows import WorkflowRun, wait_for_run, wait_for_run_async


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

    # --- Workflows (beta) ---------------------------------------------------
    # The routes of the gateway contract Code.Workflows.md §7. Workflows are in
    # beta; bugs may occur.

    def get_code_workflows(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows

        List the workflows; query `isEnabled?`, `pageSize`, `startingAfter`, `endingBefore`.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_code_workflow(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: PUT /{version}/code/workflows

        Save the draft (create when `definition.workflowId` is absent); body `definition`.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/{Id}

        One workflow (latest published, or the draft when never published); query `pinnedVersion?`.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: DELETE /{version}/code/workflows/{Id}

        Delete a workflow; waiting runs are cancelled.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def publish_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/{Id}/publish

        The draft becomes the next published version.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/publish",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_workflow_draft(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/{Id}/draft

        The workflow with its draft as `definition`.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/draft",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def discard_code_workflow_draft(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: DELETE /{version}/code/workflows/{Id}/draft

        Discard the draft.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/draft",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_workflow_versions(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/{Id}/versions

        The published versions of a workflow.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/versions",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_workflow_version_diff(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/{Id}/versions/diff

        What changed between two versions; query `fromVersion`, `toVersion`.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/versions/diff",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: PUT /{version}/code/workflows/{Id}/enable

        Enable a workflow (resets the runaway counters).
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: PUT /{version}/code/workflows/{Id}/disable

        Disable a workflow: no new runs; runs in flight continue.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def invoke_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/{Id}/invoke

        Start a run; body `payload?`, `waitSeconds?` (0–30), `runVersion?` ("draft" or a version).
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/invoke",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_workflow_runs(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/{Id}/runs

        Runs of a workflow, newest first; query `status?`, `from?`, `to?` and paging.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/runs",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def resume_code_workflow_run_by_key(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/{Id}/resume

        Resume the run waiting on `key`; body `key`, `stepId?`, `decision?`, `payload?`.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/resume",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def validate_code_workflow(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/validate

        Run every save check, write nothing; body `definition`.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/validate",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_workflow_schema(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/schema

        The definition JSON Schema, the step kinds and the binding families.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/schema",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_code_workflows(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: PUT /{version}/code/workflows/enable

        Turn the Workflows beta switch on for the Code module.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/enable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_code_workflows(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: PUT /{version}/code/workflows/disable

        Turn the Workflows beta switch off for the Code module.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/disable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_workflow_waiting_runs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/runs

        The inbox of waiting runs; query `status?`, `waitingKind?`, `assignee?`, `workflowId?`, `key?`, paging.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/runs",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_workflow_run(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/runs/{RunId}

        One run with its steps (`{"run": {...}}`).
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/runs/{RunId}",
            method="GET",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_workflow_run_logs(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/runs/{RunId}/logs

        The run's log lines, newest first; query `stepId?`, `level?` and paging.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/runs/{RunId}/logs",
            method="GET",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def resume_code_workflow_run(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/runs/{RunId}/resume

        Resume a waiting run; body `stepId?`, `decision?` ("approved" / "rejected"), `payload?`.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/runs/{RunId}/resume",
            method="POST",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def retry_code_workflow_run_step(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/runs/{RunId}/retry

        Retry the failed step of a failed run; body `stepId?`.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/runs/{RunId}/retry",
            method="POST",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def cancel_code_workflow_run(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/runs/{RunId}/cancel

        Stop a running or waiting run; body `reason?`.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/runs/{RunId}/cancel",
            method="POST",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def open_code_workflow_resume_link(self, token: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/resume/{Token}

        Check a signed resume link (changes nothing). No session needed: the link is the key;
        auth is still sent when the client has a token.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/resume/{Token}",
            method="GET",
            path_params={"Token": token},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def use_code_workflow_resume_link(self, token: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/resume/{Token}

        Answer a signed resume link. No session needed: the link is the key; auth is still
        sent when the client has a token.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/code/workflows/resume/{Token}",
            method="POST",
            path_params={"Token": token},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def wait_for_run(self, run_id: str, *, timeout_ms: int = 60000, poll_ms: int = 1000, timeout: float | None = None, bearer_token: str | None = None) -> WorkflowRun:
        """Beta: poll ``get_code_workflow_run`` until the run is settled.

        Gives back the run (a :class:`~norbix_python.WorkflowRun`) as soon as its
        ``status`` is ``succeeded``, ``failed``, ``cancelled`` or ``waiting``.
        Raises :class:`~norbix_python.WorkflowRunTimeoutError` (``.run`` = the
        last run read) after ``timeout_ms``, and ``NorbixError`` when an answer
        carries no run. ``timeout`` and ``bearer_token`` apply to each poll.
        """
        return wait_for_run(
            lambda: self.get_code_workflow_run(run_id, timeout=timeout, bearer_token=bearer_token),
            timeout_ms=timeout_ms,
            poll_ms=poll_ms,
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

    # --- Workflows (beta) ---------------------------------------------------
    # The routes of the gateway contract Code.Workflows.md §7. Workflows are in
    # beta; bugs may occur.

    async def get_code_workflows(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows

        List the workflows; query `isEnabled?`, `pageSize`, `startingAfter`, `endingBefore`.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_code_workflow(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: PUT /{version}/code/workflows

        Save the draft (create when `definition.workflowId` is absent); body `definition`.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/{Id}

        One workflow (latest published, or the draft when never published); query `pinnedVersion?`.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: DELETE /{version}/code/workflows/{Id}

        Delete a workflow; waiting runs are cancelled.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def publish_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/{Id}/publish

        The draft becomes the next published version.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/publish",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_workflow_draft(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/{Id}/draft

        The workflow with its draft as `definition`.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/draft",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def discard_code_workflow_draft(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: DELETE /{version}/code/workflows/{Id}/draft

        Discard the draft.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/draft",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_workflow_versions(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/{Id}/versions

        The published versions of a workflow.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/versions",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_workflow_version_diff(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/{Id}/versions/diff

        What changed between two versions; query `fromVersion`, `toVersion`.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/versions/diff",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: PUT /{version}/code/workflows/{Id}/enable

        Enable a workflow (resets the runaway counters).
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: PUT /{version}/code/workflows/{Id}/disable

        Disable a workflow: no new runs; runs in flight continue.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def invoke_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/{Id}/invoke

        Start a run; body `payload?`, `waitSeconds?` (0–30), `runVersion?` ("draft" or a version).
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/invoke",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_workflow_runs(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/{Id}/runs

        Runs of a workflow, newest first; query `status?`, `from?`, `to?` and paging.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/runs",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def resume_code_workflow_run_by_key(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/{Id}/resume

        Resume the run waiting on `key`; body `key`, `stepId?`, `decision?`, `payload?`.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/{Id}/resume",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def validate_code_workflow(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/validate

        Run every save check, write nothing; body `definition`.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/validate",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_workflow_schema(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/schema

        The definition JSON Schema, the step kinds and the binding families.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/schema",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_code_workflows(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: PUT /{version}/code/workflows/enable

        Turn the Workflows beta switch on for the Code module.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/enable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_code_workflows(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: PUT /{version}/code/workflows/disable

        Turn the Workflows beta switch off for the Code module.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/disable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_workflow_waiting_runs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/runs

        The inbox of waiting runs; query `status?`, `waitingKind?`, `assignee?`, `workflowId?`, `key?`, paging.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/runs",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_workflow_run(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/runs/{RunId}

        One run with its steps (`{"run": {...}}`).
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/runs/{RunId}",
            method="GET",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_workflow_run_logs(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/runs/{RunId}/logs

        The run's log lines, newest first; query `stepId?`, `level?` and paging.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/runs/{RunId}/logs",
            method="GET",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def resume_code_workflow_run(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/runs/{RunId}/resume

        Resume a waiting run; body `stepId?`, `decision?` ("approved" / "rejected"), `payload?`.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/runs/{RunId}/resume",
            method="POST",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def retry_code_workflow_run_step(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/runs/{RunId}/retry

        Retry the failed step of a failed run; body `stepId?`.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/runs/{RunId}/retry",
            method="POST",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def cancel_code_workflow_run(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/runs/{RunId}/cancel

        Stop a running or waiting run; body `reason?`.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/runs/{RunId}/cancel",
            method="POST",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def open_code_workflow_resume_link(self, token: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/resume/{Token}

        Check a signed resume link (changes nothing). No session needed: the link is the key;
        auth is still sent when the client has a token.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/resume/{Token}",
            method="GET",
            path_params={"Token": token},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def use_code_workflow_resume_link(self, token: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/resume/{Token}

        Answer a signed resume link. No session needed: the link is the key; auth is still
        sent when the client has a token.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/code/workflows/resume/{Token}",
            method="POST",
            path_params={"Token": token},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def wait_for_run(self, run_id: str, *, timeout_ms: int = 60000, poll_ms: int = 1000, timeout: float | None = None, bearer_token: str | None = None) -> WorkflowRun:
        """Beta: poll ``get_code_workflow_run`` until the run is settled.

        Gives back the run (a :class:`~norbix_python.WorkflowRun`) as soon as its
        ``status`` is ``succeeded``, ``failed``, ``cancelled`` or ``waiting``.
        Raises :class:`~norbix_python.WorkflowRunTimeoutError` (``.run`` = the
        last run read) after ``timeout_ms``, and ``NorbixError`` when an answer
        carries no run. ``timeout`` and ``bearer_token`` apply to each poll.
        """
        return await wait_for_run_async(
            lambda: self.get_code_workflow_run(run_id, timeout=timeout, bearer_token=bearer_token),
            timeout_ms=timeout_ms,
            poll_ms=poll_ms,
        )
