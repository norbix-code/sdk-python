from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_api_echo_module_surface() -> None:
    client, _ = make_client()
    module = client.api.echo
    assert callable(module.echo)


def test_api_echo_echo_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.api.echo.echo()
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
