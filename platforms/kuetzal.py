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
            form = login_wrapper.find_element_by_tag_name('form')

            # Solve CAPTCHA math equation
            captcha_row = form.find_elements_by_tag_name('li')[2]
            captcha_test = captcha_row.find_elements_by_tag_name('td')[0]
            test_str = captcha_test.text.split('=')[0]
            test_result = str(eval(test_str))
            captcha_input = captcha_row.find_element_by_name('rr')
            captcha_input.send_keys(test_result)

            username = login_wrapper.find_element_by_name('login')
            username.send_keys(self.get_username())
            password = login_wrapper.find_element_by_name('password')
            password.send_keys(self.get_password())
            form.submit()
            
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            self.browser.get('https://kuetzal.com/en/profile/')

            column = self.browser.getElement(self.By.CLASS_NAME, 'careerfy-column-3')
            account_value_unit = column.find_elements_by_tag_name('b')[6]
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

