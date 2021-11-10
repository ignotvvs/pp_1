try:
    hours = int(input("Enter hours: "))
    rate = int(input("Enter rate: "))
    if hours > 40:
        print(f"Pay: {40*rate+(hours-40)*rate*1.5}")
    else:
        print(f"Pay: {hours*rate}")
except:
    print("ERROR | enter a number")