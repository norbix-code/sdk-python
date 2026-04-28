from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

class DatabaseModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disable_database(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/disable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_database(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/enable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_schema_trigger(self, trigger_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/schemas/triggers/{triggerId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{triggerId}",
            method="DELETE",
            path_params={"triggerId": trigger_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_schema_trigger(self, trigger_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/database/schemas/triggers/{triggerId}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{triggerId}/disable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_schema_trigger(self, trigger_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/database/schemas/triggers/{triggerId}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{triggerId}/enable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_schema_trigger(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/triggers/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_schema_triggers(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/triggers"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_schema_trigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/schemas/triggers"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_database_taxonomy(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/taxonomies/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_taxonomy(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/taxonomies/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_taxonomies(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/taxonomies"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_database_taxonomy(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/taxonomies"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_database_taxonomy_term(self, taxonomy_id: str, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}",
            method="DELETE",
            path_params={"TaxonomyId": taxonomy_id, "Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_many_database_taxonomy_terms(self, taxonomy_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/taxonomies/{TaxonomyId}/terms/many"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/many",
            method="DELETE",
            path_params={"TaxonomyId": taxonomy_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_taxonomy_term(self, taxonomy_id: str, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}",
            method="GET",
            path_params={"TaxonomyId": taxonomy_id, "Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_database_taxonomy_term(self, taxonomy_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/taxonomies/{TaxonomyId}/terms"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms",
            method="POST",
            path_params={"TaxonomyId": taxonomy_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_database_taxonomy_term(self, taxonomy_id: str, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}",
            method="PUT",
            path_params={"TaxonomyId": taxonomy_id, "Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_database_schema(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/schemas/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def discard_database_schema_draft(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/schemas/{Id}/draft"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/draft",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_schema(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_schemas(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_schema_draft(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{Id}/draft"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/draft",
            method="GET",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_schema_version_diff(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{Id}/versions/diff"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/versions/diff",
            method="GET",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_schema_versions(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{Id}/versions"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/versions",
            method="GET",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def publish_database_schema(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/schemas/{Id}/publish"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/publish",
            method="POST",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def rename_database_schema(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/schemas/{Id}/rename"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/rename",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_database_schema(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/schemas"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_database_schema_draft(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/schemas/{Id}/draft"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/draft",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_database_schema_settings(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/schemas/{Id}/settings"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/settings",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_database_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/integrations/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_database_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/integrations/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_database_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/integrations/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/integrations/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_integrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_database_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def set_database_integration_as_default(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/integrations/{Id}/default"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/default",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_database_aggregate(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/aggregates/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/aggregates/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_aggregate(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/aggregates/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/aggregates/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_aggregates(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/aggregates"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/aggregates",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_database_aggregate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/aggregates"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/aggregates",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_database_aggregate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/aggregates/test"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/aggregates/test",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncDatabaseModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def disable_database(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/disable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_database(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/enable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_schema_trigger(self, trigger_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/schemas/triggers/{triggerId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{triggerId}",
            method="DELETE",
            path_params={"triggerId": trigger_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_schema_trigger(self, trigger_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/database/schemas/triggers/{triggerId}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{triggerId}/disable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_schema_trigger(self, trigger_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/database/schemas/triggers/{triggerId}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{triggerId}/enable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_schema_trigger(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/triggers/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_schema_triggers(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/triggers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_schema_trigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/schemas/triggers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_database_taxonomy(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/taxonomies/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_taxonomy(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/taxonomies/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_taxonomies(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/taxonomies"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_database_taxonomy(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/taxonomies"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_database_taxonomy_term(self, taxonomy_id: str, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}",
            method="DELETE",
            path_params={"TaxonomyId": taxonomy_id, "Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_many_database_taxonomy_terms(self, taxonomy_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/taxonomies/{TaxonomyId}/terms/many"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/many",
            method="DELETE",
            path_params={"TaxonomyId": taxonomy_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_taxonomy_term(self, taxonomy_id: str, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}",
            method="GET",
            path_params={"TaxonomyId": taxonomy_id, "Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_database_taxonomy_term(self, taxonomy_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/taxonomies/{TaxonomyId}/terms"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms",
            method="POST",
            path_params={"TaxonomyId": taxonomy_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_database_taxonomy_term(self, taxonomy_id: str, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}",
            method="PUT",
            path_params={"TaxonomyId": taxonomy_id, "Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_database_schema(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/schemas/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def discard_database_schema_draft(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/schemas/{Id}/draft"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/draft",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_schema(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_schemas(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_schema_draft(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{Id}/draft"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/draft",
            method="GET",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_schema_version_diff(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{Id}/versions/diff"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/versions/diff",
            method="GET",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_schema_versions(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{Id}/versions"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/versions",
            method="GET",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def publish_database_schema(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/schemas/{Id}/publish"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/publish",
            method="POST",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def rename_database_schema(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/schemas/{Id}/rename"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/rename",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_database_schema(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/schemas"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_database_schema_draft(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/schemas/{Id}/draft"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/draft",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_database_schema_settings(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/schemas/{Id}/settings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/settings",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_database_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/integrations/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_database_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/integrations/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_database_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/integrations/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/integrations/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_integrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_database_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def set_database_integration_as_default(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/integrations/{Id}/default"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/default",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_database_aggregate(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/aggregates/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/aggregates/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_aggregate(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/aggregates/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/aggregates/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_aggregates(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/aggregates"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/aggregates",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_database_aggregate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/aggregates"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/aggregates",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_database_aggregate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/aggregates/test"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/aggregates/test",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
