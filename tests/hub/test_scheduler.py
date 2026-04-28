from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_scheduler_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.scheduler
    assert callable(module.disable_scheduler)
    assert callable(module.enable_scheduler)
    assert callable(module.delete_scheduler_task)
    assert callable(module.disable_scheduler_task)
    assert callable(module.enable_scheduler_task)
    assert callable(module.get_scheduler_task)
    assert callable(module.get_scheduler_tasks)
    assert callable(module.save_scheduler_task)


def test_hub_scheduler_disable_scheduler_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.scheduler.disable_scheduler()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_enable_scheduler_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.scheduler.enable_scheduler()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_delete_scheduler_task_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.scheduler.delete_scheduler_task(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_disable_scheduler_task_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.scheduler.disable_scheduler_task(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_enable_scheduler_task_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.scheduler.enable_scheduler_task(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_get_scheduler_task_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.scheduler.get_scheduler_task(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_get_scheduler_tasks_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.scheduler.get_scheduler_tasks()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_scheduler_save_scheduler_task_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.scheduler.save_scheduler_task()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
