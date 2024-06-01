class Rectangle:
    def __init__(self):
        self.length = 0.0
        self.breath = 0.0
    def set_length(self, length):
        if 0.0 < length < 20.0:
            self._length = float(length)
        else:
            print("INVALID LENGTH")
    def get_length(self):
        return self._length
    def set_width(self,width):
        if 0.0 < width < 20.0:
            self._width = float(width)
        else:
            print("INVALID WIDTH")
    def get_width(self):
        return self._width
    def calc_area(self):
        return self._length * self._width
    def calc_perimeter(self):
        return 2 * (self._length + self._width)

rectangle = Rectangle()
rectangle.set_length(18.0)
rectangle.set_width(2.0)
print("LENGTH: ",rectangle.get_length())
print("WIDTH: ",rectangle.get_width())
print("AREA: ",rectangle.calc_area())
print("PERIMETER: ",rectangle.calc_perimeter())