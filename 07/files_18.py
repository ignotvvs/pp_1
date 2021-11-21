with open("sample.txt") as file, open("copylines.txt","w") as file2:
    for i in file:
        file2.write(i)