"""
roadmap_agent.py

This agent reads the client brief and generates a multi-phase roadmap based on the project scope.
It is designed to be triggered by the Genki Engine when a roadmap needs to be constructed or updated.
"""

from pathlib import Path

CLIENT_BRIEF_PATH = Path("../../client_portal/client_brief.md")
ROADMAP_OUTPUT_PATH = Path("../../data/roadmap.md")

def handle_roadmap_agent(task):
    print(f"→ [roadmap_agent] Generating roadmap from {CLIENT_BRIEF_PATH}")

    try:
        with open(CLIENT_BRIEF_PATH, 'r') as brief_file:
            brief = brief_file.read()
    except FileNotFoundError:
        print(f"⚠️ Client brief not found at: {CLIENT_BRIEF_PATH}")
        return

    # Placeholder: extract features and generate fake roadmap phases
    phases = [
        "Phase 1: Input Handling and Resume Assembly",
        "Phase 2: Cover Letter Generator",
        "Phase 3: Keyword Compliance Reporter",
        "Phase 4: Output Packaging and Review",
        "Phase 5: Application Tracker Integration"
    ]

    roadmap = "# Roadmap for Job Portfolio Agent\n\n"
    roadmap += "Generated from client brief.\n\n"

    for phase in phases:
        roadmap += f"## {phase}\n- [ ] Task 1\n- [ ] Task 2\n\n"

    try:
        with open(ROADMAP_OUTPUT_PATH, 'w') as output_file:
            output_file.write(roadmap)
            print(f"✅ Roadmap written to: {ROADMAP_OUTPUT_PATH}")
    except Exception as e:
        print(f"❌ Failed to write roadmap: {e}")