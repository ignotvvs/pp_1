def power(x,n):
    if n == 1:
        return x
    return power(x,n-1)*x
print(power(5,3))