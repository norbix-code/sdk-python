from __future__ import annotations

from typing import Any

from ..transport import Transport

class NotificationsModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def getUserNotificationPreferences(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/user/preferences"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/user/preferences',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateUserNotificationsPreferences(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/user/preferences"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/user/preferences',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableEmail(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/disable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableEmail(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/enable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def attachFileToTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/templates/attachments"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/templates/attachments',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def createEmailTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/templates"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/templates',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteEmailTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/templates/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/templates/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/templates/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/templates/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailTemplates(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/templates"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/templates',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getMjml(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/templates/mjml"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/templates/mjml',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getSystemEmailTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/system-templates/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/system-templates/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getSystemEmailTemplates(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/system-templates"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/system-templates',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailTemplateAvailableTokens(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/templates/{id}/tokens"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/templates/{id}/tokens',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateEmailTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/templates"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/templates',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteEmailSignature(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/signatures/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/signatures/{id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailSignature(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/signatures/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/signatures/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailSignatures(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/signatures"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/signatures',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveEmailSignature(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/signatures"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/signatures',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailSettings(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/settings"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/settings',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def confirmEmailIntegrationHumanDelivery(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/integrations/confirm-human-delivery"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/integrations/confirm-human-delivery',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteEmailIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/integrations/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/integrations/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableEmailIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/integrations/{Id}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/integrations/{Id}/disable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableEmailIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/integrations/{Id}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/integrations/{Id}/enable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/integrations/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/integrations/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailIntegrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/integrations',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveEmailIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/integrations',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def setEmailsIntegrationAsDefault(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/integrations/{Id}/default"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/integrations/{Id}/default',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def testEmailIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/integrations/test"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/integrations/test',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def archiveEmailTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/templates/{Id}/archive"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/templates/{Id}/archive',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def cloneEmailTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/templates/{Id}/clone"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/templates/{Id}/clone',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def unArchiveEmailTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/templates/{Id}/unarchive"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/templates/{Id}/unarchive',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteEmailFooter(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/footers/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/footers/{id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailFooter(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/footers/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/footers/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailFooters(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/footers"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/footers',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveEmailFooter(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/footers"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/footers',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def createEmailCampaign(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/campaigns"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/campaigns',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteEmailCampaign(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/campaigns/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/campaigns/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailCampaign(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/campaigns/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailCampaigns(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/campaigns',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailCampaignBatches(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/campaigns/{id}/batches',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailCampaignBatchNotification(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailCampaignBatchNotifications(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches/{batchId}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/campaigns/{id}/batches/{batchId}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailCampaignStatistics(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/stats"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/campaigns/{id}/stats',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def previewEmailNotification(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/preview"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/email/preview',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailCampaignMessage(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/emails/campaigns/{campaignId}/messages/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/emails/campaigns/{campaignId}/messages/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getEmailCampaignMessages(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/emails/campaigns/{campaignId}/messages"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/emails/campaigns/{campaignId}/messages',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disablePush(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/disable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enablePush(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/enable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def archivePushTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/templates/{Id}/archive"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/templates/{Id}/archive',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def clonePushTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/templates/{Id}/clone"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/templates/{Id}/clone',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def createPushTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/templates"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/templates',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deletePushTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/push/templates/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/templates/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getPushTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/templates/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/templates/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getPushTemplates(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/templates"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/templates',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getPushMessageContentTokens(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/templates/{id}/tokens"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/templates/{id}/tokens',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def unArchivePushTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/templates/{Id}/unarchive"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/templates/{Id}/unarchive',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updatePushTemplate(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/templates"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/templates',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def confirmPushIntegrationHumanDelivery(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/integrations/confirm-human-delivery"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/integrations/confirm-human-delivery',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deletePushIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/push/integrations/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/integrations/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disablePushIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/integrations/{Id}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/integrations/{Id}/disable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enablePushIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/integrations/{Id}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/integrations/{Id}/enable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getPushIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/integrations/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/integrations/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getPushIntegrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/integrations',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def savePushIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/integrations',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def setPushIntegrationAsDefault(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/integrations/{Id}/default"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/integrations/{Id}/default',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def testPushIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/integrations/test"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/integrations/test',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def registerCodeMashAppPushIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/integrations/app/request"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/integrations/app/request',
            method='POST',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def registerDevice(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/devices"""
        return self._transport.send(
            target='hub',
            path='/{version}/notifications/push/devices',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
