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
