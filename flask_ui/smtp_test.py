from dotenv import load_dotenv
import os, smtplib

load_dotenv()
cred = os.getenv("PASS", "default_pass")
# print(cred)

from_add = "aaditya.mukherjee2019@gmail.com"
to_add = "aaditya.mukherjee2007@gmail.com"
msg = "This is a test message"

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_add, cred)
    server.sendmail(from_add, to_add, msg)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    server.quit()
