import time
import codecs
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

host = "https://www.grupeer.com/login"
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
        username = getElement(By.ID, 'email')
        username.send_keys(credentials['usr'])
        password = getElement(By.NAME, 'password')
        password.send_keys(credentials['pwd'])
        login = getElement(By.CLASS_NAME, 'content-wrapper')
        form = login.find_element_by_tag_name('form')
        form.submit()
    
        # Retreive total value of account
        account_info = getElement(By.CLASS_NAME, 'block-value')
        total_value = account_info.text.split('€')[1].strip()
    
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
        data = json.load(f_check)['grupeer']
    return data


print(login())
quit()
