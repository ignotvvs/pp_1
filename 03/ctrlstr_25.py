a = int(input("podaj a: "))
b = int(input("podaj b: "))

for i in range(0,a):
    if i == a-1 or i == 0:
        print("*"*b)
    else:
        print("*"+" "*(b-2) + "*")