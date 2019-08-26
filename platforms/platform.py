import abc
from selenium.webdriver.common.by import By
from utils.browser import Browser
from utils.credentials import Credentials
from utils.email_alert import EmailAlert


class Platform(abc.ABC):

    def __init__(self, platform):
        self.browser = Browser()
        self.credentials = Credentials(platform)
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


    def send_alert_email(self, platform_name, message):
    	self.email_alert.send_email_alert(platform_name, message)


    def quit(self):
    	self.browser.quit()

