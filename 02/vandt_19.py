a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
s = (a+b+c)/2
formula = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"Pole trojkata wynosi {formula}")