# Design Changelog: UI Panel Redesign (Wireframe Revision)

## 1. Grouping & Layout Strategy
**Goal:** De-clutter the main panel and enforce overflow-safe widths.

### Proposed Hierarchy (Vertical Layout)
1.  **Source Asset (Collapsible - Expanded)**
2.  **Dimensions & Matting (Collapsible - Expanded)**
3.  **Frame Specs (Collapsible - Collapsed)**
4.  **Appearance (Collapsible - Expanded)**
5.  **Metric Display (Pinned Bottom)**

---

## 2. Wireframe Specification: Layout & Constraints
**Goal:** Address overflow and truncation by defining rigid pixel constraints.

### Relative Positioning Wireframe (ASCII)
```text
+------------------------------------------------+
|  [Window: 1280x800]                            |
|  +------------------------------------------+  |
|  | [Export Panel (Top Layout)]              |  |
|  +------------------------------------------+  |
|  | +-----------------+ +------------------+ |  |
|  | | [Control Panel] | | [Visualization]  | |  |
|  | | Width: 360px    | | Area             | |  |
|  | | Fixed           | |                  | |  |
|  | | +-------------+ | |                  | |  |
|  | | | [Scroll]    | | |                  | |  |
|  | | | W: 340px    | | |                  | |  |
|  | | |             | | |                  | |  |
|  | | | +---------+ | | |                  | |  |
|  | | | | Groups  | | |                  | |  |
|  | | | +---------+ | | |                  | |  |
|  | | |             | | |                  | |  |
|  | | | [MetricC] | | |                  | |  |
|  | | | W: 330px  | | |                  | |  |
|  | | | Padding:10| | |                  | |  |
|  | | +---------+ | | |                  | |  |
|  | |-------------| | |                  | |  |
|  | +-----------------+ +------------------+ |  |
|  +------------------------------------------+  |
+------------------------------------------------+
```

---

## 3. MetricCard Internal Wireframe
```text
+---------------------------------------+
| MetricCard (MaxW: 330px)              |
| +-----------------------------------+ |
| | Title: "Final Dimensions" (Small) | |
| |-----------------------------------| |
| | Hero: "10.125" (257mm) x 8.2" "   | |
| | (Bold 18pt-20pt, Word Wrap: ON)   | |
| |-----------------------------------| |
| | [Grid Layout (2x2)]               | |
| | +-----------------+-------------+ | |
| | | Cut: 10" x 8"   | Aper: 9x7   | | |
| | | (Small Label)   |             | | |
| | |-----------------|-------------| | |
| | | Prnt: 7 x 5     | Mat: 1.0"   | | |
| | +-----------------+-------------+ | |
| +-----------------------------------+ |
+---------------------------------------+
```

---

## 4. Implementation Constraints (For Developer)
- **Control Panel (`panel_container`)**: Fixed width **360px**.
- **Scroll Area (`scroll_area`)**: Fixed width **340px**. (Vertical scrollbar ALWAYS visible or gutter reserved).
- **MetricCard**: 
  - `setMinimumWidth(320)`
  - `setMaximumWidth(330)`
  - Header text must use `wordWrap(True)`.
  - Grid cells must have `wordWrap(True)`.
- **Top Export Panel**: 
  - Ensure "FrameTamer Pro" label and "DPI" label have minimum widths to prevent "squeezing" which triggers the validator/truncation.
