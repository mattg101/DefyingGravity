import sys
import os
import time
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QScreen

# Add FrameTamer dir to path to import src.app
sys.path.append(os.path.join(os.getcwd(), 'FrameTamer'))
from src.app import FrameApp

def capture_regional_assets():
    # Disable tutorial for capture
    from PyQt6.QtCore import QSettings
    settings = QSettings("MattG", "FrameTamer")
    settings.setValue("startup/show_tutorial", False)
    
    app = QApplication(sys.argv)
    window = FrameApp()
    window.show()
    
    # Ensure screenshots dir exists
    os.makedirs('docs/wiki/images', exist_ok=True)
    
    def do_capture():
        print("Capturing Tutorial & Wiki Assets...")
        
        # 1. Capture Tutorial Step Images
        try:
            # Step 1: Welcome (Full Window or Editor?)
            # Let's do the full window for the welcome
            window.grab().save('docs/wiki/images/step_1_welcome.png')
            print("Captured: step_1_welcome.png")

            # Step 2: Load Your Media
            window.group_media.grab().save('docs/wiki/images/step_2_media.png')
            print("Captured: step_2_media.png")

            # Step 3: Define Dimensions (Focus on Aperture/Profile)
            window.group_dims.grab().save('docs/wiki/images/step_3_dimensions.png')
            print("Captured: step_3_dimensions.png")

            # Step 4: Master Matting
            window.gb_mat_rules.grab().save('docs/wiki/images/step_4_matting.png')
            print("Captured: step_4_matting.png")

            # Step 5: Visual Polish
            window.group_app.grab().save('docs/wiki/images/step_5_appearance.png')
            print("Captured: step_5_appearance.png")

            # Step 6: Real-time Results
            window.card_metrics.grab().save('docs/wiki/images/step_6_metrics.png')
            print("Captured: step_6_metrics.png")

            # Also keep the generic ones for wiki
            window.card_metrics.grab().save('docs/wiki/images/wiki_metric_card.png')
            window.group_media.parentWidget().grab().save('docs/wiki/images/wiki_sidebar.png') # Capture the scroll content
            
        except Exception as e:
            print(f"Capture failed: {e}")
            import traceback
            traceback.print_exc()
            
        print("Asset capture complete.")
        window.close()
        app.quit()

    QTimer.singleShot(2000, do_capture)
    sys.exit(app.exec())

if __name__ == "__main__":
    capture_regional_assets()
