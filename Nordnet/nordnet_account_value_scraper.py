import time
import codecs
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

host = "https://www.nordnet.dk/mux/web/nordnet/index.html"
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver', chrome_options = options)
wait = WebDriverWait(browser, timeout = 10) # seconds

def login():
    # Navigate to login page
    browser.get(host + "/")
    header = browser.find_element_by_class_name('signup-signin')
    account = header.find_element_by_class_name('signin-btn')
    account.click()
    time.sleep(1) # workaround: javascript needs to be loaded
    login_methods = browser.find_element_by_class_name('loginMethods')
    login_link = login_methods.find_element_by_class_name('button')
    login_link.click()
    time.sleep(1) # workaround: javascript needs to be loaded
    
    # Fill login form and submit
    credentials = get_credentials()
    username = browser.find_element_by_id('username')
    username.send_keys(credentials['usr'])
    password = browser.find_element_by_id('password')
    password.send_keys(credentials['pwd'])
    form = browser.find_element_by_class_name('sign-in-legacy_form')
    form.submit()
    
    # Retreive total value of account
    portfolio_today = getElement(By.ID, 'portfolioToday')
    result_line = portfolio_today.find_element_by_class_name('resultLine')
    result_value_and_unit = result_line.find_elements_by_tag_name('td')[1]
    result_value = result_value_and_unit.text.split('DKK')[0].replace(" ", "")

    return result_value


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
        data = json.load(f_check)['nordnet']
    return data


print(login())
quit()
