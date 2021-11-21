from random import randint
with open("numbers2.txt", "w") as file:
    for i in range(50):
        x = randint(100,999)
        file.write(str(x) + "\n")