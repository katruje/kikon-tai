from agents.prreviewer.prreviewer import handle_prreviewer as pr_logic
"""
Genki Engine – Main Execution Loop for Kikon-tai

This script coordinates the execution of autonomous agents based on the current project
backlog. It reads task definitions from `backlog.yaml` and triggers agent-specific logic.

Status: MVP scaffold
"""

import yaml
import sys
from utils.pathing import BACKLOG_PATH

# Load backlog
def load_backlog():
    if not BACKLOG_PATH.exists():
        return []
    with open(BACKLOG_PATH, 'r') as file:
        data = yaml.safe_load(file)
        return data.get('tasks', [])

# Agent handler functions (stubs)
from agents.interview.interview import handle_interview as interviewer_logic
from agents.builder.builder import handle_builder as builder_logic
from agents.reviewer.reviewer import handle_reviewer as reviewer_logic

def handle_interview(task):
    print(f"→ [interview] Handling: {task['title']}")
    interviewer_logic(task)


# Builder agent handler
def handle_builder(task):
    title = task.get("title") or task.get("description") or "[no title]"
    print(f"→ [builder] Handling: {title}")
    builder_logic(task)


# Reviewer agent handler
def handle_reviewer(task):
    title = task.get("title") or task.get("description") or "[no title]"
    print(f"→ [reviewer] Handling: {title}")
    reviewer_logic(task)

from agents.planner.planner import handle_planner as roadmap_logic

def handle_planner(task):
    print(f"→ [planner] Handling: {task['title']}")
    roadmap_logic(task)

def handle_backlog(task):
    print(f"→ [backlog] Handling: {task['title']}")

def handle_status(task):
    print(f"→ [status] Handling: {task['title']}")

from agents.pm.pm import handle_pm as project_manager_logic

def handle_project_manager(task):
    print(f"→ [pm] Handling: {task['title']}")
    project_manager_logic(task)

def handle_genki_engine(task):
    print(f"→ [genki_engine] Executing engine configuration or scheduling logic")

# PR agent handler
def handle_prreviewer(task):
    title = task.get("title") or task.get("description") or "[no title]"
    print(f"→ [prreviewer] Handling: {title}")
    pr_logic(task)

# Dispatch logic
AGENT_HANDLERS = {
    'interview': handle_interview,
    'planner': handle_planner,
    'backlog': handle_backlog,
    'status': handle_status,
    'project_manager': handle_project_manager,
    'genki_engine': handle_genki_engine,
    'builder': handle_builder,
    'project_agent': handle_builder,
    'reviewer': handle_reviewer,
    'prreviewer': handle_prreviewer,
}

# Placeholder agent execution logic
def execute_task(task):
    title = task.get("title") or task.get("description") or "[no title]"
    print(f"[{task['id']}] Executing: {title} (assigned to: {task.get('assigned_to', '[unassigned]')})")
    handler = AGENT_HANDLERS.get(task['assigned_to'])
    if handler:
        handler(task)
    else:
        print(f"⚠️  No handler for agent: {task['assigned_to']}")

# Main loop
def run_genki_engine():
    print("🌀 Genki Engine starting...")
    backlog = load_backlog()

    # Auto-inject bootstrapping task if backlog is empty
    if not backlog:
        print("ℹ️  Backlog is empty. Injecting default bootstrapping task.")
        backlog = [{
            'id': 'T001',
            'title': 'Generate roadmap and initial backlog for career-agent',
            'assigned_to': 'planner',
            'status': 'pending',
            'priority': 'high',
            'source': 'client_brief'
        }]

    for task in backlog:
        if task['status'] == 'pending':
            execute_task(task)

if __name__ == "__main__":
    run_genki_engine()
