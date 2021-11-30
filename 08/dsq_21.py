import json

with open('euro.json') as file:
    euro = json.load(file)

print("""
Date              Buying Rate       Selling Rate
================================================""")
for k,v in euro.items():
    if k!="rates":
        continue
    for i in v:
        print(f"{i['effectiveDate']}        {i['bid']}              {i['ask']}")