class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_calc(self, thickness):
        __weight_per_m2 = 25
        return self._length * self._width * __weight_per_m2 * thickness


rd = Road(5000, 20)
print(f'Weight for the road is {rd.weight_calc(5)}kg')
