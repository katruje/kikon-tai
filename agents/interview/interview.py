from utils.pathing import CLIENT_PORTAL_DIR
from pathlib import Path

def handle_interview(task):
    print(f"→ [interview] Handling: {task['title']}")
    
    brief_path = CLIENT_PORTAL_DIR / "client_brief.md"

    if not brief_path.exists():
        print(f"⚠️ Client brief not found at: {brief_path}")
        return

    try:
        with open(brief_path, 'r') as file:
            brief = file.read()
        print(f"📄 Brief loaded. Length: {len(brief)} characters.")

        # Placeholder: extract high-level goals from brief (mock logic)
        goals = ["Build an autonomous career agent", "Manage job application lifecycle"]
        print(f"🧠 Extracted high-level goals: {goals}")

    except Exception as e:
        print(f"❌ Error reading client brief: {e}")