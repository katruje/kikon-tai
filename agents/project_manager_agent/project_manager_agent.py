from utils.pathing import BACKLOG_PATH
from ruamel.yaml import YAML

def handle_project_manager_agent(task):
    print(f"→ [project_manager_agent] Handling: {task['title']}")
    
    try:
        yaml = YAML()
        if not BACKLOG_PATH.exists():
            print(f"⚠️ Backlog file not found at: {BACKLOG_PATH}")
            return

        with open(BACKLOG_PATH, 'r') as file:
            backlog = yaml.load(file) or {}

        tasks = backlog.get("tasks", [])
        print(f"📋 Loaded {len(tasks)} tasks from backlog.")

        # Placeholder for planning logic
        for t in tasks:
            print(f"  - {t['id']}: {t['description']} (priority: {t['priority']})")

        # Future: group, sort, or generate sprint tasks

    except Exception as e:
        print(f"❌ Error processing backlog: {e}")