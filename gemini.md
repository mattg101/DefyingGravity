# Agent Instructions
You are used in the Antigravity IDE by google.

different AI modeles are metered in antigravity app. if it seems like things are taking awhile suggest switching the model in the future.

You operate within a **3-Layer Architecture** designed to maximize reliability and software engineering rigor.

## The 3-Layer Architecture

### Layer 1: Directive (Specifications & SOPs)
- **SOPs:** Directives are SOPs written in `directives/`. They define Roles and Goals.
- **Skill-Driven:** Agents check `directives/skills.md` for specialized knowledge.

### Layer 2: Orchestration (Artifact-Driven Decision Making)
- This layer ensures **Deterministic Execution** via strict input/output artifacts.
- **Core Metadata:**
  - `orchestration/project_context.md`: Technology stack (Ground Truth).
  - `orchestration/project_manifesto.md`: Strategy and Roadmap.
  - `orchestration/project_design_spec.md`: High-level system architecture.
- **Artifact Pipeline (Steps):**
  1. **Analyze (Orchestrator)**: Input: Prompt -> Output: Updated `task.md`.
  2. **Design (Architect)**: Input: Prompt -> Output: `specs/tech_spec.md`.
  3. **UI/UX (Designer)**: Input: Tech Spec -> Output: `specs/ui_spec.md`.
  4. **Implement (Developer)**: Input: Specs -> Output: `pull_requests/pr_[id].md`.
  5. **Verify (Tester)**: Input: PR -> Output: `test_results/test_report.md`.
  6. **Review (Reviewer)**: Input: PR + Report -> Output: `audit_reports/audit.md`.
  7. **Release (DevOps)**: Input: Approved Audit -> Output: Release Tag/Log.

- **Rule:** Every agent MUST use the corresponding template in `orchestration/` for their output.

### Layer 3: Execution (Deterministic Automation)
- **Build System:** Adhere to `orchestration/project_context.md`.
- **Rule:** Artifacts are NOT valid if the build fails.

### Ultra-Rigorous Editing Protocol (Rule of Zero)
To eliminate "Malformed Edit" or "Target Content Not Found" errors, you MUST follow these steps:
1. **Rule of Zero (Line Numbers):** Never copy the line number prefix (e.g., `123: `) from the `view_file` or `view_code_item` output into your `TargetContent`. The file content starts *after* the colon and space.
2. **Deterministic Matching:** Always perform a `view_file` of the EXACT window you intend to edit immediately before calling an edit tool. Use this to verify whitespace and indentation character-for-character.
3. **No Guessing/No Padding:** Do not "invent" missing lines or add extra newlines/spaces at the end of `TargetContent` or `ReplacementContent` unless they are explicitly present in the source.
4. **Itemized Replacement:** If you are changing multiple methods in a class, use `multi_replace_file_content` with small, discrete chunks rather than one giant block.
5. **Self-Correction Loop:** If an edit fails, DO NOT guess a fix. Call `view_file` with a narrow 10-line range around the failure point to inspect the exact characters (e.g., CRLF vs LF, tabs vs spaces) then re-apply.

### Deterministic Path Protocol
To eliminate errors related to reviewing, removing, and copying files, you MUST follow these steps:
1. **Strict Absolute Paths:** Always use absolute paths (e.g., `C:\Users\...`) for all tool calls and terminal commands. Never rely on relative paths or assuming a certain `Cwd`.
2. **Artifact Directory Identity:** The project workspace and the artifact directory (`.gemini\antigravity\brain\...`) are distinct. 
   - Write code to the **Workspace**.
   - Store planning, verification artifacts, and media in the **Artifact Directory**.
3. **Media Lifecycle:** 
   - **Internal Evidence:** Screenshots for `walkthrough.md` or `task.md` go to the **Artifact Directory**.
   - **External Evidence:** Screenshots for PRs or documentation go to the repo's `screenshots/` or `docs/`.
   - **Embed Rule:** Only embed files using absolute paths. If embedding in an artifact (e.g., `walkthrough.md`), the file MUST be in the **Artifact Directory`.
4. **Cleanup:** Periodically prune temporary workspace files.
5. **No Placeholders:** Never use placeholder paths. If you need a path you don't have, find it with `find_by_name` or `list_dir`.

## Operating Principles

### 1. Specs First, Code Second
Always ensure a **Feature Spec** or **Technical Spec** exists. If missing, the **Architect** must write it first.

### 2. Rigor & Safety
All code must meet high standards (See `orchestration/project_context.md` for specifics):
- **Backend:** Strict Typing / Defensive Coding.
- **Frontend:** Pattern adherence (MVVM/Component).
- **Infrastructure:** Clean Builds and Installers.
- **Admin Access:** The Agent presumes **Administrator** privileges in the internal terminal.
    - *Usage:* You may execute scripts (e.g., `register.ps1`, `install_service.bat`) that require elevation without asking for permission, unless explicitly restricted by the User.

### 3. Self-Anneal & Knowledge Capture
When a build fails or app crashes:
1. **Read** the Error Log.
2. **Fix** the code.
3. **Update Directive:** Update "Known Pitfalls" in the relevant SOP or Context file.

### 4. Zero Regression
Ensure existing core functionality remains intact while refactoring.
