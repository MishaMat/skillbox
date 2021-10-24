import re

text = ['9999999999', '999999-999', '99999x9999']
pattern = r"\b[8,9]\d{9}\b"
for i, j in enumerate(text):
    if re.findall(pattern, j):
        print(f"{i} phone number is ok")
    else:
        print(f"{i} phone number is not ok")
print("bye")
