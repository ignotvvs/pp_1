def sum_digits(n):
    sum = 0
    for i in str(n):
        sum+=int(i)
   # while n>0:
    #    sum +=n%10
     #   n = n//10
    return sum

print(sum_digits(7182))
