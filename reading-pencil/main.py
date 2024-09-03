from pynput import keyboard
from pynput.keyboard import Key, Controller

# Create a keyboard controller
kb = Controller()

# Flag to track if we're currently selecting
selecting = False

def on_press(key):
    global selecting
    if key == Key.right and not selecting:
        # Start selecting
        selecting = True
        kb.press(Key.ctrl)
        kb.press(Key.shift)
        kb.press(Key.right)
        kb.release(Key.right)
    elif key == Key.esc and selecting:
        # Stop selecting
        selecting = False
        kb.release(Key.ctrl)
        kb.release(Key.shift)

def on_release(key):
    if key == Key.right and selecting:
        # Continue selecting
        kb.press(Key.right)
        kb.release(Key.right)

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()