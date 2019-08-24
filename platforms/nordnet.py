from selenium.webdriver.common.by import By
from utils.browser import Browser
from utils.credentials import Credentials
from utils.email_alert import EmailAlert


class Nordnet:

    def __init__(self):
        self.browser = Browser()
        self.credentials = Credentials('nordnet')
        self.email_alert = EmailAlert()


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://www.nordnet.dk/mux/login/start.html?cmpi=start-loggain&state=signin')
            login_methods = self.browser.getElement(By.CLASS_NAME, 'loginMethods')
            login_link = login_methods.find_element_by_class_name('button')
            login_link.click()
        
            # Fill login form and submit
            username = self.browser.getElement(By.ID, 'username')
            username.send_keys(self.credentials.username)
            password = self.browser.getElement(By.ID, 'password')
            password.send_keys(self.credentials.password)
            form = self.browser.getElement(By.CLASS_NAME, 'sign-in-legacy_form')
            form.submit()
        
        except Exception as e:
            print(e)
            self.email_alert.send_email_alert('Nordnet', e)
            self.browser.quit()


    def get_account_value(self):
        try:
            # Retreive total value of account
            section = self.browser.getElement(By.CLASS_NAME, 'section')
            result_value = section.find_element_by_class_name('value').text.replace(" ", "")

            return result_value
        except Exception as e:
            print(e)
            self.email_alert.send_email_alert('Nordnet', e)
            self.browser.quit()
        


    def quit(self):
        self.browser.quit()

