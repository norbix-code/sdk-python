from __future__ import annotations

from typing import Any

from ..transport import Transport

class DatabaseModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disableDatabase(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/disable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableDatabase(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/enable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteSchemaTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/schemas/triggers/{triggerId}"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/triggers/{triggerId}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableSchemaTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/database/schemas/triggers/{triggerId}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/triggers/{triggerId}/disable',
            method='PATCH',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableSchemaTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/database/schemas/triggers/{triggerId}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/triggers/{triggerId}/enable',
            method='PATCH',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getSchemaTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/triggers/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/triggers/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getSchemaTriggers(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/triggers"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/triggers',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveSchemaTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/schemas/triggers"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/triggers',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteDatabaseTaxonomy(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/taxonomies/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/taxonomies/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseTaxonomy(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/taxonomies/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/taxonomies/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseTaxonomies(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/taxonomies"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/taxonomies',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveDatabaseTaxonomy(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/taxonomies"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/taxonomies',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteDatabaseTaxonomyTerm(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteManyDatabaseTaxonomyTerms(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/taxonomies/{TaxonomyId}/terms/many"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/taxonomies/{TaxonomyId}/terms/many',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseTaxonomyTerm(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveDatabaseTaxonomyTerm(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/taxonomies/{TaxonomyId}/terms"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/taxonomies/{TaxonomyId}/terms',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateDatabaseTaxonomyTerm(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/taxonomies/{TaxonomyId}/terms/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteDatabaseSchema(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/schemas/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def discardDatabaseSchemaDraft(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/schemas/{Id}/draft"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/{Id}/draft',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseSchema(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{id}"""
        return self._transport.send(
            target='hub',
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
            target='hub',
            path='/{version}/database/schemas',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseSchemaDraft(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{Id}/draft"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/{Id}/draft',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseSchemaVersionDiff(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{Id}/versions/diff"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/{Id}/versions/diff',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseSchemaVersions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/schemas/{Id}/versions"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/{Id}/versions',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def publishDatabaseSchema(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/schemas/{Id}/publish"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/{Id}/publish',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def renameDatabaseSchema(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/schemas/{Id}/rename"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/{Id}/rename',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveDatabaseSchema(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/schemas"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateDatabaseSchemaDraft(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/schemas/{Id}/draft"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/{Id}/draft',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateDatabaseSchemaSettings(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/schemas/{Id}/settings"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/schemas/{Id}/settings',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteDatabaseIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/integrations/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/integrations/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableDatabaseIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/integrations/{Id}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/integrations/{Id}/disable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableDatabaseIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/integrations/{Id}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/integrations/{Id}/enable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/integrations/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/integrations/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseIntegrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/integrations',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveDatabaseIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/integrations',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def setDatabaseIntegrationAsDefault(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/database/integrations/{Id}/default"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/integrations/{Id}/default',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteDatabaseAggregate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/database/aggregates/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/aggregates/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseAggregate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/aggregates/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/aggregates/{Id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getDatabaseAggregates(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/database/aggregates"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/aggregates',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveDatabaseAggregate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/aggregates"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/aggregates',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def testDatabaseAggregate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/database/aggregates/test"""
        return self._transport.send(
            target='hub',
            path='/{version}/database/aggregates/test',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
