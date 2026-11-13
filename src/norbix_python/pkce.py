"""PKCE (RFC 7636, S256) for social sign-in and link identity.

The app keeps the verifier (memory on a device, the session on a server) and
never puts it in a URL. The start carries only the challenge
(``social_sign_in_url(..., code_challenge=...)``, ``codeChallenge`` on
``start_link_identity``); the exchange and the link finish send the verifier
(``codeVerifier``). A code started with a challenge works only with the
matching verifier: CM-ERRORS-MEMBERSHIP-058 otherwise, and the code is used
up. A challenge that is not S256 is CM-ERRORS-MEMBERSHIP-059.
"""

from __future__ import annotations

import base64
import hashlib
import re
import secrets
from typing import NamedTuple

_VERIFIER = re.compile(r"^[A-Za-z0-9\-._~]{43,128}$")


class PkcePair(NamedTuple):
    code_verifier: str
    code_challenge: str


def create_pkce_pair() -> PkcePair:
    """A fresh verifier (32 bytes from ``secrets``, base64url, 43 chars) and its S256 challenge."""
    verifier = _b64url(secrets.token_bytes(32))
    return PkcePair(verifier, pkce_challenge(verifier))


def pkce_challenge(code_verifier: str) -> str:
    """The S256 challenge of a verifier: base64url (no padding) of SHA-256 over its ASCII bytes."""
    if not _VERIFIER.match(code_verifier):
        raise ValueError("A PKCE code verifier is 43 to 128 characters of A-Z a-z 0-9 - . _ ~.")
    return _b64url(hashlib.sha256(code_verifier.encode("ascii")).digest())


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")
