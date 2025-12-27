# Design Changelog: UI Compactness & Export Refinements

## Objective
Refine the FrameTamer UI for a denser, more compact layout and improve the accessibility of export features.

## Proposed Changes

### 1. Frame Specs Box (Component Consolidation)
- **Problem:** "Frame Aperture" and "Frame Profile" take up too much vertical space.
- **Solution:** Merge these into a single collapsible box named "Frame Specs".
- **Implementation:** Use a `QGroupBox` or a custom collapsible widget to house both sections. Default to expanded, but allow users to collapse it.

### 2. Export Panel (Horizontal Top Row)
- **Problem:** Export buttons are buried or occupy valuable sidebar space.
- **Solution:** Move the following to a prominent top-row horizontal panel:
    - "Export Mat Blueprint (PDF)" button
    - "Save for Print (JPG)" button
    - DPI Selector (dropdown/spinbox)
- **Implementation:** Create a `QHBoxLayout` at the top of the main window or as the first item in the sidebar/main layout.

### 3. Dimensional Printouts (Density Increase)
- **Problem:** Metrics and stats labels have too much vertical padding.
- **Solution:** Reduce vertical spacing by approximately 30%.
- **Implementation:** 
    - Adjust `setSpacing()` on layouts.
    - Set specific `maximumHeight` or `padding` on label widgets.
    - Target: Stats and Mat Metrics labels.

## Visual Reference (Conceptual)
Based on [baseline_screenshot.png](file:///C:/Users/mattg/.gemini/antigravity/brain/3e4c7fee-f5d7-40ff-9557-63e5e836b35a/baseline_screenshot.png).

## Definition of Done for Developer
1. "Frame Specs" box exists and is collapsible.
2. Export tools are in a horizontal top row.
3. Dimensional printouts are visually denser (verified by Tester).
