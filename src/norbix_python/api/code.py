"""Workflows (beta) on the Api (project-user auth).

An app user reads the runs that wait on them and resumes them; the signed
resume links of an approval e-mail work with no session at all. An app's
backend starts a run, reads runs and their logs, resumes by key, retries a
failed step and stops a run on the same host (the api twins, as in sdk-ts). The Hub
twins of these routes are on ``hub.code``. Workflows are in beta; bugs may
occur.
"""

from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport


class CodeModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def get_code_workflow_waiting_runs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/runs

        The inbox of waiting runs; query `status?`, `waitingKind?`, `assignee?`, `workflowId?`, `key?`, paging.
        """
        return self._transport.send(
            target="api",
            path="/{version}/code/workflows/runs",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def resume_code_workflow_run(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/runs/{RunId}/resume

        Resume a waiting run; body `stepId?`, `decision?` ("approved" / "rejected"), `payload?`.
        """
        return self._transport.send(
            target="api",
            path="/{version}/code/workflows/runs/{RunId}/resume",
            method="POST",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def open_code_workflow_resume_link(self, token: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/resume/{Token}

        Check a signed resume link (changes nothing). No session needed: the link is the key;
        auth is still sent when the client has a token.
        """
        return self._transport.send(
            target="api",
            path="/{version}/code/workflows/resume/{Token}",
            method="GET",
            path_params={"Token": token},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def use_code_workflow_resume_link(self, token: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/resume/{Token}

        Answer a signed resume link. No session needed: the link is the key; auth is still
        sent when the client has a token.
        """
        return self._transport.send(
            target="api",
            path="/{version}/code/workflows/resume/{Token}",
            method="POST",
            path_params={"Token": token},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def invoke_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/{Id}/invoke

        Start a run; body ``payload?``, ``waitSeconds?`` (0-30), ``runVersion?`` (``"draft"`` or a version number as a string).
        """
        return self._transport.send(
            target="api",
            path="/{version}/code/workflows/{Id}/invoke",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_workflow_runs(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/{Id}/runs

        A workflow's runs, newest first; query ``status?``, ``from?``, ``to?``, ``pageSize?``, ``startingAfter?``, ``endingBefore?``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/code/workflows/{Id}/runs",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_workflow_run(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/runs/{RunId}

        One run: the header and every step execution.
        """
        return self._transport.send(
            target="api",
            path="/{version}/code/workflows/runs/{RunId}",
            method="GET",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_code_workflow_run_logs(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/runs/{RunId}/logs

        A run's log lines; query ``stepId?``, ``level?``, ``pageSize?``, ``startingAfter?``, ``endingBefore?``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/code/workflows/runs/{RunId}/logs",
            method="GET",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def resume_code_workflow_run_by_key(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/{Id}/resume

        Resume the run waiting on a key; body ``key``, ``stepId?``, ``decision?``, ``payload?``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/code/workflows/{Id}/resume",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def retry_code_workflow_run_step(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/runs/{RunId}/retry

        Retry the failed step; body ``stepId?``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/code/workflows/runs/{RunId}/retry",
            method="POST",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def cancel_code_workflow_run(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/runs/{RunId}/cancel

        Stop a running or waiting run; body ``reason?``.
        """
        return self._transport.send(
            target="api",
            path="/{version}/code/workflows/runs/{RunId}/cancel",
            method="POST",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncCodeModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_code_workflow_waiting_runs(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/runs

        The inbox of waiting runs; query `status?`, `waitingKind?`, `assignee?`, `workflowId?`, `key?`, paging.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/code/workflows/runs",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def resume_code_workflow_run(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/runs/{RunId}/resume

        Resume a waiting run; body `stepId?`, `decision?` ("approved" / "rejected"), `payload?`.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/code/workflows/runs/{RunId}/resume",
            method="POST",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def open_code_workflow_resume_link(self, token: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/resume/{Token}

        Check a signed resume link (changes nothing). No session needed: the link is the key;
        auth is still sent when the client has a token.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/code/workflows/resume/{Token}",
            method="GET",
            path_params={"Token": token},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def use_code_workflow_resume_link(self, token: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/resume/{Token}

        Answer a signed resume link. No session needed: the link is the key; auth is still
        sent when the client has a token.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/code/workflows/resume/{Token}",
            method="POST",
            path_params={"Token": token},
            request=request,
            scope="optional",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def invoke_code_workflow(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/{Id}/invoke

        Start a run; body ``payload?``, ``waitSeconds?`` (0-30), ``runVersion?`` (``"draft"`` or a version number as a string).
        """
        return await self._transport.send(
            target="api",
            path="/{version}/code/workflows/{Id}/invoke",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_workflow_runs(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/{Id}/runs

        A workflow's runs, newest first; query ``status?``, ``from?``, ``to?``, ``pageSize?``, ``startingAfter?``, ``endingBefore?``.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/code/workflows/{Id}/runs",
            method="GET",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_workflow_run(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/runs/{RunId}

        One run: the header and every step execution.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/code/workflows/runs/{RunId}",
            method="GET",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_code_workflow_run_logs(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: GET /{version}/code/workflows/runs/{RunId}/logs

        A run's log lines; query ``stepId?``, ``level?``, ``pageSize?``, ``startingAfter?``, ``endingBefore?``.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/code/workflows/runs/{RunId}/logs",
            method="GET",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def resume_code_workflow_run_by_key(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/{Id}/resume

        Resume the run waiting on a key; body ``key``, ``stepId?``, ``decision?``, ``payload?``.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/code/workflows/{Id}/resume",
            method="POST",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def retry_code_workflow_run_step(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/runs/{RunId}/retry

        Retry the failed step; body ``stepId?``.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/code/workflows/runs/{RunId}/retry",
            method="POST",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def cancel_code_workflow_run(self, run_id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """Beta: POST /{version}/code/workflows/runs/{RunId}/cancel

        Stop a running or waiting run; body ``reason?``.
        """
        return await self._transport.send(
            target="api",
            path="/{version}/code/workflows/runs/{RunId}/cancel",
            method="POST",
            path_params={"RunId": run_id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
