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

## ▶️ Running

CLI: python main.py --name Andy

API: uvicorn src.hello_world.api:app --reload

------------------------------------------------------------------------

## 🧠 Tagline

**Linear plans it. Cursor builds it. GitHub controls it. Python runs
it.**
