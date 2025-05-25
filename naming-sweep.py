import os
import re
import shutil

# Directory where your agents live
AGENTS_DIR = "agents"

# Old-to-new mapping: folder and main file base
RENAME_MAP = {
    "status": "status",
    "builder": "builder",
    "reviewer": "reviewer",
    "planner": "planner",
    "prreviewer": "prreviewer",
    "backlog": "backlog",
    "pm": "pm",
    "writer": "writer",
    "interview": "interview",
}

# Step 1: Rename directories and files
for old_dir, new_dir in RENAME_MAP.items():
    old_path = os.path.join(AGENTS_DIR, old_dir)
    new_path = os.path.join(AGENTS_DIR, new_dir)
    if os.path.isdir(old_path):
        print(f"Renaming directory: {old_path} -> {new_path}")
        shutil.move(old_path, new_path)
        # Rename main Python file inside the directory
        old_file = os.path.join(new_path, f"{old_dir}.py")
        new_file = os.path.join(new_path, f"{new_dir}.py")
        if os.path.isfile(old_file):
            print(f"Renaming file: {old_file} -> {new_file}")
            os.rename(old_file, new_file)

# Step 2: Update code references in all .py files
def replace_in_file(filename, patterns):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old, new in patterns:
        content = re.sub(old, new, content)
    if content != original:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filename}")

patterns = []
for old_dir, new_dir in RENAME_MAP.items():
    # Update imports: from agents.old_dir.old_dir import ...
    patterns.append((rf"from\s+agents\.{old_dir}\.{old_dir}", f"from agents.{new_dir}.{new_dir}"))
    patterns.append((rf"import\s+agents\.{old_dir}\.{old_dir}", f"import agents.{new_dir}.{new_dir}"))
    # Update any direct references
    patterns.append((rf"{old_dir}", new_dir))
    # Handler mapping
    patterns.append((rf"handle_{old_dir}", f"handle_{new_dir}"))

# Recursively process all .py files in the repo
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            replace_in_file(os.path.join(root, file), patterns)

# Step 3: Update assigned_to keys in YAML and JSON
def update_task_refs(filename, patterns):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old_dir, new_dir in RENAME_MAP.items():
        # assigned_to: old_dir
        content = re.sub(rf"(assigned_to\s*:\s*){old_dir}", rf"\1{new_dir}", content)
        # "assigned_to": "old_dir"
        content = re.sub(rf'("assigned_to"\s*:\s*"){old_dir}(")', rf'\1{new_dir}\2', content)
    if content != original:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated task refs: {filename}")

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.yaml') or file.endswith('.yml') or file.endswith('.json'):
            update_task_refs(os.path.join(root, file), RENAME_MAP.items())

print("Agent renaming sweep complete! Review your repo for correctness, then commit all changes.")