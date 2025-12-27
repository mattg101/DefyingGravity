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
    
    def step1_trigger_grid():
        print("Triggering grid via rotation...")
        dialog.slider_rot.setValue(200) # 20 deg
        
        # Immediately capture (Grid should be visible)
        print("Capturing active grid (10x10)...")
        dialog.grab().save(os.path.join("screenshots", "texture_refinement_active_grid.png"))
        
        # Schedule step 2 after 1 second (longer than 500ms timeout)
        QTimer.singleShot(1000, step2_verify_hide)

    def step2_verify_hide():
        print("Capturing inactive grid (expecting auto-hide)...")
        dialog.grab().save(os.path.join("screenshots", "texture_refinement_hidden_grid.png"))
        print("Verification complete.")
        dialog.close()
        app.quit()

    QTimer.singleShot(1000, step1_trigger_grid)
    sys.exit(app.exec())

if __name__ == "__main__":
    if not os.path.exists("screenshots"): os.makedirs("screenshots")
    main()
