with open("shopping.txt","a") as file:
    while True:
        x = input("Enrer the product name (0 to stop): ")
        if x == "0": break
        file.write(x + "\n")