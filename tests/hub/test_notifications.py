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
