with open("sample.txt") as file,open("copy.txt","w") as file2:
    file2.write(file.read())