"""A project's own API host.

Norbix serves every project on ``pr-<32 hex>.api.norbix.ai``. The label is the
project id (``pr_`` + base62) written as the hex of the same GUID, so it is
built here with no call. The gateway's side of this is ``ProjectId.HostLabel``.
"""

from __future__ import annotations

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


def compose_project_url(project_id: object, default_url: str) -> str | None:
    """The project's own base URL under a default one.

    ``https://api.norbix.ai`` + ``pr_5Xvm…`` → ``https://pr-022c….api.norbix.ai``.
    ``None`` when the id is not a Norbix project id.
    """
    label = project_host_label(project_id)
    if label is None:
        return None
    scheme, _, host = default_url.partition("://")
    return f"{scheme}://{label}.{host}"
