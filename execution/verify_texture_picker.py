import sys
import os
import time
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer, QPoint, Qt, QRectF
from PyQt6.QtTest import QTest

def main():
    # Setup environment
    project_root = os.path.join(os.getcwd(), "FrameTamer")
    sys.path.append(project_root)
    try:
        from src.dialogs import TextureSamplerDialog
    except ImportError:
        print("Error: Could not import TextureSamplerDialog.")
        return

    app = QApplication(sys.argv)
    dialog = TextureSamplerDialog()
    dialog.show()
    
    def step1_verify_no_initial_flash():
        # This capture happens roughly 1s after show(), which is after load_default_texture
        # but before any manual interaction.
        print("Capturing initial load state (expecting NO grid)...")
        dialog.grab().save(os.path.join("screenshots", "texture_final_initial_load.png"))
        
        QTimer.singleShot(500, step2_trigger_grid_1x)

    def step2_trigger_grid_1x():
        print("Triggering grid and capturing at 1.0x zoom...")
        dialog.slider_rot.setValue(100) # 10 deg
        dialog.grab().save(os.path.join("screenshots", "texture_final_grid_1x.png"))
        
        QTimer.singleShot(200, step3_zoom_and_capture)

    def step3_zoom_and_capture():
        print("Zooming to 2.5x and capturing (expecting fixed grid spacing)...")
        dialog.zoom = 2.5
        dialog.update_display()
        dialog.grab().save(os.path.join("screenshots", "texture_final_grid_2.5x.png"))
        
        QTimer.singleShot(1000, step4_verify_hide)

    def step4_verify_hide():
        print("Capturing state after 500ms timeout (expecting NO grid)...")
        dialog.grab().save(os.path.join("screenshots", "texture_final_grid_hidden.png"))
        print("Verification complete.")
        dialog.close()
        app.quit()

    QTimer.singleShot(1000, step1_verify_no_initial_flash)
    sys.exit(app.exec())

if __name__ == "__main__":
    if not os.path.exists("screenshots"): os.makedirs("screenshots")
    main()
