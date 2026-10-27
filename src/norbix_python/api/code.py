"""Workflows (beta) on the Api (project-user auth).

An app user reads the runs that wait on them and resumes them; the signed
resume links of an approval e-mail work with no session at all. The Hub
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
