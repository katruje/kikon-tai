---

## 🛠 Proposal: Autonomous Career Agent (Codename: Rōdōsha)

### Objective
Develop an autonomous agent system within Kikon-tai that supports the full job-seeking process, including resume tailoring, cover letter generation, job discovery, application tracking, and recruiter communication. This system will serve as the first official deliverable of Kikon-tai, showcasing its ability to manage real-world, high-value outputs with minimal client input.

### Background
James is currently seeking new employment as a senior-level technical communicator. Traditional job application workflows are time-consuming and inconsistent. The proposed agent system will streamline the process and demonstrate AI-native infrastructure in a practical, portfolio-worthy implementation.

### Scope
**Phase 1 MVP Capabilities:**
- Accept job description input (pasted or uploaded)
- Select relevant resume blocks from a modular YAML resume
- Generate a customized resume (Markdown)
- Generate a matching cover letter (Markdown)
- Run a keyword compliance report (Markdown)
- Conduct initial user interview to define search criteria, goals, tone, and values
- Log and organize opportunities in a searchable job tracker
- Optionally draft email or LinkedIn messages to recruiters


**Phase 2 Enhancements (future):**
- Automate job discovery via scraping or API integration
- Evaluate and rank job descriptions by alignment
- Adaptive tone generation based on user persona
- Schedule follow-up reminders and message templates
- Integrate progress and milestone tracking

**Phase 3 Expansion (post-hire):**
- Track promotions, milestones, and performance reviews
- Offer personalized professional development planning
- Maintain skill maps and recommend learning paths
- Coordinate future job changes or internal role shifts
- Integrate with long-term portfolio and achievements system

A future decision will be made whether Phase 3 functionality should exist within the same module or be managed as a separate agent system.

### Suggested Directory (in external repo: `career-agent`)
career-agent/
├── inputs/
├── outputs/
├── agents/
├── prompts/
├── logs/
└── main.py

### Required Agents
- `interview_agent`
- `resume_adapter_agent`
- `cover_letter_agent`
- `compliance_checker_agent`
- `tracker_agent`
- `outreach_agent`
- `scraper_agent` (Phase 2)

### Value
- Saves hours of manual tailoring per application
- Demonstrates real-world AI autonomy
- Professional polish for job search and portfolio

### Status
Proposed and client-approved. Ready for Kikon-tai to generate roadmap, backlog, and begin multi-repo agent scaffolding targeting the `career-agent` module.