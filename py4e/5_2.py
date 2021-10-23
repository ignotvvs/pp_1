sum = 0
count = 0
maks,mini = None,None
while True:
    try:
        x = input("gimmie: ")
        if x == 'done':
            break
        sum +=int(x)
        count +=1
        if maks == None or maks < x:
            maks = x
        if mini == None or mini > x:
            mini = x
    except:
        print("this ain't a number buddy 🤠")
print(sum,count,maks,mini)