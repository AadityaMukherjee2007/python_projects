import re

text = "My marks are 85 in math and 90 in physics"
nums = re.findall(r"\d+", text)
words = re.findall(r"[a-zA-Z]+", text)

print(nums)
print(words)
