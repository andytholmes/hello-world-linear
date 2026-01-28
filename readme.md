# 🚀 Linear Hello World --- AI-Native Python Project

This project is a **reference implementation** of an AI-native
development workflow using:

-   **Linear** → planning & orchestration\
-   **Cursor** → AI execution agent\
-   **GitHub** → source control\
-   **Python** → runtime platform

It demonstrates how issues, sub-issues, and projects in Linear map
directly to code structure and how Cursor can execute tasks directly
from Linear issues.

------------------------------------------------------------------------

## 🧠 Project Goals

This repo exists to demonstrate:

-   Issue → code determinism\
-   AI-native task execution\
-   Agent-driven development\
-   Structured repo design\
-   Linear-first planning model\
-   Cursor-first execution model

This is not just a demo app --- it's a **delivery architecture
pattern**.

------------------------------------------------------------------------

## 🧱 Architecture Model

Linear (Planning Layer)\
→ Cursor (Execution Layer)\
→ GitHub (Control Plane)\
→ Python (Runtime Layer)

------------------------------------------------------------------------

## 📦 Project Structure

linear-hello-world/\
├─ .cursor/\
├─ .linear/\
├─ src/hello_world/\
├─ tests/\
├─ main.py\
├─ pyproject.toml\
├─ Makefile\
└─ README.md

------------------------------------------------------------------------

## 🛠️ Setup

### Prerequisites

- Python 3.10 or higher

### Installation

1. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   # For production use
   pip install -e .

   # For development (includes testing & linting tools)
   pip install -e ".[dev]"
   ```

### Using Make (recommended)

```bash
make install-dev  # Install with dev dependencies
make test         # Run tests with coverage
make lint         # Run linter (ruff)
make format       # Format code
make typecheck    # Run type checker (mypy)
make all          # Run lint, typecheck, and test
```

------------------------------------------------------------------------

## ▶️ Running

**CLI:**
```bash
python main.py --name Andy
python main.py --name Andy --style casual
python main.py --name Smith --style formal --title Dr.
```

**API:**
```bash
uvicorn src.hello_world.api:app --reload --host 0.0.0.0 --port 8000
# Then visit http://localhost:8000/docs for interactive API docs
```

------------------------------------------------------------------------

## 🧠 Tagline

**Linear plans it. Cursor builds it. GitHub controls it. Python runs
it.**
