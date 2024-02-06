import re

text = "Please contact me at +12 (123) 456-7890 or via email at john@example.com"
# text = "Please contact me at +919898989898 or via email at john@example.com"

# +1 (123) 456-7890
#\+ -> this is not a metacharacter instead of it search + character

pattern = r"\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?\d{1,4}"  

matches =  re.findall(pattern, text)
print(matches) 