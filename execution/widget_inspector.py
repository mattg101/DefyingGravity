import sys
import os
import json
import time
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtCore import QTimer

def get_widget_tree(obj, depth=0):
    widget_info = {
        "name": obj.objectName() or "unnamed",
        "class": obj.__class__.__name__,
        "visible": obj.isVisible() if hasattr(obj, 'isVisible') else True,
        "geometry": f"{obj.geometry().x()},{obj.geometry().y()} {obj.geometry().width()}x{obj.geometry().height()}" if hasattr(obj, 'geometry') else "N/A",
        "children": []
    }
    
    for child in obj.children():
        if isinstance(child, QWidget):
            widget_info["children"].append(get_widget_tree(child, depth + 1))
            
    return widget_info

def main():
    # We need to launch the app in a way that we can inspect it.
    # Simple approach: Import the app and run it in this process.
    
    sys.path.append(os.path.join(os.getcwd(), "FrameTamer"))
    from FrameTamer.src.app import FrameApp
    
    app = QApplication(sys.argv)
    window = FrameApp()
    window.show()
    
    # Wait a moment for layout to settle
    def inspect():
        tree = get_widget_tree(window)
        output_path = os.path.join("orchestration", "widget_hierarchy.json")
        with open(output_path, "w") as f:
            json.dump(tree, f, indent=4)
        print(f"Widget hierarchy saved to {output_path}")
        window.close()
        app.quit()

    QTimer.singleShot(2000, inspect)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
