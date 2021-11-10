numbers = [6,2,1,3,7,8,9,23,53,12,13,15]
odd = 0
even = 0
for i in numbers:
    if i%2 == 0: even+=1
    else: odd +=1
print(f"Even numbers: {even}, odd numbers: {odd}")