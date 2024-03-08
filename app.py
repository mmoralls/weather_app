# import packages

from data import extract_data
import smtplib
import ssl
import os
from dotenv import load_dotenv
_ = load_dotenv()

extract_data()

email_address = os.environ.get("gmail_username")
email_password = os.environ.get("gmail_password")

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = email_address
password = email_password
receiver_email = "mmoralls0@gmail.com", "jeraldinemoralls@gmail.com"


with open("weather.txt", "r") as my_file:
    file_content = my_file.read()

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, file_content)
    server.quit()
