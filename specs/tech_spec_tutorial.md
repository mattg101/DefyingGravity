# Tech Spec: Tutorial System & GitHub Wiki

## Goal
To provide a smooth onboarding experience for new users through a non-interactive, clickthrough popup tutorial and to establish a documentation base via a project wiki.

## 1. Tutorial System (`src/tutorial.py`)

### Component Architecture
*   **`TutorialDialog(QDialog)`**: A modal dialog that presents the tutorial steps.
*   **State Management**:
    *   `current_step`: Integer index.
    *   `steps`: List of dictionaries containing `title`, `description`, and `image_path` (optional).
*   **Navigation**:
    *   "Next" button: Increments `current_step` or closes if last step.
    *   "Close" button: Exits tutorial immediately.
*   **Startup Logic**:
    *   Check `QSettings` for `startup/show_tutorial`.
    *   If `True` or not set (first launch), show dialog.
    *   Checkbox in the dialog footer: "Show tutorial at each startup".

### Tutorial Steps
1.  **Welcome**: Overview of FrameTamer's mission.
2.  **Source Media**: Loading images and frame textures.
3.  **Dimensions**: Setting aperture and frame profile face/rabbet.
4.  **Matting**: Matching art to frame and setting borders.
5.  **Appearance**: Customizing colors.
6.  **Results**: Reading measurements in the MetricCard and exporting findings.

## 2. GitHub Wiki (`docs/wiki/`)

### Folder Structure
*   `docs/wiki/home.md`: Main landing page for the wiki.
*   `docs/wiki/features/`: Subfolder for detailed feature guides.
*   `docs/wiki/images/`: Assets used in the wiki.

### Content Strategy
*   Port terminal descriptions from the tutorial into permanent documentation.
*   Include technical notes on the 3-layer architecture and layout constraints.

## 3. Tooling Changes
*   **`execution/generate_wiki_images.py`**: A new script to automate screenshot capture of specific UI regions for the wiki.
