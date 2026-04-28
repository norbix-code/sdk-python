from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

class NotificationsModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_user_notification_preferences(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/user/preferences"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/user/preferences",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_user_notifications_preferences(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/user/preferences"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/user/preferences",
            method="PUT",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_email(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/disable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_email(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/enable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def attach_file_to_template(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/templates/attachments"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/attachments",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_email_template(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/templates"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_email_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/templates/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/templates/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_templates(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/templates"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_mjml(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/templates/mjml"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/mjml",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_system_email_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/system-templates/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/system-templates/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_system_email_templates(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/system-templates"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/system-templates",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_template_available_tokens(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/templates/{id}/tokens"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/{id}/tokens",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_email_template(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/templates"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates",
            method="PUT",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_email_signature(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/signatures/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/signatures/{id}",
            method="DELETE",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_signature(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/signatures/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/signatures/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_signatures(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/signatures"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/signatures",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_email_signature(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/signatures"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/signatures",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_settings(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/settings"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/settings",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def confirm_email_integration_human_delivery(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/integrations/confirm-human-delivery"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/confirm-human-delivery",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_email_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/integrations/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_email_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/integrations/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_email_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/integrations/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/integrations/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_integrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_email_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def set_emails_integration_as_default(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/integrations/{Id}/default"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/{Id}/default",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_email_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/integrations/test"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/test",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def archive_email_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/templates/{Id}/archive"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/{Id}/archive",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def clone_email_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/templates/{Id}/clone"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/{Id}/clone",
            method="POST",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def un_archive_email_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/templates/{Id}/unarchive"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/{Id}/unarchive",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_email_footer(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/footers/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/footers/{id}",
            method="DELETE",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_footer(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/footers/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/footers/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_footers(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/footers"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/footers",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_email_footer(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/footers"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/footers",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_email_campaign(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/campaigns"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_email_campaign(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/campaigns/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaigns(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign_batches(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns/{id}/batches",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign_batch_notification(self, id: str, batch_id: str, notification_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id, "notificationId": notification_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign_batch_notifications(self, id: str, batch_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches/{batchId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns/{id}/batches/{batchId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign_statistics(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/stats"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns/{id}/stats",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def preview_email_notification(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/preview"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/email/preview",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign_message(self, campaign_id: str, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/emails/campaigns/{campaignId}/messages/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/emails/campaigns/{campaignId}/messages/{id}",
            method="GET",
            path_params={"campaignId": campaign_id, "id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign_messages(self, campaign_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/emails/campaigns/{campaignId}/messages"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/emails/campaigns/{campaignId}/messages",
            method="GET",
            path_params={"campaignId": campaign_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_push(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/disable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_push(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/enable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def archive_push_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/templates/{Id}/archive"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates/{Id}/archive",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def clone_push_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/templates/{Id}/clone"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates/{Id}/clone",
            method="POST",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_push_template(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/templates"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_push_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/push/templates/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/templates/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_templates(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/templates"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_message_content_tokens(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/templates/{id}/tokens"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates/{id}/tokens",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def un_archive_push_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/templates/{Id}/unarchive"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates/{Id}/unarchive",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_push_template(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/templates"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates",
            method="PUT",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def confirm_push_integration_human_delivery(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/integrations/confirm-human-delivery"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/confirm-human-delivery",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_push_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/push/integrations/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_push_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/integrations/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_push_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/integrations/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/integrations/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_integrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_push_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def set_push_integration_as_default(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/integrations/{Id}/default"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/{Id}/default",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_push_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/integrations/test"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/test",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def register_code_mash_app_push_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/integrations/app/request"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/app/request",
            method="POST",
            path_params={},
            request=request or {},
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def register_device(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/devices"""
        return self._transport.send(
            target="hub",
            path="/{version}/notifications/push/devices",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncNotificationsModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_user_notification_preferences(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/user/preferences"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/user/preferences",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_user_notifications_preferences(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/user/preferences"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/user/preferences",
            method="PUT",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_email(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/disable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_email(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/enable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def attach_file_to_template(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/templates/attachments"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/attachments",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_email_template(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/templates"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_email_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/templates/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/templates/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_templates(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/templates"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_mjml(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/templates/mjml"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/mjml",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_system_email_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/system-templates/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/system-templates/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_system_email_templates(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/system-templates"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/system-templates",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_template_available_tokens(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/templates/{id}/tokens"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/{id}/tokens",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_email_template(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/templates"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates",
            method="PUT",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_email_signature(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/signatures/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/signatures/{id}",
            method="DELETE",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_signature(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/signatures/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/signatures/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_signatures(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/signatures"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/signatures",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_email_signature(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/signatures"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/signatures",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_settings(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/settings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/settings",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def confirm_email_integration_human_delivery(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/integrations/confirm-human-delivery"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/confirm-human-delivery",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_email_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/integrations/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_email_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/integrations/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_email_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/integrations/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/integrations/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_integrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_email_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def set_emails_integration_as_default(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/integrations/{Id}/default"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/{Id}/default",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_email_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/integrations/test"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/integrations/test",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def archive_email_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/templates/{Id}/archive"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/{Id}/archive",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def clone_email_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/templates/{Id}/clone"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/{Id}/clone",
            method="POST",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def un_archive_email_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/email/templates/{Id}/unarchive"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/templates/{Id}/unarchive",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_email_footer(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/footers/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/footers/{id}",
            method="DELETE",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_footer(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/footers/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/footers/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_footers(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/footers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/footers",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_email_footer(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/footers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/footers",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_email_campaign(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/email/campaigns"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_email_campaign(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/email/campaigns/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaigns(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign_batches(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns/{id}/batches",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign_batch_notification(self, id: str, batch_id: str, notification_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id, "notificationId": notification_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign_batch_notifications(self, id: str, batch_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches/{batchId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns/{id}/batches/{batchId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign_statistics(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/stats"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/campaigns/{id}/stats",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def preview_email_notification(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/email/preview"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/email/preview",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign_message(self, campaign_id: str, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/emails/campaigns/{campaignId}/messages/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/emails/campaigns/{campaignId}/messages/{id}",
            method="GET",
            path_params={"campaignId": campaign_id, "id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign_messages(self, campaign_id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/emails/campaigns/{campaignId}/messages"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/emails/campaigns/{campaignId}/messages",
            method="GET",
            path_params={"campaignId": campaign_id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_push(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/disable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_push(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/enable",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def archive_push_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/templates/{Id}/archive"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates/{Id}/archive",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def clone_push_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/templates/{Id}/clone"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates/{Id}/clone",
            method="POST",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_push_template(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/templates"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_push_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/push/templates/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/templates/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_templates(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/templates"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_message_content_tokens(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/templates/{id}/tokens"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates/{id}/tokens",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def un_archive_push_template(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/templates/{Id}/unarchive"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates/{Id}/unarchive",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_push_template(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/templates"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/templates",
            method="PUT",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def confirm_push_integration_human_delivery(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/integrations/confirm-human-delivery"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/confirm-human-delivery",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_push_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/notifications/push/integrations/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_push_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/integrations/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_push_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/integrations/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_integration(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/integrations/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_integrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/notifications/push/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_push_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def set_push_integration_as_default(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/notifications/push/integrations/{Id}/default"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/{Id}/default",
            method="PUT",
            path_params={"Id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_push_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/integrations/test"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/test",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def register_code_mash_app_push_integration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/integrations/app/request"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/integrations/app/request",
            method="POST",
            path_params={},
            request=request or {},
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def register_device(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/notifications/push/devices"""
        return await self._transport.send(
            target="hub",
            path="/{version}/notifications/push/devices",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
