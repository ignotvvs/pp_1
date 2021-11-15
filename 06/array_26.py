def separate(a):
    even,odd = [],[]
    for i in a:
        if i%2: odd.append(i)
        else: even.append(i)
    return even  + odd

tab = [3,5,2,6,9,10,11,4,7]
print(separate(tab))