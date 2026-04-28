from __future__ import annotations

from typing import Any


class NorbixError(Exception):
    """Base error for Norbix SDK failures."""

    def __init__(
        self,
        message: str,
        *,
        status: int = 0,
        code: str = "NORBIX_ERROR",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.code = code
        self.details = details or {}

    def __str__(self) -> str:
        return f"{self.code} ({self.status}): {self.message}"


class AuthenticationError(NorbixError):
    """Invalid credentials, expired token, or missing auth."""

    def __init__(
        self,
        message: str,
        *,
        status: int = 0,
        code: str = "NORBIX_AUTHENTICATION_ERROR",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message, status=status, code=code, details=details)


class NotFoundError(NorbixError):
    """Resource does not exist (HTTP 404)."""

    def __init__(
        self,
        message: str,
        *,
        status: int = 404,
        code: str = "NORBIX_NOT_FOUND",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message, status=status, code=code, details=details)


class RateLimitError(NorbixError):
    """Too many requests (HTTP 429)."""

    def __init__(
        self,
        message: str,
        *,
        status: int = 429,
        code: str = "NORBIX_RATE_LIMIT",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message, status=status, code=code, details=details)


class ValidationError(NorbixError):
    """Invalid request payload or parameters (HTTP 400 / 422)."""

    def __init__(
        self,
        message: str,
        *,
        status: int = 0,
        code: str = "NORBIX_VALIDATION_ERROR",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message, status=status, code=code, details=details)


def error_from_http(
    *,
    message: str,
    status: int,
    code: str,
    details: dict[str, Any],
) -> NorbixError:
    if status == 404:
        return NotFoundError(message, status=status, code=code, details=details)
    if status == 429:
        return RateLimitError(message, status=status, code=code, details=details)
    if status == 401 or status == 403:
        return AuthenticationError(message, status=status, code=code, details=details)
    if status == 400 or status == 422:
        return ValidationError(message, status=status, code=code, details=details)
    return NorbixError(message, status=status, code=code, details=details)
