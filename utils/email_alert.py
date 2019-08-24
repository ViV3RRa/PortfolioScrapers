import smtplib, ssl
import json
from utils.credentials import Credentials

class EmailAlert:

    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.port = 587  # For starttls

        # Create a secure SSL context
        self.context = ssl.create_default_context()

        # Get credentials from JSON file
        self.credentials = Credentials('alert_email')
        self.sender_email = self.credentials.username
        self.password = self.credentials.password
        self.receiver_email = self.__get_receiver_email()


    def __get_receiver_email(self):
        with open("configure.json") as f_check:
            receiver_email = json.load(f_check)['alert_email_receiver']
        return receiver_email

    
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
            # Print any error messages to stdout
            print('test ' + str(e))
        finally:
            server.quit() 


    def __compose_message(self, platform, text):
        message = """\
Subject: {}: Scraper alert!

{}""".format(platform, text)

        return message

