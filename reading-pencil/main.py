from pynput import keyboard

keyboard_controller = keyboard.Controller()


def track(key):
    if key == keyboard.Key.right:
        try:
            keyboard_controller.press(keyboard.Key.ctrl)
            keyboard_controller.press(keyboard.Key.shift)
            keyboard_controller.press(keyboard.Key.right)
            keyboard_controller.release(keyboard.Key.ctrl)
            keyboard_controller.release(keyboard.Key.shift)
            keyboard_controller.release(keyboard.Key.right)
        except Exception as e:
            print(e)
    if key == keyboard.Key.esc:
        # Stop listener
        return False


with keyboard.Listener(on_press=track) as listener:
    listener.join()

# keyboard_controller.type("hello world")