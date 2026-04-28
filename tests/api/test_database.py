from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_api_database_module_surface() -> None:
    client, _ = make_client()
    module = client.api.database
    assert callable(module.find_terms)
    assert callable(module.find_terms_children)
    assert callable(module.get_database_schema)
    assert callable(module.get_database_schemas)
    assert callable(module.aggregate)
    assert callable(module.change_responsibility)
    assert callable(module.count)
    assert callable(module.delete_many)
    assert callable(module.delete_one)
    assert callable(module.distinct)
    assert callable(module.execute_aggregate)
    assert callable(module.find)
    assert callable(module.find_one)
    assert callable(module.insert_many)
    assert callable(module.insert_one)
    assert callable(module.replace_one)
    assert callable(module.update_many)
    assert callable(module.update_one)


def test_api_database_find_terms_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.find_terms(taxonomy_name="stub-taxonomyName")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_find_terms_children_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.find_terms_children(taxonomy_name="stub-taxonomyName", parent_id="stub-parentId")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_get_database_schema_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.get_database_schema(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_get_database_schemas_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.get_database_schemas({})
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_aggregate_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.aggregate(collection_name="stub-collectionName")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_change_responsibility_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.change_responsibility(collection_name="stub-collectionName", id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_count_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.count(collection_name="stub-collectionName")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_delete_many_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.delete_many(collection_name="stub-collectionName")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_delete_one_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.delete_one(collection_name="stub-collectionName", id="stub-id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_distinct_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.distinct(collection_name="stub-collectionName")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_execute_aggregate_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.execute_aggregate(collection_name="stub-collectionName", aggregate_id="stub-aggregateId")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_find_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.find(collection_name="stub-collectionName")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_find_one_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.find_one(collection_name="stub-collectionName", id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_insert_many_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.insert_many(collection_name="stub-collectionName")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_insert_one_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.insert_one(collection_name="stub-collectionName")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_replace_one_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.replace_one(collection_name="stub-collectionName", id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_update_many_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.update_many(collection_name="stub-collectionName")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_update_one_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.database.update_one(collection_name="stub-collectionName", id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
