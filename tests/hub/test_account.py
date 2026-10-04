from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_account_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.account
    assert callable(module.get_account_profile)
    assert callable(module.update_account_profile)
    assert callable(module.resend_account_verification_token)
    assert callable(module.get_account_status)
    assert callable(module.create_stripe_checkout_session)
    assert callable(module.get_stripe_billing_portal_url)
    assert callable(module.create_team_member_from_invitation)
    assert callable(module.verify_account)
    assert callable(module.delete_notifications_group)
    assert callable(module.delete_notifications_tag)
    assert callable(module.remove_tag_from_notifications_group)
    assert callable(module.save_notifications_group)
    assert callable(module.save_notifications_tag)
    assert callable(module.create_project)
    assert callable(module.delete_project)
    assert callable(module.get_project)
    assert callable(module.get_projects)
    assert callable(module.get_account_regions)
    assert callable(module.get_project_tokens)
    assert callable(module.update_project_accent_color)
    assert callable(module.update_project_icon)
    assert callable(module.update_project_logo)
    assert callable(module.update_project_main_color)
    assert callable(module.update_project_allowed_origins)
    assert callable(module.update_project_default_language)
    assert callable(module.update_project_description)
    assert callable(module.disable_project)
    assert callable(module.enable_project)
    assert callable(module.update_project_languages)
    assert callable(module.update_project_url)
    assert callable(module.update_project_name)
    assert callable(module.update_project_regions)
    assert callable(module.create_account)
    assert callable(module.get_account_collaborators)
    assert callable(module.send_invite_to_team_member)
    assert callable(module.get_licenses)


