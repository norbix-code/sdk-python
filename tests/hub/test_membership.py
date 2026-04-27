from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_hub_membership_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.membership
    assert callable(module.disableMembership)
    assert callable(module.enableMembership)
    assert callable(module.deleteMembershipTrigger)
    assert callable(module.disableMembershipTrigger)
    assert callable(module.enableMembershipTrigger)
    assert callable(module.getMembershipTrigger)
    assert callable(module.getMembershipTriggers)
    assert callable(module.saveMembershipTrigger)
    assert callable(module.createRole)
    assert callable(module.deleteRole)
    assert callable(module.getRole)
    assert callable(module.getRoles)
    assert callable(module.updateRolePolicies)
    assert callable(module.createPolicy)
    assert callable(module.deletePolicy)
    assert callable(module.getPolicy)
    assert callable(module.getPolicies)
    assert callable(module.updatePolicy)
    assert callable(module.deleteMembershipIntegration)
    assert callable(module.disableMembershipIntegration)
    assert callable(module.enableMembershipIntegration)
    assert callable(module.getMembershipIntegration)
    assert callable(module.getMembershipIntegrations)
    assert callable(module.saveMembershipIntegration)
    assert callable(module.setMembershipIntegrationAsDefault)


def test_hub_membership_disableMembership_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/disable') if False else {}
    client.hub.membership.disableMembership(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_enableMembership_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/enable') if False else {}
    client.hub.membership.enableMembership(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_deleteMembershipTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/triggers/{triggerId}') if True else {}
    client.hub.membership.deleteMembershipTrigger(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_disableMembershipTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/triggers/{triggerId}/disable') if True else {}
    client.hub.membership.disableMembershipTrigger(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_enableMembershipTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/triggers/{triggerId}/enable') if True else {}
    client.hub.membership.enableMembershipTrigger(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_getMembershipTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/triggers/{id}') if True else {}
    client.hub.membership.getMembershipTrigger(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_getMembershipTriggers_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/triggers') if False else {}
    client.hub.membership.getMembershipTriggers(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_saveMembershipTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/triggers') if False else {}
    client.hub.membership.saveMembershipTrigger(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_createRole_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/roles') if False else {}
    client.hub.membership.createRole(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_deleteRole_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/roles') if False else {}
    client.hub.membership.deleteRole(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_getRole_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/roles/{Id}') if True else {}
    client.hub.membership.getRole(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_getRoles_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/roles') if False else {}
    client.hub.membership.getRoles(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_updateRolePolicies_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/roles') if False else {}
    client.hub.membership.updateRolePolicies(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_createPolicy_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/policies') if False else {}
    client.hub.membership.createPolicy(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_deletePolicy_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/policies') if False else {}
    client.hub.membership.deletePolicy(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_getPolicy_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/policies/{Id}') if True else {}
    client.hub.membership.getPolicy(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_getPolicies_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/policies') if False else {}
    client.hub.membership.getPolicies(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_updatePolicy_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/policies') if False else {}
    client.hub.membership.updatePolicy(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_deleteMembershipIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/integrations/{Id}') if True else {}
    client.hub.membership.deleteMembershipIntegration(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_disableMembershipIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/integrations/{Id}/disable') if True else {}
    client.hub.membership.disableMembershipIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_enableMembershipIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/integrations/{Id}/enable') if True else {}
    client.hub.membership.enableMembershipIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_getMembershipIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/integrations/{id}') if True else {}
    client.hub.membership.getMembershipIntegration(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_getMembershipIntegrations_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/integrations') if False else {}
    client.hub.membership.getMembershipIntegrations(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_saveMembershipIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/integrations') if False else {}
    client.hub.membership.saveMembershipIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_membership_setMembershipIntegrationAsDefault_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/membership/integrations/{Id}/default') if True else {}
    client.hub.membership.setMembershipIntegrationAsDefault(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
