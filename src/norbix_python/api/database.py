from __future__ import annotations

import json
from typing import Any

from ..transport import AsyncTransport, Transport


class DatabaseModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def find_terms(self, taxonomy_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{taxonomyName}/terms"""
        return self._transport.send(
            target="api",
            path="/{version}/database/taxonomies/{taxonomyName}/terms",
            method="GET",
            path_params={"taxonomyName": taxonomy_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def find_terms_children(self, taxonomy_name: str, parent_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children"""
        return self._transport.send(
            target="api",
            path="/{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children",
            method="GET",
            path_params={"taxonomyName": taxonomy_name, "parentId": parent_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def find_term_tree(self, taxonomy_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{taxonomyName}/terms/tree"""
        return self._transport.send(
            target="api",
            path="/{version}/database/taxonomies/{taxonomyName}/terms/tree",
            method="GET",
            path_params={"taxonomyName": taxonomy_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def find_taxonomy_tree(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/tree"""
        return self._transport.send(
            target="api",
            path="/{version}/database/taxonomies/tree",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_database_schema(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/{id}"""
        return self._transport.send(
            target="api",
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
            target="api",
            path="/{version}/database/schemas",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def aggregate(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}/aggregate"""
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/aggregate",
            method="POST",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def change_responsibility(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}/responsibility"""
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/{id}/responsibility",
            method="PUT",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def count(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/count"""
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/count",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_many(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/collections/{collectionName}/many"""
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/many",
            method="DELETE",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_one(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/collections/{collectionName}/{id}"""
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/{id}",
            method="DELETE",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def distinct(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/distinct"""
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/distinct",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def execute_aggregate(self, collection_name: str, aggregate_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute"""
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute",
            method="POST",
            path_params={"collectionName": collection_name, "aggregateId": aggregate_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # HAND-WRITTEN keyword options (expand_references / array_filters) — keep on regeneration.
    def find(self, collection_name: str, *, expand_references: bool | None = None, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}

        ``expand_references=True`` returns every reference field (user, role,
        taxonomy term, record of another collection, file) as ``{"id", "display"}``
        — see ``norbix_python.ReferenceDisplay``. The caller needs read permission
        on every source the published schema links to, or the read is refused
        with ``CM-ERRORS-DATABASE-056``. Default ``False`` returns the stored ids.
        """
        if expand_references is not None:
            request["expandReferences"] = expand_references
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # HAND-WRITTEN keyword options (expand_references / array_filters) — keep on regeneration.
    def find_one(self, collection_name: str, id: str, *, expand_references: bool | None = None, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/{id}

        ``expand_references=True`` returns every reference field (user, role,
        taxonomy term, record of another collection, file) as ``{"id", "display"}``
        — see ``norbix_python.ReferenceDisplay``. The caller needs read permission
        on every source the published schema links to, or the read is refused
        with ``CM-ERRORS-DATABASE-056``. Default ``False`` returns the stored ids.
        """
        if expand_references is not None:
            request["expandReferences"] = expand_references
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/{id}",
            method="GET",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def insert_many(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}/many"""
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/many",
            method="POST",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def insert_one(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}"""
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}",
            method="POST",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def replace_one(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}/replace"""
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/{id}/replace",
            method="PUT",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # HAND-WRITTEN keyword options (expand_references / array_filters) — keep on regeneration.
    def update_many(self, collection_name: str, *, array_filters: str | list[dict[str, Any]] | None = None, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/many

        ``update`` keys may be nested paths (``"address.city"``, ``"lines.0.qty"``,
        ``"lines.$[].qty"``, ``"lines.$[line].qty"``). ``array_filters`` picks the
        list elements a ``$[name]`` path changes: one filter document per name,
        as a JSON string or a list of dicts (``[{"line.sku": "A-1"}]``).
        """
        if array_filters is not None:
            request["arrayFilters"] = array_filters if isinstance(array_filters, str) else json.dumps(array_filters)
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/many",
            method="PUT",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # HAND-WRITTEN keyword options (expand_references / array_filters) — keep on regeneration.
    def update_one(self, collection_name: str, id: str, *, array_filters: str | list[dict[str, Any]] | None = None, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}

        ``update`` keys may be nested paths (``"address.city"``, ``"lines.0.qty"``,
        ``"lines.$[].qty"``, ``"lines.$[line].qty"``). ``array_filters`` picks the
        list elements a ``$[name]`` path changes: one filter document per name,
        as a JSON string or a list of dicts (``[{"line.sku": "A-1"}]``).
        """
        if array_filters is not None:
            request["arrayFilters"] = array_filters if isinstance(array_filters, str) else json.dumps(array_filters)
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/{id}",
            method="PUT",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def find_merged_term_tree(self, taxonomy_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{taxonomyName}/merged-tree"""
        return self._transport.send(
            target="api",
            path="/{version}/database/taxonomies/{taxonomyName}/merged-tree",
            method="GET",
            path_params={"taxonomyName": taxonomy_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # HAND-WRITTEN keyword options (expand_references / array_filters) — keep on regeneration.
    def find_own(self, collection_name: str, *, expand_references: bool | None = None, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/own

        ``expand_references=True`` returns every reference field (user, role,
        taxonomy term, record of another collection, file) as ``{"id", "display"}``
        — see ``norbix_python.ReferenceDisplay``. The caller needs read permission
        on every source the published schema links to, or the read is refused
        with ``CM-ERRORS-DATABASE-056``. Default ``False`` returns the stored ids.
        """
        if expand_references is not None:
            request["expandReferences"] = expand_references
        return self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/own",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncDatabaseModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def find_terms(self, taxonomy_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{taxonomyName}/terms"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/taxonomies/{taxonomyName}/terms",
            method="GET",
            path_params={"taxonomyName": taxonomy_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def find_terms_children(self, taxonomy_name: str, parent_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children",
            method="GET",
            path_params={"taxonomyName": taxonomy_name, "parentId": parent_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def find_term_tree(self, taxonomy_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{taxonomyName}/terms/tree"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/taxonomies/{taxonomyName}/terms/tree",
            method="GET",
            path_params={"taxonomyName": taxonomy_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def find_taxonomy_tree(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/tree"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/taxonomies/tree",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_database_schema(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/schemas/{id}"""
        return await self._transport.send(
            target="api",
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
            target="api",
            path="/{version}/database/schemas",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def aggregate(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}/aggregate"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/aggregate",
            method="POST",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def change_responsibility(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}/responsibility"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/{id}/responsibility",
            method="PUT",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def count(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/count"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/count",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_many(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/collections/{collectionName}/many"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/many",
            method="DELETE",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_one(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/database/collections/{collectionName}/{id}"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/{id}",
            method="DELETE",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def distinct(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/distinct"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/distinct",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def execute_aggregate(self, collection_name: str, aggregate_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute",
            method="POST",
            path_params={"collectionName": collection_name, "aggregateId": aggregate_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # HAND-WRITTEN keyword options (expand_references / array_filters) — keep on regeneration.
    async def find(self, collection_name: str, *, expand_references: bool | None = None, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}

        ``expand_references=True`` returns every reference field (user, role,
        taxonomy term, record of another collection, file) as ``{"id", "display"}``
        — see ``norbix_python.ReferenceDisplay``. The caller needs read permission
        on every source the published schema links to, or the read is refused
        with ``CM-ERRORS-DATABASE-056``. Default ``False`` returns the stored ids.
        """
        if expand_references is not None:
            request["expandReferences"] = expand_references
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # HAND-WRITTEN keyword options (expand_references / array_filters) — keep on regeneration.
    async def find_one(self, collection_name: str, id: str, *, expand_references: bool | None = None, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/{id}

        ``expand_references=True`` returns every reference field (user, role,
        taxonomy term, record of another collection, file) as ``{"id", "display"}``
        — see ``norbix_python.ReferenceDisplay``. The caller needs read permission
        on every source the published schema links to, or the read is refused
        with ``CM-ERRORS-DATABASE-056``. Default ``False`` returns the stored ids.
        """
        if expand_references is not None:
            request["expandReferences"] = expand_references
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/{id}",
            method="GET",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def insert_many(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}/many"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/many",
            method="POST",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def insert_one(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/database/collections/{collectionName}"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}",
            method="POST",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def replace_one(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}/replace"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/{id}/replace",
            method="PUT",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # HAND-WRITTEN keyword options (expand_references / array_filters) — keep on regeneration.
    async def update_many(self, collection_name: str, *, array_filters: str | list[dict[str, Any]] | None = None, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/many

        ``update`` keys may be nested paths (``"address.city"``, ``"lines.0.qty"``,
        ``"lines.$[].qty"``, ``"lines.$[line].qty"``). ``array_filters`` picks the
        list elements a ``$[name]`` path changes: one filter document per name,
        as a JSON string or a list of dicts (``[{"line.sku": "A-1"}]``).
        """
        if array_filters is not None:
            request["arrayFilters"] = array_filters if isinstance(array_filters, str) else json.dumps(array_filters)
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/many",
            method="PUT",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # HAND-WRITTEN keyword options (expand_references / array_filters) — keep on regeneration.
    async def update_one(self, collection_name: str, id: str, *, array_filters: str | list[dict[str, Any]] | None = None, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}

        ``update`` keys may be nested paths (``"address.city"``, ``"lines.0.qty"``,
        ``"lines.$[].qty"``, ``"lines.$[line].qty"``). ``array_filters`` picks the
        list elements a ``$[name]`` path changes: one filter document per name,
        as a JSON string or a list of dicts (``[{"line.sku": "A-1"}]``).
        """
        if array_filters is not None:
            request["arrayFilters"] = array_filters if isinstance(array_filters, str) else json.dumps(array_filters)
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/{id}",
            method="PUT",
            path_params={"collectionName": collection_name, "id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def find_merged_term_tree(self, taxonomy_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/taxonomies/{taxonomyName}/merged-tree"""
        return await self._transport.send(
            target="api",
            path="/{version}/database/taxonomies/{taxonomyName}/merged-tree",
            method="GET",
            path_params={"taxonomyName": taxonomy_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # HAND-WRITTEN keyword options (expand_references / array_filters) — keep on regeneration.
    async def find_own(self, collection_name: str, *, expand_references: bool | None = None, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/own

        ``expand_references=True`` returns every reference field (user, role,
        taxonomy term, record of another collection, file) as ``{"id", "display"}``
        — see ``norbix_python.ReferenceDisplay``. The caller needs read permission
        on every source the published schema links to, or the read is refused
        with ``CM-ERRORS-DATABASE-056``. Default ``False`` returns the stored ids.
        """
        if expand_references is not None:
            request["expandReferences"] = expand_references
        return await self._transport.send(
            target="api",
            path="/{version}/database/collections/{collectionName}/own",
            method="GET",
            path_params={"collectionName": collection_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
