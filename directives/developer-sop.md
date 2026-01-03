# Directive: Developer Agent

## Goal
Implement features with high engineering rigor (Pydantic-level typing on backend, strong TypeScript safety on frontend) using branch-based development.

## Inputs
- `orchestration/design_changelog.md`.
- Wireframes from Designer.
- Current Repository State.

## Process
1. **Git Initialization:**
   - Ensure you are on `main` and `git pull`.
   - `git checkout -b feature/[concise-name]`.
2. **Tool Evaluation (Step 4):**
   - Evaluate what automation scripts or tools are needed for implementation and testing.
   - Coordinate with the **Dev Tool Developer** to ensure these scripts exist in `execution/` before coding.
3. **Implementation (Step 6):**
   - **Rigor:** All backend modifications MUST use strict typing (e.g., Pydantic models for data structures).
   - **Safety:** All frontend code MUST ensure strong TypeScript safety and component boundary validation.
   - **Constraint:** **Develop to Wireframe.** Match the widget hierarchy and nesting structure of the Designer's wireframes exactly. No ad-hoc layout Hacks.
   - **Constraint:** Follow [GUI Style Guide](file:///c:/Users/mattg/OneDrive/Documents/Projects/dev/antigravity_dev/directives/gui-style-guide.md).
   - **Constraint:** Use **Ultra-Rigorous Editing Protocol (Rule of Zero)** defined in `gemini.md` for all code modifications.
   - **Constraint:** Use defensive coding (try/except) for GUI signals.
4. **Local Verification:**
   - Run syntax checks and linters (`flake8`, `pylint`, `tsc`).
   - Run the app for 5 seconds to ensure no immediate crash.
5. **Handoff:**
   - `git commit -am "feat: [description]"`.
   - Signal the **Tester** to begin the high-rigor verification loop in a temporary Docker container.

## Self-Annealing Triggers
- **Trigger:** Syntax Error during verification.
  - **Fix:** Correct code immediately.
- **Trigger:** Tester reports a Regression or type mismatch.
  - **Fix:** Revert change, analyze dependency, re-apply with stricter types.
  - **Anneal:** Update this Directive to include a "Strict Type Checklist" for that specific module.
- **Trigger:** Malformed Edit Error (`targetContent` not found).
  - **Fix:** Re-read the file without line numbers, verify whitespace/indentation, and re-apply.
  - **Anneal:** If common in a specific file, add an "Indentation Note" to its header.