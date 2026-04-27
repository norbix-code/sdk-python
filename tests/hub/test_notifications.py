from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_hub_notifications_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.notifications
    assert callable(module.getUserNotificationPreferences)
    assert callable(module.updateUserNotificationsPreferences)
    assert callable(module.disableEmail)
    assert callable(module.enableEmail)
    assert callable(module.attachFileToTemplate)
    assert callable(module.createEmailTemplate)
    assert callable(module.deleteEmailTemplate)
    assert callable(module.getEmailTemplate)
    assert callable(module.getEmailTemplates)
    assert callable(module.getMjml)
    assert callable(module.getSystemEmailTemplate)
    assert callable(module.getSystemEmailTemplates)
    assert callable(module.getEmailTemplateAvailableTokens)
    assert callable(module.updateEmailTemplate)
    assert callable(module.deleteEmailSignature)
    assert callable(module.getEmailSignature)
    assert callable(module.getEmailSignatures)
    assert callable(module.saveEmailSignature)
    assert callable(module.getEmailSettings)
    assert callable(module.confirmEmailIntegrationHumanDelivery)
    assert callable(module.deleteEmailIntegration)
    assert callable(module.disableEmailIntegration)
    assert callable(module.enableEmailIntegration)
    assert callable(module.getEmailIntegration)
    assert callable(module.getEmailIntegrations)
    assert callable(module.saveEmailIntegration)
    assert callable(module.setEmailsIntegrationAsDefault)
    assert callable(module.testEmailIntegration)
    assert callable(module.archiveEmailTemplate)
    assert callable(module.cloneEmailTemplate)
    assert callable(module.unArchiveEmailTemplate)
    assert callable(module.deleteEmailFooter)
    assert callable(module.getEmailFooter)
    assert callable(module.getEmailFooters)
    assert callable(module.saveEmailFooter)
    assert callable(module.createEmailCampaign)
    assert callable(module.deleteEmailCampaign)
    assert callable(module.getEmailCampaign)
    assert callable(module.getEmailCampaigns)
    assert callable(module.getEmailCampaignBatches)
    assert callable(module.getEmailCampaignBatchNotification)
    assert callable(module.getEmailCampaignBatchNotifications)
    assert callable(module.getEmailCampaignStatistics)
    assert callable(module.previewEmailNotification)
    assert callable(module.getEmailCampaignMessage)
    assert callable(module.getEmailCampaignMessages)
    assert callable(module.disablePush)
    assert callable(module.enablePush)
    assert callable(module.archivePushTemplate)
    assert callable(module.clonePushTemplate)
    assert callable(module.createPushTemplate)
    assert callable(module.deletePushTemplate)
    assert callable(module.getPushTemplate)
    assert callable(module.getPushTemplates)
    assert callable(module.getPushMessageContentTokens)
    assert callable(module.unArchivePushTemplate)
    assert callable(module.updatePushTemplate)
    assert callable(module.confirmPushIntegrationHumanDelivery)
    assert callable(module.deletePushIntegration)
    assert callable(module.disablePushIntegration)
    assert callable(module.enablePushIntegration)
    assert callable(module.getPushIntegration)
    assert callable(module.getPushIntegrations)
    assert callable(module.savePushIntegration)
    assert callable(module.setPushIntegrationAsDefault)
    assert callable(module.testPushIntegration)
    assert callable(module.registerCodeMashAppPushIntegration)
    assert callable(module.registerDevice)


