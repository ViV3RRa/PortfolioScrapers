from platforms.platform import Platform


class Fastinvest(Platform):

    def __init__(self):
        super(Fastinvest, self).__init__('fastinvest')


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://www.fastinvest.com/en/investor/login')
        
            # Fill login form and submit
            username = self.browser.getElement(self.By.ID, 'email')
            username.send_keys(self.get_username())
            password = self.browser.getElement(self.By.ID, 'password')
            password.send_keys(self.get_password())
            form = self.browser.getElement(self.By.CLASS_NAME, 'login-form')
            form.submit()
        
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            account_info = self.browser.getElement(self.By.CLASS_NAME, 'col-xl-12')
            account_value_and_unit = account_info.find_element_by_class_name('amount-trim')
            account_value = account_value_and_unit.text.split('€')[1].strip()

            return account_value
        except Exception as e:
            raise


    def get_available_funds(self):
        try:
            # Retreive total value of account
            account_info = self.browser.getElement(self.By.CLASS_NAME, 'toggle-content-flex')
            details_row = account_info.find_elements_by_class_name('justify-content-md-end')[1]
            available_funds_and_unit = details_row.find_element_by_class_name('amount-trim')
            available_funds = available_funds_and_unit.text.split('€')[1].strip()

            return available_funds
        except Exception as e:
            raise

