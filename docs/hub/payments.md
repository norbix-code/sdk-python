# HUB · Payments

Access with `norbix.hub.payments`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disablePayments` | `GET` | `/{version}/payments/disable` | `project` |
| `enablePayments` | `GET` | `/{version}/payments/enable` | `project` |
| `deletePaymentsTrigger` | `DELETE` | `/{version}/payments/triggers/{triggerId}` | `project` |
| `disablePaymentsTrigger` | `PATCH` | `/{version}/payments/triggers/{triggerId}/disable` | `project` |
| `enablePaymentsTrigger` | `PATCH` | `/{version}/payments/triggers/{triggerId}/enable` | `project` |
| `getPaymentsTrigger` | `GET` | `/{version}/payments/triggers/{id}` | `project` |
| `getPaymentsTriggers` | `GET` | `/{version}/payments/triggers` | `project` |
| `savePaymentsTrigger` | `POST` | `/{version}/payments/triggers` | `project` |
| `confirmPaymentsIntegrationHumanDelivery` | `POST` | `/{version}/payments/integrations/confirm-human-delivery` | `project` |
| `deletePaymentsIntegration` | `DELETE` | `/{version}/payments/integrations/{Id}` | `project` |
| `disablePaymentsIntegration` | `PUT` | `/{version}/payments/integrations/{Id}/disable` | `project` |
| `enablePaymentsIntegration` | `PUT` | `/{version}/payments/integrations/{Id}/enable` | `project` |
| `getPaymentsIntegration` | `GET` | `/{version}/payments/integrations/{id}` | `project` |
| `getPaymentsIntegrations` | `GET` | `/{version}/payments/integrations` | `project` |
| `savePaymentsIntegration` | `POST` | `/{version}/payments/integrations` | `project` |
| `testPaymentsIntegration` | `POST` | `/{version}/payments/integrations/test` | `project` |
