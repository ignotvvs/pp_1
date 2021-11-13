from array_10 import array2str

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
print(f"Names: {array2str(names)}")

long = None
lname = None
for i in names:
    if long == None or len(i) > long:
        long = len(i)
        lname = names.index(i)


print(f"Longest name: {names[lname]}")
