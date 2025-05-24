# Contributing to Kikon-tai

Thank you for considering contributing! Kikon-tai is a modular system. Contributions are welcome via:

- Agent improvements
- Documentation updates
- Bug fixes and feature requests

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Adding a New Agent
1. Create a folder in /agents/{your_agent_name}/.
2. Define interface.yaml and your_agent_name.py with a handle(task) method.
3. Register your agent in main_loop.py dispach logic.

## Submitting a PR

Kikon-tai uses automated PR handling. For manual contributions:
```bash
git checkout -b your-branch
git commit -am "Describe your changes"
git push origin your-branch
```