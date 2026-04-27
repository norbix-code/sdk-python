from __future__ import annotations

from typing import Any

from ..transport import Transport

class MembershipModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def disableMembership(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/disable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableMembership(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/enable',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteMembershipTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/membership/triggers/{triggerId}"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/triggers/{triggerId}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableMembershipTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/membership/triggers/{triggerId}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/triggers/{triggerId}/disable',
            method='PATCH',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableMembershipTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/membership/triggers/{triggerId}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/triggers/{triggerId}/enable',
            method='PATCH',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getMembershipTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/triggers/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/triggers/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getMembershipTriggers(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/triggers"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/triggers',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveMembershipTrigger(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/triggers"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/triggers',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def createRole(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/roles"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/roles',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteRole(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/membership/roles"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/roles',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getRole(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/roles/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/roles/{Id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getRoles(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/roles"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/roles',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updateRolePolicies(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PATCH /{version}/membership/roles"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/roles',
            method='PATCH',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def createPolicy(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/policies"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/policies',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deletePolicy(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/membership/policies"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/policies',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getPolicy(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/policies/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/policies/{Id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getPolicies(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/policies"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/policies',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def updatePolicy(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/policies"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/policies',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def deleteMembershipIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """DELETE /{version}/membership/integrations/{Id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/integrations/{Id}',
            method='DELETE',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disableMembershipIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/integrations/{Id}/disable"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/integrations/{Id}/disable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enableMembershipIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/integrations/{Id}/enable"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/integrations/{Id}/enable',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getMembershipIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/integrations/{id}"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/integrations/{id}',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def getMembershipIntegrations(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """GET /{version}/membership/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/integrations',
            method='GET',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def saveMembershipIntegration(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """POST /{version}/membership/integrations"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/integrations',
            method='POST',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def setMembershipIntegrationAsDefault(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:
        """PUT /{version}/membership/integrations/{Id}/default"""
        return self._transport.send(
            target='hub',
            path='/{version}/membership/integrations/{Id}/default',
            method='PUT',
            request=request or {},
            scope='project',
            timeout=timeout,
            bearer_token=bearer_token,
        )
