plik = open("color.txt",'w')
numbers = ["red","blue","green","black","white"]
for i in numbers:
    plik.write(f"{i}\n")

plik.close()