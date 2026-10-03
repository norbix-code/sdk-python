# API · Ai

Access with `norbix.api.ai`. End-user AI chat for a signed-in project user (bearer token from login).

`start_end_user_chat_turn` answers at once with a `turnId`; tokens, tool calls and the final answer arrive over the gateway's SSE stream on the user's channel `ai-chat:{projectId}:{authId}` (`ai.chat.turn.started|token|tool|completed|failed`, `ai.chat.session.*`). A channel that is not the caller's is refused with 403 and `responseStatus.errorCode = "AiChatChannelRefused"` before the stream starts — do not retry it.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `get_end_user_chat_availability` | `GET` | `/{version}/ai/chat/availability` | `project` |
| `list_end_user_chat_sessions` | `GET` | `/{version}/ai/chat/sessions` | `project` |
| `create_end_user_chat_session` | `POST` | `/{version}/ai/chat/sessions` | `project` |
| `get_end_user_chat_session` | `GET` | `/{version}/ai/chat/sessions/{SessionId}` | `project` |
| `rename_end_user_chat_session` | `PATCH` | `/{version}/ai/chat/sessions/{SessionId}` | `project` |
| `delete_end_user_chat_session` | `DELETE` | `/{version}/ai/chat/sessions/{SessionId}` | `project` |
| `pin_end_user_chat_session` | `PUT` | `/{version}/ai/chat/sessions/{SessionId}/pin` | `project` |
| `archive_end_user_chat_session` | `PUT` | `/{version}/ai/chat/sessions/{SessionId}/archive` | `project` |
| `get_end_user_chat_entries` | `GET` | `/{version}/ai/chat/sessions/{SessionId}/entries` | `project` |
| `set_end_user_chat_entry_feedback` | `PUT` | `/{version}/ai/chat/sessions/{SessionId}/entries/{EntryId}/feedback` | `project` |
| `list_end_user_chat_attachments` | `GET` | `/{version}/ai/chat/sessions/{SessionId}/attachments` | `project` |
| `upload_end_user_chat_attachment` | `POST` | `/{version}/ai/chat/sessions/{SessionId}/attachments` | `project` |
| `delete_end_user_chat_attachment` | `DELETE` | `/{version}/ai/chat/attachments/{AttachmentId}` | `project` |
| `list_end_user_chat_memory` | `GET` | `/{version}/ai/chat/memory` | `project` |
| `forget_end_user_chat_memory` | `DELETE` | `/{version}/ai/chat/memory/{NoteId}` | `project` |
| `start_end_user_chat_turn` | `POST` | `/{version}/ai/chat/turn` | `project` |
