# Alias Directives

This file defines the behavior for shorthand slash commands used in this project.

## /gcp (Git Commit & Push)

**Syntax:** `/gcp -r <repo> [-b <branch>]`

**Description:**
Performs a standard git commit and push operation.

**Steps:**
1.  **Stage**: Add all changed files (`git add .`).
2.  **Commit**: Commit changes with a concise, descriptive message based on the recent changes.
3.  **Push**: Push to the specified `<repo>`.
    *   If `-b <branch>` is provided, push to that specific branch.
    *   If `-b` is omitted, push to the current checked-out branch.

---

## /gcpr (Git Commit, Push & PR)

**Syntax:** `/gcpr -r <repo> [-b <branch>]`

**Description:**
Performs a commit, push, and initializes a Pull Request (PR) process, emphasizing verification evidence.

**Steps:**
1.  **Stage & Commit**: Perform the same steps as `/gcp`.
2.  **Push**: Push to the specified `<repo>` and `<branch>`.
3.  **Create PR**:
    *   Draft a PR description summarizing the changes.
    *   **CRITICAL**: Include "Latest Test Evidence" in the PR body. This includes:
        *   Paths to relevant screenshots or screen recordings (from `screenshots/` or `execution/`).
        *   Test results or validation logs.
        *   Any `walkthrough.md` links if generated.
