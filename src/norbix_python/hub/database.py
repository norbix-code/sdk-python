from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class DatabaseModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disable_database(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/disable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_database(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/enable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_schema_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/schemas/triggers/{triggerId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{triggerId}",
            method="DELETE",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_schema_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/database/schemas/triggers/{triggerId}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{triggerId}/disable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_schema_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/database/schemas/triggers/{triggerId}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{triggerId}/enable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_schema_trigger(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/triggers/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_schema_triggers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/triggers"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_schema_trigger(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/schemas/triggers"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_database_taxonomy(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/taxonomies/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_taxonomy(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_taxonomies(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_database_taxonomy(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/taxonomies"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_database_taxonomy_term(self, taxonomy_id: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}",
            method="DELETE",
            path_params={"TaxonomyId": taxonomy_id, "Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_many_database_taxonomy_terms(self, taxonomy_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/taxonomies/{TaxonomyId}/terms/many"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/many",
            method="DELETE",
            path_params={"TaxonomyId": taxonomy_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_taxonomy_term(self, taxonomy_id: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}",
            method="GET",
            path_params={"TaxonomyId": taxonomy_id, "Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_database_taxonomy_term(self, taxonomy_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/taxonomies/{TaxonomyId}/terms"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms",
            method="POST",
            path_params={"TaxonomyId": taxonomy_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_database_taxonomy_term(self, taxonomy_id: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}",
            method="PUT",
            path_params={"TaxonomyId": taxonomy_id, "Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_database_schema(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/schemas/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def discard_database_schema_draft(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/schemas/{Id}/draft"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/draft",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_schema(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_schemas(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_schema_draft(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/{Id}/draft"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/draft",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_schema_version_diff(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/{Id}/versions/diff"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/versions/diff",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_schema_versions(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/{Id}/versions"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/versions",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def publish_database_schema(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/schemas/{Id}/publish"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/publish",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def rename_database_schema(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/schemas/{Id}/rename"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/rename",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_database_schema(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/schemas"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_database_schema_draft(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/schemas/{Id}/draft"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/draft",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_database_schema_settings(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/schemas/{Id}/settings"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/settings",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_database_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/integrations/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_database_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/integrations/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_database_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/integrations/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/integrations/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_database_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def set_database_integration_as_default(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/integrations/{Id}/default"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/default",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_database_aggregate(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/aggregates/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/aggregates/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_aggregate(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/aggregates/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/aggregates/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_aggregates(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/aggregates"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/aggregates",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_database_aggregate(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/aggregates"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/aggregates",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_database_aggregate(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/aggregates/test"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/aggregates/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_collection_import(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/imports"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/imports",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_collection_imports(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/imports"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/imports",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_collection_import(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/imports/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/imports/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_collection_import(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/imports/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/imports/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def request_import_upload_url(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/imports/upload-url"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/imports/upload-url",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def analyze_import_file(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/imports/analyze"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/imports/analyze",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_allowed_flex_tiers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/integrations/flex-tiers"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/flex-tiers",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_database_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/integrations/test"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def reveal_managed_flex_connection_string(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/integrations/{Id}/connection-string"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/connection-string",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_taxonomy_tree(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/tree"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/tree",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_merged_term_tree(self, taxonomy_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{TaxonomyName}/merged-tree"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyName}/merged-tree",
            method="GET",
            path_params={"TaxonomyName": taxonomy_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_taxonomy_term_tree(self, taxonomy_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{TaxonomyName}/terms/tree"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyName}/terms/tree",
            method="GET",
            path_params={"TaxonomyName": taxonomy_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def apply_database_schema_bundle(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/schemas/apply-bundle"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/apply-bundle",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_schema_list_settings(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/{Id}/list-settings"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/list-settings",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_database_schema_list_settings(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/schemas/{Id}/list-settings"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/list-settings",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_database_schema_embed(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/schemas/{Id}/embed"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/embed",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def aggregate_records(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}/aggregate"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/aggregate",
            method="POST",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def change_record_responsibility(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}/responsibility"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/{id}/responsibility",
            method="PUT",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def count_records(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/count"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/count",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_many_records(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/collections/{collectionName}/many"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/many",
            method="DELETE",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_record(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/collections/{collectionName}/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/{id}",
            method="DELETE",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def distinct_record_values(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/distinct"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/distinct",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def execute_records_aggregate(self, collection_name: str, aggregate_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute",
            method="POST",
            path_params={"collectionName": collection_name, "aggregateId": aggregate_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def find_records(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def find_one_record(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/{id}",
            method="GET",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_collection_indexes(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/indexes"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/indexes",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def insert_many_records(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}/many"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/many",
            method="POST",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def insert_record(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}",
            method="POST",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def replace_record(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}/replace"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/{id}/replace",
            method="PUT",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def seed_collection_records(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/seed"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/seed",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_many_records(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/many"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/many",
            method="PUT",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_one_record(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/{id}",
            method="PUT",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncDatabaseModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def disable_database(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/disable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_database(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/enable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_schema_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/schemas/triggers/{triggerId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{triggerId}",
            method="DELETE",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_schema_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/database/schemas/triggers/{triggerId}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{triggerId}/disable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_schema_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/database/schemas/triggers/{triggerId}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{triggerId}/enable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_schema_trigger(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/triggers/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_schema_triggers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/triggers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_schema_trigger(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/schemas/triggers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/triggers",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_database_taxonomy(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/taxonomies/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_taxonomy(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_taxonomies(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_database_taxonomy(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/taxonomies"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_database_taxonomy_term(self, taxonomy_id: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}",
            method="DELETE",
            path_params={"TaxonomyId": taxonomy_id, "Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_many_database_taxonomy_terms(self, taxonomy_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/taxonomies/{TaxonomyId}/terms/many"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/many",
            method="DELETE",
            path_params={"TaxonomyId": taxonomy_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_taxonomy_term(self, taxonomy_id: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}",
            method="GET",
            path_params={"TaxonomyId": taxonomy_id, "Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_database_taxonomy_term(self, taxonomy_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/taxonomies/{TaxonomyId}/terms"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms",
            method="POST",
            path_params={"TaxonomyId": taxonomy_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_database_taxonomy_term(self, taxonomy_id: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}",
            method="PUT",
            path_params={"TaxonomyId": taxonomy_id, "Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_database_schema(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/schemas/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def discard_database_schema_draft(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/schemas/{Id}/draft"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/draft",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_schema(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_schemas(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_schema_draft(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/{Id}/draft"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/draft",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_schema_version_diff(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/{Id}/versions/diff"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/versions/diff",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_schema_versions(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/{Id}/versions"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/versions",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def publish_database_schema(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/schemas/{Id}/publish"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/publish",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def rename_database_schema(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/schemas/{Id}/rename"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/rename",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_database_schema(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/schemas"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_database_schema_draft(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/schemas/{Id}/draft"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/draft",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_database_schema_settings(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/schemas/{Id}/settings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/settings",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_database_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/integrations/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_database_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/integrations/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_database_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/integrations/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/integrations/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_database_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def set_database_integration_as_default(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/integrations/{Id}/default"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/default",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_database_aggregate(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/aggregates/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/aggregates/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_aggregate(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/aggregates/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/aggregates/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_aggregates(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/aggregates"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/aggregates",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_database_aggregate(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/aggregates"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/aggregates",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_database_aggregate(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/aggregates/test"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/aggregates/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_collection_import(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/imports"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/imports",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_collection_imports(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/imports"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/imports",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_collection_import(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/imports/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/imports/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_collection_import(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/imports/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/imports/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def request_import_upload_url(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/imports/upload-url"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/imports/upload-url",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def analyze_import_file(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/imports/analyze"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/imports/analyze",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_allowed_flex_tiers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/integrations/flex-tiers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/flex-tiers",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_database_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/integrations/test"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def reveal_managed_flex_connection_string(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/integrations/{Id}/connection-string"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/integrations/{Id}/connection-string",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_taxonomy_tree(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/tree"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/tree",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_merged_term_tree(self, taxonomy_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{TaxonomyName}/merged-tree"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyName}/merged-tree",
            method="GET",
            path_params={"TaxonomyName": taxonomy_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_taxonomy_term_tree(self, taxonomy_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{TaxonomyName}/terms/tree"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/taxonomies/{TaxonomyName}/terms/tree",
            method="GET",
            path_params={"TaxonomyName": taxonomy_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def apply_database_schema_bundle(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/schemas/apply-bundle"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/apply-bundle",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_schema_list_settings(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/{Id}/list-settings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/list-settings",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_database_schema_list_settings(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/schemas/{Id}/list-settings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/list-settings",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_database_schema_embed(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/schemas/{Id}/embed"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/schemas/{Id}/embed",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def aggregate_records(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}/aggregate"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/aggregate",
            method="POST",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def change_record_responsibility(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}/responsibility"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/{id}/responsibility",
            method="PUT",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def count_records(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/count"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/count",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_many_records(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/collections/{collectionName}/many"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/many",
            method="DELETE",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_record(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/collections/{collectionName}/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/{id}",
            method="DELETE",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def distinct_record_values(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/distinct"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/distinct",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def execute_records_aggregate(self, collection_name: str, aggregate_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute",
            method="POST",
            path_params={"collectionName": collection_name, "aggregateId": aggregate_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def find_records(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def find_one_record(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/{id}",
            method="GET",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_collection_indexes(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/indexes"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/indexes",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def insert_many_records(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}/many"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/many",
            method="POST",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def insert_record(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}",
            method="POST",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def replace_record(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}/replace"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/{id}/replace",
            method="PUT",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def seed_collection_records(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/seed"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/seed",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_many_records(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/many"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/many",
            method="PUT",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_one_record(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/database/collections/{collectionName}/{id}",
            method="PUT",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
