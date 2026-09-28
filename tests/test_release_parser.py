"""Proof that breaking commits release as minor until the public launch.

Runs the parser that pyproject.toml selects (scripts/release_parser.py) on the
four sample commits of the SDK versioning policy.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
from git import Actor, Commit, Repo
from semantic_release.commit_parser.token import ParsedCommit
from semantic_release.enums import LevelBump

_PARSER_FILE = Path(__file__).resolve().parents[1] / "scripts" / "release_parser.py"
_spec = importlib.util.spec_from_file_location("release_parser", _PARSER_FILE)
assert _spec is not None and _spec.loader is not None
release_parser = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(release_parser)


def _commit(repo: Repo, message: str) -> Commit:
    author = Actor("test", "test@example.com")
    return repo.index.commit(message, author=author, committer=author)


@pytest.mark.parametrize(
    ("message", "expected"),
    [
        ("feat(x)!: y", LevelBump.MINOR),
        ("fix(x): y\n\nBREAKING CHANGE: z", LevelBump.MINOR),
        ("feat(x): y", LevelBump.MINOR),
        ("fix(x): y", LevelBump.PATCH),
    ],
)
def test_breaking_commits_bump_minor(message: str, expected: LevelBump, tmp_path: Path) -> None:
    repo = Repo.init(tmp_path)
    _commit(repo, "chore: initial commit")
    parser = release_parser.MinorUntilLaunchParser()
    parsed = parser.parse(_commit(repo, message))
    results = parsed if isinstance(parsed, list) else [parsed]

    assert len(results) == 1
    assert isinstance(results[0], ParsedCommit)
    assert results[0].bump is expected


def test_pyproject_selects_this_parser() -> None:
    pyproject = (Path(__file__).resolve().parents[1] / "pyproject.toml").read_text()
    assert 'commit_parser = "scripts/release_parser.py:MinorUntilLaunchParser"' in pyproject
