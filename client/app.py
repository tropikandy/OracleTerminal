import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QSize, Qt

# CONFIGURATION
# Set the URL of your deployed terminal here.
# Updated for private-only Tailscale access
TERMINAL_URL = "http://100.75.79.110:7681"
APP_TITLE = "Oracle Terminal"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_TITLE)
        self.setMinimumSize(QSize(1024, 768))
        
        # Create WebEngineView
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(TERMINAL_URL))
        
        # Set as central widget
        self.setCentralWidget(self.browser)
        
        # Optional: dark background for a cleaner feel before load
        self.setStyleSheet("background-color: #0f172a;")

def launch_terminal():
    """
    Launches a dedicated window for the terminal application.
    """
    print(f"Launching {APP_TITLE}...")
    print(f"Connecting to: {TERMINAL_URL}")
    print("Ensure you are connected to Tailscale!")
    
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
