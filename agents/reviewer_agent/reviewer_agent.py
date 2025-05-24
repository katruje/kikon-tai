from pathlib import Path
from utils.pathing import get_project_dir

def handle_reviewer_agent(task):
    project_name = "career-agent"  # This can be dynamically derived from task if needed
    project_path = get_project_dir(project_name)
    agents_dir = project_path / "agents"
    logs_dir = project_path / "logs"
    logs_dir.mkdir(exist_ok=True)

    print(f"→ [reviewer_agent] Reviewing project at: {project_path}")

    if not agents_dir.exists():
        print(f"⚠️ Agents directory not found: {agents_dir}")
        return

    report_lines = [f"# Review Summary for `{project_name}`\n"]

    for agent_folder in sorted(agents_dir.iterdir()):
        if agent_folder.is_dir():
            report_lines.append(f"## {agent_folder.name}")
            py_files = list(agent_folder.glob("*.py"))
            if not py_files:
                report_lines.append("- ⚠️ No Python files found.")
                continue
            for py_file in py_files:
                report_lines.append(f"- `{py_file.name}`")
                with open(py_file, 'r') as f:
                    lines = f.readlines()
                    if any("def handle()" in line for line in lines):
                        report_lines.append("  - ✅ Found `handle()` function.")
                    else:
                        report_lines.append("  - ⚠️ Missing `handle()` function.")

    report_path = logs_dir / "review_summary.md"
    with open(report_path, 'w') as report_file:
        report_file.write("\n".join(report_lines))

    print(f"✅ Review summary written to: {report_path}")