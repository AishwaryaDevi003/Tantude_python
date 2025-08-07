import re
text =input("Enter a phn num to search for the pattern: ")
pattern = r"\+91\d{10}" 
match = re.search(pattern, text)
if match:
    print("Phn num is valid:", match.group())
else:
    print("Phn num is not valid.")