import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall(r"\d{2}",message)

total = 0
for i in temperatures:
    total +=int(i)

print(total/len(temperatures))