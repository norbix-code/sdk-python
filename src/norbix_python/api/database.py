from __future__ import annotations

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

    def find(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}"""
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

    def find_one(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/{id}"""
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

    def update_many(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/many"""
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

    def update_one(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}"""
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

    async def find(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}"""
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

    async def find_one(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/database/collections/{collectionName}/{id}"""
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

    async def update_many(self, collection_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/many"""
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

    async def update_one(self, collection_name: str, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}"""
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
