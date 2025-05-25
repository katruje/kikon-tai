"""
backlog.py

This agent reads the roadmap and converts it into a structured YAML backlog.
It is designed to be triggered by the Genki Engine as part of Phase 2.
"""

import yaml
from utils.pathing import ROADMAP_PATH, BACKLOG_PATH

def handle_backlog(task):
    print(f"→ [backlog] Reading roadmap from {ROADMAP_PATH}")

    try:
        with open(ROADMAP_PATH, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"⚠️ Roadmap file not found at: {ROADMAP_PATH}")
        return

    try:
        with open(BACKLOG_PATH, 'r') as file:
            existing_data = yaml.safe_load(file) or {}
            existing_backlog = existing_data.get("backlog", [])
    except FileNotFoundError:
        existing_backlog = []

    import re
    new_backlog = []
    phase = None
    # Extract the max T### ID from existing backlog
    t_ids = [
        int(re.sub(r"^T", "", t["id"]))
        for t in existing_backlog
        if isinstance(t["id"], str) and t["id"].startswith("T") and re.match(r"T\d+", t["id"])
    ]
    task_counter = max(t_ids) + 1 if t_ids else 100

    for line in lines:
        if line.startswith("## Phase"):
            phase = line.strip().replace("## ", "")
        elif line.strip().startswith("- [ ]"):
            task_title = line.strip()[6:].strip()
            task = {
                "id": f"T{task_counter}",
                "title": task_title,
                "phase": phase,
                "assigned_to": "TBD",
                "priority": "medium",
                "status": "pending"
            }
            new_backlog.append(task)
            task_counter += 1

    if not new_backlog:
        print("⚠️ No new tasks extracted from roadmap.")
        return

    merged_backlog = existing_backlog + new_backlog

    with open(BACKLOG_PATH, 'w') as file:
        yaml.dump({"backlog": merged_backlog}, file)
        print(f"✅ Merged backlog written to: {BACKLOG_PATH}")