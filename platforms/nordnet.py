from platforms.platform import Platform

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
        
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            section = self.browser.getElement(self.By.CLASS_NAME, 'section')
            result_value = section.find_element_by_class_name('value').text.replace(" ", "")

            return result_value
        except Exception as e:
            raise

