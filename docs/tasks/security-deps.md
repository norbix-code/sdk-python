# Security dependency update (2026-10-05)
This file: https://github.com/norbix-code/sdk-python/blob/main/docs/tasks/security-deps.md (branch main; the worktree was removed after shipping)

## Goal
Close the 7 open Dependabot security alerts on `norbix-code/sdk-python` `main` by moving
GitPython and urllib3 to patched versions in the lock file, with tests, lint, types and build green.
Not in scope: the ruff / mypy dev-tool bump in Dependabot pull request #30 (not a security fix),
any change to the SDK's runtime dependencies (`httpx`, `pydantic`), any SDK code change.

## Plan
1. [done] chore(sdk-python:deps): read every open alert and trace each package to the dependency that pulls it in
2. [done] docs(sdk-python:tasks): write this task file with the alert table
3. [done] chore(sdk-python:deps): take the Dependabot lock changes from #28 (GitPython 3.1.59 → 3.1.62) and #29 (urllib3 2.7.0 → 2.8.0) onto this branch
4. [done] fix(sdk-python:deps): add uv constraint floors (urllib3 ≥ 2.8.0, GitPython ≥ 3.1.62) so a later re-lock cannot fall back to a vulnerable version
5. [done] test(sdk-python): tests, ruff, mypy, build on Python 3.10, 3.12, 3.13 — local: 865 passed on each, ruff and mypy clean, wheel built; CI runs on the pull request
6. [done] release(sdk-python): shipped as #33 (rebase merge, all checks green) and released as v3.9.1 — tag on merge commit `cf164fd`, GitHub release published 08:13 UTC, PyPI `norbix 3.9.1` (wheel + sdist) with `Requires-Dist` still only httpx ≥ 0.27.0 and pydantic ≥ 2.0
7. [done] chore(sdk-python:deps): Dependabot #28 and #29 closed with a comment pointing at #33, their branches deleted; all 7 alerts (#31–#37) are `fixed` at 08:13 UTC, 0 open alerts left
8. [done] docs(sdk-python:tasks): this final update of the task file, shipped as a docs-only pull request (no release)

## Alerts
Read with `nbx-gh api 'repos/norbix-code/sdk-python/dependabot/alerts?state=open'` on 2026-10-05: 7 open (4 high, 3 moderate).
Dependabot labels all 7 as `runtime` scope because they sit in `uv.lock`; that is wrong for this repo.
`uv tree --invert` shows both packages come **only** from the `dev` group, through `python-semantic-release`
(the release tool). The published `norbix` wheel depends on `httpx` and `pydantic` only — neither
pulls in urllib3 or GitPython. **No SDK user installs either package because of us.**

