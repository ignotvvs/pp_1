def computepay(rate,hours):
    if hours > 40:
        print(f"Pay: {40*rate+(hours-40)*rate*1.5}")
    else:
        print(f"Pay: {hours*rate}")
try:
    h = int(input("Enter hours: "))
    r = int(input("Enter rate: "))
    computepay(r,h)
except:
    print("ERROR | enter a number")