import time
import os 
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_argument("--headless")  # Run in headless mode
DRIVER = webdriver.Firefox(options=options) 
PATH = "/home/mostafa/Pictures/Screenshots"

def get_scroll_dimension(axis):
    return DRIVER.execute_script(f"return document.body.parentNode.scroll{axis}")

def screenshot():
    date_time = datetime.date.today().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = os.path.join(PATH, f'Web Screenshot from {date_time}.png')
    width = get_scroll_dimension("Width")
    height = get_scroll_dimension("Height")

    DRIVER.set_window_size(width, height)

    full_body_element = DRIVER.find_element(By.TAG_NAME, "body")

    full_body_element.screenshot(file_name)
    print("Done")
    DRIVER.quit()

if __name__ == "__main__":
    url = input("Enter url page:\n")
    DRIVER.get(url)
    time.sleep(2)
    screenshot()

