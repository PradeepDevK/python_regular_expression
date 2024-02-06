import re

# text = "Please contact me at john@example.co or send a message to rob@example.com"
# john@example.com

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"  
text = input("Enter Email Address ")
if re.match(pattern, text):
    print("Valid Email")
else:
    print("Invalid Email") 