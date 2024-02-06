import re

string = "abc"
pattern = "a"
if re.match(pattern, string):
    print("match found")
else:
    print("no match found")