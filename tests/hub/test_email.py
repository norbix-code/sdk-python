from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client


def test_hub_email_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.email
    assert callable(module.one_click_unsubscribe)


def test_hub_email_one_click_unsubscribe_request_shape() -> None:
    client, transport = make_client(account_id=None)
    client.hub.email.one_click_unsubscribe({})
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
