from math import pi
class Surfaces:
    @staticmethod
    def circle(radius):
        print(round(pi*radius**2,2))

    @staticmethod
    def rectangle(length,width):
        print(length*width)

    @staticmethod
    def triangle(base,height):
        print(0.5*base*height)

Surfaces.circle(3)
Surfaces.rectangle(4,7)
Surfaces.triangle(6,2)