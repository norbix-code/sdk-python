from __future__ import annotations

from ..transport import Transport

from .chat import ChatModule
from .database import DatabaseModule
from .echo import EchoModule
from .membership import MembershipModule


class ApiNamespace:
    def __init__(self, transport: Transport) -> None:
        self.chat = ChatModule(transport)
        self.database = DatabaseModule(transport)
        self.echo = EchoModule(transport)
        self.membership = MembershipModule(transport)
