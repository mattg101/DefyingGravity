# Design Changelog - Texture Picker Enhancements

## Problem Statement
The current texture sampler relies on manual user correction for orientation and lacks constraints to ensure high-quality texture tiling (2:1 aspect ratio). Panning is also limited to the background image.

## Proposed Changes

### 1. Aspect Ratio Detection & Orientation
- **Logic:** App should compare `selection_box.width` to `selection_box.height`.
- **Vertical Selection:** If `height > width`, system treats texture as a **Vertical Member**.
- **Horizontal Selection:** If `width > height`, system treats texture as a **Horizontal Member**.
- **Visual Feedback:** selection box color should shift slightly (e.g., lime green for Horizontal, sky blue for Vertical) to show detection.

### 2. Constraint: 2:1 Minimum Aspect Ratio
- **Rule:** As the user drags, the box should be constrained to a MINIMUM of 2:1 (or 1:2) aspect ratio.
- **Implementation:** During mouse move, if `w < 2*h` (for horizontal), clamp `w` or `h` to maintain the ratio.

### 3. Interaction: Selection-Box Panning
- **Trigger:** `Shift + Right Click + Drag`.
- **Behavior:** Offsets the `selection_norm` coordinates without resizing the box.
- **Standard Panning:** Standard `Right Click + Drag` remains for background image panning.

## Success Criteria
- [x] User cannot create a square or near-square selection.
- [x] Selection box color changes based on orientation.
- [x] Selection box can be moved via Shift-Right Click.
