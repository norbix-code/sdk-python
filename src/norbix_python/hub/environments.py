from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

# Project environments — list, create, and delete the named environments a
# project owns (PROD plus any TEST/STAGING/... the user adds).
#
# These endpoints manage the *set* of environments. To make requests *inside*
# a given environment, set ``env`` on the client (``Norbix(env="TEST")`` or
# ``client.set_env("TEST")``) or per call (``env="TEST"``), which sends the
# ``norbix-env`` header.


class EnvironmentsModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def list(
        self, *, timeout: float | None = None, bearer_token: str | None = None, env: str | None = None, **request: Any
    ) -> Any:
        """GET /{version}/account/projects/environments

        Lists the project's environments. The response always includes "PROD",
        PROD-first.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/environments",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
            env=env,
        )

    def create(
        self,
        *,
        environment_name: str,
        integration: dict[str, Any],
        timeout: float | None = None,
        bearer_token: str | None = None,
        env: str | None = None,
        **request: Any,
    ) -> Any:
        """POST /{version}/account/projects/environments

        Creates a new environment. ``integration`` is a database integration
        that seeds the new env and becomes its default.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/environments",
            method="POST",
            path_params={},
            request={"environmentName": environment_name, "integration": integration, **request},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
            env=env,
        )

    def delete(
        self,
        *,
        environment_name: str,
        timeout: float | None = None,
        bearer_token: str | None = None,
        env: str | None = None,
        **request: Any,
    ) -> Any:
        """DELETE /{version}/account/projects/environments/{environmentName}

        Deletes a non-PROD environment, cascading its integrations. PROD is
        rejected by the backend.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/environments/{environmentName}",
            method="DELETE",
            path_params={"environmentName": environment_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
            env=env,
        )


class AsyncEnvironmentsModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(
        self, *, timeout: float | None = None, bearer_token: str | None = None, env: str | None = None, **request: Any
    ) -> Any:
        """GET /{version}/account/projects/environments"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/environments",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
            env=env,
        )

    async def create(
        self,
        *,
        environment_name: str,
        integration: dict[str, Any],
        timeout: float | None = None,
        bearer_token: str | None = None,
        env: str | None = None,
        **request: Any,
    ) -> Any:
        """POST /{version}/account/projects/environments"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/environments",
            method="POST",
            path_params={},
            request={"environmentName": environment_name, "integration": integration, **request},
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
            env=env,
        )

    async def delete(
        self,
        *,
        environment_name: str,
        timeout: float | None = None,
        bearer_token: str | None = None,
        env: str | None = None,
        **request: Any,
    ) -> Any:
        """DELETE /{version}/account/projects/environments/{environmentName}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/account/projects/environments/{environmentName}",
            method="DELETE",
            path_params={"environmentName": environment_name},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
            env=env,
        )
