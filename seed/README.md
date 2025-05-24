

# 🌱 Kikon-tai Seed Files

This folder contains reusable templates for generating runtime configuration and project scaffolding within Kikon-tai. These files are **not meant to be used directly**, but to serve as **starter structures** for agent generation, onboarding new projects, and maintaining a clean separation between reusable source and runtime state.

---

## 📁 File Overview

### `client_index.yaml`
Defines the active projects Kikon-tai is managing. Used to track project metadata, status, brief location, and output path.  
✅ **Copy to:** `client_portal/client_index.yaml`  
🚫 **Ignored by Git after generation**

---

### `client_brief.md`
A structured prompt for capturing high-level project requirements. Used by `interviewer_agent` and `roadmap_agent` to begin the planning loop.  
✅ **Copy to:** `client_portal/briefs/<project>.md`  
🚫 **Only template is committed; real briefs are user-specific and ignored**

---

### `backlog.yaml`
An empty YAML structure for storing task objects, used by `backlog_agent` and consumed by the Genki Engine loop.  
✅ **Copy to:** `data/backlog.yaml`  
🚫 **Runtime backlog is ignored in Git**

---

### `roadmap.md`
Provides a basic milestone roadmap structure for agent-generated project phases.  
✅ **Copy to:** `data/roadmap.md`  
🚫 **Runtime version is dynamic and ignored**

---

### `sprint_log.md`
A markdown template for daily sprint or iteration logs, used by `sync_agent`.  
✅ **Copy to:** `sprint_log/YYYY-MM-DD.md`  
🚫 **Real sprint logs are generated and not tracked in Git**

---

### `agent_spec.yaml`
Template for defining a new agent's responsibilities, inputs, outputs, and dependencies. Helps standardize behavior across agents.  
✅ **Copy to:** `agents/<agent_name>/spec.yaml`

---

### `project_manifest.yaml`
Captures high-level information about a project, including agents involved, project description, and structure. Optional but useful for larger or multi-phase projects.  
✅ **Copy to:** `project_manifest.yaml` (project root)

---

## 📘 How to Use

1. Copy the relevant seed file into your working directory (e.g., `data/`, `client_portal/briefs/`)
2. Customize as needed for the specific project
3. Let Kikon-tai agents update, consume, or write to these locations
4. Do **not** commit runtime versions unless you are creating a new template

---

## 🧼 Notes

- These files are intended for **human authors and agents alike**
- Runtime versions are ignored via `.gitignore` rules to prevent leaking user-specific or sensitive data
- The seed folder functions like a starter kit for projects initiated by Kikon-tai

---

> Want to add a new template? Add it here and reference it in documentation or agent code for reuse.