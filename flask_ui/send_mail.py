from dotenv import load_dotenv
import os, smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
from_add = os.getenv("GMAIL", "...")
from_cred = os.getenv("PASS", "...")

to_add = ["aaditya.mukherjee2007@gmail.com"]

smtp_server = "smtp.gmail.com"
port = 465  # For SSL
sender_email = from_add
receiver_email = to_add
password = from_cred

html = """
<html>
    <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; padding: 20px;">
        <h1>This is a test email</h1>
        <p>This email is sent using Python's smtplib library.</p>
    </body>
</html>
"""

def send_email(sender="<EMAIL>", recipients=[], html_template=""):
    msg = MIMEMultipart("alternative")
    msg['Subject'] = "Test Email from SMTP"
    msg['From'] = sender
    msg['To'] = ", ".join(recipients) if len(recipients) != 1 else recipients[0]
    msg.attach(MIMEText(
        html if not html_template else html_template, "html"
    ))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, msg.as_string()
        )
        print("Email sent successfully!")