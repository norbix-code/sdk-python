from __future__ import annotations

from ..transport import AsyncTransport, Transport

from .account import AsyncAccountModule, AccountModule
from .ai import AsyncAiModule, AiModule
from .database import AsyncDatabaseModule, DatabaseModule
from .echo import AsyncEchoModule, EchoModule
from .email import AsyncEmailModule, EmailModule
from .files import AsyncFilesModule, FilesModule
from .internal import AsyncInternalModule, InternalModule
from .logs import AsyncLogsModule, LogsModule
from .membership import AsyncMembershipModule, MembershipModule
from .notifications import AsyncNotificationsModule, NotificationsModule
from .payments import AsyncPaymentsModule, PaymentsModule
from .scheduler import AsyncSchedulerModule, SchedulerModule
from .webhooks import AsyncWebhooksModule, WebhooksModule


class HubNamespace:
    def __init__(self, transport: Transport) -> None:
        self.account = AccountModule(transport)
        self.ai = AiModule(transport)
        self.database = DatabaseModule(transport)
        self.echo = EchoModule(transport)
        self.email = EmailModule(transport)
        self.files = FilesModule(transport)
        self.internal = InternalModule(transport)
        self.logs = LogsModule(transport)
        self.membership = MembershipModule(transport)
        self.notifications = NotificationsModule(transport)
        self.payments = PaymentsModule(transport)
        self.scheduler = SchedulerModule(transport)
        self.webhooks = WebhooksModule(transport)


class AsyncHubNamespace:
    def __init__(self, transport: AsyncTransport) -> None:
        self.account = AsyncAccountModule(transport)
        self.ai = AsyncAiModule(transport)
        self.database = AsyncDatabaseModule(transport)
        self.echo = AsyncEchoModule(transport)
        self.email = AsyncEmailModule(transport)
        self.files = AsyncFilesModule(transport)
        self.internal = AsyncInternalModule(transport)
        self.logs = AsyncLogsModule(transport)
        self.membership = AsyncMembershipModule(transport)
        self.notifications = AsyncNotificationsModule(transport)
        self.payments = AsyncPaymentsModule(transport)
        self.scheduler = AsyncSchedulerModule(transport)
        self.webhooks = AsyncWebhooksModule(transport)
