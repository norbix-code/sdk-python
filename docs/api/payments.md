# API · Payments

Access with `norbix.api.payments`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `create_payment_order` | `POST` | `/{version}/payments/orders` | `project` |
| `get_payment_order` | `GET` | `/{version}/payments/orders/{Id}` | `project` |
| `get_payment_orders` | `GET` | `/{version}/payments/orders` | `project` |
| `start_payment_checkout` | `POST` | `/{version}/payments/orders/{Id}/checkout` | `project` |

A payment order is what a buyer pays for: lines priced in minor units (cents),
a merchant reference and a price version. The order total is the sum of the
lines; Norbix computes it.

## Taking a payment

1. `create_payment_order` stores the order and gives back its id (`ord_…`).
   Send an `idempotencyKey` (8 characters or more): the same body with the
   same key gives back the same id, so a retry never makes a second order.
2. `start_payment_checkout` starts the provider checkout (Montonio, …) with a
   payments integration of the project. Send the buyer to
   `checkout["paymentUrl"]`. While a checkout is open, the call hands it back
   with `reused` = `True`.
3. When the provider confirms the payment, the order becomes `Paid` and a
   webhook destination or a Code function hears `payments.order.paid` (see
   [webhooks-receiver.md](../webhooks-receiver.md) and
   `FunctionEvent.as_payment_order()`).

```python
created = client.api.payments.create_payment_order(
    buyerUserId=user_id,
    merchantReference="ad-1042-promo-1",
    idempotencyKey="ad-1042-promo-1",
    currency="EUR",
    priceVersion="2026-10-01",
    lines=[{"sku": "star-day", "title": "Star × day", "quantity": 21, "unitAmountMinor": 30}],
    metadata={"adId": "ad_1042"},
)
started = client.api.payments.start_payment_checkout(
    created["id"],
    integrationId=montonio_integration_id,
    returnUrl="https://shop.example.com/orders/return",
)
redirect_to = started["checkout"]["paymentUrl"]

order = client.api.payments.get_payment_order(created["id"])["item"]
paid = client.api.payments.get_payment_orders(buyerUserId=user_id, status="Paid")["list"]["items"]
```
