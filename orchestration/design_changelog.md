# Design Changelog: Texture Picker Grid Final Polish

## Problem
1. **Low Visibility:** The dashed 60-opacity lines are too subtle against busy textures.
2. **Startup Flash:** The grid briefly appears when the dialog initializes, which feels like a glitch.
3. **Zoom Sensitivity:** The grid is locked to the image bounding box. When zoomed in, the grid lines can be sparse or non-existent in the viewport, defeating their purpose.

## Proposed Design Changes (The "Window-Frame Grid")

### 1. High-Visibility Aesthetics
- **Color:** White (`#FFFFFF`).
- **Opacity:** 100/255 (increased from 60).
- **Style:** 
  - **Center Crosshair:** Solid lines passing through the exact center of the preview label.
  - **Secondary Lines:** Dashed lines every 100 pixels.

### 2. Zoom-Independent Spacing
- **Specification:** The grid should span the **entire preview area** (the whole `lbl_preview` canvas), not just the `img_rect`.
- **Behavior:** As the user zooms or pans the image, the grid stays static relative to the dialog window. This allows the user to align image features (e.g., a frame member) against the stable vertical/horizontal axes of the window.
- **Spacing:** Fixed at **1.0 inch / 100px** intervals on screen.

### 3. "Quiet" Startup
- **Requirement:** The grid must remain hidden during initial loading and when the rotation is exactly 0.0 unless the user explicitly touches the slider.
- **Developer Action:** Initialize `self.grid_visible = False` and ensure the `grid_timer` does not fire during the automated `load_default_texture` sequence.

## Verification Guard
- Tester must verify that zooming in 10x does NOT change the screen-spacing of the grid lines.
- Tester must verify no "grey flicker" of grid lines on dialog launch.
