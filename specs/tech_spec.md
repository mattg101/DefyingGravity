# Tech Spec: SolidLink Plugin (Core Architecture)

## 1. Objective
Establish the foundation for the SolidLink Plugin, enabling high-performance robot description authoring within SolidWorks using a browser-based visualization environment.

## 2. System Boundaries
- **Entry Point:** SolidWorks `SwAddin` implementation.
- **Backend:** C# (.NET Framework/Core) interacting with `SldWorks`, `ModelDoc2`, `Component2` APIs.
- **Frontend:** WebView2 control hosting a local React application.
- **Networking:** `WebView2` Interop (JSON-based asynchronous messaging).

## 3. Data Models / Schema

### Backend (C#)
- `RobotManager`: Singleton managing the global state and SolidWorks selection events.
- `TessellationService`: Logic for converting `IPartDoc` geometry to JSON-ready vertex/normal buffers.
- `TreeTraverser`: Logic for filtering and serializing the `Component2` hierarchy.

### Frontend (TypeScript)
```typescript
interface Link {
  name: string;
  visuals: Geometry[];
  collisions: Geometry[];
  sensors: Sensor[];
  inertial?: Inertial;
}

interface Joint {
  name: string;
  parent: string;
  child: string;
  type: 'revolute' | 'continuous' | 'prismatic' | 'fixed';
  origin: Transform;
  axis: Vector3;
  limit?: { lower: number; upper: number; velocity: number; effort: number; };
}
```

## 4. Logical Flow (Multi-Stage)
1. **Stage 1 (Extraction):** C# backend extracts the full assembly tree. React UI applies filters (RegEx/Attribute-based) to prune the tree.
2. **Stage 2 (Joints):** UI requests transform matrices for Coordinate Systems. Data is bridged to React for 3D axis visualization.
3. **Stage 3 (Links):** Backend performs high-fidelity tessellation and inertia calculation. Decimation engine optimizes meshes for 60fps Three.js rendering.
4. **Stage 4 (Preview):** User enters "Live Mode" in React; Joint sliders update Three.js matrices in real-time.
5. **Stage 5 (Export):** Final model serialized to URDF XML; meshes exported to DAE/STL.

## 5. Security & Stability
- **Thread Safety:** All SolidWorks API calls must occur on the Main UI thread.
- **Async Bridging:** UI messages from WebView2 should be queued to prevent blocking the SolidWorks UI thread.
- **Memory Management:** Explicitly release Parasolid Body objects after tessellation to prevent file locks.

## 6. Definition of Done (Architect)
- [x] SwAddin boilerplate with WebView2 integrated.
- [ ] JSON bridge protocol defined for "Stage-Based" state management.
- [ ] `<sensor>` tag schema mapped to ROS standards (Camera, Ray, IMU).
- [ ] Automated Inertia-to-Ellipsoid visualization logic defined.
- [ ] Drag-and-drop feedback loop from SW Feature Tree to React UI verified.

