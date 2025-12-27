# Design Changelog: Texture Picker Grid Refinements

## Problem
The current 5x5 grid is always visible, creating unnecessary visual noise during texture sampling. It is also too sparse for precise straightening against subtle parallax or architectural lines in photos.

## Proposed Design Changes

### 1. Contextual Visibility
- **Behavior:** The grid overlay should only be visible when the `slider_rot` (Straighten) is being actively manipulated.
- **Goal:** Clear the Sampler UI for its primary task (sampling) while providing high-utility assistance only when needed (straightening).

### 2. Denser Grid Pattern
- **Specification:** Increase the grid from 5x5 to **10x10** divisions.
- **Visuals:** Maintain the semi-transparent dashed white line (`#FFFFFF3C`), but ensure it spans the entire bounding box of the rotated image.

### 3. State Management
- **Developer Action:** Introduce a `self.show_grid` boolean or a timer to manage the grid's visibility state.
- **Designer Note:** The grid should ideally persist for ~500ms after the slider is released to allow the user to confirm alignment without holding the mouse.

## Verification Guard
- Tester must confirm the grid *disappears* when focusing back on the selection resizing/dragging.
