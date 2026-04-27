from __future__ import annotations

from typing import Any

from ..transport import Transport

class AccountModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def getAccountProfile(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/account/profile"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/profile',
            method='GET',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateAccountProfile(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/account/profile"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/profile',
            method='PUT',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def resendAccountVerificationToken(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/account/verify/resend"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/verify/resend',
            method='GET',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getAccountStatus(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/account/status"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/status',
            method='GET',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def createStripeCheckoutSession(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/account/stripe/create-checkout-session"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/stripe/create-checkout-session',
            method='POST',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getStripeBillingPortalUrl(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/account/stripe/get-portal-url"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/stripe/get-portal-url',
            method='POST',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def createTeamMemberFromInvitation(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/account/team/member"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/team/member',
            method='POST',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def verifyAccount(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/account/verify"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/verify',
            method='GET',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteNotificationsGroup(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/account/projects/{projectId}/notifications/settings/group"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/notifications/settings/group',
            method='DELETE',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteNotificationsTag(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/account/projects/{projectId}/notifications/settings/tag"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/notifications/settings/tag',
            method='DELETE',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def removeTagFromNotificationsGroup(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/account/projects/{projectId}/notifications/settings/group/tag"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/notifications/settings/group/tag',
            method='DELETE',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveNotificationsGroup(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/account/projects/{projectId}/notifications/settings/group"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/notifications/settings/group',
            method='POST',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveNotificationsTag(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/account/projects/{projectId}/notifications/settings/tag"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/notifications/settings/tag',
            method='POST',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def createProject(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/account/projects"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects',
            method='POST',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteProject(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/account/projects/{projectId}"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}',
            method='DELETE',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getProject(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/account/projects/{projectId}"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}',
            method='GET',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getProjects(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/account/projects"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects',
            method='GET',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getAccountRegions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/account/regions"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/regions',
            method='GET',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getProjectTokens(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/account/projects/{projectId}/tokens"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/tokens',
            method='GET',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateProjectAccentColor(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/accent-color"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/settings/accent-color',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateProjectIcon(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/icon"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/settings/icon',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateProjectLogo(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/logo"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/settings/logo',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateProjectMainColor(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/main-color"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/settings/main-color',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateProjectAllowedOrigins(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/origins"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/settings/origins',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateProjectDefaultLanguage(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/default-language"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/settings/default-language',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateProjectDescription(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/description"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/settings/description',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableProject(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/disable',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableProject(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/enable',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateProjectLanguages(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/languages"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/settings/languages',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateProjectUrl(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/url"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/settings/url',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateProjectName(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/name"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/settings/name',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateProjectRegions(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/regions"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/projects/{projectId}/settings/regions',
            method='PATCH',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def createAccount(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/account"""
        return self._transport.send(
            target='hub',
            path='/{version}/account',
            method='POST',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getAccountCollaborators(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/account/collaborators"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/collaborators',
            method='GET',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def sendInviteToTeamMember(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/account/team/member/invite"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/team/member/invite',
            method='POST',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getLicenses(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/account/licenses"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/licenses',
            method='GET',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def askChat(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/account/chat/complete"""
        return self._transport.send(
            target='hub',
            path='/{version}/account/chat/complete',
            method='POST',
            request=request or {},
            scope='account',
            timeout=timeout,
            bearer_token=bearer_token,
        )
