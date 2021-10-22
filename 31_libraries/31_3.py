import re

text = "Even if they are djinns, I will get djinns that can outdjinn them."
pattern = r"\b[aoiyeAOIEY]\w*"
print(re.findall(pattern, text))
pattern_2 = r"\b[^\saoiyeAOIEY]\w+"
print(re.findall(pattern_2, text))

print("=" * 20)

text_2 = "Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009"
pattern_3 = "\d{2}-\d{2}-\d{4}"
print(re.findall(pattern_3, text_2))