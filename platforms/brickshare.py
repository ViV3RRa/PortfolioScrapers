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
            username.send_keys(self.get_username())
            password = self.browser.getElement(self.By.NAME, 'password')
            password.send_keys(self.get_password())
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

            return str(float(nav) * 10000)
        except Exception as e:
            raise


    def get_available_funds(self):
        return '0'


    def get_project_value(self, project_id):
        invested_amount = 0
        project_url = ''

        # Find the amount invested in the project
        self.browser.get('https://brickshare.dk/account/dashboard')
        project_container = self.browser.getElement(self.By.CLASS_NAME, 'project-detail-left')
        projects = project_container.find_elements_by_class_name('project-card-container')
        for project in projects:
            url = project.find_element_by_tag_name('a').get_attribute('href')
            if project_id in url:
                project_url = url
                content_wrapper = project.find_element_by_class_name('bottom-part')
                line = content_wrapper.find_element_by_class_name('line')
                amount_text = content_wrapper.find_element_by_class_name('amount').text
                invested_amount += float(amount_text.split(' ')[0].replace('.','').replace(',','.'))

        # Find the current NAV of the project and return the invested amount multiplied with it
        if project_url:
            self.browser.get('https://brickshare.dk/investeringsprojekter/' + project_id)
            infobox_bottom = self.browser.getElement(self.By.CLASS_NAME, 'infobox-bottom')
            nav_content = infobox_bottom.find_elements_by_class_name('infobox-bottom-content')[3]
            nav = nav_content.find_element_by_class_name('text-medium').text
            return invested_amount * float(nav)


