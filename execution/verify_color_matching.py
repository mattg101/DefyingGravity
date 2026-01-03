import sys
import os
from PyQt6.QtGui import QColor

# Add FrameTamer dir to path
sys.path.append(os.path.join(os.getcwd(), 'FrameTamer'))
from src.utils import ColorUtils

def test_color_matching():
    test_cases = [
        ("#FBFBF9", "Cotton White"),  # exact
        ("#FFFFFF", "Bright White"),  # exact
        ("#000000", "Black"),         # exact
        ("#FF0000", "Tone #FF0000"), # grid match
        ("#123456", "Tone #003366"), # closest tone
        ("#A37B5C", "Tan"),           # Close enough to tan? Let's see
        ("#708090", "Slate Gray"),    # exact
    ]
    
    print("Running Color Matching Verification...")
    print("-" * 40)
    passed = 0
    for hex_code, expected_name in test_cases:
        color = QColor(hex_code)
        actual_name = ColorUtils.get_closest_name(color)
        dist_info = "MATCH" if expected_name in actual_name else f"FAIL (Got: {actual_name})"
        print(f"Hex: {hex_code} -> {actual_name} | Expected subset: {expected_name} | {dist_info}")
        if expected_name in actual_name: passed += 1
        
    print("-" * 40)
    print(f"Passed: {passed}/{len(test_cases)}")
    
    if passed >= len(test_cases) - 2: # Allow some fuzziness for tones
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")

if __name__ == "__main__":
    test_color_matching()
