import sys
import os
import time
from PyQt6.QtWidgets import QApplication, QColorDialog, QLabel
from PyQt6.QtCore import QTimer, Qt, QPoint
from PyQt6.QtGui import QColor

# Add FrameTamer dir to path
sys.path.append(os.path.join(os.getcwd(), 'FrameTamer'))
from src.app import FrameApp
from src.dialogs import ProfessionalColorPickerDialog

def deep_color_audit():
    app = QApplication(sys.argv)
    window = FrameApp()
    window.show()
    
    os.makedirs('screenshots', exist_ok=True)
    ts = time.strftime("%Y%m%d_%H%M%S")
    
    def do_deep_audit():
        print("Starting Deep Interactive Audit...")
        try:
            # 1. Force expand ALL sections
            for box in [window.group_media, window.group_dims, window.group_app]:
                box.toggle_button.setChecked(False) # set to false so on_pressed(True)
                box.on_pressed() 
            
            # Force layout update
            window.adjustSize()
            QApplication.processEvents()
            print(f"Appearance size (after force): {window.group_app.size()}")
            QTimer.singleShot(1500, lambda: capture_step_1(window, ts))
        except Exception as e:
            print(f"Deep Audit failed at step 0: {e}")
            app.quit()

    def capture_step_1(window, ts):
        print("Step 1: Capturing full window with expanded panels...")
        window.grab().save(f'screenshots/dual_audit_1_full_{ts}.png')
        window.group_app.grab().save(f'screenshots/dual_audit_1_appearance_{ts}.png')
        
        # Step 2: Open Mat Color Picker
        print("Step 2: Opening Mat Color Picker...")
        QTimer.singleShot(1000, lambda: capture_step_2_picker(ts, "Mat Color"))
        window.pick_mat()

    def capture_step_2_picker(ts, context):
        print(f"Step 2 (Capture): Searching for open ProfessionalColorPickerDialog ({context})...")
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, ProfessionalColorPickerDialog):
                print(f"Found ProfessionalColorPickerDialog for {context}. Capturing...")
                widget.grab().save(f'screenshots/dual_audit_2_picker_{context}_{ts}.png')
                
                # Verify prefix
                found_prefix = False
                for label in widget.findChildren(QLabel):
                    if context.upper() in label.text():
                        found_prefix = True
                        print(f"Verification: Found '{context.upper()}' prefix in picker!")
                        break
                
                if context == "Mat Color":
                    widget.setCurrentColor(QColor("#708090")) # Slate Gray
                    print(f"Set Mat Color to: {widget.currentColor().name()}")
                    QTimer.singleShot(500, lambda w=widget: capture_step_3_frame(w, ts))
                else:
                    widget.setCurrentColor(QColor("#8B0000")) # Deep Red
                    print(f"Set Frame Color to: {widget.currentColor().name()}")
                    QTimer.singleShot(500, lambda w=widget: capture_step_4_final_check(w, ts))
                return
        print(f"Dialog for {context} not found!")

    def capture_step_3_frame(widget, ts):
        widget.accept()
        print("Step 3: Opening Frame Color Picker...")
        QTimer.singleShot(1000, lambda: capture_step_2_picker(ts, "Frame Color"))
        window.pick_frame()

    def capture_step_4_final_check(widget, ts):
        widget.accept()
        print("Step 4: Final verification of dual labels...")
        window.group_app.grab().save(f'screenshots/dual_audit_4_final_{ts}.png')
        
        # Check label text (simple print for log verification)
        print(f"Mat Label: {window.lbl_mat_color_name.text()}")
        print(f"Frame Label: {window.lbl_frame_color_name.text()}")
        
        print("Deep Audit Complete.")
        window.close()
        app.quit()

    QTimer.singleShot(1000, do_deep_audit)
    sys.exit(app.exec())

if __name__ == "__main__":
    deep_color_audit()
