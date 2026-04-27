# Norbix Python SDK documentation

- [API reference](./api/_index.md)
- [Hub reference](./hub/_index.md)

## Practical usage snippets

### Service-to-service call

```python
from norbix_python import Norbix

client = Norbix(api_key="sk_live_xxx", project_id="proj_123")
result = client.api.database.find({"collectionName": "orders", "take": 10})
print(result)
```

### User login flow

```python
from norbix_python import Norbix

client = Norbix(project_id="proj_123")
client.login({"userName": "alice@team.io", "password": "secret"})
profile = client.api.membership.getCurrentUser({})
print(profile)
```

### Account-scoped Hub call

```python
from norbix_python import Norbix

client = Norbix(api_key="sk_live_xxx", project_id="proj_123", account_id="acc_456")
schemas = client.hub.database.getDatabaseSchemas({})
print(schemas)
```
