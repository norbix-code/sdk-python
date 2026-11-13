from __future__ import annotations

import json
from typing import Any
from urllib.parse import urlparse

import pytest

from ..helpers import make_client

"""The "Code call" and "Workflow call" scheduler task bodies.

The task goes on the wire under ``task`` with the discriminator the gateway's
SchedulerTaskRequestJsonConverter reads (``CodeFunctionalCall``,
``WorkflowCall``) and the field names of Hub.Scheduler/Tasks/Save.Code.cs and
Save.Workflow.cs. Twins: sdk-go TestSaveSchedulerTaskSendsCodeAndWorkflowTasks
(norbix/hub/scheduler_task_bodies_test.go), sdk-ts
tests/hub/scheduler-task-bodies.test.ts. Every call goes to a capture
transport, so nothing leaves the process.
"""

CODE_TASK: dict[str, Any] = {
    "type": "CodeFunctionalCall",
    "functionRef": {"integrationId": "int_lambda", "functionId": "nightly-report", "qualifier": "live"},
    "invocationType": "Async",
    "config": '{"source":"python"}',
}

WORKFLOW_TASK: dict[str, Any] = {
    "type": "WorkflowCall",
    "workflowRef": "wf_3kQ9mZ2vXc8LpR4wT7yH1n",
    "payload": {"source": "python"},
}


@pytest.mark.parametrize("task", [CODE_TASK, WORKFLOW_TASK], ids=["CodeFunctionalCall", "WorkflowCall"])
def test_save_scheduler_task_sends_code_and_workflow_tasks(task: dict[str, Any]) -> None:
    client, transport = make_client()
    request = {
        "initiatorUserId": "usr_1",
        "name": "Nightly",
        "cron": "0 2 * * *",
        "isEnabled": True,
        "stopOnError": False,
        "task": task,
    }
    client.hub.scheduler.save_scheduler_task(**request)

    assert transport.last_request is not None
    url = urlparse(transport.last_request["url"])
    assert transport.last_request["method"] == "POST"
    assert url.path == "/v3/scheduler/tasks"
    assert url.query == ""
    assert json.loads(transport.last_request["body"]) == request
