# Design Changelog: UI & Input Refinements

## 1. Mat Dimensions Display
**Problem:** Users need to know the exact physical dimensions of each side of the mat (Top, Bottom, Left, Right) to cut it accurately, but currently only the total outer size is shown prominently.
**Solution:**
- Add a new section to the bottom status area (`lbl_stats`).
- **Format:**
  ```html
  <b>MAT BORDERS:</b><br>
  T: [val] | B: [val]<br>
  L: [val] | R: [val]
  ```
- **Context:** Place this next to the *Cut Size* dimensions.

## 2. Input Increments
**Problem:** The default spinbox increment (1.0) is too coarse for framing precision.
**Solution:**
- **Standardize Steps:** Set `singleStep` to **0.125** (1/8 inch) for Imperial mode and **2.0** (2mm) for Metric mode.
- **Toggle Logic:** Ensure this updates dynamically when the user switches units via `toggle_units`.

## 3. Frame Specs Collapse Polish
**Problem:** The `CollapsibleBox` flickers because it animates `maximumHeight` without forcing a geometry update, causing the layout to "jump".
**Solution:**
- **Animation Polish:** Switch to a simpler visibility toggle or use `QPropertyAnimation` on a fixed-height container with `updateGeometry` calls on each tick.
- **Simplification (Preferred):** For stability, remove the complex height animation and simply toggle visibility + `updateGeometry`. Getting smooth height animation in PyQt layouts is notoriously difficult without custom layout engines. A clean "snap" is better than a "glitchy slide".

## Verification Guard
- **Inputs:** Pressing Up/Down arrow on any dimension spinbox must change the value by exactly 0.125 (in) or 2.0 (mm).
- **Collapse:** Toggling "Frame Specs" must instantly hide/show content without shaking the window.
