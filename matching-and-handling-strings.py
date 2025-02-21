import re
s1 = "I am learning Python"
pattern = r"Python"
result = re.search(pattern, s1) 

if result:
    print("Match found")  
else:   
    print("Match not found")

# Matching any ten digits
pattern = r"\d{10}"
text = "My phone number is 1234567890"
match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())
else:
    print("Phone number not found")