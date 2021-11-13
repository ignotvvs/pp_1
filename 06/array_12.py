from array_10 import array2str

numbers = [15, 8, 31, 47, 2, 19]
print(f"Array: {array2str(numbers)}")
print("Reverse array: ",end="")

for i in range(len(numbers)-1,-1,-1): print(numbers[i],end=" ")