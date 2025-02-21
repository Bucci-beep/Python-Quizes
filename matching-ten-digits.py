# Matching any ten digits
pattern = r"\d{10}"
text = "My phone number is 1234567890"
match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())
else:
    print("Phone number not found")