import stack
print(dir(stack))

x = input("Natural number: ")
s = stack.stack

while x != 0:
    rem = int(x) % 2
    x = int(x) // 2
    stack.push(rem)

print("Binary number: ",end="")
while not stack.empty():
    print(stack.pop(),end="")
