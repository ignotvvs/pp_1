x = input("Enter file name: ")
try:
    file = open(x)
except:
    if x == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else: print("File couldn't be opened")
    exit()

count = 0
for line in file:
    line = line.rstrip()
    if not line.startswith("Subject"): continue
    count += 1
print(f"There were {count} subject lines in {x}")