from pathlib import Path
from utils.pathing import get_project_dir

def handle_reviewer_agent(task):
    project_name = "career-agent"  # This can be dynamically derived from task if needed
    project_path = get_project_dir(project_name)
    agents_dir = project_path / "agents"

    print(f"→ [reviewer_agent] Reviewing project at: {project_path}")

    if not agents_dir.exists():
        print(f"⚠️ Agents directory not found: {agents_dir}")
        return

    for agent_folder in sorted(agents_dir.iterdir()):
        if agent_folder.is_dir():
            print(f"\n📁 {agent_folder.name}/")
            py_files = list(agent_folder.glob("*.py"))
            if not py_files:
                print("  ⚠️ No Python files found.")
                continue
            for py_file in py_files:
                print(f"  📄 {py_file.name}")
                with open(py_file, 'r') as f:
                    lines = f.readlines()
                    if any("def handle()" in line for line in lines):
                        print("    ✅ Found `handle()` function.")
                    else:
                        print("    ⚠️ Missing `handle()` function.")