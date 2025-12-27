import sys
import os
import time
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer, QPoint, Qt, QRectF
from PyQt6.QtTest import QTest
from PyQt6.QtGui import QPixmap

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
    
    # Init state with a known vertical selection
    dialog.selection_norm = QRectF(0.4, 0.2, 0.1, 0.6) # Very vertical
    dialog.show()
    
    def run_verification():
        try:
            time.sleep(1)
            # 1. Capture Grid and Selection (Sky Blue)
            img_rect, scale = dialog.get_transforms()
            dialog.grab().save(os.path.join("screenshots", "texture_refinement_grid_v.png"))
            print("Captured Grid and Vertical Selection.")

            # 2. Verify Rotation in get_texture()
            crop_pix = dialog.get_texture()
            if crop_pix:
                print(f"Crop dimensions: {crop_pix.width()}x{crop_pix.height()}")
                if crop_pix.width() > crop_pix.height():
                    print("SUCCESS: Vertical crop was successfully rotated to horizontal.")
                    crop_pix.save(os.path.join("screenshots", "texture_rotated_output.png"))
                else:
                    print("FAILURE: Vertical crop was NOT rotated.")
            else:
                print("FAILURE: Could not extract texture.")

            # 3. Straighten slightly and capture grid again
            dialog.slider_rot.setValue(100) # 10 deg
            time.sleep(0.5)
            dialog.grab().save(os.path.join("screenshots", "texture_straighten_grid.png"))
            print("Captured Straighten Grid.")
            
        except Exception as e:
            print(f"Verification Error: {e}")
        finally:
            dialog.close()
            app.quit()

    QTimer.singleShot(1000, run_verification)
    sys.exit(app.exec())

if __name__ == "__main__":
    if not os.path.exists("screenshots"): os.makedirs("screenshots")
    main()
