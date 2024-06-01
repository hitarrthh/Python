class Square:
    def __init__(self, side):
        self.side = side
    def calc_area(self):
        return self.side * self.side

class Rectangle:
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath
    def calc_area(self):
        return self.length * self.breath

square = Square(10)
rectangle = Rectangle(20,30)
print("AREA OF SQUARE IS: ", square.calc_area())
print("AREA OF RECTANGLE IS: ", rectangle.calc_area())