# API · Ai

Access with `norbix.api.ai`. End-user AI chat for a signed-in project user (bearer token from login).

`start_end_user_chat_turn` answers at once with a `turnId`; tokens, tool calls and the final answer arrive over the gateway's SSE stream on the user's channel `ai-chat:{projectId}:{authId}` (`ai.chat.turn.started|token|tool|completed|failed`, `ai.chat.session.*`). A channel that is not the caller's is refused with 403 and `responseStatus.errorCode = "AiChatChannelRefused"` before the stream starts — do not retry it.

`ai_chat(auth_id)` opens that stream (GET `/event-stream?channels=ai-chat:{projectId}:{authId}` on the API host, with the client's token) and yields each chat envelope (`eventName`, `payload`, `frameId`); heartbeats are skipped and the read never times out. Stop iterating to close it. A refusal raises `NorbixError` (`code == "AiChatChannelRefused"`, `status == 403`) after one request. On `AsyncNorbix` it is an async generator. `ai_chat_channel(project_id, auth_id)` builds the channel name.

Tests: `tests/api/test_ai_chat_routes.py` — host, verb, exact path, query and body of every route below (sync and async), and the stream against a mock SSE answer.

**Held actions.** A tool that changes something (sends, pays, creates, deletes) is not run by the assistant: it lands in the chat as an `action.pending` entry with the tool and its exact arguments. `decide_end_user_chat_action(session_id, entry_id, decision="apply")` runs it once, as the signed-in user; `decision="dismiss"` runs nothing. The answer's `status` is `applied`, `failed` or `skipped`; a second decision is refused with 409. The model never decides.

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
| `decide_end_user_chat_action` | `POST` | `/{version}/ai/chat/sessions/{SessionId}/actions/{EntryId}` | `project` |
| `list_end_user_chat_attachments` | `GET` | `/{version}/ai/chat/sessions/{SessionId}/attachments` | `project` |
| `upload_end_user_chat_attachment` | `POST` | `/{version}/ai/chat/sessions/{SessionId}/attachments` | `project` |
| `delete_end_user_chat_attachment` | `DELETE` | `/{version}/ai/chat/attachments/{AttachmentId}` | `project` |
| `list_end_user_chat_memory` | `GET` | `/{version}/ai/chat/memory` | `project` |
| `forget_end_user_chat_memory` | `DELETE` | `/{version}/ai/chat/memory/{NoteId}` | `project` |
| `start_end_user_chat_turn` | `POST` | `/{version}/ai/chat/turn` | `project` |
| `get_end_user_ai_tools` | `GET` | `/{version}/ai/tools` | `project` |
| `invoke_end_user_ai_tool` | `POST` | `/{version}/ai/tools/{ToolName}` | `project` |
| `ai_chat` | `GET` | `/event-stream?channels=ai-chat:{projectId}:{authId}` (SSE) | `project` |

```python
turn = norbix.api.ai.start_end_user_chat_turn(sessionId=session_id, message="Where is my order?")
for event in norbix.api.ai.ai_chat(auth_id):
    if event["eventName"] == "ai.chat.turn.token":
        print(event["payload"]["text"], end="")
    if event["eventName"] in ("ai.chat.turn.completed", "ai.chat.turn.failed"):
        break
```
