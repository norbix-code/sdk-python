from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_hub_scheduler_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.scheduler
    assert callable(module.disableScheduler)
    assert callable(module.enableScheduler)
    assert callable(module.deleteSchedulerTask)
    assert callable(module.disableSchedulerTask)
    assert callable(module.enableSchedulerTask)
    assert callable(module.getSchedulerTask)
    assert callable(module.getSchedulerTasks)
    assert callable(module.saveSchedulerTask)


def test_hub_scheduler_disableScheduler_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/scheduler/disable') if False else {}
    client.hub.scheduler.disableScheduler(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_enableScheduler_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/scheduler/enable') if False else {}
    client.hub.scheduler.enableScheduler(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_deleteSchedulerTask_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/scheduler/tasks/{Id}') if True else {}
    client.hub.scheduler.deleteSchedulerTask(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_disableSchedulerTask_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/scheduler/tasks/{Id}/disable') if True else {}
    client.hub.scheduler.disableSchedulerTask(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_enableSchedulerTask_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/scheduler/tasks/{Id}/enable') if True else {}
    client.hub.scheduler.enableSchedulerTask(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_getSchedulerTask_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/scheduler/tasks/{id}') if True else {}
    client.hub.scheduler.getSchedulerTask(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_getSchedulerTasks_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/scheduler/tasks') if False else {}
    client.hub.scheduler.getSchedulerTasks(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_saveSchedulerTask_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/scheduler/tasks') if False else {}
    client.hub.scheduler.saveSchedulerTask(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
