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

## What the parts are

* An **integration** is one storage place — an Amazon S3 bucket, an Azure
  container, a folder on the server. A project can have several; one is the
  default.
* `get_folder_files` lists what is under a path. `get_file` reads the details of
  one file.
* `test_files_integration` checks the settings really work before you save them.

Uploading and downloading file bytes is on the public API side — see
[API · Files](../api/files.md).
