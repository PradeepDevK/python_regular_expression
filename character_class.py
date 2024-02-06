import re

#python, PYTHON

# string = "PYTHON"
# pattern = r"[a-zA-Z]"

string = "0123"
pattern = r"[0-9]"
if re.match(pattern, string):
    print("match found")
else:
    print("no match found")