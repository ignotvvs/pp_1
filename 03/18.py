amount = int(input("Enter the amount in PLN: "))
piatki,dwojki = 0,0
if 5<=amount:
    piatki = amount//5
    amount -=piatki*5
if 2<= amount:
    dwojki = amount//2
    amount -= dwojki*2
print(f"5 zl - {piatki}\n2 zl - {dwojki}\n 1 zl - {amount}")