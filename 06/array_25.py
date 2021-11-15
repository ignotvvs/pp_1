def minmax(a):
    minn,maks = None,None
    for i in a:
        if minn == None or minn > i: minn = i
        if maks == None or maks < i: maks = i
    return [minn,maks]

tab = [4,2,8,4,7,9,5]
print(f"Array {tab}\nResult: {minmax(tab)}")