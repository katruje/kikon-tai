from pathlib import Path

# Root of the project (assumes this file lives in Kikon-tai/utils/)
ROOT_DIR = Path(__file__).resolve().parent.parent

# Standard project directories
DATA_DIR = ROOT_DIR / "data"
CLIENT_PORTAL_DIR = ROOT_DIR / "client_portal"
AGENTS_DIR = ROOT_DIR / "agents"
INTERNAL_DIR = ROOT_DIR / "internal"
SEED_DIR = ROOT_DIR / "seed"

# Specific project files
BACKLOG_PATH = DATA_DIR / "backlog.yaml"
ROADMAP_PATH = DATA_DIR / "roadmap.md"
SPRINT_LOG_PATH = DATA_DIR / "sprint_log.md"
CLIENT_BRIEF_PATH = CLIENT_PORTAL_DIR / "client_brief.md"
REQUIREMENTS_PATH = INTERNAL_DIR / "requirements.yaml"