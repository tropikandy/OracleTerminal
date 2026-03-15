import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QSize

# CONFIGURATION
# Laptop uses the standard 14px port (7681)
TERMINAL_URL = "http://100.75.79.110:7681"
APP_TITLE = "Oracle Terminal"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_TITLE)
        self.setMinimumSize(QSize(1024, 768))
        
        self.browser = QWebEngineView()
        # Back to standard 1.0 zoom for the "perfect" laptop look
        self.browser.setZoomFactor(1.0)
        self.browser.setUrl(QUrl(TERMINAL_URL))
        
        self.setCentralWidget(self.browser)
        self.setStyleSheet("background-color: #0f172a;")

def launch_terminal():
    print(f"Launching {APP_TITLE} (Laptop Profile)...")
    print(f"Connecting to: {TERMINAL_URL}")
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    try:
        launch_terminal()
    except Exception as e:
        print(f"Error launching application: {e}")
        input("Press Enter to exit...")
