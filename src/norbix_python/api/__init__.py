from __future__ import annotations

from ..transport import AsyncTransport, Transport
from .ai import AiModule, AsyncAiModule
from .code import AsyncCodeModule, CodeModule
from .database import AsyncDatabaseModule, DatabaseModule
from .echo import AsyncEchoModule, EchoModule
from .files import AsyncFilesModule, FilesModule
from .logs import AsyncLogsModule, LogsModule
from .membership import AsyncMembershipModule, MembershipModule
from .payments import AsyncPaymentsModule, PaymentsModule
from .public import AsyncPublicModule, PublicModule


class ApiNamespace:
    def __init__(self, transport: Transport) -> None:
        self.ai = AiModule(transport)
        self.code = CodeModule(transport)
        self.database = DatabaseModule(transport)
        self.echo = EchoModule(transport)
        self.files = FilesModule(transport)
        self.logs = LogsModule(transport)
        self.membership = MembershipModule(transport)
        self.payments = PaymentsModule(transport)
        self.public = PublicModule(transport)


class AsyncApiNamespace:
    def __init__(self, transport: AsyncTransport) -> None:
        self.ai = AsyncAiModule(transport)
        self.code = AsyncCodeModule(transport)
        self.database = AsyncDatabaseModule(transport)
        self.echo = AsyncEchoModule(transport)
        self.files = AsyncFilesModule(transport)
        self.logs = AsyncLogsModule(transport)
        self.membership = AsyncMembershipModule(transport)
        self.payments = AsyncPaymentsModule(transport)
        self.public = AsyncPublicModule(transport)
