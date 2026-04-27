from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = ROOT / "src" / "norbix_python"
TEST_ROOT = ROOT / "tests"
DOCS_ROOT = ROOT / "docs"


@dataclass
class Endpoint:
    class_name: str
    route: str
    method: str
    group: str
    account_scoped: bool


TARGETS = [
    {
        "name": "api",
        "dto_file": ROOT / "references" / "api_dtos.py",
        "namespace_class": "ApiNamespace",
    },
    {
        "name": "hub",
        "dto_file": ROOT / "references" / "hub_dtos.py",
        "namespace_class": "HubNamespace",
    },
]


def main() -> None:
    clean_generated_outputs()
    for target in TARGETS:
        endpoints = parse_dto_file(target["dto_file"])
        emit_modules(target["name"], target["namespace_class"], endpoints)
        emit_tests(target["name"], endpoints)
        emit_docs(target["name"], endpoints)
    emit_docs_index()
    print("Codegen complete.")


def parse_dto_file(path: Path) -> list[Endpoint]:
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    pending_routes: list[tuple[str, str]] = []
    endpoints: list[Endpoint] = []

    for idx, line in enumerate(lines):
        route_match = re.search(r'(?:#|//)\s*@Route\("([^"]+)"(?:,\s*"([^"]+)")?\)', line)
        if route_match:
            route = route_match.group(1)
            methods = route_match.group(2) or "POST"
            method = pick_method([v.strip().upper() for v in methods.split(",") if v.strip()])
            pending_routes.append((route, method))
            continue

        class_match = re.search(r"^\s*(?:export\s+class|class)\s+([A-Za-z0-9_]+)", line)
        if not class_match or not pending_routes:
            continue
        class_name = class_match.group(1)

        header = line
        probe = idx
        while "{" not in header and ":" not in header and probe + 1 < len(lines):
            probe += 1
            header += " " + lines[probe].strip()
        is_account_scoped = (
            "IHasAccountId" in header
            or "IHasAccountId" in line
            or "/account" in route
            or "account" in class_name.lower()
        )

        route, method = pending_routes[0]
        group = derive_group(route)
        endpoints.append(
            Endpoint(
                class_name=class_name,
                route=route,
                method=method,
                group=group,
                account_scoped=is_account_scoped,
            )
        )
        pending_routes = []

    return endpoints


def pick_method(verbs: list[str]) -> str:
    order = ["POST", "PUT", "PATCH", "DELETE", "GET"]
    for verb in order:
        if verb in verbs:
            return verb
    return "POST"


def derive_group(route: str) -> str:
    route = route.lstrip("/")
    segments = route.split("/")
    head = segments[1] if segments and segments[0] == "{version}" and len(segments) > 1 else segments[0]
    head = head or "misc"
    return re.sub(r"[^a-zA-Z0-9]+", "_", head).strip("_").lower() or "misc"


def endpoint_scope(endpoint: Endpoint) -> str:
    if endpoint.route == "/auth" or endpoint.route.startswith("/auth/"):
        return "unauthenticated"
    return "account" if endpoint.account_scoped else "project"


def method_name_from_class(class_name: str, used: set[str]) -> str:
    base = re.sub(r"Request$", "", class_name)
    if not base:
        base = class_name
    method_name = base[0].lower() + base[1:]
    attempt = method_name
    idx = 1
    while attempt in used:
        idx += 1
        attempt = f"{method_name}{idx}"
    used.add(attempt)
    return attempt


def extract_path_tokens(route: str) -> list[str]:
    return [t for t in re.findall(r"\{([^/{}]+)\}", route) if t != "version"]


def clean_generated_outputs() -> None:
    for folder in (SRC_ROOT / "api", SRC_ROOT / "hub"):
        if not folder.exists():
            continue
        for path in folder.glob("*.py"):
            if path.name == "__init__.py":
                continue
            path.unlink(missing_ok=True)

    for folder in (TEST_ROOT / "api", TEST_ROOT / "hub"):
        if not folder.exists():
            continue
        for path in folder.glob("test_*.py"):
            path.unlink(missing_ok=True)

    for folder in (DOCS_ROOT / "api", DOCS_ROOT / "hub"):
        if not folder.exists():
            continue
        for path in folder.glob("*.md"):
            path.unlink(missing_ok=True)


def emit_modules(target: str, namespace_class: str, endpoints: list[Endpoint]) -> None:
    by_group: dict[str, list[Endpoint]] = defaultdict(list)
    for endpoint in endpoints:
        by_group[endpoint.group].append(endpoint)

    target_dir = SRC_ROOT / target
    target_dir.mkdir(parents=True, exist_ok=True)
    used_methods_by_group: dict[str, dict[str, str]] = {}

    for group, group_endpoints in sorted(by_group.items()):
        used: set[str] = set()
        used_methods_by_group[group] = {}
        lines: list[str] = [
            "from __future__ import annotations",
            "",
            "from typing import Any",
            "",
            "from ..transport import Transport",
            "",
            f"class {pascal(group)}Module:",
            "    def __init__(self, transport: Transport) -> None:",
            "        self._transport = transport",
            "",
        ]
        for endpoint in group_endpoints:
            method_name = method_name_from_class(endpoint.class_name, used)
            used_methods_by_group[group][endpoint.class_name] = method_name
            scope = endpoint_scope(endpoint)
            lines.extend(
                [
                    f"    def {method_name}(self, request: dict[str, Any] | None = None, *, timeout: float | None = None, bearer_token: str | None = None) -> Any:",
                    f"        \"\"\"{endpoint.method} {endpoint.route}\"\"\"",
                    "        return self._transport.send(",
                    f"            target='{target}',",
                    f"            path='{endpoint.route}',",
                    f"            method='{endpoint.method}',",
                    "            request=request or {},",
                    f"            scope='{scope}',",
                    "            timeout=timeout,",
                    "            bearer_token=bearer_token,",
                    "        )",
                    "",
                ]
            )
        (target_dir / f"{group}.py").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    import_lines = [f"from .{group} import {pascal(group)}Module" for group in sorted(by_group.keys())]
    init_lines = [
        "from __future__ import annotations",
        "",
        "from ..transport import Transport",
        "",
        *import_lines,
        "",
        "",
        f"class {namespace_class}:",
    ]
    init_lines.extend(["    def __init__(self, transport: Transport) -> None:"])
    for group in sorted(by_group.keys()):
        init_lines.append(f"        self.{group} = {pascal(group)}Module(transport)")
    init_lines.append("")
    (target_dir / "__init__.py").write_text("\n".join(init_lines), encoding="utf-8")


