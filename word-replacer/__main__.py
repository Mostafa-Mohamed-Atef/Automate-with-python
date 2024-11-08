import keyboard
import time

def replace_text(wrong_text, correct_text):
    buffer = ""
    while True:
        event = keyboard.read_event()
        
        # Capture key down events and accumulate typed characters
        if event.event_type == 'down':
            if event.name == "backspace":
                buffer = buffer[:-1]  # Handle backspace by removing the last character
            elif event.name == "space":
                buffer += " "
            elif event.name == "enter":
                buffer = ""  # Reset buffer on enter key to avoid accidental replacements
            elif len(event.name) == 1:  # Valid character input
                buffer += event.name
                
            # If buffer matches the wrong_text, replace it
            if buffer.endswith(wrong_text):
                # Remove the wrong text from the input
                for _ in range(len(wrong_text)):
                    keyboard.send("backspace")
                    time.sleep(0.05)  # Add a slight delay to avoid overlap
                
                # Type the correct text
                keyboard.write(correct_text)
                buffer = ""  # Clear buffer to avoid repeated replacements

if __name__=="__main__":
    # User input for wrong and correct text
    wrong_text = input("Enter the text you want to replace: ")
    correct_text = input("Enter the replacement text: ")

    # Run the text replacement function
    replace_text(wrong_text, correct_text)
