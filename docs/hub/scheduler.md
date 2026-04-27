# HUB · Scheduler

Access with `norbix.hub.scheduler`.

| Method | Verb | Path | Scope |
| --- | --- | --- | --- |
| `disableScheduler` | `GET` | `/{version}/scheduler/disable` | `project` |
| `enableScheduler` | `GET` | `/{version}/scheduler/enable` | `project` |
| `deleteSchedulerTask` | `DELETE` | `/{version}/scheduler/tasks/{Id}` | `project` |
| `disableSchedulerTask` | `PUT` | `/{version}/scheduler/tasks/{Id}/disable` | `project` |
| `enableSchedulerTask` | `PUT` | `/{version}/scheduler/tasks/{Id}/enable` | `project` |
| `getSchedulerTask` | `GET` | `/{version}/scheduler/tasks/{id}` | `project` |
| `getSchedulerTasks` | `GET` | `/{version}/scheduler/tasks` | `project` |
| `saveSchedulerTask` | `POST` | `/{version}/scheduler/tasks` | `project` |
