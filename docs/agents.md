# Agent Directory

Kikon-tai relies on a set of specialized agents, each responsible for a unique phase of the build lifecycle. All agents implement a `handle()` method defined in a matching `interface.yaml`.

| Agent               | Responsibility                               | Interface Path                         |
|---------------------|----------------------------------------------|----------------------------------------|
| roadmap_agent       | Reads briefs, generates roadmap + backlog    | `agents/roadmap_agent/interface.yaml`  |
| backlog_agent       | Handles and prioritizes backlog tickets      | `agents/backlog_agent/interface.yaml`  |
| sync_agent          | Maintains logs and cross-file sync           | `agents/sync_agent/interface.yaml`     |
| builder_agent       | Generates project files from tasks           | `agents/builder_agent/interface.yaml`  |
| reviewer_agent      | Reviews and documents project output         | `agents/reviewer_agent/interface.yaml` |
| pr_agent            | Automates PR creation and Git integration    | `agents/pr_agent/interface.yaml`       |
| project_manager     | Handles coordination logic across agents     | `agents/project_manager_agent/interface.yaml` |

All agents are dispatched by `main_loop.py` and invoked according to task assignment.