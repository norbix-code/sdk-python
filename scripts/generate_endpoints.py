from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

# Package root: sdks/norbix-python (parent of scripts/)
ROOT = Path(__file__).resolve().parent.parent
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
        "async_namespace_class": "AsyncApiNamespace",
    },
    {
        "name": "hub",
        "dto_file": ROOT / "references" / "hub_dtos.py",
        "namespace_class": "HubNamespace",
        "async_namespace_class": "AsyncHubNamespace",
    },
]


def main() -> None:
    clean_generated_outputs()
    for target in TARGETS:
        endpoints = parse_dto_file(target["dto_file"])
        emit_modules(
            target["name"],
            target["namespace_class"],
            target["async_namespace_class"],
            endpoints,
        )
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
        route, method = pending_routes[0]
        is_account_scoped = (
            "IHasAccountId" in header
            or "IHasAccountId" in line
            or "/account" in route
            or "account" in class_name.lower()
        )

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
    if segments and segments[0] == "{version}" and len(segments) > 1:
        head = segments[1]
    else:
        head = segments[0]
    head = head or "misc"
    return re.sub(r"[^a-zA-Z0-9]+", "_", head).strip("_").lower() or "misc"


def endpoint_scope(endpoint: Endpoint) -> str:
    if endpoint.route == "/auth" or endpoint.route.startswith("/auth/"):
        return "unauthenticated"
    return "account" if endpoint.account_scoped else "project"


def camel_to_snake(name: str) -> str:
    name = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.replace("__", "_").lower()


def method_name_from_class(class_name: str, used: set[str]) -> str:
    base = re.sub(r"Request$", "", class_name)
    if not base:
        base = class_name
    camel = base[0].lower() + base[1:] if base else ""
    method_name = camel_to_snake(camel) if camel else camel_to_snake(class_name)
    attempt = method_name
    idx = 1
    while attempt in used:
        idx += 1
        attempt = f"{method_name}_{idx}"
    used.add(attempt)
    return attempt


def extract_path_tokens(route: str) -> list[str]:
    return [t for t in re.findall(r"\{([^/{}]+)\}", route) if t != "version"]


def python_params_for_path_tokens(
    tokens: list[str],
) -> tuple[list[tuple[str, str]], dict[str, str]]:
    """Returns [(wire_token, python_param_name), ...] and mapping wire -> python."""
    seen_python: set[str] = set()
    pairs: list[tuple[str, str]] = []
    wire_to_python: dict[str, str] = {}
    for tok in tokens:
        py = camel_to_snake(tok)
        if py == "id":
            py_name = "id"
        elif py in {"type", "def", "class", "none", "true", "false"}:
            py_name = f"{py}_"
        else:
            py_name = py
        original = py_name
        n = 2
        while py_name in seen_python:
            py_name = f"{original}_{n}"
            n += 1
        seen_python.add(py_name)
        pairs.append((tok, py_name))
        wire_to_python[tok] = py_name
    return pairs, wire_to_python


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


def emit_method_body(
    *,
    indent: str,
    target: str,
    endpoint: Endpoint,
    scope: str,
    path_args: list[tuple[str, str]],
    async_: bool,
) -> list[str]:
    """path_args: (wire_token, python_name)."""
    if path_args:
        pp_parts = [f'"{w}": {py}' for w, py in path_args]
        path_params_expr = "{" + ", ".join(pp_parts) + "}"
    else:
        path_params_expr = "{}"

    req_expr = "request or {}"
    prefix = "return await " if async_ else "return "
    return [
        f"{indent}{prefix}self._transport.send(",
        f'{indent}    target="{target}",',
        f'{indent}    path="{endpoint.route}",',
        f'{indent}    method="{endpoint.method}",',
        f"{indent}    path_params={path_params_expr},",
        f"{indent}    request={req_expr},",
        f'{indent}    scope="{scope}",',
        f"{indent}    timeout=timeout,",
        f"{indent}    bearer_token=bearer_token,",
        f"{indent})",
    ]


