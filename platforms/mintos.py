from selenium.webdriver.common.by import By
from utils.browser import Browser
from utils.credentials import Credentials
from utils.email_alert import EmailAlert


class Mintos:

    def __init__(self):
        self.browser = Browser()
        self.credentials = Credentials('mintos')
        self.email_alert = EmailAlert()

    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://www.mintos.com/en/login')

            # Fill login form and submit
            username = self.browser.getElement(By.NAME, '_username')
            username.send_keys(self.credentials.username)
            password = self.browser.getElement(By.NAME, '_password')
            password.send_keys(self.credentials.password)
            form = self.browser.getElement(By.ID, 'login-form')
            form.submit()

        except Exception as e:
        	print(e)
        	self.email_alert.send_email_alert('Mintos', e)
        	self.browser.quit()


    def get_account_value(self):
        try:
            # Retreive total value of account
            overview_box = self.browser.getElement(By.CLASS_NAME, 'overview-box')
            value_element = overview_box.find_element_by_class_name('value')
            account_value = value_element.text.split('€')[1].strip()

            return account_value
        except Exception as e:
            print(e)
            self.email_alert.send_email_alert('Mintos', e)
            self.browser.quit()


    def quit(self):
        self.browser.quit()


