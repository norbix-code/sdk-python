from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class AccountModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_account_profile(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/profile"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/profile",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_account_profile(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/account/profile"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/profile",
            method="PUT",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def resend_account_verification_token(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/verify/resend"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/verify/resend",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_account_status(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/status"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/status",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_stripe_checkout_session(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/stripe/create-checkout-session"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/stripe/create-checkout-session",
            method="POST",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_stripe_billing_portal_url(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/stripe/get-portal-url"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/stripe/get-portal-url",
            method="POST",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_team_member_from_invitation(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/team/member"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/team/member",
            method="POST",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def verify_account(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/verify"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/verify",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_notifications_group(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/account/projects/{projectId}/notifications/settings/group"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/notifications/settings/group",
            method="DELETE",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_notifications_tag(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/account/projects/{projectId}/notifications/settings/tag"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/notifications/settings/tag",
            method="DELETE",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def remove_tag_from_notifications_group(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/account/projects/{projectId}/notifications/settings/group/tag"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/notifications/settings/group/tag",
            method="DELETE",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_notifications_group(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/projects/{projectId}/notifications/settings/group"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/notifications/settings/group",
            method="POST",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_notifications_tag(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/projects/{projectId}/notifications/settings/tag"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/notifications/settings/tag",
            method="POST",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_project(self, *, primary_region: str | None = None, additional_regions: list[str] | None = None, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/projects

        ``primary_region`` / ``additional_regions`` optionally pin the new
        project to Norbix regions (region codes, e.g. "nb-eu-germany").
        """
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects",
            method="POST",
            path_params={},
            request={
                "primaryRegion": primary_region,
                "additionalRegions": additional_regions,
                **request,
            },
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_project(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/account/projects/{projectId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}",
            method="DELETE",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_project(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/projects/{projectId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}",
            method="GET",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_projects(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/projects"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_account_regions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/regions"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/regions",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_project_tokens(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/projects/{projectId}/tokens"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/tokens",
            method="GET",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_accent_color(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/accent-color"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/accent-color",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_icon(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/icon"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/icon",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_logo(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/logo"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/logo",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_main_color(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/main-color"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/main-color",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_allowed_origins(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/origins"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/origins",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_default_language(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/default-language"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/default-language",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_description(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/description"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/description",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_project(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/disable",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_project(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/enable",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_languages(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/languages"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/languages",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_url(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/url"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/url",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_name(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/name"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/name",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_regions(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/regions"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/regions",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_account(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account"""
        return self._transport.send(
            target="hub",
            path="/{version}/account",
            method="POST",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_account_collaborators(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/collaborators"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/collaborators",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def send_invite_to_team_member(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/team/member/invite"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/team/member/invite",
            method="POST",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_licenses(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/licenses"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/licenses",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_project_ai_settings(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/projects/{projectId}/ai/settings"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/ai/settings",
            method="GET",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_ai_settings(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/account/projects/{projectId}/ai/settings"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/ai/settings",
            method="PUT",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_project_ai_assistant(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/projects/{projectId}/ai/assistants"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/ai/assistants",
            method="POST",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_ai_assistant(self, project_id: str, assistant_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/account/projects/{projectId}/ai/assistants/{assistantId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/ai/assistants/{assistantId}",
            method="PUT",
            path_params={"projectId": project_id, "assistantId": assistant_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_project_ai_assistant(self, project_id: str, assistant_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/account/projects/{projectId}/ai/assistants/{assistantId}"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/ai/assistants/{assistantId}",
            method="DELETE",
            path_params={"projectId": project_id, "assistantId": assistant_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_project_ai_usage(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/projects/{projectId}/ai/usage"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/ai/usage",
            method="GET",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def set_admin_portal_enabled(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/account/projects/{projectId}/admin-portal/enabled"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/admin-portal/enabled",
            method="PUT",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_admin_url(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/admin-url

        Overrides the project's Admin Portal URL. Body: ``url``. Pass ``url=""`` to go back
        to the standard ``pr_{id}.admin.{host}`` address (a ``None`` value is not sent).
        Request DTO: UpdateProjectAdminUrl.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/admin-url",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_legal_documents(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/legal

        Saves the project's Terms and Privacy Policy as Markdown.
        Body: ``termsMarkdown``, ``privacyMarkdown``. Both are replaced on every call:
        a field left out or empty clears that document.
        Request DTO: UpdateProjectLegalDocuments.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/legal",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def update_project_expose_legal(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/legal/expose

        Turns the public legal pages on or off. Body: ``exposed`` (bool).
        When on, ``api.public.get_public_project_legal`` serves the documents.
        Request DTO: UpdateProjectExposeLegal.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/legal/expose",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_admin_portal_structure(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/projects/{projectId}/admin-portal/structure

        Reads what the project's Admin Portal shows: ``projectId``, ``adminPortalEnabled``,
        ``displayName`` and the ``modules`` in its navigation.
        Request DTO: GetAdminPortalStructure.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/admin-portal/structure",
            method="GET",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def assign_admin_portal_service_user(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/account/projects/{projectId}/settings/admin-portal/service-user

        Assigns an existing service user as the project's Admin Portal service user.
        Body: ``serviceUserId`` (required).
        Request DTO: AssignAdminPortalServiceUserRequest.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/admin-portal/service-user",
            method="PUT",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncAccountModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_account_profile(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/profile"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/profile",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_account_profile(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/account/profile"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/profile",
            method="PUT",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def resend_account_verification_token(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/verify/resend"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/verify/resend",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_account_status(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/status"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/status",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_stripe_checkout_session(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/stripe/create-checkout-session"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/stripe/create-checkout-session",
            method="POST",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_stripe_billing_portal_url(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/stripe/get-portal-url"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/stripe/get-portal-url",
            method="POST",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_team_member_from_invitation(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/team/member"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/team/member",
            method="POST",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def verify_account(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/verify"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/verify",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_notifications_group(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/account/projects/{projectId}/notifications/settings/group"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/notifications/settings/group",
            method="DELETE",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_notifications_tag(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/account/projects/{projectId}/notifications/settings/tag"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/notifications/settings/tag",
            method="DELETE",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def remove_tag_from_notifications_group(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/account/projects/{projectId}/notifications/settings/group/tag"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/notifications/settings/group/tag",
            method="DELETE",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_notifications_group(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/projects/{projectId}/notifications/settings/group"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/notifications/settings/group",
            method="POST",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_notifications_tag(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/projects/{projectId}/notifications/settings/tag"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/notifications/settings/tag",
            method="POST",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_project(self, *, primary_region: str | None = None, additional_regions: list[str] | None = None, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/projects

        ``primary_region`` / ``additional_regions`` optionally pin the new
        project to Norbix regions (region codes, e.g. "nb-eu-germany").
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects",
            method="POST",
            path_params={},
            request={
                "primaryRegion": primary_region,
                "additionalRegions": additional_regions,
                **request,
            },
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_project(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/account/projects/{projectId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}",
            method="DELETE",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_project(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/projects/{projectId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}",
            method="GET",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_projects(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/projects"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_account_regions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/regions"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/regions",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_project_tokens(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/projects/{projectId}/tokens"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/tokens",
            method="GET",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_accent_color(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/accent-color"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/accent-color",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_icon(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/icon"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/icon",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_logo(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/logo"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/logo",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_main_color(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/main-color"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/main-color",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_allowed_origins(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/origins"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/origins",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_default_language(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/default-language"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/default-language",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_description(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/description"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/description",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_project(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/disable",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_project(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/enable",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_languages(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/languages"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/languages",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_url(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/url"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/url",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_name(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/name"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/name",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_regions(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/regions"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/regions",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_account(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account",
            method="POST",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_account_collaborators(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/collaborators"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/collaborators",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def send_invite_to_team_member(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/team/member/invite"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/team/member/invite",
            method="POST",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_licenses(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/licenses"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/licenses",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_project_ai_settings(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/projects/{projectId}/ai/settings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/ai/settings",
            method="GET",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_ai_settings(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/account/projects/{projectId}/ai/settings"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/ai/settings",
            method="PUT",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_project_ai_assistant(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/account/projects/{projectId}/ai/assistants"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/ai/assistants",
            method="POST",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_ai_assistant(self, project_id: str, assistant_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/account/projects/{projectId}/ai/assistants/{assistantId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/ai/assistants/{assistantId}",
            method="PUT",
            path_params={"projectId": project_id, "assistantId": assistant_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_project_ai_assistant(self, project_id: str, assistant_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/account/projects/{projectId}/ai/assistants/{assistantId}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/ai/assistants/{assistantId}",
            method="DELETE",
            path_params={"projectId": project_id, "assistantId": assistant_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_project_ai_usage(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/projects/{projectId}/ai/usage"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/ai/usage",
            method="GET",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def set_admin_portal_enabled(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/account/projects/{projectId}/admin-portal/enabled"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/admin-portal/enabled",
            method="PUT",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_admin_url(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/admin-url

        Overrides the project's Admin Portal URL. Body: ``url``. Pass ``url=""`` to go back
        to the standard ``pr_{id}.admin.{host}`` address (a ``None`` value is not sent).
        Request DTO: UpdateProjectAdminUrl.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/admin-url",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_legal_documents(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/legal

        Saves the project's Terms and Privacy Policy as Markdown.
        Body: ``termsMarkdown``, ``privacyMarkdown``. Both are replaced on every call:
        a field left out or empty clears that document.
        Request DTO: UpdateProjectLegalDocuments.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/legal",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def update_project_expose_legal(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/legal/expose

        Turns the public legal pages on or off. Body: ``exposed`` (bool).
        When on, ``api.public.get_public_project_legal`` serves the documents.
        Request DTO: UpdateProjectExposeLegal.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/legal/expose",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_admin_portal_structure(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/account/projects/{projectId}/admin-portal/structure

        Reads what the project's Admin Portal shows: ``projectId``, ``adminPortalEnabled``,
        ``displayName`` and the ``modules`` in its navigation.
        Request DTO: GetAdminPortalStructure.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/admin-portal/structure",
            method="GET",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def assign_admin_portal_service_user(self, project_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/account/projects/{projectId}/settings/admin-portal/service-user

        Assigns an existing service user as the project's Admin Portal service user.
        Body: ``serviceUserId`` (required).
        Request DTO: AssignAdminPortalServiceUserRequest.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/admin-portal/service-user",
            method="PUT",
            path_params={"projectId": project_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
