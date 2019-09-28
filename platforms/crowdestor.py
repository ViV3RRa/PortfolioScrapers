from platforms.platform import Platform


class Crowdestor(Platform):

    def __init__(self):
        super(Crowdestor, self).__init__('crowdestor')


    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://crowdestor.com/register/')
        
            # Fill login form and submit
            form = self.browser.getElement(self.By.ID, 'modal-login')
            username = form.find_element_by_id('email')
            username.send_keys(self.get_username())
            password = form.find_element_by_id('password')
            password.send_keys(self.get_password())
            form.submit()
        
        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            self.browser.get('https://crowdestor.com/account/')

            return self.__get_value_from_component_with_title('Account balance')
        except Exception as e:
            raise


    def get_available_funds(self):
        try:
            # Retreive total value of account

            return self.__get_value_from_component_with_title('Amount available')
        except Exception as e:
            raise


    def __get_value_from_component_with_title(self, title):
    	try:
    		# Retreive total value of account
    		account_content = self.browser.getElement(self.By.CLASS_NAME, 'account-content')
    		overview_components = account_content.find_elements_by_class_name('col-md-6')
    		for component in overview_components:
    			component_title = component.find_element_by_class_name('overview-title').text
    			if component_title == title:
    				account_value_and_unit = component.find_element_by_class_name('overview-value')
    				account_value = account_value_and_unit.text.split('€')[0].strip()
    				return account_value

    		return None
    	except Exception as e:
    		raise
