from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

# HAND-WRITTEN module: scripts/generate_endpoints.py (gitignored, not in the
# repo) did not produce it. Keep it — and its registration in hub/__init__.py —
# when the hub modules are regenerated.


class TriggersModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_triggers_needing_attention(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/triggers/attention

        Lists the triggers of one type that need attention (for example, a
        trigger whose provider integration is gone). Pass ``triggerType=...``
        (Membership, Schema, Files, Payments or Ai). Response: ``{"items": [...]}``.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/triggers/attention",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def check_trigger_execution_identity(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/triggers/execution-identity/check

        Answers whether the caller may name ``executionIdentityId`` (empty = the
        environment's default) for this ``triggerType`` and ``action``, and what the
        identity lacks for that action. Nothing is saved.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/triggers/execution-identity/check",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_trigger_runs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/triggers/runs

        Lists one trigger's runs, newest first, kept 30 days. Pass ``triggerType=...``
        and ``triggerId=...``, optionally ``status=...`` (queued, running, succeeded,
        failed or skipped) and the paging fields.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/triggers/runs",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_trigger_run(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/triggers/runs/{Id}

        One run (``trr_...``). ``triggerType=...`` is required: a run of another
        type answers not found.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/triggers/runs/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_trigger_definition(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/triggers/{id}/definition

        One trigger (``trg_...``) in the shape its save takes: read, change, save
        it back through the module's ``save_*_trigger``. ``triggerType=...`` is
        required; a Schema trigger also needs ``schemaId=...``. The answer holds
        the trigger under ``"trigger"``.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/triggers/{id}/definition",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_trigger_pre_execute_code(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/triggers/pre-execute-code/test

        Runs a trigger's ``code`` (the preExecuteCode: C# ending in ``return true;``
        or ``return false;``) for ``triggerType`` against the sample ``newRecord``
        and ``oldRecord`` (JSON text), without saving or firing anything. The
        answer says whether the trigger would run and lists the code's problems.
        """
        return self._transport.send(
            target="hub",
            path="/{version}/triggers/pre-execute-code/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncTriggersModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_triggers_needing_attention(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/triggers/attention

        Lists the triggers of one type that need attention (for example, a
        trigger whose provider integration is gone). Pass ``triggerType=...``
        (Membership, Schema, Files, Payments or Ai). Response: ``{"items": [...]}``.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/triggers/attention",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def check_trigger_execution_identity(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/triggers/execution-identity/check

        Answers whether the caller may name ``executionIdentityId`` (empty = the
        environment's default) for this ``triggerType`` and ``action``, and what the
        identity lacks for that action. Nothing is saved.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/triggers/execution-identity/check",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_trigger_runs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/triggers/runs

        Lists one trigger's runs, newest first, kept 30 days. Pass ``triggerType=...``
        and ``triggerId=...``, optionally ``status=...`` (queued, running, succeeded,
        failed or skipped) and the paging fields.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/triggers/runs",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_trigger_run(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/triggers/runs/{Id}

        One run (``trr_...``). ``triggerType=...`` is required: a run of another
        type answers not found.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/triggers/runs/{Id}",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_trigger_definition(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/triggers/{id}/definition

        One trigger (``trg_...``) in the shape its save takes: read, change, save
        it back through the module's ``save_*_trigger``. ``triggerType=...`` is
        required; a Schema trigger also needs ``schemaId=...``. The answer holds
        the trigger under ``"trigger"``.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/triggers/{id}/definition",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_trigger_pre_execute_code(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/triggers/pre-execute-code/test

        Runs a trigger's ``code`` (the preExecuteCode: C# ending in ``return true;``
        or ``return false;``) for ``triggerType`` against the sample ``newRecord``
        and ``oldRecord`` (JSON text), without saving or firing anything. The
        answer says whether the trigger would run and lists the code's problems.
        """
        return await self._transport.send(
            target="hub",
            path="/{version}/triggers/pre-execute-code/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
