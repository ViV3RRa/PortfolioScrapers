from selenium.webdriver.common.by import By
from utils.browser import Browser
from utils.credentials import Credentials
from utils.email_alert import EmailAlert


class Grupeer:

    def __init__(self):
        self.browser = Browser()
        self.credentials = Credentials('grupeer')
        self.email_alert = EmailAlert()


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://www.grupeer.com/login')
        
            # Fill login form and submit
            username = self.browser.getElement(By.ID, 'email')
            username.send_keys(self.credentials.username)
            password = self.browser.getElement(By.NAME, 'password')
            password.send_keys(self.credentials.password)
            login = self.browser.getElement(By.CLASS_NAME, 'content-wrapper')
            form = login.find_element_by_tag_name('form')
            form.submit()
        
        except Exception as e:
            print(e)
            self.email_alert.send_email_alert('Grupeer', e)
            self.browser.quit()


    def get_account_value(self):
        try:
            # Retreive total value of account
            account_info = self.browser.getElement(By.CLASS_NAME, 'block-value')
            total_value = account_info.text.split('€')[1].strip()

            return total_value
        except Exception as e:
            print(e)
            self.email_alert.send_email_alert('Grupeer', e)
            self.browser.quit()


    def quit(self):
        self.browser.quit()

