# CoDeD By AnAnT
# 2048 game autoplay bot.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# You can also install any extension in the browser.
# Just uncomment the below code and change path accordingly.

extension = '/home/anant/vscode/uBlock0_1.30.5b1.firefox.signed.xpi'

#pass in the path of your driver if it is not in the same directory.
driver = webdriver.Firefox()
driver.install_addon(extension, temporary=True)
driver.get('https://play2048.co/')
# driver.fullscreen_window()
time.sleep(4)
html_elem = driver.find_element_by_tag_name('body')
max_score = 0

def playbot1():
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

def playbot2():
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

for i in range(50):
    playbot1()
    playbot2()
driver.close()