# Directive: GUI Style Guide & Technical Standards

## Core Principles
1. **Defensive UI Slots:** Every slot connected to a signal (e.g., `button.clicked`) MUST be wrapped in a `try/except` block to prevent the entire event loop from crashing on local errors.
   ```python
   def on_click(self):
       try:
           # Logic here
       except Exception as e:
           QMessageBox.critical(self, "Error", str(e))
   ```
2. **State Persistence:** All user settings and window geometries MUST be persisted using `QSettings`.
3. **Separation of Concerns:** Business logic (math, file processing) MUST be located in `src/utils.py` or separate classes, never directly inside the `setup_ui` or layout methods.
4. **Dark Mode UX:** Default to dark palettes with high-contrast accessibility (WCAG AA).

## Layout Standards
- **Spacing:** Use 10px margins and 10px spacing for top-level layouts unless specified otherwise.
- **Density:** Favor `QScrollArea` over expanding layouts to ensure usability on smaller screens.
- **Unit Handling:** Use `src/utils.py` for all unit conversions to ensure consistency between UI and export layers.
