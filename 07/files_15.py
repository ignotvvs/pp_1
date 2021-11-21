x = input("Enter file name: ")
try:
    with open(x) as file:
        count = 0
        for i in file:
            count +=1
    print(f"File name: {x}\nNumber of lines: {count}")
except:
    print("File couldn't be opened")
    exit()