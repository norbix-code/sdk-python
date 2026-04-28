from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from ..client import Norbix
from ..models import DatabaseFindResult


class Collection:
    """Convenience wrapper for a single collection name (uses generated API under the hood)."""

    def __init__(self, client: Norbix, name: str) -> None:
        self._client = client
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def find_all(
        self,
        *,
        take: int = 100,
        skip: int = 0,
        order_by: list[dict[str, Any]] | None = None,
        **extra: Any,
    ) -> Any:
        req: dict[str, Any] = {"take": take, "skip": skip, **extra}
        if order_by is not None:
            req["orderBy"] = order_by
        return self._client.api.database.find(self._name, request=req)

    def find_one(self, id: str, *, request: dict[str, Any] | None = None) -> Any:
        return self._client.api.database.find_one(self._name, id, request=request or {})

    def find_all_typed(
        self,
        *,
        take: int = 100,
        skip: int = 0,
        order_by: list[dict[str, Any]] | None = None,
        **extra: Any,
    ) -> DatabaseFindResult:
        raw = self.find_all(take=take, skip=skip, order_by=order_by, **extra)
        if isinstance(raw, dict):
            return DatabaseFindResult.model_validate(raw)
        return DatabaseFindResult()

    def iter_pages(self, *, page_size: int = 100, **extra: Any) -> Iterator[dict[str, Any]]:
        skip = 0
        while True:
            batch = self.find_all(take=page_size, skip=skip, **extra)
            if not isinstance(batch, dict):
                break
            items = batch.get("results", []) if isinstance(batch.get("results"), list) else []
            yield from items
            if len(items) < page_size:
                break
            skip += page_size


def DatabaseCollection(client: Norbix, name: str) -> Collection:
    """Alias for :class:`Collection` constructor for readability."""
    return Collection(client, name)
