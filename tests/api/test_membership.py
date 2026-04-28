from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_api_membership_module_surface() -> None:
    client, _ = make_client()
    module = client.api.membership
    assert callable(module.block_user)
    assert callable(module.save_system_user_with_permissions)
    assert callable(module.save_guest_user)
    assert callable(module.save_user_name_user)
    assert callable(module.save_email_user)
    assert callable(module.save_phone_user)
    assert callable(module.save_phone_user_name_with_permissions)
    assert callable(module.save_email_user_name_with_permissions)
    assert callable(module.save_user_name_with_permissions)
    assert callable(module.delete_user)
    assert callable(module.get_user)
    assert callable(module.get_users)
    assert callable(module.get_user_preferences)
    assert callable(module.invite_user)
    assert callable(module.assign_role_permissions)
    assert callable(module.unblock_user)
    assert callable(module.update_user)
    assert callable(module.update_user_preferences)


def test_api_membership_block_user_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.block_user()
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_save_system_user_with_permissions_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.save_system_user_with_permissions()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_save_guest_user_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.save_guest_user()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_save_user_name_user_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.save_user_name_user()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_save_email_user_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.save_email_user()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_save_phone_user_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.save_phone_user()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_save_phone_user_name_with_permissions_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.save_phone_user_name_with_permissions()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_save_email_user_name_with_permissions_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.save_email_user_name_with_permissions()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_save_user_name_with_permissions_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.save_user_name_with_permissions()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_delete_user_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.delete_user()
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_get_user_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.get_user(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_get_users_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.get_users()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_get_user_preferences_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.get_user_preferences(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_invite_user_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.invite_user()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_assign_role_permissions_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.assign_role_permissions()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_unblock_user_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.unblock_user()
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_update_user_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.update_user()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_update_user_preferences_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.membership.update_user_preferences(id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
