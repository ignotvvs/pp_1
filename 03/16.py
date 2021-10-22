number_uno = int(input("Podaj numer uno: "))
number_zwei = int(input("Podaj numer zwei: "))
if number_zwei > number_uno:
    print(f"Liczby rosnaca: {number_uno},{number_zwei}")
else:
    print(f"Liczby rosnaca: {number_zwei},{number_uno}")