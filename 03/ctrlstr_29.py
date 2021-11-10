quantity = 0
sum = 0
mean = 0
while True:
    a = int(input("enter number: "))
    if a == 0:
        break
    quantity+=1
    sum+=a
if quantity != 0: print(f"RESULT: Quantity = {quantity}, Sum = {sum}, Mean = {sum/quantity}")
else: print("No numbers entered :|")