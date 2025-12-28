# Design Changelog: Project Management & Menu System

## 1. Menu Bar Architecture
**Goal:** Transition from a utility-app layout to a document-based application layout by introducing a standard Menu Bar.

### Hierarchy Standard
- **File**
  - **New Project** (Ctrl+N): Resets all fields to defaults.
  - **Open Project...** (Ctrl+O): Opens file picker for `.frame` files.
  - **Recent Projects >**: Submenu listing last 5 files.
  - **Save Project** (Ctrl+S): Saves current state. Matches `Ctrl+S` convention.
  - **Save Project As...** (Ctrl+Shift+S): Save as new file.
  - **Exit**: Closes app.
- **Preferences**
  - **Workflow Mode >**: Submenu (Radio behavior).
    - **Fixed Frame (Fit Art)**: Checked if active.
    - **Fixed Art (Build Frame)**: Checked if active.
  - **Toggle Units**: Action to toggle between Inches/MM (Alternative to top-right radio).
- **Help**
  - **Tutorial**: Opens separate window.
  - **About**: Opens separate window.

## 2. File Format (`.frame`)
**Goal:** Robust, human-readable JSON storage for project state.
**Schema:**
```json
{
  "version": "14.0",
  "timestamp": "ISO-8601",
  "settings": {
    "unit": "in",
    "mode": "fixed_frame"
  },
  "dimensions": {
    "aperture_w": 16.0,
    "aperture_h": 20.0,
    "mat_borders": [2.0, 2.0, 2.0, 2.0],
    "frame_face": 0.75
  },
  "assets": {
    "image_path": "abs/path/to/img.jpg",
    "crop_rect": [0.0, 0.0, 1.0, 1.0],
    "frame_texture_path": "(optional) serialization of texture"
  }
}
```
*Note: For texture assets, we should store them relative to the project file if possible, or absolute paths with a warning if missing.*

## 3. Workflow Mode Migration
**Problem:** "Workflow Mode" takes up valuable vertical space in the main panel.
**Solution:** Move exclusively to `Preferences > Workflow Mode`. 
**Feedback:** When changed via menu, show a small temporary status bar message or toast: "Switched to Fixed Art Mode".

## 4. Helper Windows
**Design:**
- **Structure:** Non-modal `QDialog` or secondary `QWidget` so the user can keep them open while working.
- **Content:** Placeholder text for now ("Tutorial coming soon..." / "FrameTamer v14.0\nCreated by Antigravity").
- **Controls:** Simple "Close" button at bottom right.

## Verification Guard
- **Save/Load:** Saving a complex setup (custom mat, crop, mode) and reloading it must verify **exact** state restoration.
- **Persistence:** "Recent Projects" must persist across app restarts.
