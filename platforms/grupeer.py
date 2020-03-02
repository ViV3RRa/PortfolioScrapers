from platforms.platform import Platform


class Grupeer(Platform):

    def __init__(self):
        super(Grupeer, self).__init__('grupeer')


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://www.grupeer.com/login')
        
            # Fill login form and submit
            username = self.browser.getElement(self.By.ID, 'email')
            username.send_keys(self.get_username())
            password = self.browser.getElement(self.By.NAME, 'password')
            password.send_keys(self.get_password())
            login = self.browser.getElement(self.By.CLASS_NAME, 'content-wrapper')
            form = login.find_element_by_tag_name('form')
            form.submit()
        
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            account_info = self.browser.getElement(self.By.CLASS_NAME, 'main-value  ')
            total_value = account_info.text.split('€')[1].strip()

            return total_value
        except Exception as e:
            raise


    def get_available_funds(self):
        try:
            # Retreive total value of account
            overview_block = self.browser.getElement(self.By.CLASS_NAME, 'overview-block')
            available_funds_row = overview_block.find_elements_by_class_name('row')[1]
            available_funds_component = available_funds_row.find_element_by_class_name('block-info-value')
            available_funds = available_funds_component.text.split('€')[1].strip()

            return available_funds
        except Exception as e:
            raise

