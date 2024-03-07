# import packages

from data import extract_data
import smtplib, os, ssl
from dotenv import load_dotenv
_ = load_dotenv()

extract_data()

def send_mail():
    email_address = os.environ.get("gmail_username")
    email_password = os.environ.get("gmail_password")

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = email_address
    # Enter receiver address
    receiver_email = "mmoralls0@gmail.com"
    password = email_password

    #finally!; file is opened, read and parsed into the email
    with open("weather.txt", "r") as my_file:
        file_content = my_file.read()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, file_content)
        server.quit()
