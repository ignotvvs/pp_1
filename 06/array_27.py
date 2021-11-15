def display(a):
    text = ""
    for i in range(len(a)):
        if i == 0: text += f"{a[i]}"
        else: text+= f",{a[i]}"

    return text

tab = [5,4,3,2,6,5]
print(display(tab))