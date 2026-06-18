from __future__ import annotations

import hashlib
import hmac
import time
from collections.abc import Mapping
from typing import Final

#: Outbound Norbix webhook delivery headers (gateway WebhookDeliveryClient).
NORBIX_WEBHOOK_HEADERS: Final[dict[str, str]] = {
    "event": "X-Norbix-Event",
    "delivery": "X-Norbix-Delivery",
    "idempotency_key": "Idempotency-Key",
    "account": "X-Norbix-Account",
    "project": "X-Norbix-Project",
    "integration": "X-Norbix-Integration",
    "destination": "X-Norbix-Destination",
    "signature": "X-Norbix-Signature",
    "timestamp": "X-Norbix-Timestamp",
}


def _header(headers: Mapping[str, str], name: str) -> str | None:
    """Case-insensitive header lookup (HTTP header names are case-insensitive)."""
    if name in headers:
        return headers[name]
    lower = name.lower()
    for key, value in headers.items():
        if key.lower() == lower:
            return value
    return None


class DeliveryHeaders:
    """Parsed Norbix delivery headers from an inbound request."""

    __slots__ = (
        "event",
        "delivery_id",
        "idempotency_key",
        "account_id",
        "project_id",
        "integration_id",
        "destination_id",
        "signature",
        "timestamp",
    )

    def __init__(self, headers: Mapping[str, str]) -> None:
        h = NORBIX_WEBHOOK_HEADERS
        self.event = _header(headers, h["event"])
        self.delivery_id = _header(headers, h["delivery"]) or _header(headers, h["idempotency_key"])
        self.idempotency_key = _header(headers, h["idempotency_key"])
        self.account_id = _header(headers, h["account"])
        self.project_id = _header(headers, h["project"])
        self.integration_id = _header(headers, h["integration"])
        self.destination_id = _header(headers, h["destination"])
        self.signature = _header(headers, h["signature"])
        self.timestamp = _header(headers, h["timestamp"])


def parse_webhook_headers(headers: Mapping[str, str]) -> DeliveryHeaders:
    """Read Norbix delivery headers from an inbound request."""
    return DeliveryHeaders(headers)


def compute_signature(secret: str, timestamp: str, raw_body: str) -> str:
    """``sha256=<hex>`` HMAC-SHA256 of ``"<timestamp>.<rawBody>"``."""
    mac = hmac.new(secret.encode("utf-8"), f"{timestamp}.{raw_body}".encode(), hashlib.sha256)
    return f"sha256={mac.hexdigest()}"


def verify_signature(
    *,
    secret: str,
    raw_body: str,
    signature: str | None,
    timestamp: str | None,
    tolerance_seconds: int = 300,
) -> tuple[bool, str | None]:
    """Verify ``X-Norbix-Signature``. Returns ``(ok, reason)``."""
    if not signature:
        return False, "missing X-Norbix-Signature header"
    if not timestamp:
        return False, "missing X-Norbix-Timestamp header"

    if tolerance_seconds > 0:
        try:
            sent = float(timestamp)
        except ValueError:
            return False, "X-Norbix-Timestamp is not a number"
        age = abs(time.time() - sent)
        if age > tolerance_seconds:
            return False, f"timestamp outside {tolerance_seconds}s tolerance (age {round(age)}s)"

    expected = compute_signature(secret, timestamp, raw_body)
    if not hmac.compare_digest(expected, signature):
        return False, "signature mismatch"
    return True, None
