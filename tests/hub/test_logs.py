from __future__ import annotations

import asyncio
import json
from urllib.parse import parse_qs, urlparse

import httpx

from norbix_python import AsyncNorbix, Norbix, NorbixError
from ..helpers import make_client


def test_hub_logs_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.logs
    assert callable(module.disable_logging)
    assert callable(module.enable_logging)
    assert callable(module.delete_logging_integration)
    assert callable(module.disable_logging_integration)
    assert callable(module.enable_logging_integration)
    assert callable(module.get_logging_integration)
    assert callable(module.get_logging_integrations)
    assert callable(module.save_logging_integration)
    assert callable(module.test_logging_integration)


def test_hub_logs_disable_logging_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.disable_logging()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_enable_logging_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.enable_logging()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_delete_logging_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.delete_logging_integration(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_disable_logging_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.disable_logging_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_enable_logging_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.enable_logging_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_get_logging_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.get_logging_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_get_logging_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.get_logging_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_save_logging_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.save_logging_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_logs_test_logging_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.test_logging_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_logs_new_endpoints_surface() -> None:
    client, _ = make_client()
    module = client.hub.logs
    assert callable(module.get_logs_by_correlation_id)


def test_hub_logs_get_logs_by_correlation_id_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.get_logs_by_correlation_id()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_logs_read_and_settings_surface() -> None:
    client, _ = make_client()
    module = client.hub.logs
    assert callable(module.get_logs)
    assert callable(module.get_log)
    assert callable(module.clean_logs)
    assert callable(module.get_log_settings)
    assert callable(module.save_log_settings)


def test_hub_logs_get_logs_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.get_logs(level="error", eventCode="app:order.paid", pageSize=50)
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    url = urlparse(transport.last_request['url'])
    assert url.path == '/v3/logs'
    assert parse_qs(url.query) == {"level": ["error"], "eventCode": ["app:order.paid"], "pageSize": ["50"]}
    assert transport.last_request['body'] == ''


def test_hub_logs_get_log_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.get_log("log_1")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert urlparse(transport.last_request['url']).path == '/v3/logs/log_1'


def test_hub_logs_clean_logs_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.clean_logs()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert urlparse(transport.last_request['url']).path == '/v3/logs/clean'


def test_hub_logs_get_log_settings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.get_log_settings()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert urlparse(transport.last_request['url']).path == '/v3/logs/settings'


def test_hub_logs_save_log_settings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.save_log_settings(skipHttpBodyMeta=True, aiChatLoggingEnabled=False)
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert urlparse(transport.last_request['url']).path == '/v3/logs/settings'
    assert json.loads(transport.last_request['body']) == {"skipHttpBodyMeta": True, "aiChatLoggingEnabled": False}


def test_hub_logs_test_logging_integration_sends_integration_id() -> None:
    client, transport = make_client(account_id=None)
    client.hub.logs.test_logging_integration(integrationId="int_1")
    assert transport.last_request is not None
    assert urlparse(transport.last_request['url']).path == '/v3/logs/integrations/test'
    assert json.loads(transport.last_request['body']) == {"integrationId": "int_1"}


def test_async_hub_logs_hit_the_routes() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={})

    async def run() -> None:
        client = AsyncNorbix(
            project_id='test-project',
            bearer_token='test-token',
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        try:
            await client.hub.logs.get_logs(level="error")
            await client.hub.logs.get_log("log_1")
            await client.hub.logs.clean_logs()
            await client.hub.logs.get_log_settings()
            await client.hub.logs.save_log_settings(skipCloudDashboardLogs=True)
            await client.hub.logs.enable_logging()
            await client.hub.logs.disable_logging()
        finally:
            await client.aclose()

    asyncio.run(run())
    assert [(r.method, urlparse(str(r.url)).path) for r in seen] == [
        ('GET', '/v3/logs'),
        ('GET', '/v3/logs/log_1'),
        ('POST', '/v3/logs/clean'),
        ('GET', '/v3/logs/settings'),
        ('POST', '/v3/logs/settings'),
        ('PUT', '/v3/logs/enable'),
        ('PUT', '/v3/logs/disable'),
    ]
