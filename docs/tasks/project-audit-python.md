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
6. [todo] docs(sdk-python:project): docs pages, docs index and README section for all of the above
7. [todo] release(sdk-python:project): ruff, mypy, pytest green; push branch; open one pull request to main

## Changes
| file (absolute, branch audit/project) | what changed | step |
|------|--------------|------|

## Findings

## Rejected / moved out

## Needs you

## Open questions
- none
