from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_membership_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.membership
    assert callable(module.disable_membership)
    assert callable(module.enable_membership)
    assert callable(module.delete_membership_trigger)
    assert callable(module.disable_membership_trigger)
    assert callable(module.enable_membership_trigger)
    assert callable(module.get_membership_trigger)
    assert callable(module.get_membership_triggers)
    assert callable(module.save_membership_trigger)
    assert callable(module.create_role)
    assert callable(module.delete_role)
    assert callable(module.get_role)
    assert callable(module.get_roles)
    assert callable(module.update_role_policies)
    assert callable(module.create_policy)
    assert callable(module.delete_policy)
    assert callable(module.get_policy)
    assert callable(module.get_policies)
    assert callable(module.update_policy)
    assert callable(module.delete_membership_integration)
    assert callable(module.disable_membership_integration)
    assert callable(module.enable_membership_integration)
    assert callable(module.get_membership_integration)
    assert callable(module.get_membership_integrations)
    assert callable(module.save_membership_integration)
    assert callable(module.set_membership_integration_as_default)


def test_hub_membership_disable_membership_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.disable_membership()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_enable_membership_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.enable_membership()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_delete_membership_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.delete_membership_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_disable_membership_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.disable_membership_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_enable_membership_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.enable_membership_trigger(trigger_id="stub-triggerId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_get_membership_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.get_membership_trigger(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_get_membership_triggers_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.get_membership_triggers()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_save_membership_trigger_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.save_membership_trigger()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_create_role_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.create_role()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_delete_role_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.delete_role()
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_get_role_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.get_role(id="stub-Id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_get_roles_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.get_roles()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_update_role_policies_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.update_role_policies()
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_create_policy_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.create_policy()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_delete_policy_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.delete_policy()
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_get_policy_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.get_policy(id="stub-Id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_get_policies_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.get_policies()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_update_policy_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.update_policy()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_delete_membership_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.delete_membership_integration(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_disable_membership_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.disable_membership_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_enable_membership_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.enable_membership_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_get_membership_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.get_membership_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_get_membership_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.get_membership_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_save_membership_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.save_membership_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_set_membership_integration_as_default_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.membership.set_membership_integration_as_default(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
