import abc
from selenium.webdriver.common.by import By
from utils.browser import Browser
from utils.config import Config
from utils.email_alert import EmailAlert


class Platform(abc.ABC):    

    def __init__(self, platform):
        self.browser = Browser()
        self.credentials = Config(platform)
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


    def get_account(self):
        return self.credentials.account


    def get_currency(self):
        return self.credentials.currency


    def send_alert_email(self, platform_name, message):
    	self.email_alert.send_email_alert(platform_name, message)


    def quit(self):
    	self.browser.quit()

