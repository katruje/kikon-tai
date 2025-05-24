# 🗺️ Kikon-tai Development Roadmap

## Overview
This roadmap outlines the phased development of Kikon-tai as a fully autonomous, agent-driven software development framework. The goal is to transform high-level product requirements into working prototypes with minimal client involvement. The roadmap is structured to support incremental delivery, client feedback, and portfolio-grade documentation.

---

## Phase 1: Foundation Setup
- [x] Create clean project structure and repo
- [x] Define sanitized `role_configs.yaml`
- [x] Conduct client intake interview
- [x] Generate `requirements.yaml`
- [ ] Draft this `roadmap.md`
- [ ] Define tone flexibility strategy (completed)
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

---

## Notes
Kikon-tai emphasizes practical, modular AI infrastructure with clearly defined roles and agent boundaries. Future enhancements may include integration with live scheduling, feedback loops via file watching or calendar triggers, and API-based execution environments.

## Upcoming File Paths

- Agent Interface Spec (Interviewer): `/agents/interviewer_agent/interface.yaml`