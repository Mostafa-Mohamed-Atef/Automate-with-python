import time
import keyboard  # Using only the 'keyboard' library

# Flag to track if we're currently selecting
selecting = False

def on_press():
    global selecting
    try:
        if not selecting:  # Ensure we only press once
            selecting = True
            keyboard.press('ctrl')
            time.sleep(0.1)
            keyboard.press('shift')
            time.sleep(0.1)
            keyboard.press('right')
            # time.sleep(0.1)
            keyboard.release('right')
            return
    except Exception as e:
        print(e)

def on_release():
    global selecting
    try:
        if selecting:  # Ensure we only release if selecting
            # time.sleep(0.1)
            keyboard.release('shift')
            time.sleep(0.1)
            keyboard.release('ctrl')
            selecting = False
            return
    except Exception as e:
        print(e)

def start_listening():
    def on_key_event(event):
        if event.event_type == 'down' and event.name == 'right':
            on_press()
        elif event.event_type == 'up' and event.name == 'right':
            on_release()

    print("Listening....")
    keyboard.hook(on_key_event)
    keyboard.wait('esc')

start_listening()
