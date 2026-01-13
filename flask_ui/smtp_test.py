from json import load
from dotenv import load_dotenv
import os, smtplib

load_dotenv()

from_add = "aaditya.mukherjee2007@gmail.com"
to_add = "aaditya.mukherjee2007@gmail.com"
msg = "This is a test message"

server = smtplib.SMTP("localhost")
server.set_debuglevel(1)
server.sendmail(from_add, to_add, msg)
server.quit()