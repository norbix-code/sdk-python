from __future__ import annotations

from ..helpers import make_client
def test_api_ai_wave3_module_surface() -> None:
    client, _ = make_client()
    module = client.api.ai
    assert callable(module.get_end_user_chat_availability)
    assert callable(module.list_end_user_chat_sessions)
    assert callable(module.create_end_user_chat_session)
    assert callable(module.get_end_user_chat_session)
    assert callable(module.rename_end_user_chat_session)
    assert callable(module.delete_end_user_chat_session)
    assert callable(module.pin_end_user_chat_session)
    assert callable(module.archive_end_user_chat_session)
    assert callable(module.get_end_user_chat_entries)
    assert callable(module.set_end_user_chat_entry_feedback)
    assert callable(module.list_end_user_chat_attachments)
    assert callable(module.upload_end_user_chat_attachment)
    assert callable(module.delete_end_user_chat_attachment)
    assert callable(module.list_end_user_chat_memory)
    assert callable(module.forget_end_user_chat_memory)
    assert callable(module.start_end_user_chat_turn)


def test_api_ai_get_end_user_chat_availability_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.get_end_user_chat_availability()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request['url'].endswith('/v3/ai/chat/availability')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_list_end_user_chat_sessions_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.list_end_user_chat_sessions()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request['url'].endswith('/v3/ai/chat/sessions')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_create_end_user_chat_session_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.create_end_user_chat_session()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request['url'].endswith('/v3/ai/chat/sessions')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_get_end_user_chat_session_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.get_end_user_chat_session(session_id="stub-SessionId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request['url'].endswith('/v3/ai/chat/sessions/stub-SessionId')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_rename_end_user_chat_session_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.rename_end_user_chat_session(session_id="stub-SessionId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request['url'].endswith('/v3/ai/chat/sessions/stub-SessionId')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_delete_end_user_chat_session_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.delete_end_user_chat_session(session_id="stub-SessionId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request['url'].endswith('/v3/ai/chat/sessions/stub-SessionId')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_pin_end_user_chat_session_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.pin_end_user_chat_session(session_id="stub-SessionId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request['url'].endswith('/v3/ai/chat/sessions/stub-SessionId/pin')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_archive_end_user_chat_session_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.archive_end_user_chat_session(session_id="stub-SessionId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request['url'].endswith('/v3/ai/chat/sessions/stub-SessionId/archive')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_get_end_user_chat_entries_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.get_end_user_chat_entries(session_id="stub-SessionId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request['url'].endswith('/v3/ai/chat/sessions/stub-SessionId/entries')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_set_end_user_chat_entry_feedback_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.set_end_user_chat_entry_feedback(session_id="stub-SessionId", entry_id="stub-EntryId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request['url'].endswith('/v3/ai/chat/sessions/stub-SessionId/entries/stub-EntryId/feedback')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_list_end_user_chat_attachments_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.list_end_user_chat_attachments(session_id="stub-SessionId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request['url'].endswith('/v3/ai/chat/sessions/stub-SessionId/attachments')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_upload_end_user_chat_attachment_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.upload_end_user_chat_attachment(session_id="stub-SessionId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request['url'].endswith('/v3/ai/chat/sessions/stub-SessionId/attachments')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_delete_end_user_chat_attachment_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.delete_end_user_chat_attachment(attachment_id="stub-AttachmentId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request['url'].endswith('/v3/ai/chat/attachments/stub-AttachmentId')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_list_end_user_chat_memory_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.list_end_user_chat_memory()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request['url'].endswith('/v3/ai/chat/memory')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_forget_end_user_chat_memory_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.forget_end_user_chat_memory(note_id="stub-NoteId")
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request['url'].endswith('/v3/ai/chat/memory/stub-NoteId')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'


def test_api_ai_start_end_user_chat_turn_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.ai.start_end_user_chat_turn()
    assert transport.last_request is not None
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request['url'].endswith('/v3/ai/chat/turn')
    assert transport.last_request['headers']['authorization'] == 'Bearer test-token'
    assert transport.last_request['headers']['x-cm-projectid'] == 'test-project'

