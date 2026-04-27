from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_hub_echo_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.echo
    assert callable(module.echo)


def test_hub_echo_echo_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/echo') if False else {}
    client.hub.echo.echo(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
