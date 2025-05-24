---

## 🛠 Proposal: Self-Updating Job Portfolio Agent

### Objective
Develop an autonomous agent system within Kikon-tai that accepts a job description and produces a tailored resume, personalized cover letter, and a keyword compliance report. This system will be the first official deliverable of Kikon-tai, showcasing its ability to handle real-world, high-value outputs for professional use.

### Background
James is currently seeking new employment as a senior-level technical communicator. Traditional job application workflows are time-consuming and inconsistent. The proposed agent system will streamline the process and demonstrate AI-native infrastructure in a practical, portfolio-worthy implementation.

### Scope
**Phase 1 MVP Features:**
- Accept job description input (pasted or uploaded)
- Select relevant resume blocks from a modular YAML resume
- Generate a customized resume (Markdown)
- Generate a matching cover letter (Markdown)
- Run a keyword compliance report (Markdown)

**Phase 2 Enhancements (future):**
- Integrate job feed scraping
- Enable ranking of multiple job descriptions
- Add persona-based tone adaptation (e.g., Minami-style, corporate, assertive)
- Log submissions with an application tracker

### Suggested Directory
```
job_app_agent/
├── inputs/
├── outputs/
├── prompts/
└── main.py
```
### Required Agents
- `resume_adapter_agent`
- `cover_letter_agent`
- `compliance_checker_agent`
- `scraper_agent` (Phase 2)

### Value
- Saves hours of manual tailoring per application
- Demonstrates real-world AI autonomy
- Professional polish for job search and portfolio

### Status
Proposed and client-approved. Ready for Kikon-tai to generate roadmap, backlog, and begin agent task implementation.