def emit_tests(target: str, endpoints: list[Endpoint]) -> None:
    test_target = TEST_ROOT / target
    test_target.mkdir(parents=True, exist_ok=True)
    by_group: dict[str, list[Endpoint]] = defaultdict(list)
    for endpoint in endpoints:
        by_group[endpoint.group].append(endpoint)

    for group, group_endpoints in sorted(by_group.items()):
        used: set[str] = set()
        blocks: list[str] = [
            "from __future__ import annotations",
            "",
            "from norbix_python import Norbix, NorbixError",
            "from ..helpers import make_client, stub_request_for_path",
            "",
            "",
            f"def test_{target}_{group}_module_surface() -> None:",
            "    client, _ = make_client()",
            f"    module = client.{target}.{group}",
        ]
        for endpoint in group_endpoints:
            method_name = method_name_from_class(endpoint.class_name, used)
            blocks.append(f"    assert callable(module.{method_name})")
        blocks.append("")

        used.clear()
        for endpoint in group_endpoints:
            method_name = method_name_from_class(endpoint.class_name, used)
            route = endpoint.route
            path_tokens = extract_path_tokens(route)
            account_note = "True" if endpoint.account_scoped else "False"
            blocks.extend(
                [
                    "",
                    f"def test_{target}_{group}_{method_name}_request_shape() -> None:",
                    f"    client, transport = make_client(account_id='acc-1' if {account_note} else None)",
                    f"    payload = stub_request_for_path('{route}') if {bool(path_tokens)} else {{}}",
                    f"    client.{target}.{group}.{method_name}(payload)",
                    f"    assert transport.last_request['method'] == '{endpoint.method}'",
                    "    assert transport.last_request is not None",
                    "    assert transport.last_request['url'].startswith('https://')",
                ]
            )
            if endpoint.account_scoped:
                blocks.extend(
                    [
                        "",
                        f"def test_{target}_{group}_{method_name}_requires_account_scope() -> None:",
                        "    client = Norbix(project_id='p1', bearer_token='token')",
                        "    payload = stub_request_for_path('"
                        + route
                        + "') if "
                        + str(bool(path_tokens))
                        + " else {}",
                        "    try:",
                        f"        client.{target}.{group}.{method_name}(payload)",
                        "    except NorbixError as exc:",
                        "        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'",
                        "    else:",
                        "        raise AssertionError('Expected account scope error')",
                    ]
                )
        (test_target / f"test_{group}.py").write_text("\n".join(blocks).rstrip() + "\n", encoding="utf-8")


def emit_docs(target: str, endpoints: list[Endpoint]) -> None:
    docs_target = DOCS_ROOT / target
    docs_target.mkdir(parents=True, exist_ok=True)
    by_group: dict[str, list[Endpoint]] = defaultdict(list)
    for endpoint in endpoints:
        by_group[endpoint.group].append(endpoint)

    index_rows: list[str] = []
    for group, group_endpoints in sorted(by_group.items()):
        used: set[str] = set()
        methods = []
        for endpoint in group_endpoints:
            methods.append((method_name_from_class(endpoint.class_name, used), endpoint))
        lines = [
            f"# {target.upper()} · {pascal(group)}",
            "",
            f"Access with `norbix.{target}.{group}`.",
            "",
            "| Method | Verb | Path | Scope |",
            "| --- | --- | --- | --- |",
        ]
        for method, endpoint in methods:
            scope = "account" if endpoint.account_scoped else "project"
            lines.append(f"| `{method}` | `{endpoint.method}` | `{endpoint.route}` | `{scope}` |")
        (docs_target / f"{group}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        index_rows.append(f"| [`{group}`](./{group}.md) | {len(group_endpoints)} |")

    index_lines = [
        f"# {target.upper()} reference",
        "",
        "| Module | Endpoints |",
        "| --- | ---: |",
        *index_rows,
    ]
    (docs_target / "_index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")


def emit_docs_index() -> None:
    lines = [
        "# Norbix Python SDK documentation",
        "",
        "- [API reference](./api/_index.md)",
        "- [Hub reference](./hub/_index.md)",
    ]
    (DOCS_ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def pascal(value: str) -> str:
    return "".join(part.capitalize() for part in re.split(r"[_-]+", value) if part)


def camel(value: str) -> str:
    p = pascal(value)
    return p[:1].lower() + p[1:] if p else value


if __name__ == "__main__":
    main()
