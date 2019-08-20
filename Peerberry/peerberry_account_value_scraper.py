import time
import codecs
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

host = "https://peerberry.com/en/login"
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver', chrome_options = options)
wait = WebDriverWait(browser, timeout = 10) # seconds

def login():
    try:
        # Navigate to login page
        browser.get(host)
    
        # Fill login form and submit
        credentials = get_credentials()
        username = getElement(By.NAME, 'email')
        username.send_keys(credentials['usr'])
        password = getElement(By.NAME, 'password')
        password.send_keys(credentials['pwd'])
        login = getElement(By.CLASS_NAME, 'PAGE')
        form = login.find_element_by_tag_name('form')
        form.submit()
    
        # Retreive total value of account
        account_info = getElement(By.CLASS_NAME, 'account-info')
        account_balance = account_info.find_elements_by_class_name('row')
        total_div = account_balance[1].find_elements_by_class_name('col-sm-4')
        total_value_component = total_div[2].find_element_by_tag_name('div')
        total_value = total_value_component.text.split('€')[0].strip()
    
        return total_value
    except Exception as e:
        print(e)
        codecs.open('tmp/dump', 'w', encoding='utf-8').write(browser.page_source)
        quit()


def getElement(by, name):
    try:
        return wait.until(EC.presence_of_element_located((by, name)))
    except:
        codecs.open('tmp/dump', 'w', encoding='utf-8').write(browser.page_source)


def quit():
    browser.quit()

def get_credentials():
    # read json file data from previous run
    with open("../credentials.json") as f_check:
        data = json.load(f_check)['peerberry']
    return data


print(login())
quit()
