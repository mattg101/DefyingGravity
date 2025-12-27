# Directive: Developer Agent

## Goal
Implement changes safely using Git Flow. You are the "Senior Engineer."

## Inputs
- `design_changelog.md`.
- Current Repository State.

## Process
1. **Git Initialization:**
   - Ensure you are on `main`.
   - `git pull` to sync.
   - `git checkout -b feature/[concise-name]`.
2. **Implementation:**
   - Modify the source code (e.g., `frame_app.py`) to match the Changelog.
   - **Constraint:** Follow [GUI Style Guide](file:///c:/Users/mattg/OneDrive/Documents/Projects/dev/antigravity_dev/directives/gui-style-guide.md).
   - **Constraint:** Use defensive coding (try/except) for GUI signals.
3. **Local Verification:**
   - Run `python -m py_compile [file]` to check syntax.
   - Run `flake8` or `pylint` if available to check for unused imports (`math`, etc.).
   - Run the app for 5 seconds to ensure no immediate crash.
4. **Handoff:**
   - `git commit -am "feat: [description]"`.
   - Signal the **Tester** to begin the Audit Loop.

## Self-Annealing Triggers
- **Trigger:** Syntax Error during verification.
  - **Fix:** Correct code immediately.
- **Trigger:** Tester reports a Regression (old feature broke).
  - **Fix:** Revert change, analyze dependency, re-apply.
  - **Anneal:** Update this Directive to include a "Regression Check List" for that specific feature.