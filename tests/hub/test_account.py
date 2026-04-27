from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_hub_account_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.account
    assert callable(module.getAccountProfile)
    assert callable(module.updateAccountProfile)
    assert callable(module.resendAccountVerificationToken)
    assert callable(module.getAccountStatus)
    assert callable(module.createStripeCheckoutSession)
    assert callable(module.getStripeBillingPortalUrl)
    assert callable(module.createTeamMemberFromInvitation)
    assert callable(module.verifyAccount)
    assert callable(module.deleteNotificationsGroup)
    assert callable(module.deleteNotificationsTag)
    assert callable(module.removeTagFromNotificationsGroup)
    assert callable(module.saveNotificationsGroup)
    assert callable(module.saveNotificationsTag)
    assert callable(module.createProject)
    assert callable(module.deleteProject)
    assert callable(module.getProject)
    assert callable(module.getProjects)
    assert callable(module.getAccountRegions)
    assert callable(module.getProjectTokens)
    assert callable(module.updateProjectAccentColor)
    assert callable(module.updateProjectIcon)
    assert callable(module.updateProjectLogo)
    assert callable(module.updateProjectMainColor)
    assert callable(module.updateProjectAllowedOrigins)
    assert callable(module.updateProjectDefaultLanguage)
    assert callable(module.updateProjectDescription)
    assert callable(module.disableProject)
    assert callable(module.enableProject)
    assert callable(module.updateProjectLanguages)
    assert callable(module.updateProjectUrl)
    assert callable(module.updateProjectName)
    assert callable(module.updateProjectRegions)
    assert callable(module.createAccount)
    assert callable(module.getAccountCollaborators)
    assert callable(module.sendInviteToTeamMember)
    assert callable(module.getLicenses)
    assert callable(module.askChat)


