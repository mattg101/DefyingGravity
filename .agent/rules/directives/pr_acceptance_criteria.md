# PR Acceptance Criteria

This document defines the **Definition of Done** for any Pull Request (PR) attempting to merge into `main`. The **Reviewer Agent** uses this checklist to accept or reject changes.

## 1. Artifacts & Evidence
-   [ ] **Desc:** PR Description clearly states *what* changed and *why*.
-   [ ] **Evidence:** Screenshot or Video evidence of the feature working (in the correct artifacts-dir).
-   [ ] **Tests:** Screenshot or Log showing `PASS` for relevant Unit/Integration tests.

## 2. Code Quality (The "Rigor")
-   [ ] **Strict Typing:** No implicit `any` (TS) or `dynamic` (C#) unless justified by COM/Interop constraints.
-   [ ] **Error Handling:** External boundaries (API/DB/Solidworks) are wrapped in `try/catch` or defensive checks.
-   [ ] **No Dead Code:** No commented-out blocks, print statements, or `TODO`s intended for this release.
-   [ ] **Style:** Variable names are descriptive (PascalCase/camelCase per `orchestration/project_context.md`).
-   [ ] **Separation:** UI logic (View) is separated from Business logic (ViewModel/Controller).

## 3. Context & Stability
-   [ ] **Project Context:** Adheres to constraints in `orchestration/project_context.md` (e.g., Threading rules).
-   [ ] **Skills:** Demonstrates adherence to `.agent/rules/directives/skills.md` (e.g., Aesthetic quality if UI).
-   [ ] **Regression:** Core features (Export, Save) still function.

## 4. Documentation
-   [ ] **SOP Loop:** If this PR fixes a bug, is a "Known Pitfall" added to the relevant SOP?
-   [ ] **Specs:** Does the implementation match the Architect's Tech Spec?

