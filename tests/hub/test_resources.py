from __future__ import annotations

from ..helpers import make_client


def test_hub_resources_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.resources
    assert callable(module.resolve_resources)


def test_hub_resources_resolve_resources_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.resources.resolve_resources()
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
