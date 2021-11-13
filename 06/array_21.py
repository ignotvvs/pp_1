def maks(n):
    a = None
    for i in n:
        if a == None or i>a:
            a=i
    return a

numbers = [5,1,10,6,10,4,6,8,9,11,11]

sec_max = None

for i in numbers:
    if sec_max == None or (i>sec_max and i < maks(numbers)):
        sec_max = i


print(f"Array: {numbers}")
print(f"Result: {sec_max}")

