import smtplib, ssl
import json
from utils.config import Config

class EmailAlert:

    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.port = 587  # For starttls

        # Create a secure SSL context
        self.context = ssl.create_default_context()

        # Get credentials from JSON file
        self.config = Config(None)
        self.sender_email = self.config.get_alert_email_sender()
        self.password = self.config.get_alert_email_sender_pwd()
        self.receiver_email = self.config.get_alert_email_receiver()

    
    def send_email_alert(self, platform, text):
        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(self.smtp_server,self.port)
            server.ehlo() # Can be omitted
            server.starttls(context=self.context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, self.__compose_message(platform, text))
        except Exception as e:
            print(e)
        finally:
            server.quit() 


    def __compose_message(self, platform, text):
        message = """\
Subject: {}: Scraper alert!

{}""".format(platform, text)

        return message

