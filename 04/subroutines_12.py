def sum(n):
    """calculates the sum of all  ntrl numbers between 1 and N"""
    if n == 1:
        return 1
    else:
        return sum(n-1)+n
print(sum(10))