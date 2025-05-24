import os
import subprocess
from dotenv import load_dotenv

def handle_pr_agent(task):
    load_dotenv()

    branch_name = task.get("branch_name", "auto/pr_update")
    commit_message = task.get("commit_message", "Automated PR commit by pr_agent")
    pr_title = task.get("pr_title", "Automated Pull Request")
    pr_body = task.get("pr_body", "This pull request was created by Kikon-tai's pr_agent.")

    github_token = os.getenv("GITHUB_TOKEN")
    github_user = os.getenv("GITHUB_USER")
    github_email = os.getenv("GITHUB_EMAIL")
    repo_url = f"https://{github_user}:{github_token}@github.com/{github_user}/career-agent.git"

    # Configure Git if needed
    subprocess.run(["git", "config", "user.name", github_user])
    subprocess.run(["git", "config", "user.email", github_email])

    # Create new branch
    subprocess.run(["git", "checkout", "-b", branch_name])

    # Stage all changes
    subprocess.run(["git", "add", "."])

    # Commit
    subprocess.run(["git", "commit", "-m", commit_message])

    # Push to new branch
    subprocess.run(["git", "push", "-u", repo_url, branch_name])

    # Create the pull request using GitHub CLI
    subprocess.run([
        "gh", "pr", "create",
        "--title", pr_title,
        "--body", pr_body,
        "--base", "main",
        "--head", branch_name,
        "--assignee", github_user
    ])

    print(f"✅ Pull request submitted for branch: {branch_name}")