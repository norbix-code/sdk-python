"""Commit parser for python-semantic-release: breaking changes release as minor.

Until the public launch every Norbix SDK keeps its current major version. The
conventional parser always gives a breaking commit (`feat!:` or a
`BREAKING CHANGE:` footer) a MAJOR bump and has no option to change that, so
this parser runs it unchanged and lowers MAJOR to MINOR afterwards. The
breaking description is kept, so release notes still list it.

Selected in pyproject.toml:
    [tool.semantic_release]
    commit_parser = "scripts/release_parser.py:MinorUntilLaunchParser"

Remove it (back to commit_parser = "conventional") at the public launch.
"""

from __future__ import annotations

from git.objects.commit import Commit
from semantic_release.commit_parser.conventional import ConventionalCommitParser
from semantic_release.commit_parser.token import ParsedCommit, ParseResult
from semantic_release.enums import LevelBump


def _lower_major(result: ParseResult) -> ParseResult:
    if isinstance(result, ParsedCommit) and result.bump is LevelBump.MAJOR:
        return result._replace(bump=LevelBump.MINOR)
    return result


class MinorUntilLaunchParser(ConventionalCommitParser):
    def parse(self, commit: Commit) -> ParseResult | list[ParseResult]:
        parsed = super().parse(commit)
        if isinstance(parsed, list):
            return [_lower_major(result) for result in parsed]
        return _lower_major(parsed)
