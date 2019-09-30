from platforms.platform import Platform


class Kuetzal(Platform):

    def __init__(self):
        super(Kuetzal, self).__init__('kuetzal')


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://kuetzal.com/en/#')
            signin_button = self.browser.getElement(self.By.CLASS_NAME, 'careerfy-open-signup-tab')
            signin_button.click()
        
            # Fill login form and submit
            login_wrapper = self.browser.getElement(self.By.CLASS_NAME, 'fade-in')
            username = login_wrapper.find_element_by_name('login')
            username.send_keys(self.get_username())
            password = login_wrapper.find_element_by_name('password')
            password.send_keys(self.get_password())
            form = login_wrapper.find_element_by_tag_name('form')
            form.submit()
            
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            profile_button_wrapper = self.browser.getElement(self.By.CLASS_NAME, 'theaccount')
            profile_button = profile_button_wrapper.find_element_by_class_name('careerfy-simple-btn')
            profile_button.click()

            column = self.browser.getElement(self.By.CLASS_NAME, 'careerfy-column-3')
            account_value_unit = column.find_element_by_tag_name('span')
            account_value = account_value_unit.text.split(' ')[0]

            return account_value
        except Exception as e:
            raise


    def get_available_funds(self):
        try:
            # Retreive available funds in account
            user_section = self.browser.getElement(self.By.CLASS_NAME, 'careerfy-user-section')
            available_funds_wrapper = user_section.find_element_by_class_name('deposit')
            available_funds_unit = available_funds_wrapper.find_element_by_tag_name('b')
            available_funds = available_funds_unit.text.split(' ')[1]

            return available_funds
        except Exception as e:
            raise

