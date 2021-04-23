class Punct:
    
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_value(self):
        return self._x, self._y

    def set_coordinates(self, x, y):
        self._x = x
        self._y = y


p1 = Punct()
p2 = p1

print(p1.get_value())
print(p2.get_value())

p1.set_coordinates(10, 15)

print(p1.get_value())
print(p2.get_value())