import json

with open("sample2.json") as file:
    data = json.load(file)

for k,v in data.items():
    print(k,":",v)