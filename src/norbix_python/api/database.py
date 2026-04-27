from __future__ import annotations

from typing import Any

from ..transport import Transport

class DatabaseModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def findTerms(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/taxonomies/{taxonomyName}/terms"""
        return self._transport.send(
            target='api',
            path='/{version}/database/taxonomies/{taxonomyName}/terms',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def findTermsChildren(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children"""
        return self._transport.send(
            target='api',
            path='/{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseSchema(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{id}"""
        return self._transport.send(
            target='api',
            path='/{version}/database/schemas/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseSchemas(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas"""
        return self._transport.send(
            target='api',
            path='/{version}/database/schemas',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def aggregate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/collections/{collectionName}/aggregate"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}/aggregate',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def changeResponsibility(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}/responsibility"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}/{id}/responsibility',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def count(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/collections/{collectionName}/count"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}/count',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteMany(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/collections/{collectionName}/many"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}/many',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteOne(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/collections/{collectionName}/{id}"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}/{id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def distinct(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/collections/{collectionName}/distinct"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}/distinct',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def executeAggregate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def find(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/collections/{collectionName}"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def findOne(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/collections/{collectionName}/{id}"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def insertMany(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/collections/{collectionName}/many"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}/many',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def insertOne(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/collections/{collectionName}"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def replaceOne(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}/replace"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}/{id}/replace',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateMany(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/collections/{collectionName}/many"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}/many',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateOne(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/collections/{collectionName}/{id}"""
        return self._transport.send(
            target='api',
            path='/{version}/database/collections/{collectionName}/{id}',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
