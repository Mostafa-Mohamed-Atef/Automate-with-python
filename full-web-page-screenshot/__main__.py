import time
import os 
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

DRIVER = webdriver.Firefox()
PATH = "/home/mostafa/Pictures/Screenshots"

def get_scroll_dimension(axis):
    return DRIVER.execute_script(f"return document.body.parentNode.scroll{axis}")

def screenshot():
    date_time = datetime.date.today().strftime("%Y-%m-%d")
    file_name = os.path.join(PATH, f'Web Screenshot from {date_time}.png')
    width = get_scroll_dimension("Width")
    height = get_scroll_dimension("Height")

    DRIVER.set_window_size(width, height)

    full_body_element = DRIVER.find_element(By.TAG_NAME, "body")

    full_body_element.screenshot(file_name)

    DRIVER.quit()

if __name__ == "__main__":
    url = input("Enter url page:\n")
    DRIVER.get(url)
    time.sleep(2)
    screenshot()

