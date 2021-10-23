sum = 0
count = 0
avg = 0
while True:
    try:
        x = input("gimmie: ")
        if x == 'done':
            break
        sum +=int(x)
        count +=1
    except:
        print("this ain't a number buddy 🤠")
print(sum,count,sum/count)