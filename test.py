from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import math
import time

def add_visual_cursor(driver):
    cursor_script = """
    var body = document.querySelector('body');
    var cursor = document.createElement('div');
    cursor.style.width = '10px';
    cursor.style.height = '10px';
    cursor.style.borderRadius = '5px';
    cursor.style.backgroundColor = 'red';
    cursor.style.position = 'absolute';
    cursor.style.zIndex = '999999';
    cursor.style.pointerEvents = 'none';
    body.appendChild(cursor);
    return cursor;
    """
    return driver.execute_script(cursor_script)

def move_visual_cursor(driver, cursor, x, y):
    driver.execute_script("arguments[0].style.left = arguments[1] + 'px'; arguments[0].style.top = arguments[2] + 'px';", cursor, x, y)

def wind_mouse(driver, cursor, start_x, start_y, end_x, end_y, gravity=9, wind=2, min_wait=0.1, max_wait=0.3, max_step=10, target_area=3):
    wind_x = 0
    wind_y = 0
    distance = math.sqrt((end_x - start_x) ** 2 + (end_y - start_y) ** 2)

    while distance > target_area:
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
        move_visual_cursor(driver, cursor, start_x, start_y)
        time.sleep(random.uniform(min_wait, max_wait))
        distance = math.sqrt((end_x - start_x) ** 2 + (end_y - start_y) ** 2)

# Set up Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://pixelscan.net")

# Add a visual cursor to the webpage
visual_cursor = add_visual_cursor(driver)

# Define start and end points for the mouse movement
start_x = 0
start_y = 0
end_x = 100
end_y = 100

# Perform wind mouse movement with visual tracking
wind_mouse(driver, visual_cursor, start_x, start_y, end_x, end_y)

# Keep the browser open (remove driver.quit())
