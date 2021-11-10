fib1 = 0
fib2 = 1
print(fib1,fib2,end=" ")
for i in range(3,51):
    a = fib1 + fib2
    fib1 = fib2
    fib2 = a
    print(a, end=" ")