def test_hub_account_getAccountProfile_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/profile') if False else {}
    client.hub.account.getAccountProfile(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_getAccountProfile_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/profile') if False else {}
    try:
        client.hub.account.getAccountProfile(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_updateAccountProfile_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/profile') if False else {}
    client.hub.account.updateAccountProfile(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_updateAccountProfile_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/profile') if False else {}
    try:
        client.hub.account.updateAccountProfile(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_resendAccountVerificationToken_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/verify/resend') if False else {}
    client.hub.account.resendAccountVerificationToken(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_resendAccountVerificationToken_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/verify/resend') if False else {}
    try:
        client.hub.account.resendAccountVerificationToken(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_getAccountStatus_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/status') if False else {}
    client.hub.account.getAccountStatus(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_getAccountStatus_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/status') if False else {}
    try:
        client.hub.account.getAccountStatus(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_createStripeCheckoutSession_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/stripe/create-checkout-session') if False else {}
    client.hub.account.createStripeCheckoutSession(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_createStripeCheckoutSession_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/stripe/create-checkout-session') if False else {}
    try:
        client.hub.account.createStripeCheckoutSession(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_getStripeBillingPortalUrl_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/stripe/get-portal-url') if False else {}
    client.hub.account.getStripeBillingPortalUrl(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_getStripeBillingPortalUrl_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/stripe/get-portal-url') if False else {}
    try:
        client.hub.account.getStripeBillingPortalUrl(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_createTeamMemberFromInvitation_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/team/member') if False else {}
    client.hub.account.createTeamMemberFromInvitation(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_createTeamMemberFromInvitation_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/team/member') if False else {}
    try:
        client.hub.account.createTeamMemberFromInvitation(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_verifyAccount_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/verify') if False else {}
    client.hub.account.verifyAccount(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_verifyAccount_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/verify') if False else {}
    try:
        client.hub.account.verifyAccount(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_deleteNotificationsGroup_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/notifications/settings/group') if True else {}
    client.hub.account.deleteNotificationsGroup(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_deleteNotificationsGroup_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/notifications/settings/group') if True else {}
    try:
        client.hub.account.deleteNotificationsGroup(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_deleteNotificationsTag_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/notifications/settings/tag') if True else {}
    client.hub.account.deleteNotificationsTag(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_deleteNotificationsTag_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/notifications/settings/tag') if True else {}
    try:
        client.hub.account.deleteNotificationsTag(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_removeTagFromNotificationsGroup_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/notifications/settings/group/tag') if True else {}
    client.hub.account.removeTagFromNotificationsGroup(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_removeTagFromNotificationsGroup_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/notifications/settings/group/tag') if True else {}
    try:
        client.hub.account.removeTagFromNotificationsGroup(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_saveNotificationsGroup_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/notifications/settings/group') if True else {}
    client.hub.account.saveNotificationsGroup(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_saveNotificationsGroup_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/notifications/settings/group') if True else {}
    try:
        client.hub.account.saveNotificationsGroup(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_saveNotificationsTag_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/notifications/settings/tag') if True else {}
    client.hub.account.saveNotificationsTag(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_saveNotificationsTag_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/notifications/settings/tag') if True else {}
    try:
        client.hub.account.saveNotificationsTag(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_createProject_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects') if False else {}
    client.hub.account.createProject(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_createProject_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects') if False else {}
    try:
        client.hub.account.createProject(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_deleteProject_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}') if True else {}
    client.hub.account.deleteProject(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_deleteProject_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}') if True else {}
    try:
        client.hub.account.deleteProject(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_getProject_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}') if True else {}
    client.hub.account.getProject(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_getProject_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}') if True else {}
    try:
        client.hub.account.getProject(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_getProjects_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects') if False else {}
    client.hub.account.getProjects(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_getProjects_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects') if False else {}
    try:
        client.hub.account.getProjects(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_getAccountRegions_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/regions') if False else {}
    client.hub.account.getAccountRegions(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_getAccountRegions_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/regions') if False else {}
    try:
        client.hub.account.getAccountRegions(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_getProjectTokens_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/tokens') if True else {}
    client.hub.account.getProjectTokens(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_getProjectTokens_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/tokens') if True else {}
    try:
        client.hub.account.getProjectTokens(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_updateProjectAccentColor_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/accent-color') if True else {}
    client.hub.account.updateProjectAccentColor(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_updateProjectAccentColor_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/accent-color') if True else {}
    try:
        client.hub.account.updateProjectAccentColor(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_updateProjectIcon_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/icon') if True else {}
    client.hub.account.updateProjectIcon(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_updateProjectIcon_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/icon') if True else {}
    try:
        client.hub.account.updateProjectIcon(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_updateProjectLogo_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/logo') if True else {}
    client.hub.account.updateProjectLogo(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_updateProjectLogo_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/logo') if True else {}
    try:
        client.hub.account.updateProjectLogo(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_updateProjectMainColor_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/main-color') if True else {}
    client.hub.account.updateProjectMainColor(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_updateProjectMainColor_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/main-color') if True else {}
    try:
        client.hub.account.updateProjectMainColor(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_updateProjectAllowedOrigins_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/origins') if True else {}
    client.hub.account.updateProjectAllowedOrigins(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_updateProjectAllowedOrigins_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/origins') if True else {}
    try:
        client.hub.account.updateProjectAllowedOrigins(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_updateProjectDefaultLanguage_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/default-language') if True else {}
    client.hub.account.updateProjectDefaultLanguage(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_updateProjectDefaultLanguage_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/default-language') if True else {}
    try:
        client.hub.account.updateProjectDefaultLanguage(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_updateProjectDescription_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/description') if True else {}
    client.hub.account.updateProjectDescription(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_updateProjectDescription_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/description') if True else {}
    try:
        client.hub.account.updateProjectDescription(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_disableProject_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/disable') if True else {}
    client.hub.account.disableProject(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_disableProject_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/disable') if True else {}
    try:
        client.hub.account.disableProject(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_enableProject_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/enable') if True else {}
    client.hub.account.enableProject(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_enableProject_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/enable') if True else {}
    try:
        client.hub.account.enableProject(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_updateProjectLanguages_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/languages') if True else {}
    client.hub.account.updateProjectLanguages(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_updateProjectLanguages_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/languages') if True else {}
    try:
        client.hub.account.updateProjectLanguages(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_updateProjectUrl_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/url') if True else {}
    client.hub.account.updateProjectUrl(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_updateProjectUrl_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/url') if True else {}
    try:
        client.hub.account.updateProjectUrl(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_updateProjectName_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/name') if True else {}
    client.hub.account.updateProjectName(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_updateProjectName_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/name') if True else {}
    try:
        client.hub.account.updateProjectName(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_updateProjectRegions_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/regions') if True else {}
    client.hub.account.updateProjectRegions(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_updateProjectRegions_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/projects/{projectId}/settings/regions') if True else {}
    try:
        client.hub.account.updateProjectRegions(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_createAccount_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account') if False else {}
    client.hub.account.createAccount(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_createAccount_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account') if False else {}
    try:
        client.hub.account.createAccount(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_getAccountCollaborators_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/collaborators') if False else {}
    client.hub.account.getAccountCollaborators(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_getAccountCollaborators_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/collaborators') if False else {}
    try:
        client.hub.account.getAccountCollaborators(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_sendInviteToTeamMember_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/team/member/invite') if False else {}
    client.hub.account.sendInviteToTeamMember(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_sendInviteToTeamMember_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/team/member/invite') if False else {}
    try:
        client.hub.account.sendInviteToTeamMember(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_getLicenses_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/licenses') if False else {}
    client.hub.account.getLicenses(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_getLicenses_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/licenses') if False else {}
    try:
        client.hub.account.getLicenses(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_askChat_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/account/chat/complete') if False else {}
    client.hub.account.askChat(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_askChat_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/account/chat/complete') if False else {}
    try:
        client.hub.account.askChat(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')
