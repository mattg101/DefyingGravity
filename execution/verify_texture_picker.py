import sys
import os
import time
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer, QRectF
from PyQt6.QtGui import QPixmap
import pyautogui

def main():
    # Setup environment
    project_root = os.path.join(os.getcwd(), "FrameTamer")
    sys.path.append(project_root)
    from src.dialogs import TextureSamplerDialog
    
    app = QApplication(sys.argv)
    dialog = TextureSamplerDialog()
    
    # Load the default image
    default_img = os.path.join(os.getcwd(), "rick_default.png")
    if os.path.exists(default_img):
        dialog.pixmap_orig = QPixmap(default_img)
        dialog.pixmap_rotated = dialog.pixmap_orig # No rotation for test
        dialog.update_display()
    
    # 1. Capture Horizontal Selection (Green)
    dialog.selection_norm = QRectF(0.2, 0.4, 0.6, 0.2) # 3:1 ratio
    dialog.update_display()
    
    def capture_h():
        time.sleep(1)
        pyautogui.screenshot().save(os.path.join("screenshots", "texture_picker_h_verify.png"))
        print("Captured Horizontal Selection")
        
        # 2. Capture Vertical Selection (Blue)
        dialog.selection_norm = QRectF(0.4, 0.2, 0.2, 0.6) # 1:3 ratio
        dialog.update_display()
        QTimer.singleShot(1000, capture_v)

    def capture_v():
        time.sleep(1)
        pyautogui.screenshot().save(os.path.join("screenshots", "texture_picker_v_verify.png"))
        print("Captured Vertical Selection")
        dialog.close()
        app.quit()

    QTimer.singleShot(2000, capture_h)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
