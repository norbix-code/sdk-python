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
