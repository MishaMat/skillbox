import re

text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
print(re.match(r"wo", text))
print(re.search(r"wo", text))
print(re.search(r"wo", text).group(0))
print(re.search(r"wo", text).start())
print(re.search(r"wo", text).end())
print(re.findall(r"wo", text))
print(re.sub(r"wo", "SWAP", text))
print("=" * 20)
text = "How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,"
pattern = r"\\wwood\+\?\,"
print(pattern)
print(re.findall(pattern, text))
