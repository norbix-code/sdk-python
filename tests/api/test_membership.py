from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_api_membership_module_surface() -> None:
    client, _ = make_client()
    module = client.api.membership
    assert callable(module.blockUser)
    assert callable(module.saveSystemUserWithPermissions)
    assert callable(module.saveGuestUser)
    assert callable(module.saveUserNameUser)
    assert callable(module.saveEmailUser)
    assert callable(module.savePhoneUser)
    assert callable(module.savePhoneUserNameWithPermissions)
    assert callable(module.saveEmailUserNameWithPermissions)
    assert callable(module.saveUserNameWithPermissions)
    assert callable(module.deleteUser)
    assert callable(module.getUser)
    assert callable(module.getUsers)
    assert callable(module.getUserPreferences)
    assert callable(module.inviteUser)
    assert callable(module.assignRolePermissions)
    assert callable(module.unblockUser)
    assert callable(module.updateUser)
    assert callable(module.updateUserPreferences)


def test_api_membership_blockUser_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/block') if False else {}
    client.api.membership.blockUser(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_saveSystemUserWithPermissions_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/register/service') if False else {}
    client.api.membership.saveSystemUserWithPermissions(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_saveGuestUser_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/register/guest') if False else {}
    client.api.membership.saveGuestUser(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_saveUserNameUser_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/register/user-name') if False else {}
    client.api.membership.saveUserNameUser(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_saveEmailUser_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/register/email') if False else {}
    client.api.membership.saveEmailUser(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_savePhoneUser_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/register/phone') if False else {}
    client.api.membership.savePhoneUser(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_savePhoneUserNameWithPermissions_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/register/phone-with-permissions') if False else {}
    client.api.membership.savePhoneUserNameWithPermissions(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_saveEmailUserNameWithPermissions_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/register/email-with-permissions') if False else {}
    client.api.membership.saveEmailUserNameWithPermissions(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_saveUserNameWithPermissions_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/register/user-name-with-permissions') if False else {}
    client.api.membership.saveUserNameWithPermissions(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_deleteUser_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users') if False else {}
    client.api.membership.deleteUser(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_getUser_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/{id}') if True else {}
    client.api.membership.getUser(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_getUsers_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users') if False else {}
    client.api.membership.getUsers(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_getUserPreferences_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/{id}/preferences') if True else {}
    client.api.membership.getUserPreferences(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_inviteUser_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/invite') if False else {}
    client.api.membership.inviteUser(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_assignRolePermissions_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/assign-roles') if False else {}
    client.api.membership.assignRolePermissions(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_unblockUser_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/unblock') if False else {}
    client.api.membership.unblockUser(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_updateUser_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users') if False else {}
    client.api.membership.updateUser(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_api_membership_updateUserPreferences_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/users/{id}/preferences') if True else {}
    client.api.membership.updateUserPreferences(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