def test_hub_account_get_account_profile_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.get_account_profile()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_get_account_profile_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.get_account_profile()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_update_account_profile_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.update_account_profile()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_update_account_profile_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.update_account_profile()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_resend_account_verification_token_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.resend_account_verification_token()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_resend_account_verification_token_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.resend_account_verification_token()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_get_account_status_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.get_account_status()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_get_account_status_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.get_account_status()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_create_stripe_checkout_session_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.create_stripe_checkout_session()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_create_stripe_checkout_session_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.create_stripe_checkout_session()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_get_stripe_billing_portal_url_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.get_stripe_billing_portal_url()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_get_stripe_billing_portal_url_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.get_stripe_billing_portal_url()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_create_team_member_from_invitation_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.create_team_member_from_invitation()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_create_team_member_from_invitation_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.create_team_member_from_invitation()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_verify_account_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.verify_account()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_verify_account_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.verify_account()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_delete_notifications_group_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.delete_notifications_group(project_id="stub-projectId")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_delete_notifications_group_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.delete_notifications_group(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_delete_notifications_tag_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.delete_notifications_tag(project_id="stub-projectId")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_delete_notifications_tag_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.delete_notifications_tag(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_remove_tag_from_notifications_group_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.remove_tag_from_notifications_group(project_id="stub-projectId")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_remove_tag_from_notifications_group_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.remove_tag_from_notifications_group(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_save_notifications_group_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.save_notifications_group(project_id="stub-projectId")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_save_notifications_group_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.save_notifications_group(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_save_notifications_tag_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.save_notifications_tag(project_id="stub-projectId")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_save_notifications_tag_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.save_notifications_tag(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_create_project_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.create_project()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_create_project_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.create_project()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_delete_project_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.delete_project(project_id="stub-projectId")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_delete_project_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.delete_project(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_get_project_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.get_project(project_id="stub-projectId")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_get_project_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.get_project(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_get_projects_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.get_projects()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_get_projects_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.get_projects()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_get_account_regions_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.get_account_regions()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_get_account_regions_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.get_account_regions()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_get_project_tokens_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.get_project_tokens(project_id="stub-projectId")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_get_project_tokens_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.get_project_tokens(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_update_project_accent_color_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.update_project_accent_color(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_update_project_accent_color_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.update_project_accent_color(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_update_project_icon_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.update_project_icon(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_update_project_icon_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.update_project_icon(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_update_project_logo_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.update_project_logo(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_update_project_logo_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.update_project_logo(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_update_project_main_color_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.update_project_main_color(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_update_project_main_color_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.update_project_main_color(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_update_project_allowed_origins_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.update_project_allowed_origins(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_update_project_allowed_origins_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.update_project_allowed_origins(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_update_project_default_language_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.update_project_default_language(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_update_project_default_language_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.update_project_default_language(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_update_project_description_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.update_project_description(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_update_project_description_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.update_project_description(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_disable_project_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.disable_project(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_disable_project_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.disable_project(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_enable_project_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.enable_project(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_enable_project_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.enable_project(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_update_project_languages_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.update_project_languages(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_update_project_languages_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.update_project_languages(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_update_project_url_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.update_project_url(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_update_project_url_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.update_project_url(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_update_project_name_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.update_project_name(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_update_project_name_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.update_project_name(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_update_project_regions_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.update_project_regions(project_id="stub-projectId")
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_update_project_regions_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.update_project_regions(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_create_account_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.create_account()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_create_account_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.create_account()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_get_account_collaborators_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.get_account_collaborators()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_get_account_collaborators_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.get_account_collaborators()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_send_invite_to_team_member_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.send_invite_to_team_member()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_send_invite_to_team_member_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.send_invite_to_team_member()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_get_licenses_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.account.get_licenses()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_account_get_licenses_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.get_licenses()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_account_wave3_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.account
    assert callable(module.get_project_ai_settings)
    assert callable(module.update_project_ai_settings)
    assert callable(module.create_project_ai_assistant)
    assert callable(module.update_project_ai_assistant)
    assert callable(module.delete_project_ai_assistant)
    assert callable(module.get_project_ai_usage)
    assert callable(module.set_admin_portal_enabled)


def test_hub_account_get_project_ai_settings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.account.get_project_ai_settings(project_id="stub-projectId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request['url'].endswith('/v2/account/projects/stub-projectId/ai/settings')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_hub_account_update_project_ai_settings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.account.update_project_ai_settings(project_id="stub-projectId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request['url'].endswith('/v2/account/projects/stub-projectId/ai/settings')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_hub_account_create_project_ai_assistant_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.account.create_project_ai_assistant(project_id="stub-projectId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request['url'].endswith('/v2/account/projects/stub-projectId/ai/assistants')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_hub_account_update_project_ai_assistant_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.account.update_project_ai_assistant(project_id="stub-projectId", assistant_id="stub-assistantId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request['url'].endswith('/v2/account/projects/stub-projectId/ai/assistants/stub-assistantId')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_hub_account_delete_project_ai_assistant_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.account.delete_project_ai_assistant(project_id="stub-projectId", assistant_id="stub-assistantId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request['url'].endswith('/v2/account/projects/stub-projectId/ai/assistants/stub-assistantId')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_hub_account_get_project_ai_usage_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.account.get_project_ai_usage(project_id="stub-projectId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request['url'].endswith('/v2/account/projects/stub-projectId/ai/usage')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_hub_account_set_admin_portal_enabled_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.account.set_admin_portal_enabled(project_id="stub-projectId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request['url'].endswith('/v2/account/projects/stub-projectId/admin-portal/enabled')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_hub_account_check_project_languages_request_shape() -> None:
    import json
    from urllib.parse import urlparse

    client, transport = make_client(account_id='acc-1')
    client.hub.account.check_project_languages(
        project_id="proj-1", defaultLanguage="en", languages=["en", "de"]
    )
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert urlparse(transport.last_request['url']).path == '/v2/account/projects/proj-1/settings/languages/check'
    assert json.loads(transport.last_request['body']) == {"defaultLanguage": "en", "languages": ["en", "de"]}
    assert transport.last_request['headers']['x-cm-accountid'] == 'acc-1'

def test_hub_account_check_project_languages_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.account.check_project_languages(project_id="stub")
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_async_hub_account_check_project_languages_hits_the_route() -> None:
    import asyncio
    import json
    from urllib.parse import urlparse

    import httpx

    from norbix_python import AsyncNorbix

    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"templates": []})

    async def run() -> object:
        client = AsyncNorbix(
            project_id='test-project',
            bearer_token='test-token',
            account_id='acc-1',
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        try:
            return await client.hub.account.check_project_languages(project_id="proj-1", languages=["en"])
        finally:
            await client.aclose()

    assert asyncio.run(run()) == {"templates": []}
    assert [(r.method, urlparse(str(r.url)).path, json.loads(r.content)) for r in seen] == [
        ('POST', '/v2/account/projects/proj-1/settings/languages/check', {"languages": ["en"]}),
    ]
