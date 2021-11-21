import re

text = "To be, or not to be, that is the question"

words = re.findall("\w+",text)

print(len(words))