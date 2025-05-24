# 📦 Kikon-tai

**Kikon-tai – The Spirit Mechanism Team**

The name *Kikon-tai* (機魂隊) combines the characters for "machine" (機), "soul" (魂), and "team" (隊). It represents a development system driven by autonomous agents with structured coordination and an animating vision.
Autonomous development infrastructure for AI-led projects.  
Builds and coordinates modular agents to deliver software in partnership with a human client.  
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
- Accept high-level product briefs from a client (currently the creator of MinamiOS).
- Break them down into deliverable roadmaps and tasks.
- Coordinate agent-based development to build working prototypes.
- Iterate based on client feedback.

It is intended as both a usable infrastructure and a demonstration project for job applications. While capable of expressive, emotionally intelligent interaction when enabled, Kikon-tai defaults to a professional tone for external use.


## Usage in Private Projects

Kikon-tai is designed as a modular, public-facing infrastructure layer. To use it in private or sensitive projects (such as MinamiOS), we recommend structuring your implementation as a separate wrapper repository.

A typical layout might include:
```
minamios/
├── framework/           # Kikon-tai as submodule
├── product_data/        # Private requirements, prompts, and plans
├── outputs/             # Generated documents or prototypes
└── README.md            # Project-specific overview
```

This allows you to:
- Keep Kikon-tai clean and open source
- Safely evolve your own product in private
- Reuse and update the framework as it improves