from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class MembershipModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def enable_membership(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/enable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_membership_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/triggers/{triggerId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/triggers/{triggerId}",
            method="DELETE",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_membership_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/membership/triggers/{triggerId}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/triggers/{triggerId}/disable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_membership_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/membership/triggers/{triggerId}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/triggers/{triggerId}/enable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_membership_trigger(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/triggers/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/triggers/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_membership_triggers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/triggers"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/triggers",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_execution_identities(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/execution-identities

        Lists the service users of the environment that a trigger, a scheduled task
        or a workflow can run as, the default identity first. ``canAssign`` says
        whether the caller may name one.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/execution-identities",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_execution_identity(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/execution-identities

        Creates a service user (``name=...``) and gives it roles (``roleIds=[...]``:
        role ids or role names) in one call. Returns the new id.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/execution-identities",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_membership_trigger(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/triggers"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/triggers",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_role(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/roles"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/roles",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_role(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/roles"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/roles",
            method="DELETE",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_role(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/roles/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/roles/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_roles(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/roles"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/roles",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_role_policies(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/membership/roles"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/roles",
            method="PATCH",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_policy(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/policies"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/policies",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_policy(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/policies"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/policies",
            method="DELETE",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_policy(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/policies/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/policies/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_policies(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/policies"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/policies",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_policy(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/policies"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/policies",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_membership_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/integrations/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_membership_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/integrations/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_membership_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/integrations/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_membership_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/integrations/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_membership_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_membership_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/integrations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_passkey_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/passkey/settings"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/passkey/settings",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_passkey_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/passkey/settings"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/passkey/settings",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_contact(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_all_contacts(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/users"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_contact(self, contact_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/users/{contactId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}",
            method="GET",
            path_params={"contactId": contact_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_contact(self, contact_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/users/{contactId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}",
            method="DELETE",
            path_params={"contactId": contact_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def merge_contacts(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/merge"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/merge",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def add_contact_identity(self, contact_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/{contactId}/identities"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}/identities",
            method="POST",
            path_params={"contactId": contact_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def remove_contact_identity(
        self, contact_id: str, auth_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any
    ) -> Any:
        """DELETE /{version}/membership/users/{contactId}/identities/{authId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}/identities/{authId}",
            method="DELETE",
            path_params={"contactId": contact_id, "authId": auth_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def promote_contact_identity(
        self, contact_id: str, auth_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any
    ) -> Any:
        """POST /{version}/membership/users/{contactId}/identities/{authId}/promote"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}/identities/{authId}/promote",
            method="POST",
            path_params={"contactId": contact_id, "authId": auth_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_authentication_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/authentication"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/authentication",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_password_complexity(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/authorization/password-complexity"""
        return self._transport.send(
            target="hub",
            path="/{version}/membership/authorization/password-complexity",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def import_users(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/import

        Imports users in one call: ``users`` rows, ``ignoreDefaultRoles``, ``dryRun``.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/import",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def repair_login_project_ids(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/repair-logins

        Repairs the project ids of the sign-in records; ``dryRun=True`` reports without writing.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/repair-logins",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_authentication_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/authentication

        Reads the sign-in settings: logout URL, user names, credential modes.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/authentication",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_authorization_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/authorization

        Reads the registration, invitation, verification and password settings.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/authorization",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_authorization_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/authorization

        Saves the registration, invitation, verification and password settings.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/authorization",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def list_service_user_api_keys(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/users/{Id}/api-keys

        Lists the API keys of a service user.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/{Id}/api-keys",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def issue_service_user_api_key(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/{Id}/api-keys

        Issues an API key for a service user: ``name``, ``scopes``, ``expiresInDays``, ``notes``. The key text is in the answer once.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/{Id}/api-keys",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_service_user_api_key(self, id: str, key_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/users/{Id}/api-keys/{KeyId}

        Deletes one API key of a service user.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/{Id}/api-keys/{KeyId}",
            method="DELETE",
            path_params={"Id": id, "KeyId": key_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def repair_contact_roles(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/repair-roles

        Repairs the roles of every contact; ``dryRun=True`` reports without writing.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/repair-roles",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_contact(self, contact_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/membership/users/{contactId}

        Changes the profile fields of a contact (``displayName``, ``firstName``, ``company``, ``language`` …).
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}",
            method="PATCH",
            path_params={"contactId": contact_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def clear_contact_bounce(self, contact_id: str, channel: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/{contactId}/marketing-state/{channel}/clear-bounce

        Clears the bounce flag of the contact on a channel (``Email``, ``Sms``, ``Push``).
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}/marketing-state/{channel}/clear-bounce",
            method="POST",
            path_params={"contactId": contact_id, "channel": channel},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def set_user_ai_plan(self, user_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/users/{userId}/ai-plan

        Gives the user an AI plan (``planId``).
        """
        return self._transport.send(
            target="hub",
            path="/{version}/membership/users/{userId}/ai-plan",
            method="PUT",
            path_params={"userId": user_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncMembershipModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def enable_membership(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/enable",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_membership_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/triggers/{triggerId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/triggers/{triggerId}",
            method="DELETE",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_membership_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/membership/triggers/{triggerId}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/triggers/{triggerId}/disable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_membership_trigger(self, trigger_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/membership/triggers/{triggerId}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/triggers/{triggerId}/enable",
            method="PATCH",
            path_params={"triggerId": trigger_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_membership_trigger(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/triggers/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/triggers/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_membership_triggers(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/triggers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/triggers",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_execution_identities(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/execution-identities

        Lists the service users of the environment that a trigger, a scheduled task
        or a workflow can run as, the default identity first. ``canAssign`` says
        whether the caller may name one.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/execution-identities",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_execution_identity(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/execution-identities

        Creates a service user (``name=...``) and gives it roles (``roleIds=[...]``:
        role ids or role names) in one call. Returns the new id.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/execution-identities",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_membership_trigger(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/triggers"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/triggers",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_role(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/roles"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/roles",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_role(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/roles"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/roles",
            method="DELETE",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_role(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/roles/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/roles/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_roles(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/roles"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/roles",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_role_policies(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/membership/roles"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/roles",
            method="PATCH",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_policy(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/policies"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/policies",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_policy(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/policies"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/policies",
            method="DELETE",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_policy(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/policies/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/policies/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_policies(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/policies"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/policies",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_policy(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/policies"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/policies",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_membership_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/integrations/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/integrations/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_membership_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/integrations/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/integrations/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_membership_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/integrations/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/integrations/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_membership_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/integrations/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/integrations/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_membership_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_membership_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/integrations",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_passkey_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/passkey/settings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/passkey/settings",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_passkey_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/passkey/settings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/passkey/settings",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_contact(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_all_contacts(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/users"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_contact(self, contact_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/users/{contactId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}",
            method="GET",
            path_params={"contactId": contact_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_contact(self, contact_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/users/{contactId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}",
            method="DELETE",
            path_params={"contactId": contact_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def merge_contacts(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/merge"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/merge",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def add_contact_identity(self, contact_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/{contactId}/identities"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}/identities",
            method="POST",
            path_params={"contactId": contact_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def remove_contact_identity(
        self, contact_id: str, auth_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any
    ) -> Any:
        """DELETE /{version}/membership/users/{contactId}/identities/{authId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}/identities/{authId}",
            method="DELETE",
            path_params={"contactId": contact_id, "authId": auth_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def promote_contact_identity(
        self, contact_id: str, auth_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any
    ) -> Any:
        """POST /{version}/membership/users/{contactId}/identities/{authId}/promote"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}/identities/{authId}/promote",
            method="POST",
            path_params={"contactId": contact_id, "authId": auth_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_authentication_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/authentication"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/authentication",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_password_complexity(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/authorization/password-complexity"""
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/authorization/password-complexity",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def import_users(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/import

        Imports users in one call: ``users`` rows, ``ignoreDefaultRoles``, ``dryRun``.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/import",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def repair_login_project_ids(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/repair-logins

        Repairs the project ids of the sign-in records; ``dryRun=True`` reports without writing.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/repair-logins",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_authentication_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/authentication

        Reads the sign-in settings: logout URL, user names, credential modes.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/authentication",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_authorization_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/authorization

        Reads the registration, invitation, verification and password settings.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/authorization",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_authorization_settings(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/authorization

        Saves the registration, invitation, verification and password settings.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/authorization",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def list_service_user_api_keys(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/users/{Id}/api-keys

        Lists the API keys of a service user.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/{Id}/api-keys",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def issue_service_user_api_key(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/{Id}/api-keys

        Issues an API key for a service user: ``name``, ``scopes``, ``expiresInDays``, ``notes``. The key text is in the answer once.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/{Id}/api-keys",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_service_user_api_key(self, id: str, key_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/users/{Id}/api-keys/{KeyId}

        Deletes one API key of a service user.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/{Id}/api-keys/{KeyId}",
            method="DELETE",
            path_params={"Id": id, "KeyId": key_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def repair_contact_roles(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/repair-roles

        Repairs the roles of every contact; ``dryRun=True`` reports without writing.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/repair-roles",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_contact(self, contact_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/membership/users/{contactId}

        Changes the profile fields of a contact (``displayName``, ``firstName``, ``company``, ``language`` …).
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}",
            method="PATCH",
            path_params={"contactId": contact_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def clear_contact_bounce(self, contact_id: str, channel: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/{contactId}/marketing-state/{channel}/clear-bounce

        Clears the bounce flag of the contact on a channel (``Email``, ``Sms``, ``Push``).
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/{contactId}/marketing-state/{channel}/clear-bounce",
            method="POST",
            path_params={"contactId": contact_id, "channel": channel},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def set_user_ai_plan(self, user_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/users/{userId}/ai-plan

        Gives the user an AI plan (``planId``).
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/membership/users/{userId}/ai-plan",
            method="PUT",
            path_params={"userId": user_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
