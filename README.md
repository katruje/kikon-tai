# 📦 Kikon-tai

**Kikon-tai – The Spirit Mechanism Team**

Kikon-tai is a modular, autonomous development framework for AI-led projects. It orchestrates modular agents that work collaboratively to deliver software with a human-in-the-loop approach.

The name *Kikon-tai* (機魂隊) combines the characters for "machine" (機), "soul" (魂), and "team" (隊). It represents a development system driven by autonomous agents with structured coordination and an animating vision.

First mission: build a fully autonomous dev team capable of turning high-level product requirements into a working prototype with minimal client involvement. This project serves as a demonstration of AI-integrated software excellence.

---

## 📁 Project Structure

```
kikon-tai/
│
├── genki_engine/                  # Core task loop and dispatcher
│   └── main_loop.py               # Engine entry point (placeholder)
│
├── agents/                        # Role-based modular agents
│   ├── interviewer_agent/
│   ├── roadmap_agent/
│   ├── backlog_agent/
│   └── sync_agent/
│
├── configs/                       # Agent role configs and global settings
│   ├── role_configs.yaml          # Clean version only (no Misama)
│   ├── tone_guidelines.yaml       # Style guidance for outputs
│   └── schedule.yaml              # Optional future: CRON-style agent triggers
│
├── prompts/                       # Modular prompts per agent
│   └── [agent_name].txt
│
├── data/                          # Generated output from loop execution
│   ├── requirements.yaml
│   ├── roadmap.md
│   ├── backlog.yaml
│   └── sprint_log/
│       └── 2025-05-23.md
│
├── client_portal/                 # Where user inputs, desires, and interview data go
│   └── client_brief.md
│
└── README.md                      # Overview of the Kikon-tai framework
```

---

## 🧭 Vision

Kikon-tai is an autonomous, full-service design and development organization. Its purpose is to:
- Accept high-level product briefs from a human client.
- Break them down into deliverable roadmaps and tasks.
- Coordinate agent-based development to build working prototypes.
- Iterate based on client feedback.

It is intended as both a usable infrastructure and a demonstration project for job applications. While capable of expressive, emotionally intelligent interaction when enabled, Kikon-tai defaults to a professional tone for external use.

---

Kikon-tai is modular, open source, and designed for both internal and public-facing applications. Whether used as a development scaffold or an autonomous design partner, it serves as a blueprint for how AI-led systems can collaborate meaningfully with human creators.

*_Last Updated: May 24, 2025_*