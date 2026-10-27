from __future__ import annotations

import asyncio
import json
from typing import Any
from urllib.parse import urlparse

import httpx
import pytest

import norbix_python.workflows as workflows
from norbix_python import (
    AsyncNorbix,
    Norbix,
    NorbixError,
    WorkflowRun,
    WorkflowRunTimeoutError,
    step_output,
)

"""The Workflows (beta) helpers of Code.Workflows.md §15: ``hub.code.wait_for_run``
(sync and async) and ``step_output``. Waits are made instant with a fake clock."""

RUN_ID = "wfr_4hT2b9QkLm3XcT1yRfGh7a"
RUN_PATH = f"/v3/code/workflows/runs/{RUN_ID}"


def _run(status: str, **extra: Any) -> dict[str, Any]:
    return {"run": {"runId": RUN_ID, "workflowId": "wf_1", "status": status, "steps": [], **extra}}


class FakeClock:
    """``time.monotonic`` that only moves when someone sleeps."""

    def __init__(self) -> None:
        self.now = 0.0
        self.sleeps: list[float] = []

    def clock(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds

    async def async_sleep(self, seconds: float) -> None:
        self.sleep(seconds)


@pytest.fixture
def clock(monkeypatch: pytest.MonkeyPatch) -> FakeClock:
    fake = FakeClock()
    monkeypatch.setattr(workflows, "_clock", fake.clock)
    monkeypatch.setattr(workflows, "_sleep", fake.sleep)
    monkeypatch.setattr(workflows, "_async_sleep", fake.async_sleep)
    return fake


def _answers(seen: list[httpx.Request], bodies: list[dict[str, Any]]) -> httpx.MockTransport:
    """Answer each request with the next body; the last one repeats."""

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json=bodies[min(len(seen), len(bodies)) - 1])

    return httpx.MockTransport(handler)


def _sync_client(transport: httpx.MockTransport) -> Norbix:
    return Norbix(project_id="test-project", bearer_token="test-token", http_client=httpx.Client(transport=transport))


def _wait_async(transport: httpx.MockTransport, **kwargs: Any) -> WorkflowRun:
    async def run() -> WorkflowRun:
        client = AsyncNorbix(
            project_id="test-project",
            bearer_token="test-token",
            http_client=httpx.AsyncClient(transport=transport),
        )
        try:
            return await client.hub.code.wait_for_run(RUN_ID, **kwargs)
        finally:
            await client.aclose()

    return asyncio.run(run())


def _assert_polled_the_run(seen: list[httpx.Request], times: int) -> None:
    assert len(seen) == times
    for request in seen:
        assert request.method == "GET"
        assert urlparse(str(request.url)).path == RUN_PATH
        assert request.content == b""


# --- wait_for_run --------------------------------------------------------------

RUNNING_THEN_SUCCEEDED = [_run("running"), _run("running"), _run("succeeded", output={"ok": True})]


def test_wait_for_run_polls_until_succeeded(clock: FakeClock) -> None:
    seen: list[httpx.Request] = []
    client = _sync_client(_answers(seen, RUNNING_THEN_SUCCEEDED))

    run = client.hub.code.wait_for_run(RUN_ID, timeout_ms=10_000, poll_ms=250)

    assert isinstance(run, WorkflowRun)
    assert run["status"] == "succeeded"
    assert run["output"] == {"ok": True}
    _assert_polled_the_run(seen, 3)
    assert clock.sleeps == [0.25, 0.25]


def test_async_wait_for_run_polls_until_succeeded(clock: FakeClock) -> None:
    seen: list[httpx.Request] = []

    run = _wait_async(_answers(seen, RUNNING_THEN_SUCCEEDED), timeout_ms=10_000, poll_ms=250)

    assert isinstance(run, WorkflowRun)
    assert run["status"] == "succeeded"
    _assert_polled_the_run(seen, 3)
    assert clock.sleeps == [0.25, 0.25]


@pytest.mark.parametrize("status", ["waiting", "failed", "cancelled"])
def test_wait_for_run_returns_at_once_on_a_settled_status(clock: FakeClock, status: str) -> None:
    seen: list[httpx.Request] = []
    waiting_on = [{"stepId": "approve", "kind": "approval", "assignees": ["usr_1"]}]
    client = _sync_client(_answers(seen, [_run(status, waitingOn=waiting_on)]))

    run = client.hub.code.wait_for_run(RUN_ID)

    assert run["status"] == status
    _assert_polled_the_run(seen, 1)
    assert clock.sleeps == []


def test_async_wait_for_run_returns_at_once_when_waiting(clock: FakeClock) -> None:
    seen: list[httpx.Request] = []

    run = _wait_async(_answers(seen, [_run("waiting")]))

    assert run["status"] == "waiting"
    _assert_polled_the_run(seen, 1)
    assert clock.sleeps == []


