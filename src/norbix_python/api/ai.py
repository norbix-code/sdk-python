from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class AiModule:
    """End-user AI chat for a signed-in project user.

    ``start_end_user_chat_turn`` answers at once with a ``turnId``; the answer
    streams over the gateway's SSE endpoint on the user's own channel
    ``ai-chat:{projectId}:{authId}`` (events ``ai.chat.turn.*`` and
    ``ai.chat.session.*``). A subscription to another user's channel is
    refused with HTTP 403 and ``responseStatus.errorCode = "AiChatChannelRefused"``
    before the stream starts — do not retry it.
    """

    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_end_user_chat_availability(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/chat/availability"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/availability",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def list_end_user_chat_sessions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/chat/sessions"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def create_end_user_chat_session(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/chat/sessions"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_end_user_chat_session(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/chat/sessions/{SessionId}"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}",
            method="GET",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def rename_end_user_chat_session(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/ai/chat/sessions/{SessionId}"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}",
            method="PATCH",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_end_user_chat_session(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/ai/chat/sessions/{SessionId}"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}",
            method="DELETE",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def pin_end_user_chat_session(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/chat/sessions/{SessionId}/pin"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/pin",
            method="PUT",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def archive_end_user_chat_session(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/chat/sessions/{SessionId}/archive"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/archive",
            method="PUT",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_end_user_chat_entries(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/chat/sessions/{SessionId}/entries"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/entries",
            method="GET",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def set_end_user_chat_entry_feedback(self, session_id: str, entry_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/chat/sessions/{SessionId}/entries/{EntryId}/feedback"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/entries/{EntryId}/feedback",
            method="PUT",
            path_params={"SessionId": session_id, "EntryId": entry_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def list_end_user_chat_attachments(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/chat/sessions/{SessionId}/attachments"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/attachments",
            method="GET",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def upload_end_user_chat_attachment(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/chat/sessions/{SessionId}/attachments"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/attachments",
            method="POST",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_end_user_chat_attachment(self, attachment_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/ai/chat/attachments/{AttachmentId}"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/attachments/{AttachmentId}",
            method="DELETE",
            path_params={"AttachmentId": attachment_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def list_end_user_chat_memory(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/chat/memory"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/memory",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def forget_end_user_chat_memory(self, note_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/ai/chat/memory/{NoteId}"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/memory/{NoteId}",
            method="DELETE",
            path_params={"NoteId": note_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def start_end_user_chat_turn(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/chat/turn"""
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/turn",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncAiModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_end_user_chat_availability(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/chat/availability"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/availability",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def list_end_user_chat_sessions(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/chat/sessions"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def create_end_user_chat_session(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/chat/sessions"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_end_user_chat_session(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/chat/sessions/{SessionId}"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}",
            method="GET",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def rename_end_user_chat_session(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PATCH /{version}/ai/chat/sessions/{SessionId}"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}",
            method="PATCH",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_end_user_chat_session(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/ai/chat/sessions/{SessionId}"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}",
            method="DELETE",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def pin_end_user_chat_session(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/chat/sessions/{SessionId}/pin"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/pin",
            method="PUT",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def archive_end_user_chat_session(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/chat/sessions/{SessionId}/archive"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/archive",
            method="PUT",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_end_user_chat_entries(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/chat/sessions/{SessionId}/entries"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/entries",
            method="GET",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def set_end_user_chat_entry_feedback(self, session_id: str, entry_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/chat/sessions/{SessionId}/entries/{EntryId}/feedback"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/entries/{EntryId}/feedback",
            method="PUT",
            path_params={"SessionId": session_id, "EntryId": entry_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def list_end_user_chat_attachments(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/chat/sessions/{SessionId}/attachments"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/attachments",
            method="GET",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def upload_end_user_chat_attachment(self, session_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/chat/sessions/{SessionId}/attachments"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/attachments",
            method="POST",
            path_params={"SessionId": session_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_end_user_chat_attachment(self, attachment_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/ai/chat/attachments/{AttachmentId}"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/attachments/{AttachmentId}",
            method="DELETE",
            path_params={"AttachmentId": attachment_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def list_end_user_chat_memory(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/chat/memory"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/memory",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def forget_end_user_chat_memory(self, note_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/ai/chat/memory/{NoteId}"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/memory/{NoteId}",
            method="DELETE",
            path_params={"NoteId": note_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def start_end_user_chat_turn(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/chat/turn"""
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/turn",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
