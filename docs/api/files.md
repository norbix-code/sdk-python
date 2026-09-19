# API · Files

Access with `norbix.api.files`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `list_files` | `GET` | `/{version}/files/{filesIntegrationId}` | `project` |
| `get_file_info` | `GET` | `/{version}/files/{filesIntegrationId}/info` | `project` |
| `get_signed_url` | `GET` | `/{version}/files/{filesIntegrationId}/sign` | `project` |
| `request_upload_url` | `POST` | `/{version}/files/{filesIntegrationId}/upload-url` | `project` |
| `commit_upload` | `POST` | `/{version}/files/{filesIntegrationId}/commit` | `project` |
| `download_file_api` | `GET` | `/{version}/files/{filesIntegrationId}/download` | `project` |
| `delete_file_api` | `DELETE` | `/{version}/files/{filesIntegrationId}` | `project` |
| `delete_many_files_api` | `DELETE` | `/{version}/files/{filesIntegrationId}/bulk` | `project` |
| `test_files_integration` | `POST` | `/{version}/files/{filesIntegrationId}/test` | `project` |

`filesIntegrationId` names the storage integration to work with. Get it from
`norbix.hub.files.get_files_integrations()`.

## Uploading a file

Uploading takes two steps, so the file bytes never pass through Norbix:

1. `request_upload_url` returns a short-lived address to upload to.
2. Send the bytes to that address with a plain `PUT`.
3. `commit_upload` tells Norbix the upload finished.

```python
upload = client.api.files.request_upload_url(
    integration_id,
    path="invoices/invoice.pdf",
    contentType="application/pdf",
)
httpx.put(upload["url"], content=pdf_bytes, headers={"Content-Type": "application/pdf"})
client.api.files.commit_upload(
    integration_id,
    path="invoices/invoice.pdf",
    contentType="application/pdf",
    sizeBytes=len(pdf_bytes),
)
```

## Reading a file

`get_signed_url` returns a short-lived address anyone can open, which suits a
browser preview or a download link. `download_file_api` streams the bytes
through Norbix instead.

## Testing an integration

`test_files_integration` checks that a storage integration really works. It
runs a live probe: it uploads a small file, reads it back, lists the folder and
deletes the file again. Because the probe writes to the storage, the API key
needs the `files:create` permission.

```python
result = client.api.files.test_files_integration(integration_id)
for step in result["items"]:
    print(step["operation"], step["result"], step.get("errors"))
# Upload OK None
# Read OK None
# ...
```

Each item has `operation`, `result` (`"OK"` or `"Failed"`) and `errors`.
When the gateway answers with an error status (for example for an unknown
integration id), the call raises a `NorbixError`, like the other methods; the
gateway's `responseStatus` is in the error's `details`.

The dashboard has its own method for the same probe,
[`hub.files.test_files_integration`](../hub/files.md), which takes the id in the
body (`integrationId=...`) instead of the path. This one is for code that uses
an API key.

## Reading a public link

`get_public_file` reads a file somebody made public with
[`hub.files.make_file_public`](../hub/files.md#public-file-links).

**This call carries no sign-in and no project id.** The SDK deliberately sends
no `Authorization` header for it, even when the client you call it on is signed
in. That is what public means: the link has to work in an e-mail, in an
`<img src>`, or in a browser on a stranger's phone, and the unguessable
`nbpf_…` id is the whole credential.

```python
pdf_bytes = client.api.files.get_public_file("nbpf_7hK2abc", "invoice.pdf")

# a file inside a published folder — the path keeps its slashes
report = client.api.files.get_public_file("nbpf_folder1", "2026/q1/report.pdf")
```

It gives back raw `bytes`. When the storage provider signs its own links
(Amazon S3, Azure Blob, Google Cloud Storage) Norbix answers `302` and the call
follows the redirect, so the bytes come straight from the provider.

Every miss is the same plain `404` — an unknown id, a name that does not match,
a file made private again, a file gone from storage. A more precise answer
would tell a stranger that the file is there.

The link is a plain HTTP address, so anything that can do a `GET` can read it —
`httpx`, `curl`, an `<img>` tag. You do not need this SDK, or a Norbix client
at all, to open one; the method is here for code that already has a client.