def test_wait_for_run_times_out_with_the_last_run(clock: FakeClock) -> None:
    seen: list[httpx.Request] = []
    client = _sync_client(_answers(seen, [_run("running", stepRuns=1), _run("running", stepRuns=2)]))

    with pytest.raises(WorkflowRunTimeoutError) as caught:
        client.hub.code.wait_for_run(RUN_ID, timeout_ms=3000, poll_ms=1000)

    error = caught.value
    assert isinstance(error, NorbixError)
    assert error.code == "NORBIX_WORKFLOW_RUN_TIMEOUT"
    assert error.run["status"] == "running"
    assert error.run["stepRuns"] == 2
    assert error.context == {"runId": RUN_ID}
    assert RUN_ID in error.message and "running" in error.message
    _assert_polled_the_run(seen, 4)  # t = 0, 1, 2 and the last look at 3 s
    assert clock.sleeps == [1.0, 1.0, 1.0]


def test_async_wait_for_run_times_out_with_the_last_run(clock: FakeClock) -> None:
    seen: list[httpx.Request] = []

    with pytest.raises(WorkflowRunTimeoutError) as caught:
        _wait_async(_answers(seen, [_run("running")]), timeout_ms=1500, poll_ms=1000)

    assert caught.value.run["status"] == "running"
    _assert_polled_the_run(seen, 3)
    assert clock.sleeps == [1.0, 0.5]  # the last sleep never runs past the deadline


def test_wait_for_run_without_a_run_raises_the_base_error(clock: FakeClock) -> None:
    seen: list[httpx.Request] = []
    client = _sync_client(_answers(seen, [{"responseStatus": {"isSuccess": True}}]))

    with pytest.raises(NorbixError) as caught:
        client.hub.code.wait_for_run(RUN_ID)

    assert type(caught.value) is NorbixError
    assert caught.value.code == "NORBIX_WORKFLOW_RUN_MISSING"


def test_wait_for_run_refuses_a_poll_interval_of_zero() -> None:
    client = _sync_client(_answers([], [_run("running")]))
    with pytest.raises(ValueError):
        client.hub.code.wait_for_run(RUN_ID, poll_ms=0)


# --- step_output ---------------------------------------------------------------

STEPS_RUN: dict[str, Any] = {
    "runId": RUN_ID,
    "status": "succeeded",
    "steps": [
        {"stepId": "charge", "status": "failed", "attempt": 1, "pass": 1, "error": {"code": "x"}},
        {"stepId": "charge", "status": "succeeded", "attempt": 2, "pass": 1, "output": {"n": "p1a2"}},
        {"stepId": "charge", "status": "succeeded", "attempt": 1, "pass": 2, "output": {"n": "p2a1"}},
        {"stepId": "charge", "status": "succeeded", "attempt": 3, "pass": 2, "output": {"n": "p2a3"}},
        {"stepId": "charge", "status": "failed", "attempt": 4, "pass": 3, "output": {"n": "p3a4"}},
        {"stepId": "notify", "status": "skipped", "attempt": 1, "pass": 1},
        {"stepId": "approve", "status": "succeeded", "attempt": 1, "pass": 1},
    ],
}


def test_step_output_takes_the_highest_pass_then_the_highest_attempt() -> None:
    assert step_output(STEPS_RUN, "charge") == {"n": "p2a3"}
    assert WorkflowRun(STEPS_RUN).step_output("charge") == {"n": "p2a3"}


def test_step_output_pass_wins_over_attempt() -> None:
    run = {"steps": [
        {"stepId": "s", "status": "succeeded", "attempt": 9, "pass": 1, "output": "old"},
        {"stepId": "s", "status": "succeeded", "attempt": 1, "pass": 2, "output": "new"},
    ]}
    assert step_output(run, "s") == "new"


@pytest.mark.parametrize("step_id", ["notify", "approve", "missing"])
def test_step_output_is_none_without_a_succeeded_output(step_id: str) -> None:
    assert step_output(STEPS_RUN, step_id) is None


def test_step_output_is_none_on_a_run_without_steps() -> None:
    assert step_output({"runId": RUN_ID, "status": "running"}, "charge") is None
    assert WorkflowRun({"steps": None}).step_output("charge") is None


def test_wait_for_run_answer_supports_step_output(clock: FakeClock) -> None:
    client = _sync_client(_answers([], [{"run": STEPS_RUN}]))
    run = client.hub.code.wait_for_run(RUN_ID)
    assert run.step_output("charge") == {"n": "p2a3"}
    assert json.loads(json.dumps(run)) == STEPS_RUN  # still a plain dict for JSON