def test_hub_notifications_getUserNotificationPreferences_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/user/preferences') if False else {}
    client.hub.notifications.getUserNotificationPreferences(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_updateUserNotificationsPreferences_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/user/preferences') if False else {}
    client.hub.notifications.updateUserNotificationsPreferences(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_disableEmail_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/disable') if False else {}
    client.hub.notifications.disableEmail(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_enableEmail_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/enable') if False else {}
    client.hub.notifications.enableEmail(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_attachFileToTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/templates/attachments') if False else {}
    client.hub.notifications.attachFileToTemplate(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_createEmailTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/templates') if False else {}
    client.hub.notifications.createEmailTemplate(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_deleteEmailTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/templates/{Id}') if True else {}
    client.hub.notifications.deleteEmailTemplate(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/templates/{id}') if True else {}
    client.hub.notifications.getEmailTemplate(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailTemplates_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/templates') if False else {}
    client.hub.notifications.getEmailTemplates(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getMjml_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/templates/mjml') if False else {}
    client.hub.notifications.getMjml(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getSystemEmailTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/system-templates/{id}') if True else {}
    client.hub.notifications.getSystemEmailTemplate(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getSystemEmailTemplates_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/system-templates') if False else {}
    client.hub.notifications.getSystemEmailTemplates(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailTemplateAvailableTokens_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/templates/{id}/tokens') if True else {}
    client.hub.notifications.getEmailTemplateAvailableTokens(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_updateEmailTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/templates') if False else {}
    client.hub.notifications.updateEmailTemplate(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_deleteEmailSignature_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/signatures/{id}') if True else {}
    client.hub.notifications.deleteEmailSignature(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailSignature_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/signatures/{id}') if True else {}
    client.hub.notifications.getEmailSignature(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailSignatures_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/signatures') if False else {}
    client.hub.notifications.getEmailSignatures(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_saveEmailSignature_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/signatures') if False else {}
    client.hub.notifications.saveEmailSignature(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailSettings_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/settings') if False else {}
    client.hub.notifications.getEmailSettings(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_confirmEmailIntegrationHumanDelivery_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/integrations/confirm-human-delivery') if False else {}
    client.hub.notifications.confirmEmailIntegrationHumanDelivery(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_deleteEmailIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/integrations/{Id}') if True else {}
    client.hub.notifications.deleteEmailIntegration(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_disableEmailIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/integrations/{Id}/disable') if True else {}
    client.hub.notifications.disableEmailIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_enableEmailIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/integrations/{Id}/enable') if True else {}
    client.hub.notifications.enableEmailIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/integrations/{id}') if True else {}
    client.hub.notifications.getEmailIntegration(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailIntegrations_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/integrations') if False else {}
    client.hub.notifications.getEmailIntegrations(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_saveEmailIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/integrations') if False else {}
    client.hub.notifications.saveEmailIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_setEmailsIntegrationAsDefault_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/integrations/{Id}/default') if True else {}
    client.hub.notifications.setEmailsIntegrationAsDefault(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_testEmailIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/integrations/test') if False else {}
    client.hub.notifications.testEmailIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_archiveEmailTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/templates/{Id}/archive') if True else {}
    client.hub.notifications.archiveEmailTemplate(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_cloneEmailTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/templates/{Id}/clone') if True else {}
    client.hub.notifications.cloneEmailTemplate(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_unArchiveEmailTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/templates/{Id}/unarchive') if True else {}
    client.hub.notifications.unArchiveEmailTemplate(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_deleteEmailFooter_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/footers/{id}') if True else {}
    client.hub.notifications.deleteEmailFooter(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailFooter_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/footers/{id}') if True else {}
    client.hub.notifications.getEmailFooter(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailFooters_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/footers') if False else {}
    client.hub.notifications.getEmailFooters(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_saveEmailFooter_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/footers') if False else {}
    client.hub.notifications.saveEmailFooter(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_createEmailCampaign_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/campaigns') if False else {}
    client.hub.notifications.createEmailCampaign(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_deleteEmailCampaign_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/campaigns/{Id}') if True else {}
    client.hub.notifications.deleteEmailCampaign(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailCampaign_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/campaigns/{id}') if True else {}
    client.hub.notifications.getEmailCampaign(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailCampaigns_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/campaigns') if False else {}
    client.hub.notifications.getEmailCampaigns(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailCampaignBatches_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/campaigns/{id}/batches') if True else {}
    client.hub.notifications.getEmailCampaignBatches(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailCampaignBatchNotification_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}') if True else {}
    client.hub.notifications.getEmailCampaignBatchNotification(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailCampaignBatchNotifications_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/campaigns/{id}/batches/{batchId}') if True else {}
    client.hub.notifications.getEmailCampaignBatchNotifications(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailCampaignStatistics_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/campaigns/{id}/stats') if True else {}
    client.hub.notifications.getEmailCampaignStatistics(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_previewEmailNotification_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/email/preview') if False else {}
    client.hub.notifications.previewEmailNotification(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailCampaignMessage_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/emails/campaigns/{campaignId}/messages/{id}') if True else {}
    client.hub.notifications.getEmailCampaignMessage(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getEmailCampaignMessages_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/emails/campaigns/{campaignId}/messages') if True else {}
    client.hub.notifications.getEmailCampaignMessages(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_disablePush_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/disable') if False else {}
    client.hub.notifications.disablePush(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_enablePush_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/enable') if False else {}
    client.hub.notifications.enablePush(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_archivePushTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/templates/{Id}/archive') if True else {}
    client.hub.notifications.archivePushTemplate(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_clonePushTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/templates/{Id}/clone') if True else {}
    client.hub.notifications.clonePushTemplate(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_createPushTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/templates') if False else {}
    client.hub.notifications.createPushTemplate(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_deletePushTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/templates/{Id}') if True else {}
    client.hub.notifications.deletePushTemplate(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getPushTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/templates/{id}') if True else {}
    client.hub.notifications.getPushTemplate(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getPushTemplates_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/templates') if False else {}
    client.hub.notifications.getPushTemplates(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getPushMessageContentTokens_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/templates/{id}/tokens') if True else {}
    client.hub.notifications.getPushMessageContentTokens(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_unArchivePushTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/templates/{Id}/unarchive') if True else {}
    client.hub.notifications.unArchivePushTemplate(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_updatePushTemplate_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/templates') if False else {}
    client.hub.notifications.updatePushTemplate(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_confirmPushIntegrationHumanDelivery_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/integrations/confirm-human-delivery') if False else {}
    client.hub.notifications.confirmPushIntegrationHumanDelivery(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_deletePushIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/integrations/{Id}') if True else {}
    client.hub.notifications.deletePushIntegration(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_disablePushIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/integrations/{Id}/disable') if True else {}
    client.hub.notifications.disablePushIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_enablePushIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/integrations/{Id}/enable') if True else {}
    client.hub.notifications.enablePushIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getPushIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/integrations/{id}') if True else {}
    client.hub.notifications.getPushIntegration(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_getPushIntegrations_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/integrations') if False else {}
    client.hub.notifications.getPushIntegrations(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_savePushIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/integrations') if False else {}
    client.hub.notifications.savePushIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_setPushIntegrationAsDefault_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/integrations/{Id}/default') if True else {}
    client.hub.notifications.setPushIntegrationAsDefault(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_testPushIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/integrations/test') if False else {}
    client.hub.notifications.testPushIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_registerCodeMashAppPushIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if True else None)
    payload = stub_request_for_path('/{version}/notifications/push/integrations/app/request') if False else {}
    client.hub.notifications.registerCodeMashAppPushIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_notifications_registerCodeMashAppPushIntegration_requires_account_scope() -> None:
    client = Norbix(project_id='p1', bearer_token='token')
    payload = stub_request_for_path('/{version}/notifications/push/integrations/app/request') if False else {}
    try:
        client.hub.notifications.registerCodeMashAppPushIntegration(payload)
    except NorbixError as exc:
        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'
    else:
        raise AssertionError('Expected account scope error')

def test_hub_notifications_registerDevice_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/notifications/push/devices') if False else {}
    client.hub.notifications.registerDevice(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
