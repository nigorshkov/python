class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mass):
        return '{:.0f}'.format(self._length * self._width * mass / 1000)

a = Road(20, 5000)
print(a.mass(125))