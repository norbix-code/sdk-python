"""A project's own API host.

Norbix serves every project on ``pr-<32 hex>.api.norbix.ai`` (an install on
its own domain on ``pr-<32 hex>.api.<domain>``). The label is the project id
(``pr_`` + base62) written as the hex of the same GUID, so it is built here
with no call. The gateway's side of this is ``ProjectId.HostLabel``.
"""

from __future__ import annotations

import re
from typing import NamedTuple
from urllib.parse import urlsplit

_BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_DIGITS = {ch: index for index, ch in enumerate(_BASE62)}
_PROJECT_ID_PREFIX = "pr_"
_MAX_GUID = 1 << 128
# .NET "N" format: the first three groups are stored little-endian.
_HEX_ORDER = (3, 2, 1, 0, 5, 4, 7, 6, 8, 9, 10, 11, 12, 13, 14, 15)


def project_host_label(project_id: object) -> str | None:
    """The DNS label of a project.

    ``pr_5XvmrTA6JVggZdmEE5bGdm`` → ``pr-022c4aca9f9e4df787ab0a20c83c44b6``.
    Returns ``None`` for anything that is not a Norbix project id (a test id,
    another prefix, a value that is not a version-4 GUID) — it never raises.
    """
    if not isinstance(project_id, str) or not project_id.startswith(_PROJECT_ID_PREFIX):
        return None
    digits = project_id[len(_PROJECT_ID_PREFIX) :]
    # 62^22 is just above 2^128: a GUID never needs more than 22 digits.
    if not 1 <= len(digits) <= 22:
        return None

    value = 0
    for ch in digits:
        digit = _DIGITS.get(ch)
        if digit is None:
            return None
        value = value * 62 + digit
    if value >= _MAX_GUID:
        return None

    # The number is the GUID's bytes, least significant first (.NET `Guid.ToByteArray()`).
    b = value.to_bytes(16, "little")

    # Only a version-4 GUID is a Norbix id (the gateway refuses the rest).
    if b[7] >> 4 != 4 or b[8] >> 6 != 2:
        return None

    return "pr-" + "".join(f"{b[i]:02x}" for i in _HEX_ORDER)


PROJECT_HOST_LABEL_PLACEHOLDER = "{projectHostLabel}"
"""The placeholder an install's address template carries (``/echo`` → ``apiUrlTemplate``)."""

_NORBIX_API_DOMAIN = "api.norbix.ai"
_PROJECT_LABEL = re.compile(r"pr-[0-9a-f]{32}", re.IGNORECASE)


class ProjectApiBaseUrl(NamedTuple):
    """Where a project's API calls go (``project``); the address without a label (``shared``)."""

    project: str
    shared: str


def project_api_base_url(base_url: str, project_id: object) -> ProjectApiBaseUrl:
    """Where a project's API calls go, from the API base URL the client has.

    devops docs/tasks/clients-project-host.md, round 2:

    - a template with ``{projectHostLabel}`` (an install on its own domain that
      serves project hosts) is filled with the project's label;
    - an address that is already a project's host (``https://pr-<hex>.…``) gets
      the current project's label, so host and ``norbix-project-id`` always
      name the same project;
    - a norbix.ai API address — ``https://api.norbix.ai`` or
      ``https://<region>.api.norbix.ai``, built in or written out — becomes the
      project's own host ``https://pr-<hex>.api.norbix.ai`` (its DNS record
      follows the project's region);
    - any other address is used as given.

    ``shared`` is the same address without a project label (the social sign-in
    link is built on it). With a project id that is not a Norbix id,
    ``project`` is ``shared``. Scheme, port and path are kept; no trailing
    slash is added. Never raises.
    """
    label = project_host_label(project_id)

    if PROJECT_HOST_LABEL_PLACEHOLDER in base_url:
        shared = base_url.replace(f"{PROJECT_HOST_LABEL_PLACEHOLDER}.", "")
        project = base_url.replace(PROJECT_HOST_LABEL_PLACEHOLDER, label) if label else shared
        return ProjectApiBaseUrl(project, shared)

    try:
        parts = urlsplit(base_url)
        hostname = parts.hostname
    except ValueError:
        return ProjectApiBaseUrl(base_url, base_url)
    if not hostname:
        return ProjectApiBaseUrl(base_url, base_url)
    labels = hostname.lower().split(".")

    if len(labels) > 1 and _PROJECT_LABEL.fullmatch(labels[0]):
        shared = _with_host(base_url, ".".join(labels[1:]))
        project = _with_host(base_url, ".".join([label, *labels[1:]])) if label else shared
        return ProjectApiBaseUrl(project, shared)

    host = ".".join(labels)
    is_norbix_api = host == _NORBIX_API_DOMAIN or (
        len(labels) == 4 and host.endswith(f".{_NORBIX_API_DOMAIN}")
    )
    if is_norbix_api and parts.scheme.lower() == "https":
        project = _with_host(base_url, f"{label}.{_NORBIX_API_DOMAIN}") if label else base_url
        return ProjectApiBaseUrl(project, base_url)

    return ProjectApiBaseUrl(base_url, base_url)


def _with_host(base_url: str, hostname: str) -> str:
    """``base_url`` with another host name; scheme, user info, port, path and query are kept."""
    scheme, sep, rest = base_url.partition("://")
    authority_end = len(rest)
    for ch in "/?#":
        index = rest.find(ch)
        if index != -1:
            authority_end = min(authority_end, index)
    authority, tail = rest[:authority_end], rest[authority_end:]
    userinfo, at, host_port = authority.rpartition("@")
    _, colon, port = host_port.partition(":")
    return f"{scheme}{sep}{userinfo}{at}{hostname}{colon}{port}{tail}"
