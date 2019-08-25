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
            username.send_keys(self.credentials.username)
            password = self.browser.getElement(self.By.NAME, 'password')
            password.send_keys(self.credentials.password)
            login = self.browser.getElement(self.By.CLASS_NAME, 'content-wrapper')
            form = login.find_element_by_tag_name('form')
            form.submit()
        
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            account_info = self.browser.getElement(self.By.CLASS_NAME, 'block-value')
            total_value = account_info.text.split('€')[1].strip()

            return total_value
        except Exception as e:
            raise

