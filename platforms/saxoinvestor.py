from platforms.platform import Platform
import codecs
import time

class SaxoInvestor(Platform):

    def __init__(self):
        super(SaxoInvestor, self).__init__('saxoinvestor')


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://www.saxoinvestor.dk/Login/da/?ReturnUrl=%2Finvestor%2Fpage%2Fmarkets')
        
            # Fill login form and submit
            username = self.browser.getElement(self.By.ID, 'field_userid')
            username.send_keys(self.get_username())
            password = self.browser.getElement(self.By.ID, 'field_password')
            password.send_keys(self.get_password())
            form = self.browser.getElement(self.By.ID, 'loginForm')
            form.submit()
        
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            time.sleep(2)
            self.browser.get('https://www.saxoinvestor.dk/investor/investments/current-holdings')
            pricebar = self.browser.getElement(self.By.CLASS_NAME, 'pricebar-items')
            portfolio_value_container = pricebar.find_elements_by_class_name('pricebar-item')[2]
            portfolio_value_element = portfolio_value_container.find_element_by_class_name('pricebar-value')
            portfolio_value = portfolio_value_element.text.split(' ')[0].replace(".", "")

            return portfolio_value
        except Exception as e:
            raise


    def get_available_funds(self):
        try:
            # Retreive available funds in account
            pricebar = self.browser.getElement(self.By.CLASS_NAME, 'pricebar-items')
            available_funds_container = pricebar.find_elements_by_class_name('pricebar-item')[0]
            available_funds_element = available_funds_container.find_element_by_class_name('pricebar-value')
            available_funds = available_funds_element.text.split(' ')[0].replace(".", "")

            return available_funds
        except Exception as e:
            raise

