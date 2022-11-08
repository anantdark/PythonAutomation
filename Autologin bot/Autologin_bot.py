#CoDeD By AnAnT

# I stored the passwords in a dictionary in another file named passwords.py
# from passwords import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options

# <<-- Webdriver template for firefox browser -->>
# extension = '/home/anant/vscode/uBlock0_1.30.5b1.firefox.signed.xpi'
# driver = webdriver.Firefox()
# driver.install_addon(extension, temporary=True)

def stackoverflow():
    chrome_options = Options()
    # Ublock origin extension to be installed at startup (for ad-block)
    # chrome_options.add_extension("/home/anant/vscode/ublock_origin.crx")
    driver = webdriver.Chrome(executable_path="/home/anant/vscode/chromedriver", chrome_options=chrome_options)
    driver.get("https://stackoverflow.com/users/login")
    user = 'username@domain.com'
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")
    email.send_keys(user)
    password.send_keys(passcode('stackoverflow'))
    driver.find_element_by_id("submit-button").click()
    fin = input()
    driver.close()

def github():
    chrome_options = Options()
    # Ublock origin extension to be installed at startup (for ad-block)
    # chrome_options.add_extension("/home/anant/vscode/ublock_origin.crx")
    # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(executable_path="/home/anant/vscode/chromedriver", chrome_options=chrome_options)
    
    # Uncomment this if you also use TOTP based authentication.
    # otp = timeotp("githubdark")
    # driver.get("https://totp.danhersam.com/#/"+otp)
    # token = driver.find_element_by_id("token").text
    driver.get("https://github.com/login")
    user = 'anantdark'
    username = driver.find_element(By.ID, "login_field")
    password = driver.find_element(By.ID, "password")
    username.send_keys(user)
    password.send_keys(passcode("github"))
    driver.find_element(By.NAME, "commit").click()
    # otp_box = driver.find_element_by_xpath('//*[@id="otp"]')
    # otp_box.send_keys(token)
    # driver.find_element_by_xpath("/html/body/div[3]/main/div/div[5]/form/button").click()
    fin = input()
    driver.close()


def passcode(param):
    dictemp = {}
    with open("password.txt", 'r') as files:
        line = files.readline()
        templist = line.split()
        dictemp[templist[0]] = templist[1]

    return dictemp[param]

def codechef():
    chrome_options = Options()
    # Ublock origin extension to be installed at startup (for ad-block)
    # chrome_options.add_extension("/home/anant/vscode/ublock_origin.crx")
    driver = webdriver.Chrome(executable_path="/home/anant/vscode/chromedriver", chrome_options=chrome_options)
    driver.get("https://codechef.com")
    user = 'username'
    username = driver.find_element_by_id("edit-name")
    username.send_keys(user)
    password = driver.find_element_by_id("edit-pass")
    password.send_keys(passcode("codechef"))
    driver.find_element_by_id("edit-submit").click()
    fin = input()
    driver.close()
    
def amazon():
    chrome_options = Options()
    # Ublock origin extension to be installed at startup (for ad-block)
    # chrome_options.add_extension("/home/anant/vscode/ublock_origin.crx")
    driver = webdriver.Chrome(executable_path="/home/anant/vscode/chromedriver", chrome_options=chrome_options)
    driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&%2F%3Fie%3DUTF8%26from%3Dhz%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
    user = 'username'
    username = driver.find_element_by_id("ap_email")
    username.send_keys(user)
    driver.find_element_by_id("continue").click()
    password = driver.find_element_by_id("ap_password")
    password.send_keys(passcode("amazon"))
    driver.find_element_by_id("signInSubmit").click()
    fin = input()
    driver.close()
    
def flipkart():
    chrome_options = Options()
    # Ublock origin extension to be installed at startup (for ad-block)
    # chrome_options.add_extension("/home/anant/vscode/ublock_origin.crx")
    driver = webdriver.Chrome(executable_path="/home/anant/vscode/chromedriver", chrome_options=chrome_options)
    driver.get("https://flipkart.com")
    user = 'username'
    username = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
    username.send_keys(user)
    password = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
    password.send_keys(passcode("flipkart"))
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
    fin = input()
    driver.close()
    
if __name__ == "__main__":
    print("<<---------WELCOME TO AUTOBOT v1.10--------->>\n".center(65))
    print("<<---------DEVELOPED BY [[ ANANT ]]--------->>\n".center(65))
    service = input('What do you want?\n\n')
    
    if service == "stackoverflow" or service == "stack":
        stackoverflow()
    elif service == "github" or service == "gh":
        github()
    elif service == "codechef" or service == "chef":
        codechef()
    elif service == "amazon":
        amazon()
    elif service == "flipkart" or service == "flip":
        flipkart()
    else:
        print('Sorry this is not supported yet, try later.')
        exit(0)




