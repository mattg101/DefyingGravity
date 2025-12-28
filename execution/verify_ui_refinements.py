import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt

def main():
    project_root = os.path.join(os.getcwd(), "FrameTamer")
    sys.path.append(project_root)
    try:
        from src.app import FrameApp
    except ImportError:
        print("Error: Could not import FrameApp.")
        return

    app = QApplication(sys.argv)
    window = FrameApp()

    # TEST 1: Check Default Increment (Imperial)
    print("\n--- TEST 1: Default Increment (Imperial) ---")
    spinboxes = window.unit_inputs
    if not spinboxes:
        print("FAIL: No spinboxes found.")
        sys.exit(1)
    
    # Verify default is 0.125
    s = spinboxes[0]
    if abs(s.singleStep() - 0.125) < 0.0001:
        print(f"PASS: Spinbox increment is {s.singleStep()}")
    else:
        print(f"FAIL: Spinbox increment is {s.singleStep()}, expected 0.125")

    # TEST 2: Check Metric Switch
    print("\n--- TEST 2: Metric Switch ---")
    window.rb_met.setChecked(True)
    # Unit logic runs via signal; force update if needed (toggled calls toggle_units)
    
    s = spinboxes[0]
    if abs(s.singleStep() - 2.0) < 0.0001:
        print(f"PASS: Metric increment is {s.singleStep()}")
    else:
        print(f"FAIL: Metric increment is {s.singleStep()}, expected 2.0")

    # TEST 3: Mat Stats Display
    print("\n--- TEST 3: Mat Stats Display ---")
    window.recalc()
    stats_text = window.lbl_stats.text()
    if "MAT BORDERS" in stats_text:
        print("PASS: 'MAT BORDERS' found in stats label.")
        if "T: " in stats_text and "B: " in stats_text:
             print("PASS: Top/Bottom labels found.")
    else:
        print("FAIL: 'MAT BORDERS' not found in stats label.")
        print(f"Content: {stats_text}")

    sys.exit(0)

if __name__ == "__main__":
    main()
