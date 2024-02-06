import re

text = "the sun is shining, the birds are singing"
pattern = r"the"

matches =  re.findall(pattern, text)
print(matches) 