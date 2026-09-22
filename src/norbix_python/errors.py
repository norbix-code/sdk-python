from __future__ import annotations

from typing import Any


class ErrorItem:
    """One error inside the gateway's ``responseStatus.errors`` list."""

    def __init__(
        self,
        *,
        error_code: str = "",
        message: str = "",
        field_name: str = "",
        context: dict[str, Any] | None = None,
    ) -> None:
        self.error_code = error_code
        self.message = message
        self.field_name = field_name
        self.context = context or {}

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return (
            f"ErrorItem(error_code={self.error_code!r}, message={self.message!r}, "
            f"field_name={self.field_name!r})"
        )


class NorbixError(Exception):
    """Base error for Norbix SDK failures."""

    def __init__(
        self,
        message: str,
        *,
        status: int = 0,
        code: str = "NORBIX_ERROR",
        details: dict[str, Any] | None = None,
        errors: list[ErrorItem] | None = None,
        body: Any = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.code = code
        self.details = details or {}
        #: Every error the gateway sent, in the order it sent them.
        self.errors = errors or []
        #: The answer exactly as it arrived, for whoever needs the rest of it.
        self.body = body

    @property
    def http_status(self) -> int:
        """Same value as :attr:`status`. The name every Norbix SDK uses."""
        return self.status

    @property
    def error_code(self) -> str:
        """Same value as :attr:`code`. The name every Norbix SDK uses."""
        return self.code

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
        errors: list[ErrorItem] | None = None,
        body: Any = None,
    ) -> None:
        super().__init__(
            message, status=status, code=code, details=details, errors=errors, body=body
        )


class NotFoundError(NorbixError):
    """Resource does not exist (HTTP 404)."""

    def __init__(
        self,
        message: str,
        *,
        status: int = 404,
        code: str = "NORBIX_NOT_FOUND",
        details: dict[str, Any] | None = None,
        errors: list[ErrorItem] | None = None,
        body: Any = None,
    ) -> None:
        super().__init__(
            message, status=status, code=code, details=details, errors=errors, body=body
        )


class RateLimitError(NorbixError):
    """Too many requests (HTTP 429)."""

    def __init__(
        self,
        message: str,
        *,
        status: int = 429,
        code: str = "NORBIX_RATE_LIMIT",
        details: dict[str, Any] | None = None,
        errors: list[ErrorItem] | None = None,
        body: Any = None,
    ) -> None:
        super().__init__(
            message, status=status, code=code, details=details, errors=errors, body=body
        )


class ValidationError(NorbixError):
    """Invalid request payload or parameters (HTTP 400 / 422)."""

    def __init__(
        self,
        message: str,
        *,
        status: int = 0,
        code: str = "NORBIX_VALIDATION_ERROR",
        details: dict[str, Any] | None = None,
        errors: list[ErrorItem] | None = None,
        body: Any = None,
    ) -> None:
        super().__init__(
            message, status=status, code=code, details=details, errors=errors, body=body
        )


def error_from_http(
    *,
    message: str,
    status: int,
    code: str,
    details: dict[str, Any],
    errors: list[ErrorItem] | None = None,
    body: Any = None,
) -> NorbixError:
    kwargs: dict[str, Any] = {
        "status": status,
        "code": code,
        "details": details,
        "errors": errors,
        "body": body,
    }
    if status == 404:
        return NotFoundError(message, **kwargs)
    if status == 429:
        return RateLimitError(message, **kwargs)
    if status == 401 or status == 403:
        return AuthenticationError(message, **kwargs)
    if status == 400 or status == 422:
        return ValidationError(message, **kwargs)
    return NorbixError(message, **kwargs)


def _response_status_of(body: Any) -> dict[str, Any] | None:
    """The ``responseStatus`` block of a body, whatever the casing of the key."""
    if not isinstance(body, dict):
        return None
    for key in ("responseStatus", "ResponseStatus"):
        value = body.get(key)
        if isinstance(value, dict):
            return value
    return None


def says_it_failed(body: Any) -> bool:
    """``True`` when the body carries ``responseStatus.isSuccess = False``.

    The gateway answers a business refusal — an unknown id, a rule that says
    no — with HTTP 200 and that flag. Without this check the SDK would hand
    such an answer back as a value and the caller would carry on as if the call
    had worked (10b-files, issue #67).
    """
    status = _response_status_of(body)
    if status is None:
        return False
    for key in ("isSuccess", "IsSuccess"):
        if key in status:
            return status[key] is False
    return False


def _items_of(value: Any) -> list[ErrorItem]:
    if not isinstance(value, list):
        return []
    items: list[ErrorItem] = []
    for entry in value:
        if not isinstance(entry, dict):
            continue
        context = entry.get("context")
        items.append(
            ErrorItem(
                error_code=_text(entry.get("errorCode")),
                message=_text(entry.get("message")),
                field_name=_text(entry.get("fieldName")),
                context=context if isinstance(context, dict) else None,
            )
        )
    return items


def _text(value: Any) -> str:
    return value if isinstance(value, str) and value else ""


def error_from_body(*, body: Any, status: int, text: str = "") -> NorbixError:
    """Build the error a gateway answer describes.

    The gateway puts its message and its error code inside
    ``responseStatus.errors[]``, not at the top of the block, so that list is
    read first: the first entry gives the message and the code, and every entry
    is kept in :attr:`NorbixError.errors`. Only when the body has no
    ``responseStatus`` are the top-level ``message`` and ``errorCode`` read.
    ``Request failed (HTTP <status>)`` is the last fallback, used when the body
    says nothing at all — a 500 page that is not JSON, say.
    """
    details: dict[str, Any] = body if isinstance(body, dict) else {}
    # source is responseStatus when the body has one, the body itself when it
    # has none — so the top-level fields are read only in the second case.
    source = _response_status_of(body) or details

    items = _items_of(source.get("errors"))
    first = next((i for i in items if i.message or i.error_code), None)

    message = (first.message if first else "") or _text(source.get("message"))
    code = (first.error_code if first else "") or _text(source.get("errorCode"))

    if not message:
        message = f"Request failed (HTTP {status})"
    if not code:
        # Callers switch on ``code``, so it is never left empty; the gateway's
        # own code wins whenever the gateway sent one.
        code = f"HTTP_{status}"

    return error_from_http(
        message=message,
        status=status,
        code=code,
        details=details,
        errors=items,
        body=body if body is not None else (text or None),
    )
