
def is_it(a,b):
    for i in a:
        if i not in b: return False
    return True

tab1 = [2,3,6,7,4]
tab2 = [7,6,3,4,2,7,4,2,6,8,9,5,3,6]

print(is_it(tab1,tab2))
