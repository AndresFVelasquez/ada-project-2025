from core.domain.figure import Figure
from core.domain.figure_type import FigureType

class Square(Figure):
    def __init__(self, vertices):
        super().__init__("Cuadrado", vertices, FigureType.SQUARE)

    def calculate_area(self) -> float:
        side = self.vertices[0].distance_to(self.vertices[1])
        self.area = side * side
        return self.area
