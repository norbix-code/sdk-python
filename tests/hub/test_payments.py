from __future__ import annotations

from norbix_python import Norbix, NorbixError
from ..helpers import make_client, stub_request_for_path


def test_hub_payments_module_surface() -> None:
    client, _ = make_client()
    module = client.hub.payments
    assert callable(module.disablePayments)
    assert callable(module.enablePayments)
    assert callable(module.deletePaymentsTrigger)
    assert callable(module.disablePaymentsTrigger)
    assert callable(module.enablePaymentsTrigger)
    assert callable(module.getPaymentsTrigger)
    assert callable(module.getPaymentsTriggers)
    assert callable(module.savePaymentsTrigger)
    assert callable(module.confirmPaymentsIntegrationHumanDelivery)
    assert callable(module.deletePaymentsIntegration)
    assert callable(module.disablePaymentsIntegration)
    assert callable(module.enablePaymentsIntegration)
    assert callable(module.getPaymentsIntegration)
    assert callable(module.getPaymentsIntegrations)
    assert callable(module.savePaymentsIntegration)
    assert callable(module.testPaymentsIntegration)


def test_hub_payments_disablePayments_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/disable') if False else {}
    client.hub.payments.disablePayments(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_enablePayments_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/enable') if False else {}
    client.hub.payments.enablePayments(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_deletePaymentsTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/triggers/{triggerId}') if True else {}
    client.hub.payments.deletePaymentsTrigger(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_disablePaymentsTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/triggers/{triggerId}/disable') if True else {}
    client.hub.payments.disablePaymentsTrigger(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_enablePaymentsTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/triggers/{triggerId}/enable') if True else {}
    client.hub.payments.enablePaymentsTrigger(payload)
    assert transport.last_request['method'] == 'PATCH'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_getPaymentsTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/triggers/{id}') if True else {}
    client.hub.payments.getPaymentsTrigger(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_getPaymentsTriggers_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/triggers') if False else {}
    client.hub.payments.getPaymentsTriggers(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_savePaymentsTrigger_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/triggers') if False else {}
    client.hub.payments.savePaymentsTrigger(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_confirmPaymentsIntegrationHumanDelivery_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/integrations/confirm-human-delivery') if False else {}
    client.hub.payments.confirmPaymentsIntegrationHumanDelivery(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_deletePaymentsIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/integrations/{Id}') if True else {}
    client.hub.payments.deletePaymentsIntegration(payload)
    assert transport.last_request['method'] == 'DELETE'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_disablePaymentsIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/integrations/{Id}/disable') if True else {}
    client.hub.payments.disablePaymentsIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_enablePaymentsIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/integrations/{Id}/enable') if True else {}
    client.hub.payments.enablePaymentsIntegration(payload)
    assert transport.last_request['method'] == 'PUT'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_getPaymentsIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/integrations/{id}') if True else {}
    client.hub.payments.getPaymentsIntegration(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_getPaymentsIntegrations_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/integrations') if False else {}
    client.hub.payments.getPaymentsIntegrations(payload)
    assert transport.last_request['method'] == 'GET'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_savePaymentsIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/integrations') if False else {}
    client.hub.payments.savePaymentsIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')

def test_hub_payments_testPaymentsIntegration_request_shape() -> None:
    client, transport = make_client(account_id='acc-1' if False else None)
    payload = stub_request_for_path('/{version}/payments/integrations/test') if False else {}
    client.hub.payments.testPaymentsIntegration(payload)
    assert transport.last_request['method'] == 'POST'
    assert transport.last_request is not None
    assert transport.last_request['url'].startswith('https://')
