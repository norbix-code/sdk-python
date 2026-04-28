from __future__ import annotations

from typing import Any

from .client import AsyncNorbix, LoginCredentials, Norbix
from .errors import (
    AuthenticationError,
    NorbixError,
    NotFoundError,
    RateLimitError,
    ValidationError,
)
from .models import AuthLoginResult, DatabaseFindResult

__all__ = [
    "AsyncNorbix",
    "AuthLoginResult",
    "AuthenticationError",
    "DatabaseFindResult",
    "LoginCredentials",
    "Norbix",
    "NorbixError",
    "NotFoundError",
    "RateLimitError",
    "ValidationError",
    "configure",
    "get_client",
]
__version__ = "0.0.0"

_default_norbix: Norbix | None = None


def configure(**kwargs: Any) -> Norbix:
    """Create a module-level default client (OpenAI/Stripe-style ``configure(api_key=...)``)."""
    global _default_norbix
    _default_norbix = Norbix(**kwargs)
    return _default_norbix


def get_client() -> Norbix:
    """Return the client from :func:`configure`, or raise if none was configured."""
    if _default_norbix is None:
        raise RuntimeError(
            "No default Norbix client. Call norbix_python.configure(...) first, "
            "or use Norbix(...) directly."
        )
    return _default_norbix
