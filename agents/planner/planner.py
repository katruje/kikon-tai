"""
planner.py

This agent reads the client brief and generates a multi-phase roadmap based on the project scope.
It is designed to be triggered by the Genki Engine when a roadmap needs to be constructed or updated.
"""

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
CLIENT_BRIEF_PATH = ROOT_DIR / "client_portal" / "client_brief.md"
ROADMAP_OUTPUT_PATH = ROOT_DIR / "data" / "roadmap.md"

def handle_planner(task):
    print(f"→ [planner] Generating roadmap from {CLIENT_BRIEF_PATH}")

    try:
        with open(CLIENT_BRIEF_PATH, 'r') as brief_file:
            brief = brief_file.read()
        print(f"📄 Brief loaded, {len(brief.splitlines())} lines read.")
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
    print(f"🧩 Roadmap phases generated: {len(phases)} phases.")

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

    # Append tasks to the backlog
    from ruamel.yaml import YAML
    yaml = YAML()
    BACKLOG_PATH = ROOT_DIR / "data" / "backlog.yaml"

    try:
        if BACKLOG_PATH.exists():
            with open(BACKLOG_PATH, 'r') as file:
                backlog_data = yaml.load(file) or {}
        else:
            backlog_data = {}

        tasks = backlog_data.get('tasks', [])
        next_id = 1
        if tasks:
            last_id = max(int(t['id'][1:]) for t in tasks if t['id'].startswith('T') and t['id'][1:].isdigit())
            next_id = last_id + 1

        print(f"📝 Preparing to update backlog with {len(phases)} new tasks...")

        for phase in phases:
            task_id = f"T{next_id:03}"
            task = {
                'id': task_id,
                'description': f"Implement phase: {phase}",
                'assigned_to': 'project_agent',
                'status': 'pending',
                'priority': 'medium',
                'source': 'planner'
            }
            tasks.append(task)
            next_id += 1

        backlog_data['tasks'] = tasks

        with open(BACKLOG_PATH, 'w') as file:
            yaml.dump(backlog_data, file)

        print(f"✅ Backlog updated with {len(phases)} new tasks.")
        print(f"📁 Backlog now contains {len(backlog_data['tasks'])} total tasks.")

    except Exception as e:
        print(f"❌ Failed to update backlog: {e}")

print("✅ planner module loaded")