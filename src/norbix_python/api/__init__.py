from __future__ import annotations

from ..transport import AsyncTransport, Transport
from .ai import AiModule, AsyncAiModule
from .database import AsyncDatabaseModule, DatabaseModule
from .echo import AsyncEchoModule, EchoModule
from .files import AsyncFilesModule, FilesModule
from .membership import AsyncMembershipModule, MembershipModule


class ApiNamespace:
    def __init__(self, transport: Transport) -> None:
        self.ai = AiModule(transport)
        self.database = DatabaseModule(transport)
        self.echo = EchoModule(transport)
        self.files = FilesModule(transport)
        self.membership = MembershipModule(transport)


class AsyncApiNamespace:
    def __init__(self, transport: AsyncTransport) -> None:
        self.ai = AsyncAiModule(transport)
        self.database = AsyncDatabaseModule(transport)
        self.echo = AsyncEchoModule(transport)
        self.files = AsyncFilesModule(transport)
        self.membership = AsyncMembershipModule(transport)
