from __future__ import annotations

from ..transport import AsyncTransport, Transport

from .chat import AsyncChatModule, ChatModule
from .database import AsyncDatabaseModule, DatabaseModule
from .echo import AsyncEchoModule, EchoModule
from .membership import AsyncMembershipModule, MembershipModule


class ApiNamespace:
    def __init__(self, transport: Transport) -> None:
        self.chat = ChatModule(transport)
        self.database = DatabaseModule(transport)
        self.echo = EchoModule(transport)
        self.membership = MembershipModule(transport)


class AsyncApiNamespace:
    def __init__(self, transport: AsyncTransport) -> None:
        self.chat = AsyncChatModule(transport)
        self.database = AsyncDatabaseModule(transport)
        self.echo = AsyncEchoModule(transport)
        self.membership = AsyncMembershipModule(transport)
