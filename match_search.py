import re

string = "bca"
pattern = "a"
#match search the pattern in the beginning of the string
if re.match(pattern, string):
    print("match found")
else:
    print("no match found")

#search go through the entire string
if re.search(pattern, string):
    print("match found")
else:
    print("no match found")