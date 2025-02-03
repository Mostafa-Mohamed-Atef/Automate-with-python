import pyautogui
import requests
import pyperclip
import time
import os
from PIL import ImageGrab  # Only needed for Windows screen capture

# Configuration
DEEPSEEK_API_KEY = "your_api_key_here"  # Replace with your actual API key
API_ENDPOINT = "https://api.deepseek.com/v1/chat/completions"  # Verify endpoint URL
TEMPORARY_IMAGE = "screenshot_temp.png"


def capture_screenshot():
    """Capture the entire screen and save as temporary image"""
    try:
        # For Windows users, you can alternatively use:
        # screenshot = ImageGrab.grab()
        screenshot = pyautogui.screenshot()
        screenshot.save(TEMPORARY_IMAGE)
        return True
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return False


def send_to_deepseek(image_path):
    """Send screenshot to DeepSeek API and return response"""
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    # First convert image to base64 or send as file
    # This part depends on DeepSeek's API requirements
    try:
        with open(image_path, "rb") as image_file:
            # This payload structure might need adjustment based on API specs
            payload = {
                "model": "deepseek-r1",
                "messages": [
                    {
                        "role": "user",
                        "content": "Please analyze this coding problem and respond with just the code solution."
                    },
                    {
                        "role": "assistant",
                        "content": image_file.read().decode("latin-1")
                    }
                ]
            }

            response = requests.post(API_ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"API Error: {e}")
        return None


def process_response(response):
    """Extract code from API response and copy to clipboard"""
    if response and "choices" in response:
        code = response["choices"][0]["message"]["content"]
        pyperclip.copy(code)
        print("Code successfully copied to clipboard!")
        return True
    print("No code found in response")
    return False


def main():
    # Step 1: Capture screenshot
    input("Press Enter to capture the screen...")
    if not capture_screenshot():
        return

    # Step 2: Send to DeepSeek
    print("Sending to DeepSeek...")
    response = send_to_deepseek(TEMPORARY_IMAGE)

    # Step 3: Process response and copy to clipboard
    if response:
        process_response(response)

    # Cleanup
    try:
        os.remove(TEMPORARY_IMAGE)
    except:
        pass


if __name__ == "__main__":
    main()