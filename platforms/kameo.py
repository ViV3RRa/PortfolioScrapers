from platforms.platform import Platform
import codecs
import time

class Kameo(Platform):

    def __init__(self):
        super(Kameo, self).__init__('kameo')


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://www.kameo.dk/user/login')
            username = self.browser.getElement(self.By.ID, 'LoginEmail')
            username.send_keys(self.get_username())
            password = self.browser.getElement(self.By.ID, 'LoginPassword')
            password.send_keys(self.get_password())
            form = self.browser.getElement(self.By.CLASS_NAME, 'form-horizontal')
            form.submit()
        
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            time.sleep(1)
            self.browser.get('https://www.kameo.dk/investor/dashboard')
            dashboard = self.browser.getElement(self.By.CLASS_NAME, 'dashboard')
            portfolio_value_container = dashboard.find_elements_by_class_name('panel-default')[3]
            portfolio_value = portfolio_value_container.find_element_by_class_name('pull-right')
            portfolio_value_formated = portfolio_value.text.split(',')[0]

            return portfolio_value_formated
        except Exception as e:
            raise


    def get_available_funds(self):
        try:
            # Retreive available funds in account
            dashboard = self.browser.getElement(self.By.CLASS_NAME, 'dashboard')
            available_funds_container = dashboard.find_elements_by_class_name('panel-default')[0]
            available_funds = available_funds_container.find_element_by_tag_name('a')
            available_funds_formated = available_funds.text.split(',')[0]

            return available_funds_formated
        except Exception as e:
            raise

