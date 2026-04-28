from __future__ import annotations

import asyncio

from norbix_python import AsyncNorbix


def test_async_norbix_aclose() -> None:
    async def run() -> None:
        client = AsyncNorbix(project_id="p1", bearer_token="t")
        await client.aclose()

    asyncio.run(run())
