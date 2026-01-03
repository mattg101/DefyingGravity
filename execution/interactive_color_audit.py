import sys
import os
import time
from PyQt6.QtWidgets import QApplication, QColorDialog
from PyQt6.QtCore import QTimer, Qt, QPoint
from PyQt6.QtGui import QColor

# Add FrameTamer dir to path
sys.path.append(os.path.join(os.getcwd(), 'FrameTamer'))
from src.app import FrameApp
from src.dialogs import MatColorPickerDialog

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
        window.grab().save(f'screenshots/deep_audit_1_full_{ts}.png')
        window.group_app.grab().save(f'screenshots/deep_audit_1_appearance_{ts}.png')
        
        # Step 2: Open Mat Color Picker
        print("Step 2: Opening Mat Color Picker...")
        # Since exec() blocks, we need a timer to capture the dialog
        QTimer.singleShot(1000, lambda: capture_step_2_picker(ts))
        
        # We simulate the button click
        window.pick_mat() # This will open the dialog

    def capture_step_2_picker(ts):
        print("Step 2 (Capture): Searching for open MatColorPickerDialog...")
        # Find the active dialog
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, MatColorPickerDialog):
                print("Found MatColorPickerDialog. Capturing...")
                widget.grab().save(f'screenshots/deep_audit_2_picker_initial_{ts}.png')
                
                # Step 3: Change color and verify live name update
                print("Step 3: Simulating color change in picker...")
                widget.setCurrentColor(QColor("#708090")) # Slate Gray
                
                # Wait for label update
                QTimer.singleShot(500, lambda w=widget: capture_step_3_updated(w, ts))
                return
        print("Dialog not found!")
        app.quit()

    def capture_step_3_updated(widget, ts):
        print("Step 3 (Capture): Verifying matched name in picker...")
        widget.grab().save(f'screenshots/deep_audit_3_picker_updated_{ts}.png')
        
        # Step 4: Accept and check main UI
        print("Step 4: Accepting picker and checking main UI...")
        widget.accept()
        
        QTimer.singleShot(500, lambda: capture_step_4_final(window, ts))

    def capture_step_4_final(window, ts):
        print("Step 4 (Capture): Verifying main UI label...")
        window.group_app.grab().save(f'screenshots/deep_audit_4_main_ui_updated_{ts}.png')
        
        print("Deep Audit Complete. Evidence captured in screenshots/deep_audit_*")
        window.close()
        app.quit()

    QTimer.singleShot(1000, do_deep_audit)
    sys.exit(app.exec())

if __name__ == "__main__":
    deep_color_audit()
