with open("sample_for_16.txt") as file:
    count = 0
    for i in file:
        count+=1
        print(i,end="")
        if count%5==0:
            input("Press Enter to continue...")
