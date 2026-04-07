
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius   

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

c1 = Circle(5)

print("Radius:", c1.radius)
print("Area of circle:", c1.area())
print("Perimeter of circle:", c1.perimeter())