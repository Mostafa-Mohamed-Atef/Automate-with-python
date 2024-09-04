import keyboard  # Using only the 'keyboard' library

# Flag to track if we're currently selecting

def on_press():
    global selecting
    try:
            keyboard.press('ctrl')
            keyboard.press('shift')
            keyboard.press('right')  # Combine press and release for 'right' key
    except Exception as e:
        print(e)

def on_release():
    try:
            keyboard.press('right')
            keyboard.release('shift')
            keyboard.release('ctrl')
    except Exception as e:
        print(e)

def start_listening():
    def on_key_event(event):
        if event.event_type == 'down' and event.name == 'right':
            on_press()
        elif event.event_type == 'up' and event.name == 'right':
            on_release()
        elif event.name == 'esc':
            return False
        else:
            keyboard.release('shift')
            keyboard.release('ctrl')


    print("Listening....")
    keyboard.hook(on_key_event)
    keyboard.wait('esc')

start_listening()
