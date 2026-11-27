from __future__ import annotations

import json
from collections.abc import AsyncIterator, Iterator
from typing import Any

from ..errors import NorbixError
from ..transport import AsyncTransport, SseFrame, Transport


def ai_chat_channel(project_id: str, auth_id: str) -> str:
    """The end-user AI chat channel of one project user, ``ai-chat:{projectId}:{authId}``.

    TypeScript twin: ``aiChatChannel``.
    """
    return f"ai-chat:{project_id}:{auth_id}"


def _chat_query(project_id: str, auth_id: str) -> dict[str, Any]:
    if not project_id:
        raise NorbixError(message="ai_chat: the client has no project id.", code="NORBIX_ERROR")
    if not auth_id:
        raise NorbixError(message="ai_chat: auth_id is required.", code="NORBIX_ERROR")
    return {"channels": ai_chat_channel(project_id, auth_id)}


def _chat_envelope(frame: SseFrame) -> dict[str, Any] | None:
    """The realtime envelope of a frame, or None for a heartbeat / notice."""
    try:
        envelope = json.loads(frame.data)
    except ValueError:
        return None
    if not isinstance(envelope, dict) or not isinstance(envelope.get("eventName"), str):
        return None
    envelope["frameId"] = frame.id
    return envelope


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

    def decide_end_user_chat_action(self, session_id: str, entry_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/chat/sessions/{SessionId}/actions/{EntryId}

        The signed-in user's own decision on an action the chat held: a tool that
        changes something (sends, pays, creates, deletes) is not run by the
        assistant but lands in the chat as an ``action.pending`` entry. Pass
        ``decision="apply"`` to run it once, as the user, or ``"dismiss"`` to run
        nothing. The answer's ``status`` is ``applied``, ``failed`` or ``skipped``;
        a second decision is refused with HTTP 409.
        """
        return self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/actions/{EntryId}",
            method="POST",
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

    def get_end_user_ai_tools(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/tools

        Lists the AI tools a signed-in project user's chat may call (own-scope
        tools only): name, description, toolsets, confirmation, parameters.
        TypeScript twin: ``getEndUserAiTools``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/ai/tools",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def invoke_end_user_ai_tool(self, tool_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/tools/{ToolName}

        Calls one end-user AI tool by name with ``argumentsJson`` (the arguments as a
        JSON string) and returns its result text.
        TypeScript twin: ``invokeEndUserAiTool``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/ai/tools/{ToolName}",
            method="POST",
            path_params={"ToolName": tool_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def ai_chat(self, auth_id: str, *, bearer_token: str | None = None) -> Iterator[dict[str, Any]]:
        """Stream the end-user AI chat (TypeScript twin: ``norbix.aiChat``).

        Opens ``GET /event-stream?channels=ai-chat:{projectId}:{authId}`` on the
        API host with the client's token and project, and yields each realtime
        envelope (``eventName`` ``ai.chat.turn.started`` / ``.token`` / ``.tool``
        / ``.completed`` / ``.failed`` or ``ai.chat.session.*``; ``payload``
        holds the ``turnId`` and, for a token, the ``text``; ``frameId`` is the
        SSE id). Heartbeats and notices are skipped. Stop iterating to close
        the stream. Another user's channel is refused with HTTP 403 and code
        ``AiChatChannelRefused`` before the stream starts; that error is raised
        and never retried.
        """
        query = _chat_query(self._transport._cfg.project_id, auth_id)
        for frame in self._transport.stream(target="api", path="/event-stream", query=query, bearer_token=bearer_token):
            envelope = _chat_envelope(frame)
            if envelope is not None:
                yield envelope


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

    async def decide_end_user_chat_action(self, session_id: str, entry_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/chat/sessions/{SessionId}/actions/{EntryId}

        The signed-in user's own decision on an action the chat held: a tool that
        changes something (sends, pays, creates, deletes) is not run by the
        assistant but lands in the chat as an ``action.pending`` entry. Pass
        ``decision="apply"`` to run it once, as the user, or ``"dismiss"`` to run
        nothing. The answer's ``status`` is ``applied``, ``failed`` or ``skipped``;
        a second decision is refused with HTTP 409.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/ai/chat/sessions/{SessionId}/actions/{EntryId}",
            method="POST",
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

    async def get_end_user_ai_tools(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/tools

        Lists the AI tools a signed-in project user's chat may call (own-scope
        tools only): name, description, toolsets, confirmation, parameters.
        TypeScript twin: ``getEndUserAiTools``.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/ai/tools",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def invoke_end_user_ai_tool(self, tool_name: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/tools/{ToolName}

        Calls one end-user AI tool by name with ``argumentsJson`` (the arguments as a
        JSON string) and returns its result text.
        TypeScript twin: ``invokeEndUserAiTool``.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/ai/tools/{ToolName}",
            method="POST",
            path_params={"ToolName": tool_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def ai_chat(self, auth_id: str, *, bearer_token: str | None = None) -> AsyncIterator[dict[str, Any]]:
        """Async twin of :meth:`AiModule.ai_chat`. Stream the end-user AI chat (TypeScript twin: ``norbix.aiChat``).

        Opens ``GET /event-stream?channels=ai-chat:{projectId}:{authId}`` on the
        API host with the client's token and project, and yields each realtime
        envelope (``eventName`` ``ai.chat.turn.started`` / ``.token`` / ``.tool``
        / ``.completed`` / ``.failed`` or ``ai.chat.session.*``; ``payload``
        holds the ``turnId`` and, for a token, the ``text``; ``frameId`` is the
        SSE id). Heartbeats and notices are skipped. Stop iterating to close
        the stream. Another user's channel is refused with HTTP 403 and code
        ``AiChatChannelRefused`` before the stream starts; that error is raised
        and never retried.
        """
        query = _chat_query(self._transport._cfg.project_id, auth_id)
        async for frame in self._transport.stream(target="api", path="/event-stream", query=query, bearer_token=bearer_token):
            envelope = _chat_envelope(frame)
            if envelope is not None:
                yield envelope
