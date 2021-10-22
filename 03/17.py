x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
if x == 0 and y == 0:
    print(f"point P({x},{y}) is on the position (0,0)")
if x > 0 and y > 0:
    print(f"point P({x},{y}) is in the first quadrant of the coordinate system")
elif y < 0 and x < 0:
    print(f"point P({x},{y}) is in the third quadrant of the coordinate system")
elif x < 0:
    print(f"point P({x},{y}) is in the second quadrant of the coordinate system")
elif y < 0:
    print(f"point P({x},{y}) is in the fourth quadrant of the coordinate system")