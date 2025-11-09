from core.figure import Figure

class Rectangle(Figure):
    def __init__(self, points):
        super().__init__(points, name = "Rectangle")