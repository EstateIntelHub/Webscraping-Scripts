from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
import random
import math
import time

def wind_mouse(start_x, start_y, end_x, end_y, gravity=9, wind=2, min_wait=0.1, max_wait=0.3, max_step=10, target_area=3):
    wind_x = 0
    wind_y = 0

    while math.sqrt((end_x - start_x) ** 2 + (end_y - start_y) ** 2) > target_area:
        wind_x = wind_x + (random.random() * 2 - 1) * wind
        wind_y = wind_y + (random.random() * 2 - 1) * wind

        velo_x = ((end_x - start_x) * gravity + wind_x) / gravity
        velo_y = ((end_y - start_y) * gravity + wind_y) / gravity

        step_x = velo_x / (random.randint(6, 12) * (0.3 + random.random()))
        step_y = velo_y / (random.randint(6, 12) * (0.3 + random.random()))

        step_x = int(max(min(step_x, max_step), -max_step))
        step_y = int(max(min(step_y, max_step), -max_step))

        start_x += step_x
        start_y += step_y

        action.move_to_element_with_offset(body_element, start_x, start_y)
        action.perform()

        time.sleep(random.uniform(min_wait, max_wait))

# Setting up Chrome options for Selenium
options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

s = Service('D:\\Manual Mininig\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

# Applying stealth settings to make Selenium more undetectable
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
)

driver.get("https://bot.sannysoft.com/")

# Create ActionChains object
action = ActionChains(driver)

# Find an element to use as a reference for movements
body_element = driver.find_element(By.TAG_NAME, 'body')

# Define start and end points for the mouse movement
start_x = 0
start_y = 0
end_x = 100  # example end point coordinates
end_y = 100

# Perform wind mouse movement
wind_mouse(start_x, start_y, end_x, end_y, gravity=9, wind=2, min_wait=0.1, max_wait=0.3, max_step=10, target_area=3)

# The browser will remain open after this script completes.
