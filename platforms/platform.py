import abc
from selenium.webdriver.common.by import By
from utils.browser import Browser
from utils.config import Config
from utils.email_alert import EmailAlert


class Platform(abc.ABC):    

    def __init__(self, platform):
        self.browser = Browser()
        self.config = Config(platform)
        self.email_alert = EmailAlert()
        self.By = By


    @abc.abstractmethod
    def login(self):
    	pass


    @abc.abstractmethod
    def get_account_value(self):
    	pass


    @abc.abstractmethod
    def get_available_funds(self):
    	pass


    def get_project_value(self, project_id):
        return 0


    def get_name(self):
        return self.__class__.__name__


    def get_username(self):
        return self.config.username


    def get_password(self):
        return self.config.password


    def get_account(self):
        return self.config.account


    def get_currency(self):
        return self.config.currency


    def has_projects(self):
        return self.config.has_projects()


    def get_projects(self):
        return self.config.projects


    def send_alert_email(self, platform_name, message):
    	self.email_alert.send_email_alert(platform_name, message)


    def quit(self):
    	self.browser.quit()

