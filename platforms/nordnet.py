from platforms.platform import Platform
import codecs

class Nordnet(Platform):

    def __init__(self):
        super(Nordnet, self).__init__('nordnet')


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://www.nordnet.dk/mux/login/start.html?cmpi=start-loggain&state=signin')
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

            navigate_button = self.browser.getElement(self.By.ID, 'alias_22066724')
            navigate_button.click()
        
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            portfolio_today = self.browser.getElement(self.By.ID, 'portfolioToday')
            result_line = portfolio_today.find_element_by_class_name('resultLine')
            value_element = result_line.find_element_by_tag_name('span')
            result_value = value_element.text.replace(" ", "").split("DKK")[0]

            return result_value
        except Exception as e:
            raise


    def get_available_funds(self):
        try:
            # Retreive available funds in account
            portfolio_today = self.browser.getElement(self.By.ID, 'portfolioToday')
            table_space = portfolio_today.find_element_by_class_name('tableSpace')
            value_row = table_space.find_elements_by_tag_name('tr')[0]
            value_element = table_space.find_element_by_tag_name('span')
            available_funds = value_element.text.replace(" ", "").split("DKK")[0]

            return available_funds
        except Exception as e:
            raise

