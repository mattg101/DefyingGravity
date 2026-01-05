# PROJECT MANIFESTO: SolidLink Plugin (SW2URDF Upgrade)

## 1. THE NORTH STAR (Objectives)
**Goal:** Create a premium SolidWorks plugin that upgrades the SW2URDF experience with a high-performance, browser-based 3D preview and a dedicated robot description configuration environment.
**Key Value:** "Trust through Visualization." Use Parasolid geometry for internal high-fidelity rendering and provide a 60fps interactive preview that matches the final URDF physics.
**Architecture:** C# (SolidWorks API) for the backend/data extraction, WebView2 (React/Three.js) for the frontend rendering and configuration UI.

---

## 2. THE FLIGHT PLAN (Roadmap)
*Status: [ ] Pending | [/] In Progress | [x] Complete*

### Phase 1: The Hybrid Bridge (Connection)
- [x] **Task 1.1:** Setup C# SolidWorks Add-in boilerplate with WebView2 integration.
- [/] **Task 1.2:** Establish JSON-based communication bridge between C# and React.

### Phase 2: High-Performance Data Extraction
- [ ] **Task 2.1:** Implement Parasolid-to-Mesh extraction logic (SolidWorks Tessellation API).
- [ ] **Task 2.2:** Build the Feature Tree Traversal engine with real-time filtering and selection.

### Phase 3: The Configuration Environment (Dedicated Windows)
*Objective: A unified, browser-based workspace that replaces the disjointed SW2URDF wizard.*
- [ ] **Task 3.1:** **Stage 1: Tree Creation (The "Fast Builder"):** Implement the assembly tree structure where users can filter, hide, and batch-associate components to Links.
- [ ] **Task 3.2:** **Stage 2: Joint Parameterization (The "Visual Editor"):** Create a panel for Joint origins, types, and limits, with real-time 3D feedback in the render window.
- [ ] **Task 3.3:** **Stage 3: Link & Physicals Refinement:** Create a panel for Inertial, Visual, and Collision data. Automate decimation and inertia calculation.
- [ ] **Task 3.4:** **Interactive Functional Preview:** Implement one-click "Preview Mode" to drag joints in 3D and verify limits/directions before export.


### Phase 4: Extended URDF Features & Export
- [ ] **Task 4.1:** Implement `<sensor>` tag support (Camera, Ray, IMU, etc.).
- [ ] **Task 4.2:** Final URDF XML and STL/DAE mesh export.

---

## 3. THE LAW (Standard Operating Procedures)

### SOP A: The Visualization Standard
> **Constraint:** The preview MUST use decimated meshes extracted from Parasolids for performance, but maintain visual fidelity.
> **Implementation:**
> 1. Use Three.js for 60fps rendering in a dedicated browser window.
> 2. Joint limits and directions must be visually indicated (e.g., arcs, arrows).

### SOP B: Data & Workflow Integrity
> **Constraint:** Maintain the logical sequence of SW2URDF (Config -> Joints -> Links) but remove the linear "Wizard" bottlenecks.
> **Implementation:**
> 1. Use a single persistent Workspace with multiple panels.
> 2. Allow non-linear navigation between Stages (e.g. go back to Link properties without losing Joint data).
> 3. Provide "Bulk Select" from the SolidWorks feature tree via our custom filtering engine.


### SOP C: Code Hygiene (SolidWorks Specific)
> **Constraint:** SolidWorks COM objects are fragile.
> **Implementation:**
> 1. Always wrap SolidWorks API calls in `try/catch` blocks.
> 2. Explicitly release COM objects (`Marshal.ReleaseComObject`).
