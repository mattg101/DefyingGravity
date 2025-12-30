import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGroupBox
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFontMetrics

def validate_widget_rendering(widget, path=""):
    """Recursively check widgets for text truncation."""
    issues = []
    
    # Check text content if applicable
    text = ""
    if isinstance(widget, (QLabel, QPushButton)):
        text = widget.text()
    elif isinstance(widget, QGroupBox):
        text = widget.title()
        
    if text:
        from PyQt6.QtGui import QTextDocument
        
        # Calculate bounding rect of text using QTextDocument for full Rich Text support
        doc = QTextDocument()
        
        # Apply widget font to document
        # Note: default stylesheet of QTextDocument might override unless we set default font
        font = widget.font()
        doc.setDefaultFont(font)
        
        # Handle wrapping
        is_wrapped = False
        if isinstance(widget, QLabel):
            is_wrapped = widget.wordWrap()
            
        if is_wrapped:
            # Set width constraint to widget width
            doc.setTextWidth(widget.width())
            doc.setHtml(text)
            
            # Check if height exceeds widget height
            req_h = doc.size().height()
            avail_h = widget.height()
            padding_h = 4
            
            if req_h > avail_h - padding_h + 2:
                issues.append(f"TRUNCATION RISK (Vertical): '{text[:20]}...' (Req H: {req_h}, Avail H: {avail_h}) in {path}/{type(widget).__name__}")
        else:
            # No wrap: width must fit
            doc.setHtml(text)
            # clone text option to get ideal width
            doc.setTextWidth(-1) 
            
            req_w = doc.idealWidth()
            avail_w = widget.width()
            padding_w = 4
            
            if req_w > avail_w - padding_w + 2:
                 issues.append(f"TRUNCATION RISK (Horizontal): '{text}' (Req W: {req_w}, Avail W: {avail_w}) in {path}/{type(widget).__name__}")
    
    # Check for horizontal scrollbars in scroll areas (indicating overflow)
    from PyQt6.QtWidgets import QScrollArea
    if isinstance(widget, QScrollArea):
        if widget.horizontalScrollBar().isVisible():
            issues.append(f"OVERFLOW DETECTED: Horizontal scrollbar is visible in {path}/{type(widget).__name__}")

    # Recurse
    for child in widget.children():
        if isinstance(child, QWidget) and child.isVisible():
            child_issues = validate_widget_rendering(child, f"{path}/{type(widget).__name__}")
            issues.extend(child_issues)
            
    return issues

def main():
    project_root = os.path.join(os.getcwd(), "FrameTamer")
    sys.path.append(project_root)
    
    try:
        from src.app import FrameApp
    except ImportError as e:
        print(f"ImportError: {e}")
        sys.exit(1)

    app = QApplication(sys.argv)
    window = FrameApp()
    
    # We must show the window to get Geometry
    window.show()
    
    # Process events to allow layout to settle
    app.processEvents()
    
    # Force a resize to simulate typical usage if needed, or stick to default 1280x800
    window.resize(1280, 800)
    app.processEvents()
    
    print("Running Rendering Validation...")
    issues = validate_widget_rendering(window, "Main Window")
    
    if issues:
        print("\nFOUND RENDERING ISSUES:")
        for i in issues:
            print(f" - {i}")
        print("\nFAIL: Potential visual regressions detected.")
        sys.exit(1)
    else:
        print("\nPASS: No obvious text truncation detected.")
        sys.exit(0)

if __name__ == "__main__":
    main()
