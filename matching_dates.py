import re

text = "Date: 2023-06-08 08-09-2023 1991-01-02"
pattern = r"\d{4}-\d{2}-\d{2}"

matches = re.findall(pattern, text)
print(matches)