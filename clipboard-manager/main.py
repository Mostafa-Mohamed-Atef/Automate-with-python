import pyperclip
import keyboard
import time
import json
import threading

class ClipboardManager:
    def __init__(self):
        self.history = []
        self.load_history()

    def copy(self, text):
        pyperclip.copy(text)
        self.history.append(text)
        self.save_history()

    def paste(self):
        return pyperclip.paste()

    def save_history(self):
        with open('clipboard_history.json', 'w') as f:
            json.dump(self.history, f)

    def load_history(self):
        try:
            with open('clipboard_history.json', 'r') as f:
                self.history = json.load(f)
        except FileNotFoundError:
            self.history = []

    def clear_history(self):
        self.history = []
        self.save_history()

    def monitor_clipboard(self):
        prev_content = ''
        while True:
            time.sleep(0.5)
            current_content = pyperclip.paste()
            if current_content != prev_content:
                self.copy(current_content)
                prev_content = current_content

def main():
    clipboard_manager = ClipboardManager()
    
    # Example: Set up a hotkey to clear clipboard history
    keyboard.add_hotkey('ctrl+alt+c', clipboard_manager.clear_history)
    
    # Start clipboard monitoring in a separate thread
    threading.Thread(target=clipboard_manager.monitor_clipboard, daemon=True).start()
    
    # Keep the script running
    keyboard.wait('esc')  # Press 'esc' to exit