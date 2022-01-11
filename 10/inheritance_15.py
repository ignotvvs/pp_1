from math import sqrt
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            print("Distance between two points is 0")
        else:
            d = sqrt((other.x-self.x)**2+(other.y-self.x)**2)
            print(f"Distance between two points is {d}")

p1 = Point(3,4)
p2 = Point(-2,5)
p1 == p2