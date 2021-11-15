x = input("Enter file name: ")
try:
    file = open(x)
except:
    print("File couldn't be opened.")
    exit()
for line in file:
    line = line.strip()
    print(line.upper())

file.close()