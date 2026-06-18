from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

# Alias so annotations inside the classes don't collide with the ``list``
# method name in class scope.
_RegionCodeList = list[str]

# Norbix regions — list the regions available to the account and update the
# regions a project runs in (primary + additional).
#
# These endpoints manage the *set* of regions. To make requests *against* a
# given region, set ``region`` on the client (``Norbix(region="nb-eu-germany")``
# or ``client.set_region("nb-eu-germany")``) or per call
# (``region="nb-eu-germany"``), which sends the ``nb-region`` header.


class RegionsModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def list(
        self, *, timeout: float | None = None, bearer_token: str | None = None, region: str | None = None, **request: Any
    ) -> Any:
        """GET /{version}/account/regions

        Lists the Norbix regions available to the account
        (``{"items": [{"id", "continent", "name"}]}``).
        """
        return self._transport.send(
            target="hub",
            path="/{version}/account/regions",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
            region=region,
        )

    def update_project_regions(
        self,
        project_id: str,
        *,
        primary_region: str | None = None,
        additional_regions: _RegionCodeList | None = None,
        timeout: float | None = None,
        bearer_token: str | None = None,
        region: str | None = None,
        **request: Any,
    ) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/regions

        Updates the regions a project runs in. Both fields are optional;
        omitted fields are left unchanged.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/regions",
            method="PATCH",
            path_params={"projectId": project_id},
            request={
                "primaryRegion": primary_region,
                "additionalRegions": additional_regions,
                **request,
            },
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
            region=region,
        )


class AsyncRegionsModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(
        self, *, timeout: float | None = None, bearer_token: str | None = None, region: str | None = None, **request: Any
    ) -> Any:
        """GET /{version}/account/regions"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/regions",
            method="GET",
            path_params={},
            request=request,
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
            region=region,
        )

    async def update_project_regions(
        self,
        project_id: str,
        *,
        primary_region: str | None = None,
        additional_regions: _RegionCodeList | None = None,
        timeout: float | None = None,
        bearer_token: str | None = None,
        region: str | None = None,
        **request: Any,
    ) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/regions"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/regions",
            method="PATCH",
            path_params={"projectId": project_id},
            request={
                "primaryRegion": primary_region,
                "additionalRegions": additional_regions,
                **request,
            },
            scope="account",
            timeout=timeout,
            bearer_token=bearer_token,
            region=region,
        )
