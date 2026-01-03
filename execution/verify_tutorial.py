import os
import time
import subprocess
import pyautogui

def verify_tutorial():
    app_path = "FrameTamer/frame_app.py"
    env = os.environ.copy()
    env["PYTHONPATH"] = os.getcwd() + ";" + os.path.join(os.getcwd(), "FrameTamer")
    
    print("Launching app for tutorial verification...")
    process = subprocess.Popen(["python", app_path], env=env, cwd=os.getcwd())
    
    time.sleep(10)
    
    # Check for Tutorial Window
    target_title = "Welcome to FrameTamer"
    windows = pyautogui.getWindowsWithTitle(target_title)
    
    success = False
    if windows:
        print(f"SUCCESS: Tutorial window '{target_title}' detected!")
        # Screenshot it
        os.makedirs("screenshots", exist_ok=True)
        pyautogui.screenshot("screenshots/tutorial_verification.png")
        print("Captured: screenshots/tutorial_verification.png")
        success = True
    else:
        print(f"FAILURE: Tutorial window '{target_title}' NOT FOUND.")
        # Also check if main window is there but tutorial isn't
        main_windows = pyautogui.getWindowsWithTitle("Pro Frame & Mat Studio v14.0")
        if main_windows:
            print("Main window found, but tutorial was skipped or blocked.")
    
    process.terminate()
    try:
        process.wait(timeout=5)
    except:
        process.kill()
        
    return success

if __name__ == "__main__":
    if verify_tutorial():
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")
        exit(1)
