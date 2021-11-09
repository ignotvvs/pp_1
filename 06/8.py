numbers = [-15, 8, -31, 47, -2, 19]
#print(min(numbers),max(numbers))
maks,minn = None,None
for i in numbers:
    if maks == None or i > maks: maks = i
    if minn == None or i < minn: minn = i
print(maks,minn)