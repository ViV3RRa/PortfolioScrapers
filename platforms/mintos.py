from platforms.platform import Platform
import codecs
import time


class Mintos(Platform):

    def __init__(self):
        super(Mintos, self).__init__('mintos')

    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://www.mintos.com/en/')
            login_button = self.browser.getElement(self.By.ID, 'header-login-button')
            login_button.click()
            #self.browser.get('https://www.mintos.com/en/login')

            # Fill login form and submit
            username = self.browser.getElement(self.By.ID, 'login-username')
            username.clear()
            username.send_keys(self.get_username())
            password = self.browser.getElement(self.By.ID, 'login-password')
            password.clear()
            password.send_keys(self.get_password())
            time.sleep(2)
            form = self.browser.getElement(self.By.ID, 'login-form')
            form.submit()

        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            codecs.open('dump.html', 'w', encoding='utf-8').write(self.browser.browser.page_source)
            overview_box = self.browser.getElement(self.By.CLASS_NAME, 'overview-box')
            print(overview_box.text)
            value_element = overview_box.find_element_by_class_name('value')
            account_value = value_element.text.split('€')[1].strip()

            return account_value
        except Exception as e:
            raise


    def get_available_funds(self):
        try:
            # Retreive available funds in account
            overview_box = self.browser.getElement(self.By.CLASS_NAME, 'overview-box')
            data = overview_box.find_element_by_class_name('data')
            value_element = data.find_elements_by_tag_name('td')[1]
            available_funds = value_element.text.split('€')[1].strip()

            return available_funds
        except Exception as e:
            raise


