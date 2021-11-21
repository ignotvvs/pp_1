with open("countries.txt") as file:
    count = 1
    for line in file:
        print(count,line, end = "")
        count+=1