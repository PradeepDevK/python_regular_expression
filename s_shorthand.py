import re

text = "The variable \t name is my_var123! \n"
# pattern = r"\s" #this is special shorthand for finding all the spaces tabs on new lines
# pattern = r"\S" #this uppercase S is a special shorthand for finding all the non whitespace
pattern = r"\S+" # + metacharacter, will get the combined string in a list

matches =  re.findall(pattern, text)
print(matches) 