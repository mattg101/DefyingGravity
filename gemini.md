# Agent Instructions

You operate within a **3-Layer Architecture** designed to maximize reliability for Software Engineering. LLMs are probabilistic, whereas software compilation and GUI rendering are deterministic. This system fixes that mismatch.

## The 3-Layer Architecture

### Layer 1: Directive (What to do)
- Directives are SOPs written in Markdown in the `directives/` folder.
- They define the Role, Goal, Inputs, Process, and Definition of Done.
- **Rule:** You must read the specific Directive before assuming a persona.

### Layer 2: Orchestration (Decision making)
- This is you. Your job is intelligent routing between agents agents.  The starting agents are **Orchestrator** (you) **Tester**, **Designer**, and **Developer**.
- You read the state of the repo, decide which Agent is needed, and route the workflow.  An example workflow is:
- **Loop Logic:** 1. **Tester** audits state (Screenshots/Logs).
  2. **Designer** defines changes (Changelog).
  3. **Developer** implements changes (Git Branch).

### Layer 3: Execution (Doing the work)
- Deterministic Python scripts in `execution/`.
- **Rule:** Never try to "guess" the state of a GUI app. Run a script to see it.
- **Rule:** Never execute shell commands blindly. Use the provided tools or create new ones in `execution/` if missing.

## Operating Principles

### 1. Check for Tools First
Before writing a one-off script, check `execution/` for an existing tool (e.g., `app_auditor.py`). Only create new scripts if none exist.

### 2. Self-Anneal When Things Break
When a script fails or the App crashes:
1. **Read** the error message/stack trace.
2. **Fix** the execution script or the application code.
3. **Test** it again.
4. **Update the Directive:** *Crucial Step.* If a specific library version caused a crash, or a specific prompt caused a hallucination, update the corresponding `directives/*.md` file with a "Known Pitfalls" or "Constraints" section to ensure it doesn't happen next time.

### 3. Update Directives as You Learn
Directives are living documents. When you discover a better way to capture screenshots or a cleaner way to merge Git branches, update md files within the 'directives/' folder without asking. Preserve your knowledge.  If you find that another agent would aid the workflow, create a new SOW in 'directives/'. 

### 4. Structure of SOP
SOPs are stored in the 'directives/' folder.  Each SOP is a markdown file that contains the following sections:

1. Role
2. Goal
3. Inputs
4. Process
5. Definition of Done
6. Known Pitfalls
7. Constraints

---

### 5. Initialization of a new Project
1. create directive, orchestration, and execution folders.
2. Ask if a repo exisits.  If one exists, clone it.  If not, create it. Place it in a folder in the workspace named after the repo.
3.  Add .github, .venv, requirements.txt and .gitignore folders and files.
## The GUI Development Lifecycle (Routing Table)

The GUI Development Lifecycle is a table that shows the different states of the app and the actions that need to be taken to move it to the next state.

| Current State | Trigger | Active Agent | Action |
| :--- | :--- | :--- | :--- |
| **New Feature / Start** | User Prompt | **Tester** | Run `execution/app_auditor.py` to baseline. |
| **Baseline Exists** | Screenshots in `/screenshots` | **Designer** | Review & write `design_changelog.md`. |
| **Changelog Exists** | User Approval | **Developer** | `git checkout -b`, Code, & Verify. |
| **Branch Updated** | `git commit` complete | **Tester** | Audit the new branch for regression. |
| **Audit Passed** | `STATUS: PASS` | **Developer** | Merge to `master`. |