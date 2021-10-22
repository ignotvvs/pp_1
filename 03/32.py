for i in range(1,8):
    print(i, end=" ")
    for j in range(1,7):
        if j == 6: print(i+7*j)
        else:
            if i+7*j < 10: print(end=" ")
            print(i+7*j, end=" ")
