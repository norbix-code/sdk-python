from __future__ import annotations

from ..errors import NorbixError


class NorbixWebhookError(NorbixError):
    """Base error for inbound webhook handling."""

    def __init__(self, message: str, *, code: str = "WEBHOOK_ERROR") -> None:
        super().__init__(message, code=code)


class NorbixWebhookSignatureError(NorbixWebhookError):
    """The delivery signature could not be verified (treat as HTTP 401)."""

    def __init__(self, message: str) -> None:
        super().__init__(message, code="WEBHOOK_SIGNATURE_INVALID")
        self.status = 401


class NorbixWebhookParseError(NorbixWebhookError):
    """The delivery body was not a valid webhook envelope (treat as HTTP 400)."""

    def __init__(self, message: str) -> None:
        super().__init__(message, code="WEBHOOK_PARSE_INVALID")
        self.status = 400
