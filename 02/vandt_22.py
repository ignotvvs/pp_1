import random
number = random.randint(1,6)
print("Jaka liczba zostala wylosowana?")
while 1:
    x = int(input("Liczba: "))
    if x == number:
        print(True)
        break
