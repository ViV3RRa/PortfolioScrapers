from selenium.webdriver.common.by import By
from utils.browser import Browser
from utils.credentials import Credentials
from utils.email_alert import EmailAlert


class Fastinvest:

    def __init__(self):
        self.browser = Browser()
        self.credentials = Credentials('fastinvest')
        self.email_alert = EmailAlert()


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://www.fastinvest.com/en/investor/login')
        
            # Fill login form and submit
            username = self.browser.getElement(By.ID, 'email')
            username.send_keys(self.credentials.username)
            password = self.browser.getElement(By.ID, 'password')
            password.send_keys(self.credentials.password)
            form = self.browser.getElement(By.CLASS_NAME, 'login-form')
            form.submit()
        
        except Exception as e:
            print(e)
            self.email_alert.send_email_alert('Fastinvest', e)
            self.browser.quit()


    def get_account_value(self):
        try:
            # Retreive total value of account
            account_info = self.browser.getElement(By.CLASS_NAME, 'col-xl-9')
            account_value_and_unit = account_info.find_element_by_class_name('amount-trim')
            account_value = account_value_and_unit.text.split('€')[1].strip()

            return account_value
        except Exception as e:
            print(e)
            self.email_alert.send_email_alert('Fastinvest', e)
            self.browser.quit()


    def quit(self):
        self.browser.quit()

