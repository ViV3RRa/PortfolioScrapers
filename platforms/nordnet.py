from platforms.platform import Platform
import codecs
import time

class Nordnet(Platform):

    def __init__(self):
        super(Nordnet, self).__init__('nordnet')


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://classic.nordnet.dk/mux/login/startDK.html?clearEndpoint=0&intent=next')
            login_methods = self.browser.getElement(self.By.CLASS_NAME, 'loginMethods')
            login_link = login_methods.find_element_by_class_name('button')
            login_link.click()
        
            # Fill login form and submit
            username = self.browser.getElement(self.By.ID, 'username')
            username.send_keys(self.credentials.username)
            password = self.browser.getElement(self.By.ID, 'password')
            password.send_keys(self.credentials.password)
            form = self.browser.getElement(self.By.CLASS_NAME, 'sign-in-legacy_form')
            form.submit()
        
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            time.sleep(2)
            self.browser.get('https://www.nordnet.dk/oversigt')
            portfolio_today = self.browser.getElement(self.By.CLASS_NAME, 'kgnLnO')
            portfolio_today_value = portfolio_today.text.replace(".", "")

            return portfolio_today_value
        except Exception as e:
            raise


    def get_available_funds(self):
        try:
            # Retreive available funds in account
            available_funds_container = self.browser.getElement(self.By.CLASS_NAME, 'dULHMh')
            available_funds_element = available_funds_container.find_element_by_class_name('gJPols')

            return available_funds_element.text
        except Exception as e:
            raise

