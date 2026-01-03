import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QColor, QPixmap

# Add FrameTamer dir to path
sys.path.append(os.path.join(os.getcwd(), 'FrameTamer'))
from src.constants import DEFAULT_FRAME_COLOR, DEFAULT_TEXTURE_PATH
from src.utils import ColorUtils

def diag():
    app = QApplication(sys.argv)
    print(f"CWD: {os.getcwd()}")
    print(f"DEFAULT_FRAME_COLOR: {DEFAULT_FRAME_COLOR.name()}")
    print(f"Matched Name: {ColorUtils.get_closest_name(DEFAULT_FRAME_COLOR)}")
    
    print(f"DEFAULT_TEXTURE_PATH: {DEFAULT_TEXTURE_PATH}")
    print(f"Exists? {os.path.exists(DEFAULT_TEXTURE_PATH)}")
    
    # Try looking in FrameTamer/
    alt_path = os.path.join("FrameTamer", DEFAULT_TEXTURE_PATH)
    print(f"Alt Path: {alt_path}")
    print(f"Exists? {os.path.exists(alt_path)}")

if __name__ == "__main__":
    diag()
