from platforms.platform import Platform


class Mintos(Platform):

    def __init__(self):
        super(Mintos, self).__init__('mintos')

    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://www.mintos.com/en/login')

            # Fill login form and submit
            username = self.browser.getElement(self.By.NAME, '_username')
            username.send_keys(self.credentials.username)
            password = self.browser.getElement(self.By.NAME, '_password')
            password.send_keys(self.credentials.password)
            form = self.browser.getElement(self.By.ID, 'login-form')
            form.submit()

        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            overview_box = self.browser.getElement(self.By.CLASS_NAME, 'overview-box')
            value_element = overview_box.find_element_by_class_name('value')
            account_value = value_element.text.split('€')[1].strip()

            return account_value
        except Exception as e:
            raise


