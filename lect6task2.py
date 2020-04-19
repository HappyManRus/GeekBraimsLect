class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    # методы класса
    def mas_asfalt(self):
        return self._length * self._width * 25 * 0.005


roadclass = Road(20, 5000)
print(roadclass.mas_asfalt())
