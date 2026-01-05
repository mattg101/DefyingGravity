# UI Spec: SolidLink Plugin

## 1. Visual Objective
Provide a "Pro-Grade" configuration environment that feels integrated with SolidWorks but offers modern, high-performance visual feedback. The goal is to maximize the speed of associating SolidWorks geometry with the robot description.

## 2. Wireframes

### Dedicated Render Window (3D Preview)
```
+---------------------------------------------------+
| [60 FPS Perspective View]                         |
|                                                   |
|   (o) Gizmo: Selected Link                        |
|   [---] Joint Slider (Rotates Link)               |
|   <---> Limit Visualizer (Red Arc)                |
|                                                   |
+---------------------------------------------------+
```

### Configuration Window (Unified Workspace)
```
+---------------------------------------------------+
| [Stage 1: Config] [Stage 2: Joints] [Stage 3: Links]|
+---------------------------------------------------+
| [Filter: (o) Nuts/Bolts (x) Screws             ]  |
| + Assembly Root                                   |
|   - BaseLink (Associated: 12 parts)               |
|   - Arm_Link (Associated: 3 parts) <--- [Drag]    |
+---------------------------------------------------+
| [Panel: Contextual Data]                          |
| (Depends on Stage selected above)                 |
| - Stage 2: Joint Offset, Axis, Limits             |
| - Stage 3: Mass, Inertia, Sensors                 |
+---------------------------------------------------+
```


## 3. Interaction Design
- **Action**: User filters Feature Tree -> **Result**: Unmatched items are hidden/greyed out; matched items are highlighted in 3D.
- **Action**: Dragging an item to a Link -> **Result**: Instant mesh extraction (C# -> JS) and appearance in 3D Render Window.
- **Action**: Toggling "Editor Mode" -> **Result**: Parameters panel switches to Joint/Limit controls; the 3D view shows persistent joint axes.

## 4. Styling Tokens
- **Theme:** Dark Mode (VS Code aesthetics).
- **Colors:**
    - Highlight: Electron Blue (#0984e3)
    - Alert: Mars Red (for joint limit violations) (#d63031)
- **Typography:** Inter or Roboto (Modern Sans-Serif).

## 5. Definition of Done (Designer)
- [ ] Render Window layout responsive to resizing.
- [ ] Build vs. Editor mode transitions defined.
- [ ] Batched assignment UI (multi-select) implemented.
- [ ] Sensor visualization (frustum/rays) mockups complete.
