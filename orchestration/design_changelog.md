# Design Changelog: UI Panel Redesign

## 1. Grouping & Layout Strategy
**Goal:** De-clutter the main panel by leveraging Collapsible Boxes and logical grouping, now that global actions are in the Menu Bar.

### Proposed Hierarchy (Vertical Layout)
1.  **Source Asset (Collapsible - Expanded by Default)**
    *   *Controls:* Import Buttons (if not strictly in menu), Google Photos, Crop Editor.
    *   *Note:* The "Import" and "Google Photos" buttons in the top row are redundant with the File menu but might be kept as "Quick Actions" or moved inside this group.
    *   *Decision:* Keep "Source Art" specific controls here.

2.  **Dimensions & Matting (Collapsible - Expanded by Default)**
    *   *Controls:* Aperture Width/Height, Mat Borders (T/B/L/R), "Link All" toggle.
    *   *Layout:* Grid layout for compact visuals.

3.  **Frame Specs (Collapsible - Collapsed by Default)**
    *   *Controls:* Frame Face, Rabbet, Print Border (moved from top/scattered).
    *   *Note:* This already exists but can be refined.

4.  **Appearance (Collapsible - Expanded by Default)**
    *   *Controls:* Mat Color Picker, Frame Color Picker, Texture Actions.

### Defaults Management
*   **Move:** "Save as Default" button -> **Preferences > Save Current as Default**.
*   **Rationale:** This is a "set and forget" action, not a daily workflow button.

## 2. Metric Display Redesign
**Goal:** Make the final dimensions "stand out" as the primary output of the tool.

### Visual Style
*   **Location:** Bottom of the Control Panel (pinned) or a dedicated "Status Bar" area?
*   **Current:** Small text in `lbl_stats`.
*   **New Design:**
    *   **Card-based Layout:** A dedicated styled `QFrame` at the bottom.
    *   **Typography:** Large, bold font for the "Outer Frame Size" (e.g., 24pt).
    *   **Information Hierarchy:**
        1.  **Outer Size** (Hero Text)
        2.  **Aperture / Cut Size** (Secondary Text)
    *   **Colors:** High-contrast background (dark grey/black) with accent color for the numbers (e.g., `#0078d7` or Gold).

## 3. Implementation Details
*   **Widget:** `MetricCard(QFrame)`
    *   `setStyleSheet` for background and borders.
    *   `QVBoxLayout` with `QLabel`s for hierarchy.
*   **Refactoring:**
    *   Remove `btn_save_defaults` from `setup_ui`.
    *   Add `act_save_defaults` to `setup_menu`.
    *   Wrap existing layouts in `CollapsibleBox` containers where missing.
