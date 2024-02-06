import re

text = "The cat and the dog sat on the mat."
pattern = r"[abc]"

matches =  re.findall(pattern, text)
print(matches) 