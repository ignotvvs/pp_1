with open("MeatAndFish.txt") as one,open("GrainsAndBread.txt") as file2,open("shoppinglist.txt","w") as three:
    three.write(one.read() + "\n" + file2.read())