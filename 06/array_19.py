from array_10 import array2str
numbers = [2,3,2,5,9,1,9,8]
print(f"Array: {array2str(numbers)}")

print("Unique elements: ",end= "")

#for i in numbers:
#    if numbers.count(i) == 1:
#        print(i,end= " ")
for i in numbers:
    count = 0
    for j in numbers:
        if i == j: count+=1
    if count == 1:
        print(i,end = " ")