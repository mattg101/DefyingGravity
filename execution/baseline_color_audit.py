import sys
import os
import time
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QColor

# Add FrameTamer dir to path to import src.app
sys.path.append(os.path.join(os.getcwd(), 'FrameTamer'))
from src.app import FrameApp

def audit_color_baseline():
    app = QApplication(sys.argv)
    window = FrameApp()
    window.show()
    
    # Ensure screenshots dir exists
    os.makedirs('screenshots', exist_ok=True)
    ts = time.strftime("%Y%m%d_%H%M%S")
    
    def do_audit():
        print("Auditing Baseline Color UI...")
        try:
            # 1. Capture Appearance Group (where the buttons are)
            window.group_app.grab().save(f'screenshots/color_audit_appearance_{ts}.png')
            print(f"Captured: screenshots/color_audit_appearance_{ts}.png")

            # 2. Capture Full Window
            window.grab().save(f'screenshots/color_audit_main_{ts}.png')
            print(f"Captured: screenshots/color_audit_main_{ts}.png")
            
        except Exception as e:
            print(f"Audit failed: {e}")
            
        print("Baseline audit complete.")
        window.close()
        app.quit()

    QTimer.singleShot(1000, do_audit)
    sys.exit(app.exec())

if __name__ == "__main__":
    audit_color_baseline()
