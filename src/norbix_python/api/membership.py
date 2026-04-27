from __future__ import annotations

from typing import Any

from ..transport import Transport

class MembershipModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def blockUser(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/membership/users/block"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/block',
            method='PATCH',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveSystemUserWithPermissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/service"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/register/service',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveGuestUser(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/guest"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/register/guest',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveUserNameUser(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/user-name"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/register/user-name',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveEmailUser(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/email"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/register/email',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def savePhoneUser(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/phone"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/register/phone',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def savePhoneUserNameWithPermissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/phone-with-permissions"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/register/phone-with-permissions',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveEmailUserNameWithPermissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/email-with-permissions"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/register/email-with-permissions',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveUserNameWithPermissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/register/user-name-with-permissions"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/register/user-name-with-permissions',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteUser(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/membership/users"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getUser(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/users/{id}"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getUsers(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/users"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getUserPreferences(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/users/{id}/preferences"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/{id}/preferences',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def inviteUser(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/users/invite"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/invite',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def assignRolePermissions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/users/assign-roles"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/assign-roles',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def unblockUser(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/membership/users/unblock"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/unblock',
            method='PATCH',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateUser(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/users"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateUserPreferences(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/users/{id}/preferences"""
        return self._transport.send(
            target='api',
            path='/{version}/membership/users/{id}/preferences',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
