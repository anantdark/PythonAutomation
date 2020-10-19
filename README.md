# PythonAutomation

A repo for some fun python automation scripts.
----------------
## All pull requests are welcome. Anyone is free to fork, modify and help grow the repo.

## Pull requests will be approved at the earliest within 6 hrs.

## keep contributing to open source. HAPPY CODING.
---------------------------------
## - 2048_bot

This is a bot that plays the game 2048.
You can play the game [here](https://play2048.co)

![2048 game](https://raw.githubusercontent.com/anantdark/PythonAutomation/main/shot.png)

The bot will automatically open the link and play.
It will also create a screenshot of the highest score.

----------------------------------------
## - Auto Login Bot

This is another python bot that can automatically login to many sites
Currently supports login to
- Github
- Stackoverflow
- Codechef
- Amazon
- Flipkart

Also supports TOTP based login, implemented for github(can be extended).

Passwords are stored in a separate file, and imported directly.

### Deployment:

- Install required modules and webdriver.
- Create passwords.py file and store all the passwords in a dictionary.(Will add encryption soon)
- Create Alias to use the scipts efficiently, more about aliases here.

----------------------------------------
### How to use the scripts?
You need
### - WebDriver

Get all info about webdriver installation [here](#Webdriver)
### - Selenium

Get all info about selenium installation [here](#Selenium)

## Selenium

It is a python library that will help you with the automation.
Run the command `pip install selenium` in the terminal to install.
## Webdriver

It is the application that selenium uses to browse the web.
You need to download the webdriver from the internet.

Driver for-
- Firefox - [here](https://github.com/mozilla/geckodriver/releases)
- Chrome - [here](https://chromedriver.chromium.org/downloads)

After downloading either place the driver and the script in the same folder.
Or link the path to the driver in the line `driver = webdriver.Firefox(*your-path-here*)`
