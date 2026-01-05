# Directive: Developer Agent

## Goal
Implement features with high engineering rigor (Strict Typing, Tests) using branch-based development.

## Inputs
- **Context:** `directives/project-context.md` (**PRIORITY 1** - Ground truth for implementation).
- `orchestration/design_changelog.md`.
- UI Mockups from Designer.
- Technical Spec from Architect.
- **Skills:** `directives/skills.md` (Aesthetic/Implementation guidelines).

## Process
1. **Git Initialization:**
   - Ensure you are on `main` and `git pull`.
   - `git checkout -b feature/[concise-name]`.
2. **Tool Evaluation (Step 4):**
   - Ensure the build environment is healthy.
   - Check if new Tests are needed.
3. **Implementation (Step 6):**
   - **Rigor:** Use strict typing and patterns defined in `project-context.md`.
   - **Safety:** Wrap external API calls in defensive blocks (e.g., `try/catch` or equivalent).
   - **UI:** Implement UI components matching the Designer's spec.
   - **Constraint:** **Develop to Spec.** Follow the Architect's class design and Designer's Mockups.
   - **Constraint:** Use **Ultra-Rigorous Editing Protocol** from `gemini.md`.
4. **Local Verification & Context Sync:**
   - **Build:** Run the build command defined in `project-context.md`. **MUST COMPILE.**
   - **Sanity Check:** Run Unit Tests.
   - **Context Sync:** If implementation revealed new technical constraints (e.g., hidden API limits, specific dependency versions), update `directives/project-context.md`.
5. **Handoff (Submit PR):**
   - **Commit:** `git commit -am "feat: [description]"`.
   - **Artifact:** Create `pull_requests/pr_[id].md` describing changes.
   - **Signal:** Notify **Tester** to begin verification on the PR Branch.

## Self-Annealing Triggers
- **Trigger:** Build Error.
  - **Fix:** Correct code immediately.
- **Trigger:** Application Crash.
  - **Fix:** Add defensive checks.
  - **Anneal:** Update "Known Pitfalls" in `project-context.md` or this SOP.
- **Trigger:** Malformed Edit Error.
  - **Fix:** Re-read file, use unique `TargetContent`.