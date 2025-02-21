import re
pattern = r"\W"
text = "Hello, world!?#$"
matches = re.findall(pattern, text)
print("Matches:", matches)