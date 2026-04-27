from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class NorbixError(Exception):
    message: str
    status: int = 0
    code: str = "NORBIX_ERROR"
    details: dict[str, Any] = field(default_factory=dict)

    def __str__(self) -> str:
        return f"{self.code} ({self.status}): {self.message}"
