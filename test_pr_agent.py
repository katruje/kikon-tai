from agents.pr_agent.pr_agent import handle_pr_agent

test_task = {
    "branch_name": "auto/initial-pr",
    "commit_message": "Add PR agent and test automation",
    "pr_title": "Initial PR from Kikon-tai",
    "pr_body": "This PR was automatically created using Kikon-tai's `pr_agent`. It's the beginning of autonomous GitHub integration."
}

handle_pr_agent(test_task)