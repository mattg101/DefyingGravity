import sys
import os
import json
import shutil
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt, QRectF

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

    print("\n--- TEST: Project Save/Load Roundtrip ---")
    
    from PyQt6.QtGui import QColor
    window.spin_iw.setValue(10.5)
    window.spin_face.setValue(2.0)
    window.mat_color = QColor(Qt.GlobalColor.red)
    
    # Toggle Mode via Action
    window.act_mode_art.setChecked(True)
    window.act_mode_art.triggered.emit(True) # Force trigger logic if needed, but setChecked + recalc should be enough?
    # Logic is triggered by signal. Emitting it is safer.
    
    # 2. Save
    test_file = os.path.join(os.getcwd(), "test_project.frame")
    window.current_project_path = test_file
    # Mocking QFileDialog not needed if we call _do_save directly or set path first
    window._do_save(test_file)
    
    if not os.path.exists(test_file):
        print("FAIL: Project file not created.")
        sys.exit(1)
        
    print(f"PASS: Saved project to {test_file}")
    
    # 3. New Project (Reset)
    window.new_project()
    if window.spin_iw.value() != 16.0:
        print("FAIL: New Project did not reset Aperture Width.")
    else:
        print("PASS: New Project reset successful.")
        
    # 4. Load Project
    window.load_project(test_file)
    
    # 5. Verify
    if abs(window.spin_iw.value() - 10.5) < 0.001:
        print("PASS: Aperture Width restored.")
    else:
        print(f"FAIL: Aperture Width mismatch. Got {window.spin_iw.value()}, expected 10.5")
        
    if window.spin_face.value() == 2.0:
        print("PASS: Frame Face restored.")
        
    if window.act_mode_art.isChecked():
        print("PASS: Workflow Mode restored (Fixed Art).")
    else:
        print("FAIL: Workflow Mode not restored.")

    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)

    sys.exit(0)

if __name__ == "__main__":
    main()
