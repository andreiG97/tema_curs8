import math


class Cerc:
    def __init__(self, r):
        self._r = r

    def get_radius(self):
        return self._r

    def set_radius(self, r):
        self._r = r

    def area(self):
        return 2 * math.pi * self._r ** 2

    def perimeter(self):
        return 2 * math.pi * self._r


c1 = Cerc(10)

print(c1.get_radius())

c1.set_radius(15)

print(c1.get_radius())
print(c1.area())
print(c1.perimeter())
