# Design: Expanded Color Library & Mat Color Picker

## Feature Set
- **Expanded Library:** 500+ named colors stored in centralized `colors.py`.
- **Perceptual Matching:** Use CIEDE2000 algorithm to find the closest human-perceived color name.
- **Matched Name Feedback:** Show the name instantly in the picker and app headers.

## UI Wireframes

### 1. Main Application (Appearance Panel)
```
+---------------------------------------+
| Appearance                            |
+---------------------------------------+
| Mat Color [btn] | Frame Color [btn]   |
| [ Mat Color Name Label (e.g. "Sage") ]| <--- NEW!
| Mat Ply: [Dropdown]                   |
+---------------------------------------+
```

### 2. Custom Color Picker Dialog
```
+---------------------------------------+
| Pick Mat Color                        |
+---------------------------------------+
| [ Standard Color Palette/Sliders ]    |
|                                       |
| Selected: [ #708090 ]                 |
| Name: [ Slate Gray ]                  | <--- NEW!
|                                       |
| [ OK ]                [ Cancel ]      |
+---------------------------------------+
```

## Transition Logic
- Clicking "Mat Color" button in `app.py` triggers `MatColorPickerDialog`.
- As the user moves the slider/clicks a color, `ColorUtils.get_closest_name(qcolor)` is called.
- The name is updated in the dialog label.
- On "OK", the name is also pushed to the main app's `lbl_mat_name`.

## Audit Baseline
Captured in `screenshots/color_audit_appearance_*.png`
- Current buttons: "Mat Color", "Frame Color"
- Current logic: Straight to `QColorDialog`, no name visible.
