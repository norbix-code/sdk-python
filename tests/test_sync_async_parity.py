from __future__ import annotations

from norbix_python.api.chat import AsyncChatModule, ChatModule
from norbix_python.api.database import AsyncDatabaseModule, DatabaseModule


def _public_methods(cls: type) -> set[str]:
    return {n for n in dir(cls) if not n.startswith("_")}


def test_database_sync_async_public_methods_match() -> None:
    assert _public_methods(DatabaseModule) == _public_methods(AsyncDatabaseModule)


def test_chat_sync_async_public_methods_match() -> None:
    assert _public_methods(ChatModule) == _public_methods(AsyncChatModule)
