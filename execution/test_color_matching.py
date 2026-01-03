import sys
import os
import math
from PyQt6.QtGui import QColor

# Add FrameTamer dir to path
sys.path.append(os.path.join(os.getcwd(), 'FrameTamer'))
from src.utils import ColorUtils
from src.colors import COLORS

def test():
    # Test Slate Gray
    c = QColor("#708090")
    print(f"Testing #708090 (Slate Gray): RGB({c.red()}, {c.green()}, {c.blue()})")
    name = ColorUtils.get_closest_name(c)
    print(f"Matched Name: {name}")
    
    # Test Deep Red
    c2 = QColor("#8B0000")
    print(f"Testing #8B0000 (Deep Red): RGB({c2.red()}, {c2.green()}, {c2.blue()})")
    name2 = ColorUtils.get_closest_name(c2)
    print(f"Matched Name: {name2}")

    # Check if Slate Gray is in COLORS
    print(f"Is 'Slate Gray' in COLORS? {'Slate Gray' in COLORS}")
    if 'Slate Gray' in COLORS:
        print(f"Slate Gray Value: {COLORS['Slate Gray']}")

if __name__ == "__main__":
    test()
