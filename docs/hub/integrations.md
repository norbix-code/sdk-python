# HUB · Integrations

Access with `norbix.hub.integrations`. Helpers shared by the integrations of
every module: keyless cloud setup and quick connect.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `get_keyless_integration_setup` | `GET` | `/{version}/integrations/keyless/setup` | `project` |
| `get_quick_connect_providers` | `GET` | `/{version}/integrations/connect/providers` | `project` |
| `get_integration_connect_targets` | `GET` | `/{version}/integrations/connect/{ConnectId}/targets` | `project` |

## Keyless cloud connections

The AWS (S3, SES, Lambda) and Azure (Blob, Communication Services, Functions)
save requests take `authMode`: `"Keyless"` (the gateway default when left out)
or `"AccessKey"`. Keyless stores no secret. Ask for the setup first, run the
script it returns in the cloud account, then save with the same integration id
and the role ARN (AWS) or tenant + client id (Azure). A key mode needs
`acceptKeyRisk: True`, or the save is refused (`CM-ERRORS-INTEGRATIONS-034`).

```python
setup = norbix.hub.integrations.get_keyless_integration_setup(module="files", cloud="aws")
if not setup["available"]:
    raise RuntimeError(setup["unavailableReason"])
print(setup["subject"], setup["audience"])
print(setup["script"])  # run this in the AWS account

norbix.hub.files.save_files_integration(
    id=setup["integrationId"],
    integration={
        "provider": "AwsS3",
        "integrationName": "Invoices bucket",
        "bucketName": "my-invoices",
        "region": "eu-central-1",
        "authMode": "Keyless",
        "roleArn": "arn:aws:iam::123456789012:role/norbix-files",
    },
)
```

The answer carries `integrationId`, `env`, `module`, `cloud`, `issuer`,
`subject`, `audience`, `available`, `unavailableReason` (when `available` is
false), `script` and `templates` — templates: ready CloudFormation / Bicep /
Terraform files for this integration (`[{"kind", "fileName", "content"}]`,
`kind` = `cloudformation` | `bicep` | `terraform`). Pass `integrationId` to get the setup of an integration
that already exists.

Keyless setup is served for every module the gateway serves it for: `files`,
`email` and `code` on `aws`, `azure`, `google`; `logs` on `aws`, `azure`; `push`
and `payments` on `google`; `database` on `atlas` (MongoDB Atlas M10+). The
gateway answers `available: False` with the reason for a pair it does not serve.

## Quick connect (one-click OAuth)

`get_quick_connect_providers(module="payments")` lists which providers can
quick-connect on this install — available or not, the `requiredInputs` to ask
for before the provider's page opens (e.g. `storeUrl`), the `modes` (test /
live) and the `redirectUrl` Norbix registered. Once a person approved on the
provider's page, `get_integration_connect_targets(connect_id)` lists the
accounts (`targets`: `id`, `name`, `detail`) the connect may finish with. The
start / complete / disconnect calls are on the module:
[payments](./payments.md#quick-connect-one-click-oauth).
