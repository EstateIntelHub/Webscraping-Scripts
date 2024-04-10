from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
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

# Setting up Chrome options for Selenium
options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Update the path to your chromedriver.exe
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

driver.get("https://www.imobiliare.ro/vanzare-garsoniere/timisoara/torontalului/garsoniera-de-vanzare-XEAT100EN?exprec=similare&rec_ref=home&sursa_rec=home&imoidviz=4239785372")

# Add a visual cursor to the webpage
visual_cursor = add_visual_cursor(driver)


time.sleep(60)


# Define start and end points for the mouse movement
start_x = 0
start_y = 0
end_x = 543 # Adjust these end coordinates as needed
end_y = 784

# Perform wind mouse movement with visual tracking
wind_mouse(driver, visual_cursor, start_x, start_y, end_x, end_y)

# The browser will remain open after the script execution.
