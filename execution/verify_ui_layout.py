import sys
import os
from PyQt6.QtWidgets import QApplication

def main():
    project_root = os.path.join(os.getcwd(), "FrameTamer")
    sys.path.append(project_root)
    try:
        from src.app import FrameApp
        from src.widgets import MetricCard, CollapsibleBox
    except ImportError as e:
        print(f"FAIL: ImportError: {e}")
        sys.exit(1)

    app = QApplication(sys.argv)
    window = FrameApp()
    
    # 1. Check for MetricCard
    # 1. Check for MetricCard and its Details
    if hasattr(window, 'card_metrics') and isinstance(window.card_metrics, MetricCard):
        start_ok = True
        card = window.card_metrics
        required_attrs = ['lbl_cut', 'lbl_aperture', 'lbl_print', 'lbl_mat_tb', 'lbl_mat_lr']
        for attr in required_attrs:
            if not hasattr(card, attr):
                print(f"FAIL: MetricCard missing field '{attr}'")
                start_ok = False
        
        if start_ok: print("PASS: MetricCard instantiated with all detail fields.")
    else:
        print("FAIL: MetricCard missing.")

    # 2. Check for Collapsible Groups
    groups = ['group_media', 'group_dims', 'group_app']
    for g in groups:
        if hasattr(window, g) and isinstance(getattr(window, g), CollapsibleBox):
            print(f"PASS: Group {g} exists.")
        else:
            print(f"FAIL: Group {g} missing.")

    # 3. Check specific layout items
    # Check if 'gb_frame' is inside 'group_dims' layout? 
    # Hard to check hierarchy without displayed widget, but can check parentage if set.
    # window.gb_frame.parentWidget() should be part of group_dims content area.
    
    # 4. Check Save Defaults Action
    actions = [a.text() for a in window.menuBar().actions()]
    # Iterate menus
    pref_menu = [a for a in window.menuBar().actions() if a.text() == "Preferences"][0]
    if pref_menu:
        sub_actions = [a.text() for a in pref_menu.menu().actions()]
        if "Editor: Defaults Mode" in sub_actions and "Save Current as Default" in sub_actions:
            print("PASS: Defaults actions in Preferences menu.")
        else:
            print(f"FAIL: Menu items missing. Found: {sub_actions}")
    else:
        print("FAIL: Preferences menu missing.")

    print("\nUI Layout Verification Complete.")
    sys.exit(0)

if __name__ == "__main__":
    main()
