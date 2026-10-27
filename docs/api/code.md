# API · Code — Workflows (beta)

Access with `norbix.api.code` (or `NorbixApi(...).code`; the same methods,
awaited, on `AsyncNorbix`). Workflows are in beta; bugs may occur.

An app user (project-user login) reads the workflow runs that wait on them
and answers them. The team's view of the same routes, and every other
workflow route, is on [HUB · Code](../hub/code.md#workflows-beta).

| Method | Verb | Path | Scope | Parameters go in |
| --- | --- | --- | --- | --- |
| `get_code_workflow_waiting_runs` | `GET` | `/{version}/code/workflows/runs` | `project` | query: `status?`, `waitingKind?`, `assignee?` (absent = `me` for an app user), `workflowId?`, `key?`, `pageSize`, `startingAfter`, `endingBefore` |
| `resume_code_workflow_run` | `POST` | `/{version}/code/workflows/runs/{RunId}/resume` | `project` | path: `run_id`; JSON body: `stepId?`, `decision?` (`"approved"` / `"rejected"`), `payload?` |
| `open_code_workflow_resume_link` | `GET` | `/{version}/code/workflows/resume/{Token}` | `optional` | path: `token` (checks the link, changes nothing) |
| `use_code_workflow_resume_link` | `POST` | `/{version}/code/workflows/resume/{Token}` | `optional` | path: `token` (answers the link) |

The two resume-link routes need no session: the signed token in the link is
the key, so a client with no credentials can call them. Auth is still sent
when the client has a token.

```python
inbox = norbix.api.code.get_code_workflow_waiting_runs(waitingKind="approval")
for row in inbox["list"]["items"]:
    norbix.api.code.resume_code_workflow_run(row["runId"], decision="approved")

link = norbix.api.code.open_code_workflow_resume_link(token)   # what the link would do
done = norbix.api.code.use_code_workflow_resume_link(token)    # answer it
```

Every method, its verb, path, query and body are asserted in
`tests/api/test_code.py`, for the sync and the async client.
