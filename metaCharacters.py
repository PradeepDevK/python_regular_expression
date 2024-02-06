import re

# * character should be present or not present
string = "abbbbc"
pattern = r"ab*c"
if re.match(pattern, string):
    print("match found")
else:
    print("no match found")

# + the character should atleast present one time
string1 = "abbbc"
pattern1 = r"ab+c"
if re.match(pattern1, string1):
    print("match found")
else:
    print("no match found")

# {} repeats a character at least x times
string2 = "abbbbbb"
pattern2 = r"ab{2}"
if re.match(pattern2, string2):
    print("match found")
else:
    print("no match found")

# . can take place any other symbol
string3 = "acbb"
pattern3 = r"a.b"
if re.match(pattern3, string3):
    print("match found")
else:
    print("no match found")

# ? is optional, (i.e. it may or may not be present)
string4 = "ab"
pattern4 = r"abc?"
if re.match(pattern4, string4):
    print("match found")
else:
    print("no match found")

# ^ that the match must start at the  beginning  of the string (or) the line
string5 = "919898989898"
pattern5 = r"^92"
if re.match(pattern5, string5):
    print("match found")
else:
    print("no match found")