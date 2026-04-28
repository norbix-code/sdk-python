from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_database_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.database
    assert callable(module.disable_database)
    assert callable(module.enable_database)
    assert callable(module.delete_schema_trigger)
    assert callable(module.disable_schema_trigger)
    assert callable(module.enable_schema_trigger)
    assert callable(module.get_schema_trigger)
    assert callable(module.get_schema_triggers)
    assert callable(module.save_schema_trigger)
    assert callable(module.delete_database_taxonomy)
    assert callable(module.get_database_taxonomy)
    assert callable(module.get_database_taxonomies)
    assert callable(module.save_database_taxonomy)
    assert callable(module.delete_database_taxonomy_term)
    assert callable(module.delete_many_database_taxonomy_terms)
    assert callable(module.get_database_taxonomy_term)
    assert callable(module.save_database_taxonomy_term)
    assert callable(module.update_database_taxonomy_term)
    assert callable(module.delete_database_schema)
    assert callable(module.discard_database_schema_draft)
    assert callable(module.get_database_schema)
    assert callable(module.get_database_schemas)
    assert callable(module.get_database_schema_draft)
    assert callable(module.get_database_schema_version_diff)
    assert callable(module.get_database_schema_versions)
    assert callable(module.publish_database_schema)
    assert callable(module.rename_database_schema)
    assert callable(module.save_database_schema)
    assert callable(module.update_database_schema_draft)
    assert callable(module.update_database_schema_settings)
    assert callable(module.delete_database_integration)
    assert callable(module.disable_database_integration)
    assert callable(module.enable_database_integration)
    assert callable(module.get_database_integration)
    assert callable(module.get_database_integrations)
    assert callable(module.save_database_integration)
    assert callable(module.set_database_integration_as_default)
    assert callable(module.delete_database_aggregate)
    assert callable(module.get_database_aggregate)
    assert callable(module.get_database_aggregates)
    assert callable(module.save_database_aggregate)
    assert callable(module.test_database_aggregate)


def test_hub_database_disable_database_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.disable_database({})
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_enable_database_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.enable_database({})
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_schema_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_schema_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_disable_schema_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.disable_schema_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_enable_schema_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.enable_schema_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_schema_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_schema_trigger(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_schema_triggers_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_schema_triggers({})
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_save_schema_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.save_schema_trigger({})
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_database_taxonomy_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_database_taxonomy(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_taxonomy_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_taxonomy(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_taxonomies_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_taxonomies({})
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_save_database_taxonomy_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.save_database_taxonomy({})
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_database_taxonomy_term_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_database_taxonomy_term(taxonomy_id="stub-TaxonomyId", id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_many_database_taxonomy_terms_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_many_database_taxonomy_terms(taxonomy_id="stub-TaxonomyId")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_taxonomy_term_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_taxonomy_term(taxonomy_id="stub-TaxonomyId", id="stub-Id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_save_database_taxonomy_term_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.save_database_taxonomy_term(taxonomy_id="stub-TaxonomyId")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_update_database_taxonomy_term_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.update_database_taxonomy_term(taxonomy_id="stub-TaxonomyId", id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_database_schema_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_database_schema(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_discard_database_schema_draft_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.discard_database_schema_draft(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_schema_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_schema(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_schemas_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_schemas({})
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_schema_draft_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_schema_draft(id="stub-Id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_schema_version_diff_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_schema_version_diff(id="stub-Id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_schema_versions_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_schema_versions(id="stub-Id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_publish_database_schema_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.publish_database_schema(id="stub-Id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_rename_database_schema_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.rename_database_schema(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_save_database_schema_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.save_database_schema({})
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_update_database_schema_draft_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.update_database_schema_draft(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_update_database_schema_settings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.update_database_schema_settings(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_database_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_database_integration(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_disable_database_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.disable_database_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_enable_database_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.enable_database_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_integrations({})
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_save_database_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.save_database_integration({})
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_set_database_integration_as_default_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.set_database_integration_as_default(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_delete_database_aggregate_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.delete_database_aggregate(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_aggregate_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_aggregate(id="stub-Id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_get_database_aggregates_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.get_database_aggregates({})
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_save_database_aggregate_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.save_database_aggregate({})
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_database_test_database_aggregate_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.database.test_database_aggregate({})
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
