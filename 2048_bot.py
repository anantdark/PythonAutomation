
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
extension = '/home/anant/vscode/uBlock0_1.30.5b1.firefox.signed.xpi'
driver = webdriver.Firefox()
driver.install_addon(extension, temporary=True)
driver.get('https://play2048.co/')
driver.fullscreen_window()
time.sleep(4)
html_elem = driver.find_element_by_tag_name('body')
max_score = 0

def checker():
    global max_score
    for i in range(200):
        html_elem.send_keys(Keys.UP)
        html_elem.send_keys(Keys.RIGHT)
        html_elem.send_keys(Keys.DOWN)
        html_elem.send_keys(Keys.LEFT)
    temp = driver.find_element_by_class_name("score-container")
    score = int(temp.text)
    if max_score < score:
        time.sleep(1)
        max_score = score
        driver.save_screenshot("2048.png")
        print('shot')
    driver.find_element_by_class_name("retry-button").click()

def checker2():
    global max_score
    for j in range(5):
        for i in range(50):
            html_elem.send_keys(Keys.UP)
            html_elem.send_keys(Keys.LEFT)
            html_elem.send_keys(Keys.DOWN)
            html_elem.send_keys(Keys.LEFT)
        html_elem.send_keys(Keys.RIGHT)
        html_elem.send_keys(Keys.LEFT)
    temp = driver.find_element_by_class_name("score-container")
    score = int(temp.text)
    if max_score < score:
        time.sleep(1)
        max_score = score
        driver.save_screenshot("2048.png")
        print('shot')
    driver.find_element_by_class_name("retry-button").click()

def random():
    import time
    from random import choice
    global max_score
    up = elem.send_keys(Keys.UP)
    down = elem.send_keys(Keys.DOWN)
    left = elem.send_keys(Keys.LEFT)
    right = elem.send_keys(Keys.RIGHT)

    choices = [up, left, right, down]
    for i in range(200):
        time.sleep(1)
        ch = choice(choices)
        ch

# random()
for i in range(50):
    checker()
    checker2()
