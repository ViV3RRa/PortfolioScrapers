import smtplib, ssl
import json
import utils
from utils.credentials import Credentials

class EmailAlert:

    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.port = 587  # For starttls

        # Create a secure SSL context
        self.context = ssl.create_default_context()

        # Get credentials from JSON file
        self.credentials = Credentials('alert_email_sender')
        self.sender_email = self.credentials.username
        self.password = self.credentials.password
        
        from utils.utils import get_receiver_email
        self.receiver_email = get_receiver_email()

    
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

