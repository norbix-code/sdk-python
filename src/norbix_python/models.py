from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class AuthLoginResult(BaseModel):
    """Response shape from POST /auth (typical fields)."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bearer_token: str | None = Field(default=None, alias="bearerToken")


class DatabaseFindResult(BaseModel):
    """Common database list response (fields vary by API version)."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[dict[str, Any]] = Field(default_factory=list)


class ReferenceDisplay(BaseModel):
    """One reference value as a record read with ``expand_references=True`` returns it.

    ``id`` is the stored id; ``display`` is the value of the target's ``displayField``
    (a user property, a role name, a term title or slug — a string or a language map —,
    a record field, a file name). ``None`` when the target is gone. A field that holds
    several ids returns a list of these.
    """

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    display: Any | None = None

    @classmethod
    def from_value(cls, value: Any) -> ReferenceDisplay | list[ReferenceDisplay] | None:
        """Parse one expanded field value: a dict, a list of dicts, or ``None``."""
        if value is None:
            return None
        if isinstance(value, list):
            return [cls.model_validate(item) for item in value]
        return cls.model_validate(value)
