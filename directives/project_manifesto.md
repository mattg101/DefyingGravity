# PROJECT MANIFESTO: SolidWorks URDF Exporter & Visualizer

## 1. THE NORTH STAR (Objectives)
**Goal:** Create a robust SolidWorks plugin that exports URDFs and provides a high-fidelity, interactive 3D preview of the kinematic chain *before* export.
**Key Value:** "What you see is what you get." The user must trust that the preview matches the final URDF physics.
**Architecture:** C# (SolidWorks API) for the backend, WPF for the UI, Python/Pytest for external "Puppet Master" testing.

---

## 2. THE FLIGHT PLAN (Roadmap)
*Status: [ ] Pending | [/] In Progress | [x] Complete*

### Phase 1: Core Export Logic (Current Baseline)
- [x] Basic URDF XML generation
- [x] Geometry export (STL/mesh)
- [x] Feature tree traversal

### Phase 2: The "Puppet Master" Testing Rig (HIGHEST PRIORITY)
*Objective: Establish a robust testing loop before building complex GUI features.*
- [ ] **Task 2.1:** Setup Python environment (pywinauto, pywin32, pytest) on Windows host.
- [ ] **Task 2.2:** Create "Golden Master" repository (5 reference assemblies + expected URDFs + expected screenshots).
- [ ] **Task 2.3:** Implement `test_runner.py` that launches SolidWorks, loads a model, and verifies API output.
- [ ] **Task 2.4:** Integrate into CI/CD (or local script) to run before every commit.

### Phase 3: The Visual Preview (The "Gooey" Features)
*Objective: Interactive 3D preview with sensor visualization.*
- [ ] **Task 3.1:** Implement "Decimation Engine" (Auto-simplify meshes for lightweight preview).
- [ ] **Task 3.2:** Build WPF Preview Window (Embedded in Task Pane).
- [ ] **Task 3.3:** Connect Joint Sliders to 3D Transform logic.
    - *Requirement:* Must support flipping axes and changing limits in real-time.
- [ ] **Task 3.4:** Implement Sensor Visualization (overlays for cameras/LIDAR).

### Phase 4: Git Integration
- [ ] **Task 4.1:** Add "Push to Repo" button in the GUI.

---

## 3. THE LAW (Standard Operating Procedures)

### SOP A: The "Puppet Master" Rule (Testing)
> **Constraint:** No GUI feature is considered "Complete" until it has an automated test.
> **Implementation:**
> 1. You must write a Python script using `pywinauto` that clicks the new button/slider.
> 2. You must assert the result either via internal API checks or Visual Diffing (OpenCV) of the screenshot.
> 3. "It works on my machine" is not acceptable.

### SOP B: The Visualization Standard
> **Constraint:** The preview is for *logic verification*, not rendering beauty.
> **Implementation:**
> 1. Always use decimated meshes for the preview to ensure 60fps performance.
> 2. Joint limits must be visually indicated (e.g., a red arc showing the range of motion).

### SOP C: Code Hygiene (SolidWorks Specific)
> **Constraint:** SolidWorks COM objects are fragile.
> **Implementation:**
> 1. Always wrap SolidWorks API calls in `try/catch` blocks.
> 2. Explicitly release COM objects (marshal release) when done to prevent "zombie" SLDWORKS.exe processes.