def emit_modules(
    target: str,
    namespace_class: str,
    async_namespace_class: str,
    endpoints: list[Endpoint],
) -> None:
    by_group: dict[str, list[Endpoint]] = defaultdict(list)
    for endpoint in endpoints:
        by_group[endpoint.group].append(endpoint)

    target_dir = SRC_ROOT / target
    target_dir.mkdir(parents=True, exist_ok=True)

    for group, group_endpoints in sorted(by_group.items()):
        used: set[str] = set()
        lines: list[str] = [
            "from __future__ import annotations",
            "",
            "from typing import Any",
            "",
            "from ..transport import AsyncTransport, Transport",
            "",
            f"class {pascal(group)}Module:",
            "    def __init__(self, transport: Transport) -> None:",
            "        self._transport = transport",
            "",
        ]

        for endpoint in group_endpoints:
            method_name = method_name_from_class(endpoint.class_name, used)
            scope = endpoint_scope(endpoint)
            tokens = extract_path_tokens(endpoint.route)
            param_pairs, _ = python_params_for_path_tokens(tokens)

            if param_pairs:
                args_list = [f"{py}: str" for _, py in param_pairs]
                sig = (
                    f"    def {method_name}(self, {', '.join(args_list)}, "
                    f"*, request: dict[str, Any] | None = None, timeout: float | None = None, "
                    f"bearer_token: str | None = None) -> Any:"
                )
            else:
                sig = (
                    f"    def {method_name}(self, request: dict[str, Any] | None = None, *, "
                    f"timeout: float | None = None, bearer_token: str | None = None) -> Any:"
                )

            lines.append(sig)
            lines.append(f'        """{endpoint.method} {endpoint.route}"""')
            lines.extend(
                emit_method_body(
                    indent="        ",
                    target=target,
                    endpoint=endpoint,
                    scope=scope,
                    path_args=param_pairs,
                    async_=False,
                )
            )
            lines.append("")

        lines.extend(
            [
                "",
                f"class Async{pascal(group)}Module:",
                "    def __init__(self, transport: AsyncTransport) -> None:",
                "        self._transport = transport",
                "",
            ]
        )

        used_async: set[str] = set()
        for endpoint in group_endpoints:
            method_name = method_name_from_class(endpoint.class_name, used_async)
            scope = endpoint_scope(endpoint)
            tokens = extract_path_tokens(endpoint.route)
            param_pairs, _ = python_params_for_path_tokens(tokens)

            if param_pairs:
                args_list = [f"{py}: str" for _, py in param_pairs]
                sig = (
                    f"    async def {method_name}(self, {', '.join(args_list)}, "
                    f"*, request: dict[str, Any] | None = None, timeout: float | None = None, "
                    f"bearer_token: str | None = None) -> Any:"
                )
            else:
                sig = (
                    f"    async def {method_name}(self, request: dict[str, Any] | None = None, *, "
                    f"timeout: float | None = None, bearer_token: str | None = None) -> Any:"
                )

            lines.append(sig)
            lines.append(f'        """{endpoint.method} {endpoint.route}"""')
            lines.extend(
                emit_method_body(
                    indent="        ",
                    target=target,
                    endpoint=endpoint,
                    scope=scope,
                    path_args=param_pairs,
                    async_=True,
                )
            )
            lines.append("")

        (target_dir / f"{group}.py").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    import_lines = []
    for group in sorted(by_group.keys()):
        pg = pascal(group)
        import_lines.append(f"from .{group} import Async{pg}Module, {pg}Module")
    init_lines = [
        "from __future__ import annotations",
        "",
        "from ..transport import AsyncTransport, Transport",
        "",
        *import_lines,
        "",
        "",
        f"class {namespace_class}:",
        "    def __init__(self, transport: Transport) -> None:",
    ]
    for group in sorted(by_group.keys()):
        init_lines.append(f"        self.{group} = {pascal(group)}Module(transport)")
    init_lines.extend(
        [
            "",
            "",
            f"class {async_namespace_class}:",
            "    def __init__(self, transport: AsyncTransport) -> None:",
        ]
    )
    for group in sorted(by_group.keys()):
        init_lines.append(f"        self.{group} = Async{pascal(group)}Module(transport)")
    init_lines.append("")
    (target_dir / "__init__.py").write_text("\n".join(init_lines), encoding="utf-8")


def _emit_single_group_tests(
    test_target: Path,
    target: str,
    group: str,
    group_endpoints: list[Endpoint],
) -> None:
    blocks: list[str] = [
        "from __future__ import annotations",
        "",
        "from norbix_python import Norbix, NorbixError",
        "from ..helpers import make_client",
        "",
        "",
        f"def test_{target}_{group}_module_surface() -> None:",
        "    client, _ = make_client()",
        f"    module = client.{target}.{group}",
    ]
    used_surf: set[str] = set()
    for endpoint in group_endpoints:
        method_name = method_name_from_class(endpoint.class_name, used_surf)
        blocks.append(f"    assert callable(module.{method_name})")
    blocks.append("")

    used: set[str] = set()
    for endpoint in group_endpoints:
        method_name = method_name_from_class(endpoint.class_name, used)
        route = endpoint.route
        path_tokens = extract_path_tokens(route)
        account_scoped = endpoint.account_scoped

        if path_tokens:
            pt = python_params_for_path_tokens(path_tokens)[0]
            call_inner = ", ".join(f'{py}="stub-{wire}"' for wire, py in pt)
            call_line = f"    client.{target}.{group}.{method_name}({call_inner})"
        else:
            call_line = f"    client.{target}.{group}.{method_name}({{}})"

        acct_arg = "account_id='acc-1'" if account_scoped else "account_id=None"
        blocks.extend(
            [
                "",
                f"def test_{target}_{group}_{method_name}_request_shape() -> None:",
                f"    client, transport = make_client({acct_arg})",
                call_line,
                f"    assert transport.last_request['method'] == '{endpoint.method}'",
                "    assert transport.last_request is not None",
                "    assert transport.last_request['url'].startswith('https://')",
            ]
        )

        if account_scoped:
            if path_tokens:
                pt = python_params_for_path_tokens(path_tokens)[0]
                inner = ", ".join(f'{py}="stub"' for _, py in pt)
                inner_call = f"client.{target}.{group}.{method_name}({inner})"
            else:
                inner_call = f"client.{target}.{group}.{method_name}({{}})"

            blocks.extend(
                [
                    "",
                    f"def test_{target}_{group}_{method_name}_requires_account_scope() -> None:",
                    "    client = Norbix(project_id='p1', bearer_token='token')",
                    "    try:",
                    f"        {inner_call}",
                    "    except NorbixError as exc:",
                    "        assert exc.code == 'NORBIX_ACCOUNT_SCOPE_REQUIRED'",
                    "    else:",
                    "        raise AssertionError('Expected account scope error')",
                ]
            )

    out_path = test_target / f"test_{group}.py"
    out_path.write_text("\n".join(blocks).rstrip() + "\n", encoding="utf-8")


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


def emit_tests(target: str, endpoints: list[Endpoint]) -> None:
    test_target = TEST_ROOT / target
    test_target.mkdir(parents=True, exist_ok=True)
    by_group: dict[str, list[Endpoint]] = defaultdict(list)
    for endpoint in endpoints:
        by_group[endpoint.group].append(endpoint)

    for group, group_endpoints in sorted(by_group.items()):
        _emit_single_group_tests(test_target, target, group, group_endpoints)


if __name__ == "__main__":
    main()
