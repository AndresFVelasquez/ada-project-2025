from core.figure import Figure


class Triangle(Figure):
    def __init__(self, points):
        super().__init__(points, name = "Triangle")