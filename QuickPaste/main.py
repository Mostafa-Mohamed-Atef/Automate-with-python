from pynput import mouse, keyboard
import pyperclip

def copy_selected_text():
    pass


# Create a keyboard controller
keyboard_controller = keyboard.Controller()

def on_click(x, y, button, pressed):
    if button == mouse.Button.middle and pressed:
        try:
            keyboard_controller.press(keyboard.Key.ctrl)
            keyboard_controller.press('v')
            keyboard_controller.release('v')
            keyboard_controller.release(keyboard.Key.ctrl)
            
        except Exception as e:
            print(f"An error occurred: {e}")

# Set up the mouse listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