| # | package | severity | affected | fixed | kind of dependency | does our code path use the vulnerable part? | advisory |
|---|---------|----------|----------|-------|--------------------|---------------------------------------------|----------|
| 31 | urllib3 | high | ≥ 1.26.0, < 2.8.0 | 2.8.0 | dev / CI only (`python-semantic-release` → `requests` → urllib3) | No. HTTPS proxy TLS settings — the release job runs on GitHub's runner with no proxy. | [GHSA-8988-9cw3-xx77](https://github.com/advisories/GHSA-8988-9cw3-xx77) (CVE-2026-97687) |
| 32 | urllib3 | high | ≥ 1.10.3, < 2.8.0 | 2.8.0 | dev / CI only | Partly. `requests` reads chunked responses, but only from `api.github.com` in the release job; a hostile server is needed. | [GHSA-vxq7-64xx-v4gw](https://github.com/advisories/GHSA-vxq7-64xx-v4gw) (CVE-2026-97689) |
| 33 | urllib3 | moderate | ≥ 2.6.2, < 2.8.0 | 2.8.0 | dev / CI only | Partly. Same as #32: needs a hostile server sending deflate chunks. | [GHSA-gh4c-6fx4-qh6g](https://github.com/advisories/GHSA-gh4c-6fx4-qh6g) (CVE-2026-97688) |
| 34 | GitPython | high | ≤ 3.1.59 | 3.1.60 | dev / CI only (`python-semantic-release` → GitPython; also our release parser and its test) | Yes, the code is reached: semantic-release opens our own checkout with `Repo(...)`. The content comes from protected `main`, so an attacker needs a merged pull request first. | [GHSA-239g-whfq-7xj9](https://github.com/advisories/GHSA-239g-whfq-7xj9) (CVE-2026-87817) |
| 35 | GitPython | moderate | ≥ 3.1.59, < 3.1.60 | 3.1.60 | dev / CI only | No. Only `repo.index.diff("HEAD")` is called; nothing passes `--no-index` or user options to diff. | [GHSA-whh4-5q6c-9v3x](https://github.com/advisories/GHSA-whh4-5q6c-9v3x) |
| 36 | GitPython | high | ≤ 3.1.59 | 3.1.60 | dev / CI only | Yes, the code is reached: semantic-release reads the author of every commit since the last tag. A crafted author string on `main` could hang the release job (no data leak). | [GHSA-g5vv-9gxw-82hx](https://github.com/advisories/GHSA-g5vv-9gxw-82hx) (CVE-2026-87819) |
| 37 | GitPython | moderate | ≤ 3.1.61 | 3.1.62 | dev / CI only | No. The repo has no submodules and nothing calls submodule update. | [GHSA-59cr-6r3x-644w](https://github.com/advisories/GHSA-59cr-6r3x-644w) |

Nothing blocks the fix: `python-semantic-release` 10.7.0 asks for `gitpython~=3.0` and `requests~=2.25`,
and `requests` 2.33.1 asks for `urllib3<3,>=1.26`, so the patched versions fit without touching any other package.

Evidence — who pulls the packages in (`uv tree --frozen --invert`, branch fix/security-deps, before the change, now merged):
```text
urllib3 v2.7.0
└── requests v2.33.1
    ├── python-gitlab v6.5.0
    │   └── python-semantic-release v10.7.0
    │       └── norbix v1.1.1 (group: dev)          <-- here: dev group only
    ├── python-semantic-release v10.7.0 (*)
    └── requests-toolbelt v1.0.0
gitpython v3.1.59
└── python-semantic-release v10.7.0
    └── norbix v1.1.1 (group: dev)                  <-- here: dev group only
```
```toml
# pyproject.toml:10 and :18-24 (main) — runtime vs dev
dependencies = ["httpx>=0.27.0", "pydantic>=2.0"]     # <-- here: runtime; no urllib3, no GitPython
[dependency-groups]
dev = [
  ...
  "python-semantic-release>=9.15.0",                  # <-- here: the only way both packages come in
]
```
```python
# .venv/.../semantic_release/gitproject.py:226-227 (python-semantic-release 10.7.0) — the only diff call
        with Repo(str(self.project_root)) as repo:      # <-- here: opens our checkout (alert #34 path)
            has_index_changes = bool(repo.index.diff("HEAD"))   # <-- here: no --no-index (alert #35 not reached)
```

## Changes
| file (absolute, branch) | what changed | step |
|------|--------------|------|
| https://github.com/norbix-code/sdk-python/blob/main/docs/tasks/security-deps.md (main) | this task file | 2 |
| https://github.com/norbix-code/sdk-python/blob/main/uv.lock (main) | GitPython 3.1.59 → 3.1.62 (Dependabot #28 commit, cherry-picked) | 3 |
| https://github.com/norbix-code/sdk-python/blob/main/uv.lock (main) | urllib3 2.7.0 → 2.8.0 (Dependabot #29 commit, cherry-picked) | 3 |
| https://github.com/norbix-code/sdk-python/blob/main/pyproject.toml (main) | new `[tool.uv] constraint-dependencies` floors: gitpython ≥ 3.1.62, urllib3 ≥ 2.8.0 | 4 |
| https://github.com/norbix-code/sdk-python/blob/main/uv.lock (main) | `[manifest] constraints` block recorded by `uv lock`; no package version moved | 4 |

Evidence — the change (step 3 and 4):
```diff
# uv.lock (main) — steps 3 and 4
+[manifest]
+constraints = [
+    { name = "gitpython", specifier = ">=3.1.62" },
+    { name = "urllib3", specifier = ">=2.8.0" },
+]
 name = "gitpython"
-version = "3.1.59"
+version = "3.1.62"                                   # <-- fixes alerts 34, 35, 36, 37
 name = "urllib3"
-version = "2.7.0"
+version = "2.8.0"                                    # <-- fixes alerts 31, 32, 33
```
```toml
# pyproject.toml:26-31 (main) — step 4, after
[tool.uv]
# Security floors for packages only the release tool pulls in (python-semantic-release →
# GitPython, requests → urllib3). Locking only, never in the published wheel's metadata.
# Alerts: GHSA-239g-whfq-7xj9, GHSA-g5vv-9gxw-82hx, GHSA-whh4-5q6c-9v3x, GHSA-59cr-6r3x-644w
# (GitPython), GHSA-8988-9cw3-xx77, GHSA-vxq7-64xx-v4gw, GHSA-gh4c-6fx4-qh6g (urllib3).
constraint-dependencies = ["gitpython>=3.1.62", "urllib3>=2.8.0"]   # <-- added
```
Proof the published package did not change its dependencies (wheel built from this branch):
```text
Requires-Python: >=3.10
Requires-Dist: httpx>=0.27.0
Requires-Dist: pydantic>=2.0
```
No major bump anywhere: GitPython stays on 3.1.x (3.2.0 exists; not needed), urllib3 stays on 2.x, supported Python stays `>=3.10`.

## Findings
- docs(sdk-python:release): the task brief said the latest release is v3.8.0 at `c445230`; on 2026-10-05 `origin/main` is `8c2760e` and the latest release is v3.9.0 (database methods, released 08:00 UTC). The work branches from `8c2760e`. — noted, nothing to fix
    where: https://github.com/norbix-code/sdk-python/releases/tag/v3.9.0
- chore(sdk-python:deps): Dependabot pull request #30 (ruff 0.16.9 → 0.16.10, mypy, `librt` 0.15 → 0.16) opened today; dev tools only, no advisory — left open for the weekly dependency pass
    where: https://github.com/norbix-code/sdk-python/pull/30
- chore(sdk-python:deps): Dependabot marks every `uv.lock` entry as `runtime` scope, so dev-only alerts look like SDK-user alerts. The table above corrects that by hand; nothing in GitHub can be set to change it. — left open
    where: https://github.com/norbix-code/sdk-python/security/dependabot
- chore(sdk-python:ci): the main checkout `/Users/djovaisas/Projects/norbix/sdks/norbix-python` is on `chore/ci-release-fixes`, not `main` (nbx-doctor WARN) — not touched, as asked
    where: /Users/djovaisas/Projects/norbix/sdks/norbix-python (branch chore/ci-release-fixes)

- chore(git:nbx-ship): the release wait finds the tag with `git tag --points-at <merge commit>`; the Release workflow tags the *remote tip* ("Sync branch tip" step), so if a second merge lands during the run, nbx-ship prints "tag: none" although a release was made — left open
    where: /Users/djovaisas/Projects/norbix/scripts/git/nbx-ship:129
```bash
# scripts/git/nbx-ship:118-131 (not a git repo — workspace scripts)
  sha=$(git rev-parse "origin/$base")
  ...
    git fetch -q --tags origin
    tag=$(git tag --points-at "$sha" | head -1)      # <-- here: only the merge commit, not the tip the workflow released
```
```yaml
# .github/workflows/release.yml:51-58 (main)
      - name: Sync branch tip
        ...
          git reset --hard "origin/${GITHUB_REF_NAME}"   # <-- here: the job may release a later commit
```
- decision(sdk-python:release): the branch carries one `fix(deps)` commit, so the merge makes a patch release (expected v3.9.1). The wheel's code and dependencies are the same as v3.9.0; the release is how the brief asked to prove the cycle. Dependabot's own `chore(deps)` commits do not release. — done

- chore(git:nbx-ship): the new release wait (changed 2026-10-05) worked on its first real run: it found Release run 37282223595 for `cf164fd`, waited for it, and printed `tag: v3.9.1 · GitHub release page: v3.9.1`; checked by hand against `nbx-gh release view v3.9.1` and PyPI — done (the tip-race gap above is still untested)
    where: https://github.com/norbix-code/sdk-python/releases/tag/v3.9.1
- chore(git:nbx-gh): `nbx-gh` picks the account from the folder it runs in; run from a gateway folder, the Dependabot alerts call fails with HTTP 403 and a misleading "needs the admin:repo_hook scope" hint. Happened once in this task (my loop ran from the wrong folder); running it from the sdk-python folder fixed it — left open, a clearer error would help
    where: /Users/djovaisas/Projects/norbix/scripts/git/nbx-gh

## Rejected / moved out
- decision(sdk-python:deps): raise `python-semantic-release` itself — rejected — 10.7.0 already allows the patched GitPython and requests/urllib3; a bump would change the release tool for no security gain
- decision(sdk-python:deps): change runtime floors (`httpx`, `pydantic`) — rejected — neither depends on a vulnerable package; changing them would only narrow what SDK users can install

## Needs you
(nothing)

## Open questions
(none)
