from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_api_database_module_surface() -> None:
    client, _ = make_client()
    module = client.api.database
    assert callable(module.findTerms)
    assert callable(module.findTermsChildren)
    assert callable(module.getDatabaseSchema)
    assert callable(module.getDatabaseSchemas)
    assert callable(module.aggregate)
    assert callable(module.changeResponsibility)
    assert callable(module.count)
    assert callable(module.deleteMany)
    assert callable(module.deleteOne)
    assert callable(module.distinct)
    assert callable(module.executeAggregate)
    assert callable(module.find)
    assert callable(module.findOne)
    assert callable(module.insertMany)
    assert callable(module.insertOne)
    assert callable(module.replaceOne)
    assert callable(module.updateMany)
    assert callable(module.updateOne)


def test_api_database_findTerms_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/taxonomies/{taxonomyName}/terms') if True else {}
    client.api.database.findTerms(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_findTermsChildren_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children') if True else {}
    client.api.database.findTermsChildren(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_getDatabaseSchema_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas/{id}') if True else {}
    client.api.database.getDatabaseSchema(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_getDatabaseSchemas_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/schemas') if False else {}
    client.api.database.getDatabaseSchemas(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_aggregate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}/aggregate') if True else {}
    client.api.database.aggregate(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_changeResponsibility_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}/{id}/responsibility') if True else {}
    client.api.database.changeResponsibility(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_count_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}/count') if True else {}
    client.api.database.count(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_deleteMany_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}/many') if True else {}
    client.api.database.deleteMany(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_deleteOne_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}/{id}') if True else {}
    client.api.database.deleteOne(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_distinct_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}/distinct') if True else {}
    client.api.database.distinct(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_executeAggregate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute') if True else {}
    client.api.database.executeAggregate(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_find_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}') if True else {}
    client.api.database.find(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_findOne_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}/{id}') if True else {}
    client.api.database.findOne(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_insertMany_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}/many') if True else {}
    client.api.database.insertMany(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_insertOne_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}') if True else {}
    client.api.database.insertOne(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_replaceOne_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}/{id}/replace') if True else {}
    client.api.database.replaceOne(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_updateMany_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}/many') if True else {}
    client.api.database.updateMany(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_database_updateOne_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/database/collections/{collectionName}/{id}') if True else {}
    client.api.database.updateOne(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
