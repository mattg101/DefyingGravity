import os
import time
import subprocess
import pyautogui
from datetime import datetime

def capture_baseline(app_path, output_dir="screenshots"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(output_dir, f"baseline_{timestamp}.png")
    
    # Set environment to include the project root for imports
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.dirname(os.path.abspath(app_path))
    
    print(f"Starting application: {app_path} with PYTHONPATH: {env['PYTHONPATH']}")
    # Run from the project root
    process = subprocess.Popen(["python", app_path], env=env, cwd=os.getcwd())
    
    # Wait for app to load and stabilize
    print("Waiting 10 seconds for app to load...")
    time.sleep(10) 
    
    # VERIFICATION: Check if the window exists
    target_title = "Pro Frame & Mat Studio v14.0"
    windows = pyautogui.getWindowsWithTitle(target_title)
    
    if not windows:
        print(f"ERROR: Application window with title '{target_title}' NOT FOUND.")
        process.terminate()
        return None

    print(f"SUCCESS: Found window '{target_title}'. Taking screenshot...")
    
    print(f"Capturing screenshot: {screenshot_path}")
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    
    # Close the app
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
    print("Application closed.")
    
    return screenshot_path

def compare_images(img1_path, img2_path):
    if not os.path.exists(img1_path) or not os.path.exists(img2_path):
        return None
    
    from PIL import Image, ImageChops
    img1 = Image.open(img1_path).convert('RGB')
    img2 = Image.open(img2_path).convert('RGB')
    
    diff = ImageChops.difference(img1, img2)
    if diff.getbbox():
        diff_path = img2_path.replace(".png", "_diff.png")
        diff.save(diff_path)
        print(f"VISUAL DIFF DETECTED: {diff_path}")
        return diff_path
    else:
        print("No visual changes detected.")
        return None

if __name__ == "__main__":
    # Example usage for FrameTamer
    app_entry = "FrameTamer/frame_app.py"
    if os.path.exists(app_entry):
        path = capture_baseline(app_entry)
        print(f"Baseline captured at: {path}")
    else:
        print(f"Error: {app_entry} not found.")
