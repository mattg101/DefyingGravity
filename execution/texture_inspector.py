import sys
import os
import json
from PyQt6.QtWidgets import QApplication, QWidget
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
    # Append the repository root to sys.path
    project_root = os.path.join(os.getcwd(), "FrameTamer")
    sys.path.append(project_root)
    from src.dialogs import TextureSamplerDialog
    
    app = QApplication(sys.argv)
    dialog = TextureSamplerDialog()
    dialog.show()
    
    def inspect():
        tree = get_widget_tree(dialog)
        output_path = os.path.join("orchestration", "texture_widget_hierarchy.json")
        with open(output_path, "w") as f:
            json.dump(tree, f, indent=4)
        print(f"Texture Widget hierarchy saved to {output_path}")
        dialog.close()
        app.quit()

    QTimer.singleShot(1000, inspect)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
