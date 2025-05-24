import os
import subprocess
from dotenv import load_dotenv

def handle_pr_agent(task):
    load_dotenv()

    target_repo_path = os.getenv("TARGET_REPO_PATH", "../career-agent")
    original_cwd = os.getcwd()
    os.chdir(target_repo_path)

    try:
        branch_name = task.get("branch_name", "auto/pr_update")
        commit_message = task.get("commit_message", "Automated PR commit by pr_agent")
        pr_title = task.get("pr_title", "🤖 Kikon-tai: Automated Pull Request")
        pr_body = task.get("pr_body", (
            "### 🤖 Automated Pull Request by Kikon-tai\n"
            "- **Agent**: pr_agent\n"
            "- **Task ID**: Unknown\n"
            "- **Note**: This PR was generated as part of an autonomous build cycle.\n"
            "Please review before merging."
        ))

        github_token = os.getenv("GITHUB_TOKEN")
        github_user = os.getenv("GITHUB_USER")
        github_email = os.getenv("GITHUB_EMAIL")
        repo_url = f"https://{github_user}:{github_token}@github.com/{github_user}/career-agent.git"

        # Configure Git if needed
        subprocess.run(["git", "config", "user.name", github_user])
        subprocess.run(["git", "config", "user.email", github_email])

        # Create new branch
        subprocess.run(["git", "checkout", "-b", branch_name])

        # Stage all changes except ignored paths
        subprocess.run(["git", "add", "-u"])  # only updates tracked files
        subprocess.run(["git", "add", "."])

        # Check for actual staged changes
        result = subprocess.run(["git", "diff", "--cached", "--quiet"])
        if result.returncode == 0:
            print("⚠️  No changes detected to commit. Skipping PR.")
            return

        # Commit
        subprocess.run(["git", "commit", "-m", commit_message])

        # Push to new branch
        subprocess.run(["git", "push", "-u", repo_url, branch_name])

        # Create the pull request using GitHub CLI with a label
        subprocess.run([
            "gh", "pr", "create",
            "--title", pr_title,
            "--body", pr_body,
            "--base", "main",
            "--head", branch_name,
            "--assignee", github_user,
            "--label", "kikon-tai-autogen"
        ])

        print(f"✅ Pull request submitted for branch: {branch_name}")
    finally:
        os.chdir(original_cwd)