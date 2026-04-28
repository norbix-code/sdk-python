from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

class MembershipModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def block_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/membership/users/block"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/block",
            method="PATCH",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_system_user_with_permissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/service"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/service",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_guest_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/guest"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/guest",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_user_name_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/user-name"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/user-name",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_email_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/email"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/email",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_phone_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/phone"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/phone",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_phone_user_name_with_permissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/phone-with-permissions"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/phone-with-permissions",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_email_user_name_with_permissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/email-with-permissions"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/email-with-permissions",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_user_name_with_permissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/user-name-with-permissions"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/register/user-name-with-permissions",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/membership/users"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users",
            method="DELETE",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_user(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/users/{id}"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_users(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/users"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_user_preferences(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/users/{id}/preferences"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/{id}/preferences",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def invite_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/invite"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/invite",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def assign_role_permissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/users/assign-roles"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/assign-roles",
            method="PUT",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def unblock_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/membership/users/unblock"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/unblock",
            method="PATCH",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/users"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users",
            method="PUT",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_user_preferences(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/users/{id}/preferences"""
        return self._transport.send(
            target="api",
            path="/{version}/membership/users/{id}/preferences",
            method="PUT",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncMembershipModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def block_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/membership/users/block"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/block",
            method="PATCH",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_system_user_with_permissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/service"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/service",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_guest_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/guest"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/guest",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_user_name_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/user-name"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/user-name",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_email_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/email"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/email",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_phone_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/phone"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/phone",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_phone_user_name_with_permissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/phone-with-permissions"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/phone-with-permissions",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_email_user_name_with_permissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/email-with-permissions"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/email-with-permissions",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_user_name_with_permissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/user-name-with-permissions"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/register/user-name-with-permissions",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/membership/users"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users",
            method="DELETE",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_user(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/users/{id}"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/{id}",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_users(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/users"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users",
            method="GET",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_user_preferences(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/users/{id}/preferences"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/{id}/preferences",
            method="GET",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def invite_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/invite"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/invite",
            method="POST",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def assign_role_permissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/users/assign-roles"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/assign-roles",
            method="PUT",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def unblock_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/membership/users/unblock"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/unblock",
            method="PATCH",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_user(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/users"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users",
            method="PUT",
            path_params={},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_user_preferences(self, id: str, *, request: dict[str, Any] | None = None, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/users/{id}/preferences"""
        return await self._transport.send(
            target="api",
            path="/{version}/membership/users/{id}/preferences",
            method="PUT",
            path_params={"id": id},
            request=request or {},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
