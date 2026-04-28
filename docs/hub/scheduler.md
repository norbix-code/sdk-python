# HUB · Scheduler

Access with `norbix.hub.scheduler`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disable_scheduler` | `GET` | `/{version}/scheduler/disable` | `project` |
| `enable_scheduler` | `GET` | `/{version}/scheduler/enable` | `project` |
| `delete_scheduler_task` | `DELETE` | `/{version}/scheduler/tasks/{Id}` | `project` |
| `disable_scheduler_task` | `PUT` | `/{version}/scheduler/tasks/{Id}/disable` | `project` |
| `enable_scheduler_task` | `PUT` | `/{version}/scheduler/tasks/{Id}/enable` | `project` |
| `get_scheduler_task` | `GET` | `/{version}/scheduler/tasks/{id}` | `project` |
| `get_scheduler_tasks` | `GET` | `/{version}/scheduler/tasks` | `project` |
| `save_scheduler_task` | `POST` | `/{version}/scheduler/tasks` | `project` |
