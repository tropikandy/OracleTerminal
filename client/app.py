import webview
import sys
import os

# CONFIGURATION
# Set the URL of your deployed terminal here.
TERMINAL_URL = "https://terminal-app.suras.org"
APP_TITLE = "Oracle Terminal"

def launch_terminal():
    """
    Launches a dedicated window for the terminal application.
    """
    print(f"Launching {APP_TITLE}...")
    print(f"Connecting to: {TERMINAL_URL}")
    
    # Create a window
    # width=1024, height=768 is a good default for terminals
    window = webview.create_window(
        APP_TITLE,
        TERMINAL_URL,
        width=1024,
        height=768,
        resizable=True,
        confirm_close=True,
        background_color='#0f172a' # Dark background to match terminal
    )
    
    # Start the GUI loop
    webview.start()

if __name__ == '__main__':
    try:
        launch_terminal()
    except Exception as e:
        print(f"Error launching application: {e}")
        input("Press Enter to exit...")
