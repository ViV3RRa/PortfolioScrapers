from platforms.platform import Platform


class Peerberry(Platform):

    def __init__(self):
        super(Peerberry, self).__init__('peerberry')


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://peerberry.com/en/login')
        
            # Fill login form and submit
            username = self.browser.getElement(self.By.NAME, 'email')
            username.send_keys(self.credentials.username)
            password = self.browser.getElement(self.By.NAME, 'password')
            password.send_keys(self.credentials.password)
            login = self.browser.getElement(self.By.CLASS_NAME, 'PAGE')
            form = login.find_element_by_tag_name('form')
            form.submit()
            
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            account_info = self.browser.getElement(self.By.CLASS_NAME, 'account-info')
            account_balance = account_info.find_elements_by_class_name('row')
            total_div = account_balance[1].find_elements_by_class_name('col-sm-4')
            total_value_component = total_div[2].find_element_by_tag_name('div')
            total_value = total_value_component.text.split('€')[0].strip()

            return total_value
        except Exception as e:
            raise


    def get_available_funds(self):
        try:
            # Retreive available funds in account
            account_info = self.browser.getElement(self.By.CLASS_NAME, 'account-info')
            account_balance = account_info.find_elements_by_class_name('row')
            available_funds_div = account_balance[1].find_elements_by_class_name('col-sm-4')
            available_funds_component = available_funds_div[0].find_element_by_tag_name('div')
            available_funds = available_funds_component.text.split('€')[0].strip()

            return available_funds
        except Exception as e:
            raise

