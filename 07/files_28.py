import re

with open("grades.txt") as file:
    text = file.read()

grades = re.findall(r"\d\.\d{1,2}",text)
total = 0
for i in grades:
    total+= float(i)
print(total/len(grades))