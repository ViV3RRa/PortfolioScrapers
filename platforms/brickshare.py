from platforms.platform import Platform
import codecs


class BrickShare(Platform):

    def __init__(self):
        super(BrickShare, self).__init__('brickshare')
        self.project_identifier_text = 'Ejendomsfond: Nordvest'

    def login(self):
        try:
            # Navigate to login page
            self.browser.get('https://brickshare.dk/log-ind')

            # Fill login form and submit
            username = self.browser.getElement(self.By.NAME, 'email')
            username.send_keys(self.credentials.username)
            password = self.browser.getElement(self.By.NAME, 'password')
            password.send_keys(self.credentials.password)
            form = self.browser.getElement(self.By.ID, 'signin')
            form.submit()

        except Exception as e:
            raise


    def get_account_value(self):
        try:
            # Retreive total value of account
            found = False
            all_projects = self.browser.getElement(self.By.CLASS_NAME, 'home-project-section')
            project_lists_container = all_projects.find_elements_by_class_name('projects-container')
            for project_list in project_lists_container:
                if found:
                    break
                projects_container = project_list.find_elements_by_class_name('project-card-container')
                for project_container in projects_container:
                    project_description = project_container.find_element_by_class_name('type-zeta')
                    if self.project_identifier_text in project_description.text:
                        project_button = project_container.find_element_by_tag_name('a')
                        project_button.click()
                        found = True
                        break

            infobox_bottom = self.browser.getElement(self.By.CLASS_NAME, 'infobox-bottom')
            nav_content = infobox_bottom.find_elements_by_class_name('infobox-bottom-content')[3]
            nav = nav_content.find_element_by_class_name('text-medium').text

            return nav
        except Exception as e:
            raise


    def get_available_funds(self):
        return '0'


