import sys
import os
import time
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer, QPoint, Qt, QRectF
from PyQt6.QtTest import QTest

def main():
    # Setup environment
    project_root = os.path.join(os.getcwd(), "FrameTamer")
    sys.path.append(project_root)
    try:
        from src.dialogs import TextureSamplerDialog
    except ImportError:
        print("Error: Could not import TextureSamplerDialog.")
        return

    app = QApplication(sys.argv)
    dialog = TextureSamplerDialog()
    
    # Init state
    dialog.selection_norm = QRectF(0.4, 0.4, 0.2, 0.2)
    dialog.show()
    
    def run_qtest():
        try:
            # 1. HORIZONTAL TEST (Drag TOP RIGHT handle )
            # We need to find the handle screen pos
            img_rect, scale = dialog.get_transforms()
            sx = img_rect.x() + dialog.selection_norm.x() * img_rect.width()
            sy = img_rect.y() + dialog.selection_norm.y() * img_rect.height()
            sw = dialog.selection_norm.width() * img_rect.width()
            sh = dialog.selection_norm.height() * img_rect.height()
            
            tr_handle = QPoint(int(sx + sw), int(sy))
            
            print(f"QTesting: Dragging Top-Right from {tr_handle} to the right...")
            QTest.mousePress(dialog.lbl_preview, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier, tr_handle)
            # Drag 300px right
            for i in range(1, 11):
                move_pt = tr_handle + QPoint(i * 30, 0)
                QTest.mouseMove(dialog.lbl_preview, move_pt)
                time.sleep(0.01)
            QTest.mouseRelease(dialog.lbl_preview, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier, move_pt)
            
            time.sleep(0.5)
            dialog.grab().save(os.path.join("screenshots", "texture_qtest_h.png"))
            
            # 2. VERTICAL TEST (Drag BOTTOM LEFT handle down)
            img_rect, scale = dialog.get_transforms()
            sx = img_rect.x() + dialog.selection_norm.x() * img_rect.width()
            sy = img_rect.y() + dialog.selection_norm.y() * img_rect.height()
            sw = dialog.selection_norm.width() * img_rect.width()
            sh = dialog.selection_norm.height() * img_rect.height()
            
            bl_handle = QPoint(int(sx), int(sy + sh))
            
            print(f"QTesting: Dragging Bottom-Left from {bl_handle} down...")
            QTest.mousePress(dialog.lbl_preview, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier, bl_handle)
            # Drag 400px down
            for i in range(1, 11):
                move_pt = bl_handle + QPoint(0, i * 40)
                QTest.mouseMove(dialog.lbl_preview, move_pt)
                time.sleep(0.01)
            QTest.mouseRelease(dialog.lbl_preview, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier, move_pt)
            
            time.sleep(0.5)
            dialog.grab().save(os.path.join("screenshots", "texture_qtest_v.png"))

            # 3. PANNING TEST (Shift + Right Drag center)
            img_rect, scale = dialog.get_transforms()
            center = QPoint(int(img_rect.center().x()), int(img_rect.center().y()))
            
            print(f"QTesting: Panning Selection from {center}...")
            QTest.mousePress(dialog.lbl_preview, Qt.MouseButton.RightButton, Qt.KeyboardModifier.ShiftModifier, center)
            for i in range(1, 11):
                move_pt = center + QPoint(i * 20, 0)
                QTest.mouseMove(dialog.lbl_preview, move_pt)
                time.sleep(0.01)
            QTest.mouseRelease(dialog.lbl_preview, Qt.MouseButton.RightButton, Qt.KeyboardModifier.ShiftModifier, move_pt)
            
            time.sleep(0.5)
            dialog.grab().save(os.path.join("screenshots", "texture_qtest_p.png"))
            
            print("QTests complete.")
            
        except Exception as e:
            print(f"QTest Error: {e}")
        finally:
            dialog.close()
            app.quit()

    QTimer.singleShot(1000, run_qtest)
    sys.exit(app.exec())

if __name__ == "__main__":
    if not os.path.exists("screenshots"): os.makedirs("screenshots")
    main()
