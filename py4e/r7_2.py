x = input("Enter file name: ")
try:
    file = open(x)
except:
    print("File couldn't be opened.")
    exit()

suma,count = 0,0
for line in file:
    line.rstrip()
    if not line.startswith("X-DSPAM-Confidence: "): continue
    z = line.find(" ")
    count+=1
    suma += float(line[z+1:])
print(suma/count)