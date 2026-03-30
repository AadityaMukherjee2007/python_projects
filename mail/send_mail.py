from dotenv import load_dotenv
import os, smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
from_add = os.getenv("GMAIL", "...")
from_cred = os.getenv("PASS", "...")

to_add = [
    "aaditya.mukherjee2007@gmail.com", 
    "aaditya.mukherjee2007+1@gmail.com",
    "aaditya.mukherjee2007+2@gmail.com"
]

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

def send_email(sender=from_add, recipients="", subject="", message="", html_template=""):
    # Ensure recipients is properly formatted
    if isinstance(recipients, list):
        recipients_str = ','.join(recipients)
        recipients_list = recipients
    else:
        recipients_str = recipients
        recipients_list = [r.strip() for r in recipients.split(',') if r.strip()]
    
    msg = MIMEMultipart("alternative")
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients_str
    msg.attach(MIMEText(
        html_template if html_template else message, "html"
    ))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, recipients_list, msg.as_string()
        )
        print(f"Email sent successfully to {len(recipients_list)} recipient(s)!")

if __name__ == "__main__":
    send_email(sender=from_add, recipients=to_add, html_template=html)