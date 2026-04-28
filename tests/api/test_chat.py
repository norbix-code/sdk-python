from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_api_chat_module_surface() -> None:
    client, _ = make_client()
    module = client.api.chat
    assert callable(module.ask_chat)


def test_api_chat_ask_chat_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.chat.ask_chat()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
