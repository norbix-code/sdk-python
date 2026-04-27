from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_api_chat_module_surface() -> None:
    client, _ = make_client()
    module = client.api.chat
    assert callable(module.askChat)


def test_api_chat_askChat_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/chat/complete') if False else {}
    client.api.chat.askChat(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
