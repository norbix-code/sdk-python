from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_notifications_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.notifications
    assert callable(module.get_user_notification_preferences)
    assert callable(module.update_user_notifications_preferences)
    assert callable(module.disable_email)
    assert callable(module.enable_email)
    assert callable(module.attach_file_to_template)
    assert callable(module.create_email_template)
    assert callable(module.delete_email_template)
    assert callable(module.get_email_template)
    assert callable(module.get_email_templates)
    assert callable(module.get_mjml)
    assert callable(module.get_system_email_template)
    assert callable(module.get_system_email_templates)
    assert callable(module.get_email_template_available_tokens)
    assert callable(module.update_email_template)
    assert callable(module.delete_email_signature)
    assert callable(module.get_email_signature)
    assert callable(module.get_email_signatures)
    assert callable(module.save_email_signature)
    assert callable(module.get_email_settings)
    assert callable(module.confirm_email_integration_human_delivery)
    assert callable(module.delete_email_integration)
    assert callable(module.disable_email_integration)
    assert callable(module.enable_email_integration)
    assert callable(module.get_email_integration)
    assert callable(module.get_email_integrations)
    assert callable(module.save_email_integration)
    assert callable(module.set_emails_integration_as_default)
    assert callable(module.test_email_integration)
    assert callable(module.archive_email_template)
    assert callable(module.clone_email_template)
    assert callable(module.un_archive_email_template)
    assert callable(module.delete_email_footer)
    assert callable(module.get_email_footer)
    assert callable(module.get_email_footers)
    assert callable(module.save_email_footer)
    assert callable(module.create_email_campaign)
    assert callable(module.delete_email_campaign)
    assert callable(module.get_email_campaign)
    assert callable(module.get_email_campaigns)
    assert callable(module.get_email_campaign_batches)
    assert callable(module.get_email_campaign_batch_notification)
    assert callable(module.get_email_campaign_batch_notifications)
    assert callable(module.get_email_campaign_statistics)
    assert callable(module.preview_email_notification)
    assert callable(module.get_email_campaign_message)
    assert callable(module.get_email_campaign_messages)
    assert callable(module.disable_push)
    assert callable(module.enable_push)
    assert callable(module.archive_push_template)
    assert callable(module.clone_push_template)
    assert callable(module.create_push_template)
    assert callable(module.delete_push_template)
    assert callable(module.get_push_template)
    assert callable(module.get_push_templates)
    assert callable(module.get_push_message_content_tokens)
    assert callable(module.un_archive_push_template)
    assert callable(module.update_push_template)
    assert callable(module.confirm_push_integration_human_delivery)
    assert callable(module.delete_push_integration)
    assert callable(module.disable_push_integration)
    assert callable(module.enable_push_integration)
    assert callable(module.get_push_integration)
    assert callable(module.get_push_integrations)
    assert callable(module.save_push_integration)
    assert callable(module.set_push_integration_as_default)
    assert callable(module.test_push_integration)
    assert callable(module.register_code_mash_app_push_integration)
    assert callable(module.register_device)


