import re

text = "Helloooo, Python is awesomeeee!"
pattern = r"\w*o+\w*"

# \w* -> matches zero or more alphanumeric characters
# o+ -> matches one or more occurences of the letter 'o'

matches =  re.findall(pattern, text)
print(matches) 

#o
#ao
#aoo
#aoooob
#oooob