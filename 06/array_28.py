import random
tab = []
for i in range(5):
    tab.append(random.randint(1,999))
print("-"*(len(tab)*6+1))
print("|",end="")
for i in tab:
    print(f"  {i}|",end = "")
print("\n",end = "")
print("-"*(len(tab)*6+1))
