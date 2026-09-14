# HUB · Files

Access with `norbix.hub.files`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disable_files` | `GET` | `/{version}/files/disable` | `project` |
| `enable_files` | `GET` | `/{version}/files/enable` | `project` |
| `get_folder_files` | `GET` | `/{version}/files/folder` | `project` |
| `get_file` | `GET` | `/{version}/files/item` | `project` |
| `delete_files_trigger` | `DELETE` | `/{version}/files/triggers/{triggerId}` | `project` |
| `disable_files_trigger` | `PATCH` | `/{version}/files/triggers/{triggerId}/disable` | `project` |
| `enable_files_trigger` | `PATCH` | `/{version}/files/triggers/{triggerId}/enable` | `project` |
| `get_files_trigger` | `GET` | `/{version}/files/triggers/{id}` | `project` |
| `get_files_triggers` | `GET` | `/{version}/files/triggers` | `project` |
| `save_files_trigger` | `POST` | `/{version}/files/triggers` | `project` |
| `delete_files_integration` | `DELETE` | `/{version}/files/integrations/{Id}` | `project` |
| `disable_files_integration` | `PUT` | `/{version}/files/integrations/{Id}/disable` | `project` |
| `enable_files_integration` | `PUT` | `/{version}/files/integrations/{Id}/enable` | `project` |
| `get_files_integration` | `GET` | `/{version}/files/integrations/{id}` | `project` |
| `get_files_integrations` | `GET` | `/{version}/files/integrations` | `project` |
| `save_files_integration` | `POST` | `/{version}/files/integrations` | `project` |
| `set_files_integration_as_default` | `PUT` | `/{version}/files/integrations/{Id}/default` | `project` |
| `test_files_integration` | `POST` | `/{version}/files/integrations/test` | `project` |
| `make_file_public` | `POST` | `/{version}/files/item/public` | `project` |
| `make_file_private` | `POST` | `/{version}/files/item/private` | `project` |
| `make_folder_public` | `POST` | `/{version}/files/folder/public` | `project` |
| `make_folder_private` | `POST` | `/{version}/files/folder/private` | `project` |

## What the parts are

* An **integration** is one storage place — an Amazon S3 bucket, an Azure
  container, a folder on the server. A project can have several; one is the
  default.
* `get_folder_files` lists what is under a path. `get_file` reads the details of
  one file.
* `test_files_integration` checks the settings really work before you save them.

Uploading and downloading file bytes is on the public API side — see
[API · Files](../api/files.md).

## Public file links

A file, or a whole folder, can be made readable by anyone holding a link — no
sign-in, no project id, no account. Norbix keeps a record and mints an
unguessable id that looks like `nbpf_7hK2…`; the link is then

```
https://<your api host>/v3/files/public/nbpf_7hK2…/invoice.pdf
```

```python
# one file
result = client.hub.files.make_file_public(
    filesIntegrationId=integration_id,
    path="invoices/invoice.pdf",
)
public_id = result["id"]          # "nbpf_7hK2abc"

# take it back
client.hub.files.make_file_private(
    filesIntegrationId=integration_id,
    path="invoices/invoice.pdf",
)

# a whole folder — one record, however many files are under it
folder = client.hub.files.make_folder_public(
    filesIntegrationId=integration_id,
    path="invoices",
)
# every file under invoices/ is now readable at
# https://<api host>/v3/files/public/<folder["id"]>/<path inside the folder>

client.hub.files.make_folder_private(
    filesIntegrationId=integration_id,
    path="invoices",
)
```

Four rules worth knowing:

* **Publishing a folder is one record**, whatever is under it, at any depth.
* **Asking twice gives the same id back.** The first link is already in
  somebody's hands; a second id would leave it live and invisible.
* **A file cannot be made private on its own while a folder above it is
  public.** The call is refused (`CM-ERRORS-FILES-021`) and the message names
  the folder to switch off.
* **The root cannot be published**, and a folder link with nothing after it is
  a `404` — publishing a prefix must not publish its listing.

After any of these, `get_file` and `list_files` report `isPublic` and
`publicUrl` on the file, and a listing carries `publicFolders`. Opening the
link itself is on the public API side — see
[API · Files](../api/files.md#reading-a-public-link).
