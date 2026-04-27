from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_hub_database_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.database
    assert callable(module.disableDatabase)
    assert callable(module.enableDatabase)
    assert callable(module.deleteSchemaTrigger)
    assert callable(module.disableSchemaTrigger)
    assert callable(module.enableSchemaTrigger)
    assert callable(module.getSchemaTrigger)
    assert callable(module.getSchemaTriggers)
    assert callable(module.saveSchemaTrigger)
    assert callable(module.deleteDatabaseTaxonomy)
    assert callable(module.getDatabaseTaxonomy)
    assert callable(module.getDatabaseTaxonomies)
    assert callable(module.saveDatabaseTaxonomy)
    assert callable(module.deleteDatabaseTaxonomyTerm)
    assert callable(module.deleteManyDatabaseTaxonomyTerms)
    assert callable(module.getDatabaseTaxonomyTerm)
    assert callable(module.saveDatabaseTaxonomyTerm)
    assert callable(module.updateDatabaseTaxonomyTerm)
    assert callable(module.deleteDatabaseSchema)
    assert callable(module.discardDatabaseSchemaDraft)
    assert callable(module.getDatabaseSchema)
    assert callable(module.getDatabaseSchemas)
    assert callable(module.getDatabaseSchemaDraft)
    assert callable(module.getDatabaseSchemaVersionDiff)
    assert callable(module.getDatabaseSchemaVersions)
    assert callable(module.publishDatabaseSchema)
    assert callable(module.renameDatabaseSchema)
    assert callable(module.saveDatabaseSchema)
    assert callable(module.updateDatabaseSchemaDraft)
    assert callable(module.updateDatabaseSchemaSettings)
    assert callable(module.deleteDatabaseIntegration)
    assert callable(module.disableDatabaseIntegration)
    assert callable(module.enableDatabaseIntegration)
    assert callable(module.getDatabaseIntegration)
    assert callable(module.getDatabaseIntegrations)
    assert callable(module.saveDatabaseIntegration)
    assert callable(module.setDatabaseIntegrationAsDefault)
    assert callable(module.deleteDatabaseAggregate)
    assert callable(module.getDatabaseAggregate)
    assert callable(module.getDatabaseAggregates)
    assert callable(module.saveDatabaseAggregate)
    assert callable(module.testDatabaseAggregate)


def test_hub_database_disableDatabase_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/disable') if False else {}
    client.hub.database.disableDatabase(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_enableDatabase_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/enable') if False else {}
    client.hub.database.enableDatabase(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_deleteSchemaTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/triggers/{triggerId}') if True else {}
    client.hub.database.deleteSchemaTrigger(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_disableSchemaTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/triggers/{triggerId}/disable') if True else {}
    client.hub.database.disableSchemaTrigger(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_enableSchemaTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/triggers/{triggerId}/enable') if True else {}
    client.hub.database.enableSchemaTrigger(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getSchemaTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/triggers/{id}') if True else {}
    client.hub.database.getSchemaTrigger(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getSchemaTriggers_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/triggers') if False else {}
    client.hub.database.getSchemaTriggers(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_saveSchemaTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/triggers') if False else {}
    client.hub.database.saveSchemaTrigger(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_deleteDatabaseTaxonomy_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/taxonomies/{Id}') if True else {}
    client.hub.database.deleteDatabaseTaxonomy(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getDatabaseTaxonomy_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/taxonomies/{id}') if True else {}
    client.hub.database.getDatabaseTaxonomy(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getDatabaseTaxonomies_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/taxonomies') if False else {}
    client.hub.database.getDatabaseTaxonomies(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_saveDatabaseTaxonomy_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/taxonomies') if False else {}
    client.hub.database.saveDatabaseTaxonomy(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_deleteDatabaseTaxonomyTerm_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}') if True else {}
    client.hub.database.deleteDatabaseTaxonomyTerm(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_deleteManyDatabaseTaxonomyTerms_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/taxonomies/{TaxonomyId}/terms/many') if True else {}
    client.hub.database.deleteManyDatabaseTaxonomyTerms(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getDatabaseTaxonomyTerm_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}') if True else {}
    client.hub.database.getDatabaseTaxonomyTerm(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_saveDatabaseTaxonomyTerm_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/taxonomies/{TaxonomyId}/terms') if True else {}
    client.hub.database.saveDatabaseTaxonomyTerm(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_updateDatabaseTaxonomyTerm_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}') if True else {}
    client.hub.database.updateDatabaseTaxonomyTerm(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_deleteDatabaseSchema_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/{Id}') if True else {}
    client.hub.database.deleteDatabaseSchema(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_discardDatabaseSchemaDraft_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/{Id}/draft') if True else {}
    client.hub.database.discardDatabaseSchemaDraft(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getDatabaseSchema_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/{id}') if True else {}
    client.hub.database.getDatabaseSchema(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getDatabaseSchemas_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas') if False else {}
    client.hub.database.getDatabaseSchemas(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getDatabaseSchemaDraft_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/{Id}/draft') if True else {}
    client.hub.database.getDatabaseSchemaDraft(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getDatabaseSchemaVersionDiff_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/{Id}/versions/diff') if True else {}
    client.hub.database.getDatabaseSchemaVersionDiff(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getDatabaseSchemaVersions_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/{Id}/versions') if True else {}
    client.hub.database.getDatabaseSchemaVersions(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_publishDatabaseSchema_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/{Id}/publish') if True else {}
    client.hub.database.publishDatabaseSchema(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_renameDatabaseSchema_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/{Id}/rename') if True else {}
    client.hub.database.renameDatabaseSchema(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_saveDatabaseSchema_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas') if False else {}
    client.hub.database.saveDatabaseSchema(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_updateDatabaseSchemaDraft_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/{Id}/draft') if True else {}
    client.hub.database.updateDatabaseSchemaDraft(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_updateDatabaseSchemaSettings_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/{Id}/settings') if True else {}
    client.hub.database.updateDatabaseSchemaSettings(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_deleteDatabaseIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/integrations/{Id}') if True else {}
    client.hub.database.deleteDatabaseIntegration(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_disableDatabaseIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/integrations/{Id}/disable') if True else {}
    client.hub.database.disableDatabaseIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_enableDatabaseIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/integrations/{Id}/enable') if True else {}
    client.hub.database.enableDatabaseIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getDatabaseIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/integrations/{id}') if True else {}
    client.hub.database.getDatabaseIntegration(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getDatabaseIntegrations_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/integrations') if False else {}
    client.hub.database.getDatabaseIntegrations(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_saveDatabaseIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/integrations') if False else {}
    client.hub.database.saveDatabaseIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_setDatabaseIntegrationAsDefault_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/integrations/{Id}/default') if True else {}
    client.hub.database.setDatabaseIntegrationAsDefault(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_deleteDatabaseAggregate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/aggregates/{Id}') if True else {}
    client.hub.database.deleteDatabaseAggregate(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getDatabaseAggregate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/aggregates/{Id}') if True else {}
    client.hub.database.getDatabaseAggregate(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_getDatabaseAggregates_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/aggregates') if False else {}
    client.hub.database.getDatabaseAggregates(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_saveDatabaseAggregate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/aggregates') if False else {}
    client.hub.database.saveDatabaseAggregate(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_testDatabaseAggregate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/aggregates/test') if False else {}
    client.hub.database.testDatabaseAggregate(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
