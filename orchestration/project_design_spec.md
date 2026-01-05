# Project Design Spec: SolidLink Plugin

## 1. System Architecture
The SolidLink Plugin follows a **Hybrid Bridge Architecture** between a C# SolidWorks Add-in and a browser-based Frontend.

- **Backend (C# .NET):** Hosts the SolidWorks COM connection, performs geometry extraction (Parasolid tessellation), and manages the lifecycle of the WebView2 windows.
- **Frontend (React/Three.js):** Provides a high-performance 3D rendering environment and the configuration GUI. 
- **Communication:** Bi-directional JSON bridge via `WebView2.CoreWebView2.PostWebMessageAsJson` and `window.chrome.webview.addEventListener`.

## 2. Core Data Models
- **RobotDescription:** The primary in-memory model (JavaScript object) that mirrors the URDF structure.
- **JointAssociation:** Maps SolidWorks Reference Geometry (Coordinate Systems) to URDF Joint origins.
- **LinkAssociation:** Maps filtered SolidWorks Components/Bodies to URDF Link geometry (Visual/Collision).
- **SensorModel:** Encapsulates ROS-standard sensor parameters (Camera, Ray, IMU).

## 3. Key Workflows
- **Stage 1: Tree Configuration (Build):**
    1. Import SolidWorks Assembly hierarchy.
    2. Filter tree (e.g. by component name or visibility) to hide hardware/non-robot parts.
    3. Batch-associate remaining components to Links.
- **Stage 2: Joint Parameterization:**
    1. Select Joint origins (Coordinate Systems).
    2. Define Joint types and limits with 3D arcs/gizmo overlays.
- **Stage 3: Link & Physicals Refinement:**
    1. Preview generated Inertia Tensors as 3D ellipsoids.
    2. Toggle between Visual and Collision meshes (red transparent overlays).
- **Stage 4: Functional Verification:**
    1. Enter "Live Mode" to manipulate joint sliders.
    2. Verify kinematic chain behavior in the high-performance browser renderer.


## 4. Design Patterns
- **MVVM:** Frontend state management for the Robot Description model.
- **Service-Oriented (Backend):** Decimation Engine and Tree Traversal are discrete internal services.
- **Observer:** React components re-render based on updates from the C# bridge.

