import re

text = "The quick brown fox jumps over the  lazy dogs"
pattern = r"[aeiou]"

matches =  re.findall(pattern, text)
print(matches) 