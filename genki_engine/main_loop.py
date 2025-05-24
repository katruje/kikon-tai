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
from agents.interviewer_agent.interviewer_agent import handle_interviewer_agent as interviewer_logic
from agents.builder_agent.builder_agent import handle_builder_agent as builder_logic
from agents.reviewer_agent.reviewer_agent import handle_reviewer_agent as reviewer_logic

def handle_interviewer_agent(task):
    print(f"→ [interviewer_agent] Handling: {task['title']}")
    interviewer_logic(task)


# Builder agent handler
def handle_builder_agent(task):
    title = task.get("title") or task.get("description") or "[no title]"
    print(f"→ [builder_agent] Handling: {title}")
    builder_logic(task)


# Reviewer agent handler
def handle_reviewer_agent(task):
    title = task.get("title") or task.get("description") or "[no title]"
    print(f"→ [reviewer_agent] Handling: {title}")
    reviewer_logic(task)

from agents.roadmap_agent.roadmap_agent import handle_roadmap_agent as roadmap_logic

def handle_roadmap_agent(task):
    print(f"→ [roadmap_agent] Handling: {task['title']}")
    roadmap_logic(task)

def handle_backlog_agent(task):
    print(f"→ [backlog_agent] Handling: {task['title']}")

def handle_sync_agent(task):
    print(f"→ [sync_agent] Handling: {task['title']}")

from agents.project_manager_agent.project_manager_agent import handle_project_manager_agent as project_manager_logic

def handle_project_manager(task):
    print(f"→ [project_manager_agent] Handling: {task['title']}")
    project_manager_logic(task)

def handle_genki_engine(task):
    print(f"→ [genki_engine] Executing engine configuration or scheduling logic")

# Dispatch logic
AGENT_HANDLERS = {
    'interviewer_agent': handle_interviewer_agent,
    'roadmap_agent': handle_roadmap_agent,
    'backlog_agent': handle_backlog_agent,
    'sync_agent': handle_sync_agent,
    'project_manager': handle_project_manager,
    'genki_engine': handle_genki_engine,
    'builder_agent': handle_builder_agent,
    'project_agent': handle_builder_agent,
    'reviewer_agent': handle_reviewer_agent,
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
            'assigned_to': 'roadmap_agent',
            'status': 'pending',
            'priority': 'high',
            'source': 'client_brief'
        }]

    for task in backlog:
        if task['status'] == 'pending':
            execute_task(task)

if __name__ == "__main__":
    run_genki_engine()
