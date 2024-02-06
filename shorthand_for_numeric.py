import re

text = "The meeting is scheduled at 9 AM"
# pattern = r"[0-9]"
# pattern = r"\d" # get all the numeric digits
pattern = r"\D" # get all the characters in string

matches =  re.findall(pattern, text)
print(matches) 