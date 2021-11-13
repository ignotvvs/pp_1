from array_10 import array2str
def occurs(number,array):
    for i in array:
        if number==i:
            return True
    return False

n = 23
numbers = [15,38,7,23,14]
print(f"Number: {n}\nArray: {array2str(numbers)}")
print(f"Result: ",end="")
if occurs(n,numbers):
    print(f"number {n} appears in the array")
else:
    print(f"number {n} doesn't appear in the array")