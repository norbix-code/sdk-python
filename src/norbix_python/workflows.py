"""Hand-written helpers for Workflows (beta): wait for a run, read a step's output.

``hub.code.wait_for_run(run_id)`` polls ``GET /{version}/code/workflows/runs/{RunId}``
until the run is finished (``succeeded``, ``failed``, ``cancelled``) or ``waiting``,
and gives back the run as a :class:`WorkflowRun`. :func:`step_output` (also
``WorkflowRun.step_output``) reads the output of a step's latest succeeded
execution. Workflows are in beta; bugs may occur.
"""

from __future__ import annotations

import asyncio
import time
from collections.abc import Awaitable, Callable, Mapping
from typing import Any

from .errors import NorbixError, WorkflowRunTimeoutError

#: Run statuses ``wait_for_run`` stops on: finished, or parked on a wait.
SETTLED_RUN_STATUSES: frozenset[str] = frozenset({"succeeded", "failed", "cancelled", "waiting"})

# Indirections so tests can make the waits instant.
_sleep: Callable[[float], None] = time.sleep
_async_sleep: Callable[[float], Awaitable[None]] = asyncio.sleep
_clock: Callable[[], float] = time.monotonic


class WorkflowRun(dict[str, Any]):
    """A workflow run (``WorkflowRunDto``) as a plain dict, plus :meth:`step_output`."""

    def step_output(self, step_id: str) -> Any:
        """The output of the latest succeeded execution of ``step_id``; ``None`` when none."""
        return step_output(self, step_id)


def step_output(run: Mapping[str, Any], step_id: str) -> Any:
    """The output of the latest execution of ``step_id`` with status ``succeeded``.

    A step may run several times — automatic and manual retries (``attempt``) and
    loops (``pass``). The latest is the highest ``pass``, then the highest
    ``attempt``. ``None`` when the step has no succeeded execution (or no output).
    """
    best: Mapping[str, Any] | None = None
    best_key = (-1, -1)
    for step in run.get("steps") or []:
        if not isinstance(step, Mapping):
            continue
        if step.get("stepId") != step_id or step.get("status") != "succeeded":
            continue
        key = (_int(step.get("pass")), _int(step.get("attempt")))
        if best is None or key > best_key:
            best, best_key = step, key
    return None if best is None else best.get("output")


def _int(value: Any) -> int:
    return value if isinstance(value, int) and not isinstance(value, bool) else 0


def _run_of(answer: Any) -> WorkflowRun:
    run = answer.get("run") if isinstance(answer, Mapping) else None
    if not isinstance(run, Mapping):
        raise NorbixError(
            "The workflow run answer carried no run.",
            code="NORBIX_WORKFLOW_RUN_MISSING",
            body=answer,
        )
    return WorkflowRun(run)


def _check(timeout_ms: int, poll_ms: int) -> None:
    if timeout_ms < 0:
        raise ValueError("timeout_ms must be 0 or more")
    if poll_ms <= 0:
        raise ValueError("poll_ms must be more than 0")


def _timed_out(run: WorkflowRun, timeout_ms: int) -> WorkflowRunTimeoutError:
    return WorkflowRunTimeoutError(
        f"Workflow run {run.get('runId')} was still {run.get('status')} after {timeout_ms} ms.",
        run=run,
    )


def wait_for_run(fetch: Callable[[], Any], *, timeout_ms: int, poll_ms: int) -> WorkflowRun:
    """Poll ``fetch`` (one ``get_code_workflow_run`` call) until the run settles."""
    _check(timeout_ms, poll_ms)
    deadline = _clock() + timeout_ms / 1000
    while True:
        run = _run_of(fetch())
        if run.get("status") in SETTLED_RUN_STATUSES:
            return run
        remaining = deadline - _clock()
        if remaining <= 0:
            raise _timed_out(run, timeout_ms)
        _sleep(min(poll_ms / 1000, remaining))


async def wait_for_run_async(
    fetch: Callable[[], Awaitable[Any]], *, timeout_ms: int, poll_ms: int
) -> WorkflowRun:
    """The async twin of :func:`wait_for_run`."""
    _check(timeout_ms, poll_ms)
    deadline = _clock() + timeout_ms / 1000
    while True:
        run = _run_of(await fetch())
        if run.get("status") in SETTLED_RUN_STATUSES:
            return run
        remaining = deadline - _clock()
        if remaining <= 0:
            raise _timed_out(run, timeout_ms)
        await _async_sleep(min(poll_ms / 1000, remaining))
