numbers = ["red","blue","green","black","white"]
with open("color.txt",'w') as plik:
    for i in numbers:
        print(i,file=plik)
