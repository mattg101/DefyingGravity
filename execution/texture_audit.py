import os
import time
import subprocess
import pyautogui
from datetime import datetime

def run_texture_audit(app_path):
    output_dir = "screenshots"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Set environment
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.dirname(os.path.abspath(app_path))
    
    print(f"Starting application for Texture Audit: {app_path}")
    process = subprocess.Popen(["python", app_path], env=env, cwd=os.getcwd())
    
    # Wait for app
    time.sleep(8)
    
    try:
        # 1. Capture Main Window
        main_shot = os.path.join(output_dir, f"texture_audit_main_{timestamp}.png")
        pyautogui.screenshot().save(main_shot)
        print(f"Main window captured: {main_shot}")
        
        # 2. Click "Extract Texture" button
        # Based on app.py analysis, this button is in h_tex layout
        # We'll try to find it by text if possible, or just click near the bottom left
        # Let's use pyautogui to find the button or just click a coordinate
        # For robustness, let's try to find the window and click relative.
        target_title = "Pro Frame & Mat Studio v14.0"
        win = pyautogui.getWindowsWithTitle(target_title)
        if win:
            w = win[0]
            w.activate()
            # "Extract Texture" is usually near the bottom of the left panel
            # Approximating: 15% from left, 85% from top
            click_x = w.left + (w.width * 0.15)
            click_y = w.top + (w.height * 0.85)
            pyautogui.click(click_x, click_y)
            print(f"Clicked 'Extract Texture' at {click_x}, {click_y}")
            
            time.sleep(3)
            
            # 3. Capture Texture Dialog
            dialog_shot = os.path.join(output_dir, f"texture_audit_dialog_{timestamp}.png")
            pyautogui.screenshot().save(dialog_shot)
            print(f"Texture dialog captured: {dialog_shot}")
            
            # 4. (Optional) Load an image if we want to see selection box
            # This might be too complex for a blind audit, but let's try to just capture the UI first.
        else:
            print("Could not find main window.")
            
    except Exception as e:
        print(f"Audit Error: {e}")
    finally:
        process.terminate()
        process.wait()

if __name__ == "__main__":
    run_texture_audit("FrameTamer/frame_app.py")
