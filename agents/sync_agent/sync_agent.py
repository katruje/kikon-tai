

"""
sync_agent.py

This agent generates a sprint log summarizing project activity. It checks the current
backlog for completed, in-progress, and pending tasks and writes a dated Markdown log.
"""

from pathlib import Path
from datetime import datetime
import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
BACKLOG_PATH = ROOT / "data/backlog.yaml"
LOG_DIR = ROOT / "data/sprint_log"

def handle_sync_agent(task):
    print("→ [sync_agent] Generating sprint log from backlog.yaml")

    try:
        with open(BACKLOG_PATH, 'r') as file:
            backlog_data = yaml.safe_load(file)
            tasks = backlog_data.get("backlog", [])
    except Exception as e:
        print(f"❌ Failed to read backlog: {e}")
        return

    completed = [t for t in tasks if t["status"] == "done"]
    in_progress = [t for t in tasks if t["status"] == "in-progress"]
    pending = [t for t in tasks if t["status"] == "pending"]

    today = datetime.now().strftime("%Y-%m-%d")
    log_path = LOG_DIR / f"{today}.md"
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    summary = f"# Sprint Log – {today}\n\n"
    summary += f"**Completed:** {len(completed)}\n\n"
    for t in completed:
        summary += f"- ✅ {t['id']}: {t['title']}\n"
    summary += f"\n**In Progress:** {len(in_progress)}\n\n"
    for t in in_progress:
        summary += f"- 🔄 {t['id']}: {t['title']}\n"
    summary += f"\n**Pending:** {len(pending)}\n\n"
    for t in pending:
        summary += f"- ⏳ {t['id']}: {t['title']}\n"

    try:
        with open(log_path, 'w') as file:
            file.write(summary)
        print(f"✅ Sprint log written to: {log_path}")
    except Exception as e:
        print(f"❌ Failed to write sprint log: {e}")