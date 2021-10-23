wariant = 1
# 1 wariant
if wariant == 1:
    n = int(input("Enter n: "))
    pomoc = False
    for i in range(2,n+1):
        for j in range(2,int(i**0.5)+1):
            if i%j==0: pomoc = True
        if pomoc == False: print(i,end="  ")
        pomoc = False

# 2 wariant
def pierwsze(s):
    if s<2:return 0
    for i in range(2,int(s**0.5)+1):
        if s%i==0: return 0
    return 1
if wariant == 2:
    n = int(input("Enter n: "))
    prime = []
    x=2
    while len(prime)<n:
        if pierwsze(x) == 1: prime.append(x)
        x+=1
    print(prime)