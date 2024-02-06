import re

text = "The variable name is my_var123! \n"
# pattern = r"\w" # this particular shorthand matches any alphanumeric characters, which includes letters and digits

pattern = r"\W" # this particular shorthand matches non alphanumeric characters. (i.e whitespaces..)

matches =  re.findall(pattern, text)
print(matches) 