def test_hub_notifications_get_user_notification_preferences_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_user_notification_preferences()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_update_user_notifications_preferences_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.update_user_notifications_preferences()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_disable_email_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.disable_email()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_enable_email_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.enable_email()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_attach_file_to_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.attach_file_to_template()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_create_email_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.create_email_template()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_delete_email_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.delete_email_template(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_template(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_templates_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_templates()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_mjml_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_mjml()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_system_email_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_system_email_template(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_system_email_templates_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_system_email_templates()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_template_available_tokens_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_template_available_tokens(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_update_email_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.update_email_template()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_delete_email_signature_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.delete_email_signature(id="stub-id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_signature_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_signature(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_signatures_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_signatures()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_save_email_signature_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.save_email_signature()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_settings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_settings()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_confirm_email_integration_human_delivery_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.confirm_email_integration_human_delivery()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_delete_email_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.delete_email_integration(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_disable_email_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.disable_email_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_enable_email_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.enable_email_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_save_email_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.save_email_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_set_emails_integration_as_default_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.set_emails_integration_as_default(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_test_email_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.test_email_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_archive_email_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.archive_email_template(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_clone_email_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.clone_email_template(id="stub-Id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_un_archive_email_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.un_archive_email_template(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_delete_email_footer_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.delete_email_footer(id="stub-id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_footer_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_footer(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_footers_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_footers()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_save_email_footer_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.save_email_footer()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_create_email_campaign_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.create_email_campaign()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_delete_email_campaign_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.delete_email_campaign(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_campaign_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_campaign(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_campaigns_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_campaigns()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_campaign_batches_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_campaign_batches(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_campaign_batch_notification_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_campaign_batch_notification(id="stub-id", batch_id="stub-batchId", notification_id="stub-notificationId")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_campaign_batch_notifications_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_campaign_batch_notifications(id="stub-id", batch_id="stub-batchId")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_campaign_statistics_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_campaign_statistics(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_preview_email_notification_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.preview_email_notification()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_campaign_message_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_campaign_message(campaign_id="stub-campaignId", id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_email_campaign_messages_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_email_campaign_messages(campaign_id="stub-campaignId")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_disable_push_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.disable_push()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_enable_push_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.enable_push()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_archive_push_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.archive_push_template(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_clone_push_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.clone_push_template(id="stub-Id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_create_push_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.create_push_template()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_delete_push_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.delete_push_template(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_push_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_template(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_push_templates_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_templates()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_push_message_content_tokens_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_message_content_tokens(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_un_archive_push_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.un_archive_push_template(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_update_push_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.update_push_template()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_confirm_push_integration_human_delivery_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.confirm_push_integration_human_delivery()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_delete_push_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.delete_push_integration(id="stub-Id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_disable_push_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.disable_push_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_enable_push_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.enable_push_integration(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_push_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_get_push_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_save_push_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.save_push_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_set_push_integration_as_default_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.set_push_integration_as_default(id="stub-Id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_test_push_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.test_push_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_register_code_mash_app_push_integration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1')
    client.hub.notifications.register_code_mash_app_push_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_register_code_mash_app_push_integration_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    try:
        client.hub.notifications.register_code_mash_app_push_integration()
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_notifications_register_device_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.register_device()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_new_endpoints_surface() -> None:
    client, _ = make_client()
    module = client.hub.notifications
    assert callable(module.get_all_contacts)
    assert callable(module.create_contact)
    assert callable(module.merge_contacts)
    assert callable(module.delete_contact)
    assert callable(module.get_contact)
    assert callable(module.add_contact_identity)
    assert callable(module.remove_contact_identity)
    assert callable(module.promote_contact_identity)
    assert callable(module.grant_contact_consent)
    assert callable(module.unsubscribe_contact)
    assert callable(module.razor_syntax_check)
    assert callable(module.save_email_validation_integration)
    assert callable(module.test_email_validation_integration)
    assert callable(module.get_push_campaigns)
    assert callable(module.create_push_campaign)
    assert callable(module.delete_push_campaign)
    assert callable(module.get_push_campaign_messages)
    assert callable(module.get_push_campaign_message)
    assert callable(module.get_push_campaign)
    assert callable(module.get_push_campaign_batches)
    assert callable(module.get_push_campaign_batch_notifications)
    assert callable(module.get_push_campaign_batch_notification)
    assert callable(module.get_push_campaign_statistics)
    assert callable(module.check_integration_availability)
    assert callable(module.test_code_mash_ios_app_integration)
    assert callable(module.get_push_settings)
    assert callable(module.get_sms_campaigns)
    assert callable(module.create_sms_campaign)
    assert callable(module.get_sms_campaign_messages)
    assert callable(module.get_sms_campaign_message)
    assert callable(module.delete_sms_campaign)
    assert callable(module.get_sms_campaign)
    assert callable(module.get_sms_campaign_batches)
    assert callable(module.get_sms_campaign_batch_notifications)
    assert callable(module.get_sms_campaign_batch_notification)
    assert callable(module.get_sms_campaign_statistics)
    assert callable(module.disable_sms)
    assert callable(module.enable_sms)
    assert callable(module.get_sms_integrations)
    assert callable(module.save_sms_integration)
    assert callable(module.confirm_sms_integration_human_delivery)
    assert callable(module.test_sms_integration)
    assert callable(module.delete_sms_integration)
    assert callable(module.set_sms_integration_as_default)
    assert callable(module.disable_sms_integration)
    assert callable(module.enable_sms_integration)
    assert callable(module.get_sms_integration)
    assert callable(module.preview_sms_notification)
    assert callable(module.get_sms_settings)
    assert callable(module.get_sms_templates)
    assert callable(module.create_sms_template)
    assert callable(module.update_sms_template)
    assert callable(module.sms_razor_syntax_check)
    assert callable(module.delete_sms_template)
    assert callable(module.archive_sms_template)
    assert callable(module.clone_sms_template)
    assert callable(module.un_archive_sms_template)
    assert callable(module.get_sms_template)
    assert callable(module.get_sms_message_content_tokens)


def test_hub_notifications_get_all_contacts_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_all_contacts()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_create_contact_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.create_contact()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_merge_contacts_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.merge_contacts()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_delete_contact_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.delete_contact(contact_id="stub-contact_id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_contact_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_contact(contact_id="stub-contact_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_add_contact_identity_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.add_contact_identity(contact_id="stub-contact_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_remove_contact_identity_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.remove_contact_identity(contact_id="stub-contact_id", identity_id="stub-identity_id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_promote_contact_identity_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.promote_contact_identity(contact_id="stub-contact_id", identity_id="stub-identity_id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_grant_contact_consent_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.grant_contact_consent(contact_id="stub-contact_id", channel="stub-channel")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_unsubscribe_contact_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.unsubscribe_contact(contact_id="stub-contact_id", channel="stub-channel")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_razor_syntax_check_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.razor_syntax_check()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_save_email_validation_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.save_email_validation_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_test_email_validation_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.test_email_validation_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_push_campaigns_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_campaigns()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_create_push_campaign_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.create_push_campaign()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_delete_push_campaign_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.delete_push_campaign(id="stub-id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_push_campaign_messages_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_campaign_messages(campaign_id="stub-campaign_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_push_campaign_message_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_campaign_message(campaign_id="stub-campaign_id", id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_push_campaign_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_campaign(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_push_campaign_batches_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_campaign_batches(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_push_campaign_batch_notifications_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_campaign_batch_notifications(id="stub-id", batch_id="stub-batch_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_push_campaign_batch_notification_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_campaign_batch_notification(id="stub-id", batch_id="stub-batch_id", notification_id="stub-notification_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_push_campaign_statistics_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_campaign_statistics(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_check_integration_availability_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.check_integration_availability()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_test_code_mash_ios_app_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.test_code_mash_ios_app_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_push_settings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_push_settings()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_campaigns_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_campaigns()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_create_sms_campaign_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.create_sms_campaign()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_campaign_messages_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_campaign_messages(campaign_id="stub-campaign_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_campaign_message_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_campaign_message(campaign_id="stub-campaign_id", id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_delete_sms_campaign_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.delete_sms_campaign(id="stub-id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_campaign_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_campaign(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_campaign_batches_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_campaign_batches(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_campaign_batch_notifications_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_campaign_batch_notifications(id="stub-id", batch_id="stub-batch_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_campaign_batch_notification_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_campaign_batch_notification(id="stub-id", batch_id="stub-batch_id", notification_id="stub-notification_id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_campaign_statistics_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_campaign_statistics(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_disable_sms_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.disable_sms()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_enable_sms_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.enable_sms()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_integrations_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_integrations()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_save_sms_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.save_sms_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_confirm_sms_integration_human_delivery_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.confirm_sms_integration_human_delivery()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_test_sms_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.test_sms_integration()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_delete_sms_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.delete_sms_integration(id="stub-id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_set_sms_integration_as_default_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.set_sms_integration_as_default(id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_disable_sms_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.disable_sms_integration(id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_enable_sms_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.enable_sms_integration(id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_integration_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_integration(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_preview_sms_notification_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.preview_sms_notification()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_settings_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_settings()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_templates_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_templates()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_create_sms_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.create_sms_template()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_update_sms_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.update_sms_template()
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_sms_razor_syntax_check_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.sms_razor_syntax_check()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_delete_sms_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.delete_sms_template(id="stub-id")
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_archive_sms_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.archive_sms_template(id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_clone_sms_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.clone_sms_template(id="stub-id")
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_un_archive_sms_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.un_archive_sms_template(id="stub-id")
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_template_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_template(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')


def test_hub_notifications_get_sms_message_content_tokens_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.notifications.get_sms_message_content_tokens(id="stub-id")
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

