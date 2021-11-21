with open("numbers.txt") as file:
    suma = 0
    for i in file:
        suma += int(i)

print(suma)
