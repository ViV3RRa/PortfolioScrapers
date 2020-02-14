from platforms.platform import Platform


class Iuvo(Platform):

    def __init__(self):
        super(Iuvo, self).__init__('iuvo')


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://www.iuvo-group.com/en/login/')
        
            # Fill login form and submit
            username = self.browser.getElement(self.By.ID, 'p2p_login_form_login')
            username.send_keys(self.get_username())
            password = self.browser.getElement(self.By.ID, 'p2p_login_form_password')
            password.send_keys(self.get_password())
            form = login.find_element_by_tag_name('form')
            form.submit()
        
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            table = self.browser.getElement(self.By.CLASS_NAME, 'p2p-table')
            row = table.find_elements_by_tag('tr')[3]
            wrapper = row.find_elements_by_class_name('text-right')
            account_info = wrapper.find_elements_by_tag('strong')
            total_value = account_info.text.split('.')[0].strip()

            return total_value
        except Exception as e:
            raise


    def get_available_funds(self):
        try:
            # Retreive total value of account
            table = self.browser.getElement(self.By.CLASS_NAME, 'p2p-table')
            row = table.find_elements_by_tag('tr')[1]
            available_funds_info = row.find_elements_by_class_name('text-right')
            available_funds = available_funds_info.text.split('.')[0].strip()

            return available_funds
        except Exception as e:
            raise

