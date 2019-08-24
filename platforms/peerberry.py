from selenium.webdriver.common.by import By
from utils.browser import Browser
from utils.credentials import Credentials
from utils.email_alert import EmailAlert


class Peerberry:

    def __init__(self):
        self.browser = Browser()
        self.credentials = Credentials('peerberry')
        self.email_alert = EmailAlert()


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://peerberry.com/en/login')
        
            # Fill login form and submit
            username = self.browser.getElement(By.NAME, 'email')
            username.send_keys(self.credentials.username)
            password = self.browser.getElement(By.NAME, 'password')
            password.send_keys(self.credentials.password)
            login = self.browser.getElement(By.CLASS_NAME, 'PAGE')
            form = login.find_element_by_tag_name('form')
            form.submit()
            
        except Exception as e:
            print(e)
            self.email_alert.send_email_alert('Peerberry', e)
            self.browser.quit()


    def get_account_value(self):
        try:
            # Retreive total value of account
            account_info = self.browser.getElement(By.CLASS_NAME, 'account-info')
            account_balance = account_info.find_elements_by_class_name('row')
            total_div = account_balance[1].find_elements_by_class_name('col-sm-4')
            total_value_component = total_div[2].find_element_by_tag_name('div')
            total_value = total_value_component.text.split('€')[0].strip()

            return total_value
        except Exception as e:
            print(e)
            self.email_alert.send_email_alert('Peerberry', e)
            self.browser.quit()


    def quit(self):
        self.browser.quit()

