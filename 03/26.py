pin = "0805"
proba = 1
while True:
    if proba > 3:
        print("sorry,your paymnet card has been blocked 😕🧍‍")
        break
    pinw = input("enter the pin code: ")
    if pinw != pin:
        print("Incorrect ‍🤨")
        proba+=1
    else:
        print("Ok🤠")
        break