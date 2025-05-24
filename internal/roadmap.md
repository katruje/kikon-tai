# 🗺️ Kikon-tai Development Roadmap

## Overview
This roadmap outlines the phased development of Kikon-tai as a fully autonomous, agent-driven software development framework. The goal is to transform high-level product requirements into working prototypes with minimal client involvement. The roadmap is structured to support incremental delivery, client feedback, and portfolio-grade documentation.

---

## Phase 1: Foundation Setup
- [x] Create clean project structure and repo
- [x] Define sanitized `role_configs.yaml`
- [x] Conduct client intake interview
- [x] Generate `requirements.yaml`
- [x] Draft this `roadmap.md`
- [x] Create `/internal/` for Kikon-tai’s own roadmap and backlog
- [x] Move `requirements.yaml` to internal config space
- [x] Create `/seed/` directory for template-based project scaffolding
- [x] Add `.gitignore` rules for runtime files (backlog, roadmap, briefs, etc.)
- [ ] Establish MVP scope

## Phase 2: Agent Initialization
- [ ] Design interface contracts for each agent role
- [ ] Create agent interface spec at: `/agents/interviewer_agent/interface.yaml`
- [ ] Implement `interviewer_agent`
- [ ] Implement `roadmap_agent`
- [ ] Implement `backlog_agent`
- [ ] Implement `sync_agent`
- [ ] Configure Genki Engine loop to coordinate agent execution
- [ ] Validate data output structure (YAML, Markdown)

## Phase 3: MVP Execution Loop
- [ ] Intake new product brief
- [ ] Convert to requirements
- [ ] Generate a roadmap and backlog
- [ ] Simulate progress with daily sync reports
- [ ] Accept simulated feedback and iterate
- [ ] Validate client experience and control model

## Phase 4: Packaging and Demonstration
- [ ] Polish documentation and add annotated examples
- [ ] Create GitHub-ready repo with README, LICENSE, and usage guide
- [ ] Prepare short portfolio summary or demo video
- [ ] Optional: prepare walkthrough scripts or prompt examples
- [ ] Plan runtime/config separation strategy for packaging (optional)
- [ ] Determine if `/internal/` and `/seed/` should be retained or externalized

---

## Notes
Kikon-tai emphasizes practical, modular AI infrastructure with clearly defined roles and agent boundaries. Future enhancements may include integration with live scheduling, feedback loops via file watching or calendar triggers, and API-based execution environments.

## Version History


### v1.1.0 (In Progress)
- Enabled auto-bootstrapping of backlog if empty
- Injected default roadmap task to initiate project loop
- Updated `roadmap_agent` to write tasks directly into `backlog.yaml`
- Ensures seamless first-run experience without manual task seeding
- Hardened engine execution logic to gracefully handle missing 'title' fields in tasks (fallbacks to 'description' or '[no title]')
- Implemented `builder_agent` for autonomous project scaffolding
- Refined slug generation for semantic agent naming (e.g., `resume_adapter`)
- Implemented `reviewer_agent` for code quality inspection
- Connected `reviewer_agent` to engine via `AGENT_HANDLERS`
- Added backlog task to trigger reviewer agent for scaffolded agents

### v1.0.0 (Tagged)
- Initial MVP structure complete
- Internal roadmap and backlog system established
- Seed templates and `.gitignore` logic finalized
- Supports autonomous project scaffolding via agent loop

## Upcoming File Paths

- Agent Interface Spec (Interviewer): `/agents/interviewer_agent/interface.yaml`