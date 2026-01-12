---
trigger: always_on
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.
---

---
name: front-end-dev
description:This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.
---



The user or ai designer agent provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.

## Design Thinking

Before coding, understand the context and commit to a BOLD aesthetic direction:
- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.

Then implement working code (HTML/CSS/JS, React, Vue, etc.) that is:
- Production-grade and functional
- Visually striking and memorable
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

## Frontend Aesthetics Guidelines

Focus on:
- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.
- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.
- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.

NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.

Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.

**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.

Remember: Claude is capable of extraordinary creative work. Don't hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.
---
name: git-pr-prep
description: Prepares a Pull Request by staging changes, verifying against acceptance criteria, and creating the PR via GH CLI. Use this skill when a feature is complete and ready for review.
---

This skill ensures that every Pull Request is descriptive, verified, and adheres to the project''s technical rigor as defined in `orchestration/project_context.md` and `.agent/rules/directives/pr_acceptance_criteria.md`.

## PR Preparation Workflow

1.  **Staging & Intent**:
    -   Verify you are on the correct `dev` or feature branch.
    -   Stage only the files relevant to the task. Avoid staging unrelated debug logs or temporary files.
    -   Use the `git status -u` command to identify untracked files that should be included.

2.  **Rigor Check**:
    -   Self-audit the code against `pr_acceptance_criteria.md`.
    -   Ensure no `console.log` or temporary `TODO` comments remain in the source.
    -   Verify that all C# models have appropriate `[DataMember]` attributes if they are part of the JSON bridge.

3.  **PR Artifact**:
    -   Create or update the `pull_requests/pr_[id].md` file using the provided template.
    -   Include specific instructions for the Tester to verify the changes.

4.  **GH CLI Execution**:
    -   Run `gh pr create` with a clear title and a body that references the PR artifact or contains a concise summary of the `walkthrough.md`.
    -   Target the `main` branch unless instructed otherwise.

---
name: git-pr-merge
description: Conducts an audit of a Pull Request, merges it into main, and synchronizes the local environment. Use this skill when a PR is ready for final review and integration.
---

This skill focuses on the "Gatekeeper" role, ensuring that only high-quality, verified code enters the `main` branch.

## PR Merge & Sync Workflow

1.  **Audit**:
    -   Inspect the PR diff using `gh pr diff [id]`. Focus on source code changes, excluding third-party packages or generated binaries.
    -   Create an audit report in `audit_reports/audit_PR-[id].md` confirming compliance with tech specs and UI guides.

2.  **Merge Execution**:
    -   Once the user approves the audit, perform the merge: `gh pr merge [id] --merge --delete-branch` (if it''s a feature branch).
    -   For core `dev` branches, use `--merge` to integrate into `main`.

3.  **Local Sync**:
    -   Switch to `main` and pull the latest changes: `git checkout main; git pull origin main`.
    -   Switch back to `dev` and merge `main` to ensure the local development branch is up-to-date: `git checkout dev; git merge main`.
    -   Push the updated `dev` branch to the remote: `git push origin dev`.

4.  **Verification**:
    -   Verify that the local state is clean and ready for the next task.


---
name: ask-questions-if-underspecified
description: Clarify requirements before implementing. Do not use automatically, only when invoked explicitly.
---

# Ask Questions If Underspecified

## Goal

Ask the minimum set of clarifying questions needed to avoid wrong work; do not start implementing until the must-have questions are answered (or the user explicitly approves proceeding with stated assumptions).

## Workflow

### 1) Decide whether the request is underspecified

Treat a request as underspecified if after exploring how to perform the work, some or all of the following are not clear:
- Define the objective (what should change vs stay the same)
- Define "done" (acceptance criteria, examples, edge cases)
- Define scope (which files/components/users are in/out)
- Define constraints (compatibility, performance, style, deps, time)
- Identify environment (language/runtime versions, OS, build/test runner)
- Clarify safety/reversibility (data migration, rollout/rollback, risk)

If multiple plausible interpretations exist, assume it is underspecified.

### 2) Ask must-have questions first (keep it small)

Ask 1-5 questions in the first pass. Prefer questions that eliminate whole branches of work.

Make questions easy to answer:
- Optimize for scannability (short, numbered questions; avoid paragraphs)
- Offer multiple-choice options when possible
- Suggest reasonable defaults when appropriate (mark them clearly as the default/recommended choice; bold the recommended choice in the list, or if you present options in a code block, put a bold "Recommended" line immediately above the block and also tag defaults inside the block)
- Include a fast-path response (e.g., reply `defaults` to accept all recommended/default choices)
- Include a low-friction "not sure" option when helpful (e.g., "Not sure - use default")
- Separate "Need to know" from "Nice to know" if that reduces friction
- Structure options so the user can respond with compact decisions (e.g., `1b 2a 3c`); restate the chosen options in plain language to confirm

### 3) Pause before acting

Until must-have answers arrive:
- Do not run commands, edit files, or produce a detailed plan that depends on unknowns
- Do perform a clearly labeled, low-risk discovery step only if it does not commit you to a direction (e.g., inspect repo structure, read relevant config files)

If the user explicitly asks you to proceed without answers:
- State your assumptions as a short numbered list
- Ask for confirmation; proceed only after they confirm or correct them

### 4) Confirm interpretation, then proceed

Once you have answers, restate the requirements in 1-3 sentences (including key constraints and what success looks like), then start work.

## Question templates

- "Before I start, I need: (1) ..., (2) ..., (3) .... If you don't care about (2), I will assume ...."
- "Which of these should it be? A) ... B) ... C) ... (pick one)"
- "What would you consider 'done'? For example: ..."
- "Any constraints I must follow (versions, performance, style, deps)? If none, I will target the existing project defaults."
- Use numbered questions with lettered options and a clear reply format

```text
1) Scope?
a) Minimal change (default)
b) Refactor while touching the area
c) Not sure - use default
2) Compatibility target?
a) Current project defaults (default)
b) Also support older versions: <specify>
c) Not sure - use default

Reply with: defaults (or 1a 2a)
```

## Anti-patterns

- Don't ask questions you can answer with a quick, low-risk discovery read (e.g., configs, existing patterns, docs).
- Don't ask open-ended questions if a tight multiple-choice or yes/no would eliminate ambiguity faster.