def count(n,a):
    c = 0
    for i in a:
        if i>n: c+=1
    return c

tab = [4,6.5,4,6,8,2,23,6,2,674,6.7,5.6]
x = int(input("Give any number: "))
print(f"Numbers from array 'tab' greater than {x}: {count(x,tab)}")