# import packages

import smtplib
import ssl
import os
from email.message import EmailMessage
from dotenv import load_dotenv
_ = load_dotenv()


def send_mail():
    email_address = os.environ.get("EMAIL_ADDRESS")
    email_password = os.environ.get("EMAIL_PASSWORD")

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = email_address
    # Enter receiver address
    receiver_email = "mmoralls0@gmail.com", "jeraldinemoralls@gmail.com"
    password = email_password

    msg = open('weather.txt', 'r').read()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)
