from __future__ import annotations

from ..transport import Transport

from .account import AccountModule
from .ai import AiModule
from .database import DatabaseModule
from .echo import EchoModule
from .email import EmailModule
from .files import FilesModule
from .internal import InternalModule
from .logs import LogsModule
from .membership import MembershipModule
from .notifications import NotificationsModule
from .payments import PaymentsModule
from .scheduler import SchedulerModule
from .webhooks import WebhooksModule


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
