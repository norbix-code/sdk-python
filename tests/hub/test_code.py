from __future__ import annotations

from ..helpers import make_client


def test_hub_code_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.code
    assert callable(module.disable_code)
    assert callable(module.enable_code)
    assert callable(module.get_code_integrations)
    assert callable(module.save_code_integration)
    assert callable(module.confirm_code_integration_human_delivery)
    assert callable(module.test_code_integration)
    assert callable(module.delete_code_integration)
    assert callable(module.set_code_integration_as_default)
    assert callable(module.disable_code_integration)
    assert callable(module.enable_code_integration)
    assert callable(module.get_code_integration)
    assert callable(module.get_marketplace_integrations)
    assert callable(module.save_marketplace_integration)
    assert callable(module.delete_marketplace_integration)
    assert callable(module.get_marketplace_integration)
    assert callable(module.get_marketplace_bindings)
    assert callable(module.save_marketplace_function_binding)
    assert callable(module.delete_marketplace_function_binding)
    assert callable(module.get_marketplace_binding)
    assert callable(module.disable_marketplace_function_binding)
    assert callable(module.enable_marketplace_function_binding)
    assert callable(module.invoke_marketplace_function_binding)
    assert callable(module.get_marketplace_binding_tokens)
    assert callable(module.disable_marketplace_integration)
    assert callable(module.enable_marketplace_integration)
    assert callable(module.get_marketplace_function_catalog)
    assert callable(module.get_marketplace_listings)
    assert callable(module.get_marketplace_listing_function_tokens)


def test_hub_code_disable_code_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.disable_code()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_enable_code_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.enable_code()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_code_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_code_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_save_code_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.save_code_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_confirm_code_integration_human_delivery_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.confirm_code_integration_human_delivery()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_test_code_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.test_code_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_delete_code_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.delete_code_integration(id="stub-id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_set_code_integration_as_default_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.set_code_integration_as_default(id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_disable_code_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.disable_code_integration(id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_enable_code_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.enable_code_integration(id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_code_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_code_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_save_marketplace_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.save_marketplace_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_delete_marketplace_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.delete_marketplace_integration(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_integration(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_bindings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_bindings(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_save_marketplace_function_binding_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.save_marketplace_function_binding(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_delete_marketplace_function_binding_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.delete_marketplace_function_binding(integration_view_id="stub-integration_view_id", binding_view_id="stub-binding_view_id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_binding_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_binding(integration_view_id="stub-integration_view_id", binding_view_id="stub-binding_view_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_disable_marketplace_function_binding_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.disable_marketplace_function_binding(integration_view_id="stub-integration_view_id", binding_view_id="stub-binding_view_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_enable_marketplace_function_binding_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.enable_marketplace_function_binding(integration_view_id="stub-integration_view_id", binding_view_id="stub-binding_view_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_invoke_marketplace_function_binding_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.invoke_marketplace_function_binding(integration_view_id="stub-integration_view_id", binding_view_id="stub-binding_view_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_binding_tokens_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_binding_tokens(integration_view_id="stub-integration_view_id", binding_view_id="stub-binding_view_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_disable_marketplace_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.disable_marketplace_integration(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_enable_marketplace_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.enable_marketplace_integration(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_function_catalog_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_function_catalog(integration_view_id="stub-integration_view_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_listings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_listings()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_code_get_marketplace_listing_function_tokens_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.code.get_marketplace_listing_function_tokens(listing_view_id="stub-listing_view_id", function_key="stub-function_key")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
