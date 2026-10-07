from __future__ import annotations

import pytest

from norbix_python.client import DEFAULT_VERSION, _build_config

"""API and Hub default to v3, the gateway's current version. NORBIX_API_VERSION
/ NORBIX_HUB_VERSION and the constructor arguments still override it."""


def _build(**overrides: str) -> object:
    args: dict[str, object] = dict(
        project_id="proj_1", api_key="k", bearer_token=None, account_id=None, env=None,
        region=None, base_url_api=None, base_url_hub=None, api_version=None,
        hub_version=None, timeout=None, default_headers=None, client_name="Norbix",
    )
    args.update(overrides)
    return _build_config(**args)  # type: ignore[arg-type]


def test_default_version_is_v3(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("NORBIX_API_VERSION", raising=False)
    monkeypatch.delenv("NORBIX_HUB_VERSION", raising=False)
    cfg = _build()
    assert DEFAULT_VERSION == "v3"
    assert (cfg.api_version, cfg.hub_version) == ("v3", "v3")  # type: ignore[attr-defined]


def test_env_and_arguments_still_override(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("NORBIX_API_VERSION", "v2")
    cfg = _build(hub_version="v4")
    assert (cfg.api_version, cfg.hub_version) == ("v2", "v4")  # type: ignore[attr-defined]
