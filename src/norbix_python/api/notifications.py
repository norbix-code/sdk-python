"""Notifications on the Api (project scope): campaigns and the signed-in
user's own push devices and messages.

The campaign routes (Email, SMS, Push) are the same gateway services the Hub
serves — same paths, same bodies — so an app key can create, read, stop and
retry campaigns from the data API. Audience shapes: see ``docs/api/email.md``,
``docs/api/sms.md`` and ``docs/api/push.md``. The own-push routes (devices,
messages) are end-user routes: they always act on the caller's own rows.
"""

from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class NotificationsModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    # ---- Email campaigns (12 routes)

    def create_email_campaign(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/email/campaigns

        Pass the campaign under ``campaign`` (``templateId``, ``integrationId`` — the
        email provider — and ``source`` with that audience's own fields), plus the
        optional ``databaseIntegrationId`` and ``sendNow``. Same shape as
        ``hub.notifications.create_email_campaign``; answers ``{"id"}``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_email_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/notifications/email/campaigns/{Id}"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaigns(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/campaigns

        Query (all optional): ``campaignId``, ``emailAddress``, ``templateId``, ``from`` / ``to`` (Unix seconds), ``pageSize``, ``pageNumber``, ``databaseIntegrationId``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign_batches(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{id}/batches",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign_batch_notification(self, id: str, batch_id: str, notification_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id, "notificationId": notification_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign_batch_notifications(self, id: str, batch_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches/{batchId}"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{id}/batches/{batchId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign_statistics(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/stats"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{id}/stats",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def preview_email_notification(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/preview

        Opens with a signed link alone: pass ``hash=...`` and no credentials
        are needed. Auth is still sent when the client has a token. A signed-in
        member can pass ``projectId`` + ``notificationId`` instead of ``hash``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/email/preview",
            method="GET",
            path_params={},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def retry_failed_email_notifications(
        self,
        campaign_id: str,
        *,
        idempotency_key: str,
        notification_ids: list[str] | None = None,
        include_ambiguous: bool | None = None,
        categories: list[str] | None = None,
        database_integration_id: str | None = None,
        timeout: float | None = None,
        bearer_token: str | None = None,
        **request: Any,
    ) -> Any:
        """POST /{version}/notifications/email/campaigns/{Id}/retry-failed

        Sends the campaign's failed recipients again. Only recipients whose last
        attempt failed are selected; ``notification_ids`` narrows them to those
        rows, ``categories`` (``Transient`` | ``Permanent`` | ``Unknown``) to those
        failure kinds, and ``include_ambiguous=True`` also takes the rows whose
        provider answer never said whether the message went out — the answer then
        carries a ``warning`` that a duplicate may be sent. ``idempotency_key``
        (at most 64 characters) de-duplicates the request: the same key on the
        same campaign replays the first answer instead of selecting again.
        Answers ``{"retryRequestId", "selected", "skipped": {reason: count},
        "replayed", "warning"?}``. Unset options are not sent.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{Id}/retry-failed",
            method="POST",
            path_params={"Id": campaign_id},
            request={
                "idempotencyKey": idempotency_key,
                "notificationIds": notification_ids,
                "includeAmbiguous": include_ambiguous,
                "categories": categories,
                "databaseIntegrationId": database_integration_id,
                **request,
            },
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def stop_email_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/email/campaigns/{Id}/stop

        The campaign stops at its next batch; batches already sent stay sent.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{Id}/stop",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_email_campaign_messages(self, campaign_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/emails/campaigns/{campaignId}/messages

        Query: ``campaignBatchId`` (required by the gateway), ``pageSize``, ``pageNumber``, ``databaseIntegrationId``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/emails/campaigns/{campaignId}/messages",
            method="GET",
            path_params={"campaignId": campaign_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # ---- SMS campaigns (12 routes)

    def create_sms_campaign(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/sms/campaigns

        The request is flat: ``templateId``, ``integrationId`` (the SMS provider),
        ``deliveryType`` and the one settings object that matches it (``allUsers``,
        ``specifiedUsers``, ``accountUsers``, ``collection``, ``phoneNumbers``), plus the
        optional ``databaseIntegrationId``, ``language``, ``initiatorId``. Same shape
        as ``hub.notifications.create_sms_campaign``; answers ``{"id"}``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_sms_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/notifications/sms/campaigns/{id}"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{id}",
            method="DELETE",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_sms_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns/{id}"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_sms_campaigns(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns

        Query (all optional): ``campaignId``, ``templateId``, ``from`` / ``to`` (Unix seconds), ``pageSize``, ``pageNumber``, ``databaseIntegrationId``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_sms_campaign_batches(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns/{id}/batches"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{id}/batches",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_sms_campaign_batch_notification(self, id: str, batch_id: str, notification_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns/{id}/batches/{batchId}/{notificationId}"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{id}/batches/{batchId}/{notificationId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id, "notificationId": notification_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_sms_campaign_batch_notifications(self, id: str, batch_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns/{id}/batches/{batchId}"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{id}/batches/{batchId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_sms_campaign_statistics(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns/{id}/stats"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{id}/stats",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def preview_sms_notification(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/preview

        Opens with a signed link alone: pass ``hash=...`` and no credentials
        are needed. Auth is still sent when the client has a token. A signed-in
        member can pass ``projectId`` + ``notificationId`` instead of ``hash``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/sms/preview",
            method="GET",
            path_params={},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def retry_failed_sms_notifications(
        self,
        campaign_id: str,
        *,
        idempotency_key: str,
        notification_ids: list[str] | None = None,
        include_ambiguous: bool | None = None,
        categories: list[str] | None = None,
        database_integration_id: str | None = None,
        timeout: float | None = None,
        bearer_token: str | None = None,
        **request: Any,
    ) -> Any:
        """POST /{version}/notifications/sms/campaigns/{Id}/retry-failed

        Sends the campaign's failed recipients again. Only recipients whose last
        attempt failed are selected; ``notification_ids`` narrows them to those
        rows, ``categories`` (``Transient`` | ``Permanent`` | ``Unknown``) to those
        failure kinds, and ``include_ambiguous=True`` also takes the rows whose
        provider answer never said whether the message went out — the answer then
        carries a ``warning`` that a duplicate may be sent. ``idempotency_key``
        (at most 64 characters) de-duplicates the request: the same key on the
        same campaign replays the first answer instead of selecting again.
        Answers ``{"retryRequestId", "selected", "skipped": {reason: count},
        "replayed", "warning"?}``. Unset options are not sent.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{Id}/retry-failed",
            method="POST",
            path_params={"Id": campaign_id},
            request={
                "idempotencyKey": idempotency_key,
                "notificationIds": notification_ids,
                "includeAmbiguous": include_ambiguous,
                "categories": categories,
                "databaseIntegrationId": database_integration_id,
                **request,
            },
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def stop_sms_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/sms/campaigns/{Id}/stop

        The campaign stops at its next batch; batches already sent stay sent.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{Id}/stop",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_sms_campaign_messages(self, campaign_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns/{campaignId}/messages

        Query: ``campaignBatchId`` (required by the gateway), ``pageSize``, ``pageNumber``, ``databaseIntegrationId``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{campaignId}/messages",
            method="GET",
            path_params={"campaignId": campaign_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # ---- Push campaigns (13 routes)

    def create_push_campaign(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/push/campaigns

        Pass the campaign under ``campaign`` (``templateId``, ``integrationId`` — the
        push provider — and ``source`` with that audience's own fields), plus the
        optional ``databaseIntegrationId`` and ``sendNow``. Same shape as
        ``hub.notifications.create_push_campaign``; answers ``{"id"}``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_push_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/notifications/push/campaigns/{Id}"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns/{id}"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_campaigns(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns

        Query (all optional): ``templateId``, ``from`` / ``to`` (Unix seconds), ``pageSize``, ``pageNumber``, ``databaseIntegrationId``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_campaign_batches(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns/{id}/batches"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{id}/batches",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_campaign_batch_notification(self, id: str, batch_id: str, notification_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns/{id}/batches/{batchId}/{notificationId}"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{id}/batches/{batchId}/{notificationId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id, "notificationId": notification_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_campaign_batch_notifications(self, id: str, batch_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns/{id}/batches/{batchId}"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{id}/batches/{batchId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_campaign_statistics(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns/{id}/stats"""
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{id}/stats",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def preview_push_notification(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/preview

        Opens with a signed link alone: pass ``hash=...`` and no credentials
        are needed. Auth is still sent when the client has a token. A signed-in
        member can pass ``projectId`` + ``notificationId`` instead of ``hash``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/preview",
            method="GET",
            path_params={},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def retry_failed_push_notifications(
        self,
        campaign_id: str,
        *,
        idempotency_key: str,
        notification_ids: list[str] | None = None,
        include_ambiguous: bool | None = None,
        categories: list[str] | None = None,
        database_integration_id: str | None = None,
        timeout: float | None = None,
        bearer_token: str | None = None,
        **request: Any,
    ) -> Any:
        """POST /{version}/notifications/push/campaigns/{Id}/retry-failed

        Sends the campaign's failed recipients again. Only recipients whose last
        attempt failed are selected; ``notification_ids`` narrows them to those
        rows, ``categories`` (``Transient`` | ``Permanent`` | ``Unknown``) to those
        failure kinds, and ``include_ambiguous=True`` also takes the rows whose
        provider answer never said whether the message went out — the answer then
        carries a ``warning`` that a duplicate may be sent. ``idempotency_key``
        (at most 64 characters) de-duplicates the request: the same key on the
        same campaign replays the first answer instead of selecting again.
        Answers ``{"retryRequestId", "selected", "skipped": {reason: count},
        "replayed", "warning"?}``. Unset options are not sent.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{Id}/retry-failed",
            method="POST",
            path_params={"Id": campaign_id},
            request={
                "idempotencyKey": idempotency_key,
                "notificationIds": notification_ids,
                "includeAmbiguous": include_ambiguous,
                "categories": categories,
                "databaseIntegrationId": database_integration_id,
                **request,
            },
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def stop_push_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/push/campaigns/{Id}/stop

        The campaign stops at its next batch; batches already sent stay sent.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{Id}/stop",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_campaign_messages(self, campaign_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns/{campaignId}/messages

        Query: ``campaignBatchId`` (required by the gateway), ``pageSize``, ``pageNumber``, ``databaseIntegrationId``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{campaignId}/messages",
            method="GET",
            path_params={"campaignId": campaign_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_push_campaign_audience_count(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/push/campaigns/audience-count

        Counts the devices a campaign audience would reach before the campaign
        is created; nothing is sent. Pass the audience under ``campaign`` in the
        same shape ``create_push_campaign`` reads (``source`` plus that
        audience's own fields — the template and send options are ignored) and
        an optional ``databaseIntegrationId``. Answers ``{"result": {"devices",
        "recipients", "skippedUserIds", "isCapped"}}``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/audience-count",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # ---- Own push devices and messages (7 routes)

    def register_own_push_device(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/push/devices

        Registers (or refreshes) a push device for the signed-in user. Required:
        ``provider`` (``fcm`` or ``apns`` — the native token; an Expo push token,
        provider ``expo``, is refused with ``CM-ERRORS-PUSH-016``) and ``token``.
        Optional: ``platform`` (``ios`` / ``android`` / ``web``), ``osName``,
        ``osVersion``, ``appVersion``, ``deviceName``, ``modelName``, ``brand``,
        ``manufacturer``, ``installationId``, ``locale``, ``timeZone``. The same
        token again refreshes the device (same id); a token another user held
        moves to the caller. Answers ``{"id"}`` (``pnd_…``).
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/devices",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_own_push_devices(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/devices

        The caller's own push devices, last refreshed first: ``{"items": [...]}``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/devices",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_own_push_device(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/notifications/push/devices/{Id}

        Removes one of the caller's own devices by id (``pnd_…``). Another
        user's device is not found.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/devices/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_own_push_device_by_token(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/notifications/push/devices

        Sign-out from a device: removes the caller's device registered with
        ``token`` (required; sent as a query value, as every DELETE does). Safe to
        repeat.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/devices",
            method="DELETE",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_own_push_messages(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/messages

        The push messages sent to the caller, newest first, paged
        (``pageSize``, ``pageNumber``); ``unreadOnly=True`` keeps the unread ones.
        Answers ``{"list": {"items", "totalCount", ...}}``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/messages",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def mark_own_push_message_read(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/push/messages/{Id}/read

        Marks one of the caller's own messages (``ntf_…``) read. Safe to repeat.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/messages/{Id}/read",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def mark_all_own_push_messages_read(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/push/messages/read

        Marks every unread push message of the caller read.
        """
        return self._transport.send(
            target="api",
            path="/{version}/notifications/push/messages/read",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncNotificationsModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    # ---- Email campaigns (12 routes)

    async def create_email_campaign(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/email/campaigns — see :meth:`NotificationsModule.create_email_campaign`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_email_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/notifications/email/campaigns/{Id} — see :meth:`NotificationsModule.delete_email_campaign`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/campaigns/{id} — see :meth:`NotificationsModule.get_email_campaign`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaigns(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/campaigns — see :meth:`NotificationsModule.get_email_campaigns`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign_batches(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches — see :meth:`NotificationsModule.get_email_campaign_batches`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{id}/batches",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign_batch_notification(self, id: str, batch_id: str, notification_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId} — see :meth:`NotificationsModule.get_email_campaign_batch_notification`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id, "notificationId": notification_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign_batch_notifications(self, id: str, batch_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/batches/{batchId} — see :meth:`NotificationsModule.get_email_campaign_batch_notifications`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{id}/batches/{batchId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign_statistics(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/campaigns/{id}/stats — see :meth:`NotificationsModule.get_email_campaign_statistics`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{id}/stats",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def preview_email_notification(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/email/preview — see :meth:`NotificationsModule.preview_email_notification`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/email/preview",
            method="GET",
            path_params={},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def retry_failed_email_notifications(
        self,
        campaign_id: str,
        *,
        idempotency_key: str,
        notification_ids: list[str] | None = None,
        include_ambiguous: bool | None = None,
        categories: list[str] | None = None,
        database_integration_id: str | None = None,
        timeout: float | None = None,
        bearer_token: str | None = None,
        **request: Any,
    ) -> Any:
        """POST /{version}/notifications/email/campaigns/{Id}/retry-failed — see :meth:`NotificationsModule.retry_failed_email_notifications`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{Id}/retry-failed",
            method="POST",
            path_params={"Id": campaign_id},
            request={
                "idempotencyKey": idempotency_key,
                "notificationIds": notification_ids,
                "includeAmbiguous": include_ambiguous,
                "categories": categories,
                "databaseIntegrationId": database_integration_id,
                **request,
            },
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def stop_email_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/email/campaigns/{Id}/stop — see :meth:`NotificationsModule.stop_email_campaign`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/email/campaigns/{Id}/stop",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_email_campaign_messages(self, campaign_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/emails/campaigns/{campaignId}/messages — see :meth:`NotificationsModule.get_email_campaign_messages`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/emails/campaigns/{campaignId}/messages",
            method="GET",
            path_params={"campaignId": campaign_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # ---- SMS campaigns (12 routes)

    async def create_sms_campaign(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/sms/campaigns — see :meth:`NotificationsModule.create_sms_campaign`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_sms_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/notifications/sms/campaigns/{id} — see :meth:`NotificationsModule.delete_sms_campaign`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{id}",
            method="DELETE",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_sms_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns/{id} — see :meth:`NotificationsModule.get_sms_campaign`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_sms_campaigns(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns — see :meth:`NotificationsModule.get_sms_campaigns`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_sms_campaign_batches(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns/{id}/batches — see :meth:`NotificationsModule.get_sms_campaign_batches`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{id}/batches",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_sms_campaign_batch_notification(self, id: str, batch_id: str, notification_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns/{id}/batches/{batchId}/{notificationId} — see :meth:`NotificationsModule.get_sms_campaign_batch_notification`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{id}/batches/{batchId}/{notificationId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id, "notificationId": notification_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_sms_campaign_batch_notifications(self, id: str, batch_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns/{id}/batches/{batchId} — see :meth:`NotificationsModule.get_sms_campaign_batch_notifications`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{id}/batches/{batchId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_sms_campaign_statistics(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns/{id}/stats — see :meth:`NotificationsModule.get_sms_campaign_statistics`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{id}/stats",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def preview_sms_notification(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/preview — see :meth:`NotificationsModule.preview_sms_notification`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/sms/preview",
            method="GET",
            path_params={},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def retry_failed_sms_notifications(
        self,
        campaign_id: str,
        *,
        idempotency_key: str,
        notification_ids: list[str] | None = None,
        include_ambiguous: bool | None = None,
        categories: list[str] | None = None,
        database_integration_id: str | None = None,
        timeout: float | None = None,
        bearer_token: str | None = None,
        **request: Any,
    ) -> Any:
        """POST /{version}/notifications/sms/campaigns/{Id}/retry-failed — see :meth:`NotificationsModule.retry_failed_sms_notifications`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{Id}/retry-failed",
            method="POST",
            path_params={"Id": campaign_id},
            request={
                "idempotencyKey": idempotency_key,
                "notificationIds": notification_ids,
                "includeAmbiguous": include_ambiguous,
                "categories": categories,
                "databaseIntegrationId": database_integration_id,
                **request,
            },
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def stop_sms_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/sms/campaigns/{Id}/stop — see :meth:`NotificationsModule.stop_sms_campaign`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{Id}/stop",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_sms_campaign_messages(self, campaign_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/sms/campaigns/{campaignId}/messages — see :meth:`NotificationsModule.get_sms_campaign_messages`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/sms/campaigns/{campaignId}/messages",
            method="GET",
            path_params={"campaignId": campaign_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # ---- Push campaigns (13 routes)

    async def create_push_campaign(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/push/campaigns — see :meth:`NotificationsModule.create_push_campaign`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_push_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/notifications/push/campaigns/{Id} — see :meth:`NotificationsModule.delete_push_campaign`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns/{id} — see :meth:`NotificationsModule.get_push_campaign`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_campaigns(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns — see :meth:`NotificationsModule.get_push_campaigns`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_campaign_batches(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns/{id}/batches — see :meth:`NotificationsModule.get_push_campaign_batches`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{id}/batches",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_campaign_batch_notification(self, id: str, batch_id: str, notification_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns/{id}/batches/{batchId}/{notificationId} — see :meth:`NotificationsModule.get_push_campaign_batch_notification`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{id}/batches/{batchId}/{notificationId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id, "notificationId": notification_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_campaign_batch_notifications(self, id: str, batch_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns/{id}/batches/{batchId} — see :meth:`NotificationsModule.get_push_campaign_batch_notifications`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{id}/batches/{batchId}",
            method="GET",
            path_params={"id": id, "batchId": batch_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_campaign_statistics(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns/{id}/stats — see :meth:`NotificationsModule.get_push_campaign_statistics`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{id}/stats",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def preview_push_notification(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/preview — see :meth:`NotificationsModule.preview_push_notification`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/preview",
            method="GET",
            path_params={},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def retry_failed_push_notifications(
        self,
        campaign_id: str,
        *,
        idempotency_key: str,
        notification_ids: list[str] | None = None,
        include_ambiguous: bool | None = None,
        categories: list[str] | None = None,
        database_integration_id: str | None = None,
        timeout: float | None = None,
        bearer_token: str | None = None,
        **request: Any,
    ) -> Any:
        """POST /{version}/notifications/push/campaigns/{Id}/retry-failed — see :meth:`NotificationsModule.retry_failed_push_notifications`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{Id}/retry-failed",
            method="POST",
            path_params={"Id": campaign_id},
            request={
                "idempotencyKey": idempotency_key,
                "notificationIds": notification_ids,
                "includeAmbiguous": include_ambiguous,
                "categories": categories,
                "databaseIntegrationId": database_integration_id,
                **request,
            },
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def stop_push_campaign(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/push/campaigns/{Id}/stop — see :meth:`NotificationsModule.stop_push_campaign`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{Id}/stop",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_campaign_messages(self, campaign_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/campaigns/{campaignId}/messages — see :meth:`NotificationsModule.get_push_campaign_messages`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/{campaignId}/messages",
            method="GET",
            path_params={"campaignId": campaign_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_push_campaign_audience_count(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/push/campaigns/audience-count — see :meth:`NotificationsModule.get_push_campaign_audience_count`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/campaigns/audience-count",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    # ---- Own push devices and messages (7 routes)

    async def register_own_push_device(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/push/devices — see :meth:`NotificationsModule.register_own_push_device`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/devices",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_own_push_devices(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/devices — see :meth:`NotificationsModule.get_own_push_devices`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/devices",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_own_push_device(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/notifications/push/devices/{Id} — see :meth:`NotificationsModule.delete_own_push_device`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/devices/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_own_push_device_by_token(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/notifications/push/devices — see :meth:`NotificationsModule.delete_own_push_device_by_token`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/devices",
            method="DELETE",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_own_push_messages(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/notifications/push/messages — see :meth:`NotificationsModule.get_own_push_messages`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/messages",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def mark_own_push_message_read(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/push/messages/{Id}/read — see :meth:`NotificationsModule.mark_own_push_message_read`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/messages/{Id}/read",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def mark_all_own_push_messages_read(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/notifications/push/messages/read — see :meth:`NotificationsModule.mark_all_own_push_messages_read`."""
        return await self._transport.send(
            target="api",
            path="/{version}/notifications/push/messages/read",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
