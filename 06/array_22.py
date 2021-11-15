def diff(a):
    maks,minn = None,None
    for i in a:
        if maks == None or maks < i: maks = i
        if minn == None or minn > i: minn = i
    return maks - minn


tab = [5,1,9,6,1]
print(f"Array: {tab}\nResult {diff(tab)}")