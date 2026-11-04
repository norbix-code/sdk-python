# HUB · Payments

Access with `norbix.hub.payments`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disable_payments` | `PUT` | `/{version}/payments/disable` | `project` |
| `enable_payments` | `PUT` | `/{version}/payments/enable` | `project` |
| `delete_payments_trigger` | `DELETE` | `/{version}/payments/triggers/{triggerId}` | `project` |
| `disable_payments_trigger` | `PATCH` | `/{version}/payments/triggers/{triggerId}/disable` | `project` |
| `enable_payments_trigger` | `PATCH` | `/{version}/payments/triggers/{triggerId}/enable` | `project` |
| `get_payments_trigger` | `GET` | `/{version}/payments/triggers/{id}` | `project` |
| `get_payments_triggers` | `GET` | `/{version}/payments/triggers` | `project` |
| `save_payments_trigger` | `POST` | `/{version}/payments/triggers` | `project` |
| `confirm_payments_integration_human_delivery` | `POST` | `/{version}/payments/integrations/confirm-human-delivery` | `project` |
| `delete_payments_integration` | `DELETE` | `/{version}/payments/integrations/{Id}` | `project` |
| `disable_payments_integration` | `PUT` | `/{version}/payments/integrations/{Id}/disable` | `project` |
| `enable_payments_integration` | `PUT` | `/{version}/payments/integrations/{Id}/enable` | `project` |
| `get_payments_integration` | `GET` | `/{version}/payments/integrations/{id}` | `project` |
| `get_payments_integrations` | `GET` | `/{version}/payments/integrations` | `project` |
| `get_payments_webhook_log` | `GET` | `/{version}/payments/webhooks/log` | `project` |
| `save_payments_integration` | `POST` | `/{version}/payments/integrations` | `project` |
| `test_payments_integration` | `POST` | `/{version}/payments/integrations/test` | `project` |
| `start_payments_integration_connect` | `POST` | `/{version}/payments/integrations/connect/start` | `project` |
| `complete_payments_integration_connect` | `POST` | `/{version}/payments/integrations/connect/{ConnectId}/complete` | `project` |
| `disconnect_payments_integration_connect` | `POST` | `/{version}/payments/integrations/{Id}/connect/disconnect` | `project` |

## Quick connect (one-click OAuth)

A payments integration can be saved without pasting keys: the provider's page
asks the person to approve, sends them back to Norbix, and the integration is
saved from the account they pick. The module-agnostic reads are on
`norbix.hub.integrations` ([integrations](./integrations.md)).

```python
providers = norbix.hub.integrations.get_quick_connect_providers(module="payments")
started = norbix.hub.payments.start_payments_integration_connect(
    provider="woocommerce", integrationName="Shop", input={"storeUrl": "https://shop.example.com"}
)
print(started["authorizeUrl"])  # open it in a browser within 10 minutes
# … the person approves and is sent back to Norbix …
targets = norbix.hub.integrations.get_integration_connect_targets(started["connectId"])
saved = norbix.hub.payments.complete_payments_integration_connect(
    started["connectId"], targetId=targets["targets"][0]["id"], isEnabled=True
)
norbix.hub.payments.disconnect_payments_integration_connect(saved["id"])  # webhooks removed, key forgotten, off
```

`start` also takes `mode` (test / live, when the provider has modes) and
`integrationId` to reconnect an existing integration. The three payments
routes are in the gateway's `[Route]` list but not in the endpoint manifest.
Tests: `tests/hub/test_integrations_connect.py`.
