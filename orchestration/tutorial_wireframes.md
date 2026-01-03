# Wireframe Spec: Tutorial Popup

## Layout Overview
The tutorial will be a fixed-size `QDialog` (approx 600x500) to ensure consistent rendering of graphics across systems.

### Content Area (Top 80%)
*   **Header**: Step Title (e.g., "Welcome to FrameTamer").
*   **Image**: A focused visual (illustration or screenshot) illustrating the feature.
*   **Description**: 2-3 sentences explaining *why* and *how* to use the feature.

### Footer Area (Bottom 20%)
*   **Checkbox**: [X] Show tutorial at each startup.
*   **Spacer**: Flexible stretch.
*   **Button 1**: (Optional) Back - To return to previous step.
*   **Button 2**: Next / Finish - To progress or exit.
*   **Button 3**: Skip / Exit - Always available.

---

## Wireframe (ASCII)
```text
+-------------------------------------------------+
| [Step Title]                              [X]   |
+-------------------------------------------------+
|                                                 |
|    +---------------------------------------+    |
|    |                                       |    |
|    |         [GRAPHIC/IMAGE]               |    |
|    |                                       |    |
|    +---------------------------------------+    |
|                                                 |
|    [Description Paragraph: Lorem ipsum...]      |
|                                                 |
+-------------------------------------------------+
| [ ] Show at startup       [Back] [Next] [Exit] |
+-------------------------------------------------+
```

## Step Graphics Ideas
1.  **Welcome**: Hero image of a beautifully framed artwork.
2.  **Source Media**: Iconography of a folder and camera (Import/Google).
3.  **Dimensions**: Diagrams of Frame Face vs Rabbet.
4.  **Mat Specs**: Cross-section diagram of Art, Mat, and Frame.
5.  **Appearance**: Palette icons for color picking.
6.  **MetricCard**: Magnified view of the MetricCard results.

## Wiki Home Wireframe
*   A clean Home page with a "Get Started" link pointing to a step-by-step guide.
*   Sidebar with links to:
    *   Concepts (The 3-Layer Rule)
    *   Texture Calibration
    *   Mat Layout Strategies
