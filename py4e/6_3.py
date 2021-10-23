def count(s,l):
    counter = 0
    for i in s:
        if i == l: counter+=1
    return counter
print(count("banana","a"))
a = 'banana'
print(a.count('a'))