# Project audit — Python SDK: Project module completeness
This file: /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/docs/tasks/project-audit-python.md (branch audit/project)

## Goal
Give the Python SDK every Project-module route the TypeScript SDK already has: admin portal and legal settings, the public project config and legal pages, the developer MCP endpoint, and AI service users — sync and async, each with a test and a docs row.
Not in scope: AI plans, knowledge search, AI credits (decided internal); changes to the gateway or the TypeScript SDK.

## Plan
1. [done] docs(sdk-python:project): write this task file before any code
2. [done] feat(sdk-python:account:settings): admin URL, legal documents, expose legal, admin portal structure, admin portal service user
3. [done] feat(sdk-python:account:ai-service-users): create, list, delete AI service users, rotate and revoke their keys
4. [done] feat(sdk-python:account:mcp): the developer MCP endpoint — send a message (POST), read the server stream (GET), end the session (DELETE)
5. [done] feat(sdk-python:api:public): new `api.public` module — public project config and public legal document, no sign-in
6. [done] docs(sdk-python:project): docs pages, docs index and README section for all of the above
7. [done] release(sdk-python:project): ruff, mypy, pytest green; push branch; open one pull request to main — https://github.com/norbix-code/sdk-python/pull/25

## Checks
- `uv run ruff check .` — All checks passed
- `uv run mypy src` — Success: no issues found in 37 source files
- `uv run pytest` — 799 passed (31 new: 20 settings/service-user shapes, 7 MCP, 4 public)
- venv lives outside the repo: `UV_PROJECT_ENVIRONMENT=~/scratch/project-python/venv`

## Changes
| file (absolute, branch audit/project) | what changed | step |
|------|--------------|------|
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/docs/tasks/project-audit-python.md | this task file | 1–7 |
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/src/norbix_python/hub/account.py | 5 settings methods, 5 AI service user methods, 3 MCP methods + MCP helpers (sync + async) | 2, 3, 4 |
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/tests/hub/test_account_project.py | new: one table, 10 routes, each sent through the sync and async client (verb, path, body, headers) | 2, 3 |
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/src/norbix_python/transport.py | additive send options: `extra_headers`, `query`, `response_type="envelope"` (sync + async) | 4 |
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/tests/hub/test_account_mcp.py | new: initialize session header, SSE answer parsing, 202 notification, stream resume, end session, 404, async twins | 4 |
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/src/norbix_python/api/public.py | new module `api.public`: config + legal, no sign-in (sync + async) | 5 |
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/src/norbix_python/api/__init__.py | `public` added to both API namespaces | 5 |
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/src/norbix_python/client.py | `NorbixApi.public` / `.Public` | 5 |
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/tests/api/test_public.py | new: API host, path, no Authorization even when signed in, NorbixApi flat access, async twin | 5 |
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/docs/hub/account.md | 13 rows + "The developer MCP endpoint" section | 6 |
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/docs/api/public.md | new page | 6 |
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/docs/api/_index.md, /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/docs/hub/_index.md | `public` row; account count 36 → 56 | 6 |
| /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/README.md | module list mentions `client.public`; new section "Project settings, public pages, MCP and AI service users" | 6 |

## Findings
fix(sdk-python:client:api): the flat `NorbixApi` client has no `ai`, although `api.ai` exists since the AI pull request #23 — open, not fixed here
    where: /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/src/norbix_python/client.py:243 (branch audit/project)
```python
# src/norbix_python/client.py:242-248 (audit/project)
        api = ApiNamespace(self._transport)
        self.database = api.database
        self.membership = api.membership
        self.echo = api.echo
        self.files = api.files
        self.public = api.public      # added in step 5
                                      # <-- missing: self.ai = api.ai (and self.Ai)
```

decision(sdk-python:account:settings): new methods use scope `project`; the older project-settings methods use `account`, which needlessly demands `account_id` on the client — open
    where: /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/src/norbix_python/hub/account.py:325 (branch audit/project)
```python
# src/norbix_python/hub/account.py:325-333 (audit/project)
    def update_project_accent_color(self, project_id: str, *, ...) -> Any:
        """PATCH /{version}/account/projects/{projectId}/settings/accent-color"""
        return self._transport.send(
            target="hub",
            path="/{version}/account/projects/{projectId}/settings/accent-color",
            method="PATCH",
            path_params={"projectId": project_id},
            request=request,
            scope="account",          # <-- here: gateway reads the account from the session; TS uses 'project'
```

fix(sdk-ts:api:public): the TypeScript `getPublicProjectConfig` / `getPublicProjectLegal` demand a token, but the gateway routes are anonymous — open, other repo
    where: /Users/djovaisas/Projects/norbix/sdks/norbix-js src/api/public.ts:28 and :47 (branch origin/main b7230dc, not edited)
```ts
// norbix-js src/api/public.ts:24-29 (origin/main)
      path: '/{version}/public/projects/{ProjectId}/config',
      method: 'GET',
      request,
      pathParams: ['ProjectId'],
      scope: 'project',               // <-- here: needs a token; gateway has no [Authenticate] on this route
```

fix(sdk-ts:account:mcp): the TypeScript `mcp` only sends POST and cannot read the `Mcp-Session-Id` answer header, so no session can follow `initialize` — open, other repo
    where: /Users/djovaisas/Projects/norbix/sdks/norbix-js src/hub/account.ts:2055-2068 (branch origin/main b7230dc, not edited)
```ts
// norbix-js src/hub/account.ts:2059-2066 (origin/main)
    return this.transport.send<string>({
      target: 'hub',
      path: '/{version}/account/mcp',
      method: 'POST',                 // <-- here: GET (stream) and DELETE (end session) aliases unreachable
      request,
      pathParams: [],
      scope: 'project',
```

fix(sdk-python:transport): the body drops every `None` value, so a caller cannot send an explicit null (admin URL reset needs `url=""` instead) — open, documented in the docstring
    where: /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/src/norbix_python/transport.py:393 (branch audit/project)
```python
# src/norbix_python/transport.py:393 (audit/project)
    remaining = {k: v for k, v in request.items() if v is not None}   # <-- here: explicit null never reaches the gateway
```

docs(sdk-python:docs:index): endpoint counts in the docs index pages are stale (hub ai says 14, page has 20; hub email 1 vs 2; api database 18 vs 20; api files 10 vs 9; push and sms pages missing from the index) — open; only account and public fixed here
    where: /Users/djovaisas/Projects/norbix/worktrees/sdks/norbix-python/audit/project/docs/hub/_index.md:6 (branch audit/project)

## Rejected / moved out
- decision(sdk-python:account:ai): AI plans, knowledge search and AI credits not added — rejected — decided internal by the campaign brief — none
- decision(sdk-python:account:mcp): one TS-style `mcp` for all three verbs not copied; three methods instead (`mcp` POST, `mcp_stream` GET, `mcp_end_session` DELETE), because each verb needs different headers and arguments — rejected (by design) — none
- decision(sdk-python:account:mcp): no real streaming for `mcp_stream`; it returns when the server closes the stream or the timeout ends, because the SDK transport is request/response only — rejected (by design) — none

## Needs you
- [ ] release(sdk-python:project): review and squash-merge the pull request to main (expected next version: minor, no breaking change) — needs you · action: merge the PR listed in the final message
- [ ] decision(sdk-python:findings): route the findings above (NorbixApi `ai`, settings scope, TS public scope, TS mcp, null bodies, docs counts) — needs you · action: pick fix-here / own branch / hand out

## Open questions
- none
