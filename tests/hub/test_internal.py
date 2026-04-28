from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_internal_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.internal
    assert callable(module.internals_type_gen)


def test_hub_internal_internals_type_gen_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.internal.internals_type_gen({})
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
