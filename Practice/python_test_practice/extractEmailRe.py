import re

text = "Contact: abc@gmail.com or test123@yahoo.com"
email_addr = re.findall(r"\w+@\w+\.\w+", text)

print(email_addr)
