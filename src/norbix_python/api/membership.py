from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class MembershipModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def block_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/membership/users/block"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/block",
            method="PATCH",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_system_user_with_permissions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/service"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/service",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_guest_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/guest"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/guest",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_user_name_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/user-name"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/user-name",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_email_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/email"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/email",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_phone_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/phone"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/phone",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_phone_user_name_with_permissions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/phone-with-permissions"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/phone-with-permissions",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_email_user_name_with_permissions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/email-with-permissions"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/email-with-permissions",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_user_name_with_permissions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/user-name-with-permissions"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/user-name-with-permissions",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/users"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users",
            method="DELETE",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_user(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/users/{id}"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_users(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/users"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_user_preferences(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/users/{id}/preferences"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/{id}/preferences",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def invite_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/invite"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/invite",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def assign_role_permissions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/users/assign-roles"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/assign-roles",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def unblock_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/membership/users/unblock"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/unblock",
            method="PATCH",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/users"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_user_preferences(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/users/{id}/preferences"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/{id}/preferences",
            method="PUT",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def confirm_email_verification(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/email/confirm-verification"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/email/confirm-verification",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def start_email_verification(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/email/start-verification"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/email/start-verification",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def has_passkey(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/has-passkey"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/has-passkey",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def passkey_logout(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/logout"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/logout",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def passkey_authentication_options(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/passkey/authentication-options"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkey/authentication-options",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def passkey_registration_options(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/passkey/registration-options"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkey/registration-options",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def verify_passkey_authentication(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/passkey/verify-authentication"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkey/verify-authentication",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def verify_passkey_registration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/passkey/verify-registration"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkey/verify-registration",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def list_passkeys(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/userauth/passkeys"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkeys",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def rename_passkey(self, credential_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/passkeys/{CredentialId}/rename"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkeys/{CredentialId}/rename",
            method="POST",
            path_params={"CredentialId": credential_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def revoke_passkey(self, credential_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/passkeys/{CredentialId}/revoke"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkeys/{CredentialId}/revoke",
            method="POST",
            path_params={"CredentialId": credential_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def consume_magic_link(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/recovery/magic-link/consume"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/recovery/magic-link/consume",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def request_magic_link(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/recovery/magic-link/request"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/recovery/magic-link/request",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def use_recovery_code(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/recovery/use-code"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/recovery/use-code",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def refresh_passkey_token(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/token/refresh"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/userauth/token/refresh",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def link_identity(self, user_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/{userId}/link-identity"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/{userId}/link-identity",
            method="POST",
            path_params={"userId": user_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncMembershipModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def block_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/membership/users/block"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/block",
            method="PATCH",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_system_user_with_permissions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/service"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/service",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_guest_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/guest"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/guest",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_user_name_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/user-name"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/user-name",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_email_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/email"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/email",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_phone_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/phone"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/phone",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_phone_user_name_with_permissions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/phone-with-permissions"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/phone-with-permissions",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_email_user_name_with_permissions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/email-with-permissions"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/email-with-permissions",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_user_name_with_permissions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/register/user-name-with-permissions"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/user-name-with-permissions",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/membership/users"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users",
            method="DELETE",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_user(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/users/{id}"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_users(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/users"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_user_preferences(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/users/{id}/preferences"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/{id}/preferences",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def invite_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/invite"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/invite",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def assign_role_permissions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/users/assign-roles"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/assign-roles",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def unblock_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/membership/users/unblock"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/unblock",
            method="PATCH",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_user(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/users"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users",
            method="PUT",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_user_preferences(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/membership/users/{id}/preferences"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/{id}/preferences",
            method="PUT",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def confirm_email_verification(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/email/confirm-verification"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/email/confirm-verification",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def start_email_verification(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/email/start-verification"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/email/start-verification",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def has_passkey(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/has-passkey"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/has-passkey",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def passkey_logout(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/logout"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/logout",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def passkey_authentication_options(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/passkey/authentication-options"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkey/authentication-options",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def passkey_registration_options(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/passkey/registration-options"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkey/registration-options",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def verify_passkey_authentication(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/passkey/verify-authentication"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkey/verify-authentication",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def verify_passkey_registration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/passkey/verify-registration"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkey/verify-registration",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def list_passkeys(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/membership/userauth/passkeys"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkeys",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def rename_passkey(self, credential_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/passkeys/{CredentialId}/rename"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkeys/{CredentialId}/rename",
            method="POST",
            path_params={"CredentialId": credential_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def revoke_passkey(self, credential_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/passkeys/{CredentialId}/revoke"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/passkeys/{CredentialId}/revoke",
            method="POST",
            path_params={"CredentialId": credential_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def consume_magic_link(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/recovery/magic-link/consume"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/recovery/magic-link/consume",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def request_magic_link(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/recovery/magic-link/request"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/recovery/magic-link/request",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def use_recovery_code(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/recovery/use-code"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/recovery/use-code",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def refresh_passkey_token(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/userauth/token/refresh"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/userauth/token/refresh",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def link_identity(self, user_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/membership/users/{userId}/link-identity"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/{userId}/link-identity",
            method="POST",
            path_params={"userId": user_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
