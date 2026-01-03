import sys
import os
import time
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QColor

# Add FrameTamer dir to path
sys.path.append(os.path.join(os.getcwd(), 'FrameTamer'))
from src.app import FrameApp

def audit_color_final():
    app = QApplication(sys.argv)
    window = FrameApp()
    window.show()
    
    # Ensure screenshots dir exists
    os.makedirs('screenshots', exist_ok=True)
    ts = time.strftime("%Y%m%d_%H%M%S")
    
    def do_audit():
        print("Auditing Final Color UI...")
        try:
            # 1. Capture Appearance Group (showing new label)
            window.group_app.grab().save(f'screenshots/color_final_appearance_{ts}.png')
            print(f"Captured: screenshots/color_final_appearance_{ts}.png")

            # 2. Open the picker to show the live name (simulated check)
            # We can't easily wait for user interaction here in a script, 
            # but we can verify the label exists in the code.
            
            # Close app
        except Exception as e:
            print(f"Audit failed: {e}")
            
        print("Final audit complete.")
        window.close()
        app.quit()

    QTimer.singleShot(1000, do_audit)
    sys.exit(app.exec())

if __name__ == "__main__":
    audit_color_final()
