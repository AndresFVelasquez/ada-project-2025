from core.domain.figure import Figure
from core.domain.figure_type import FigureType

class Rectangle(Figure):
    def __init__(self, name, vertices):
        super().__init__(name, vertices, FigureType.RECTANGLE)

    def calculate_area(self) -> float:
        """
        Assumes vertices are ordered; ShapeDetector ensures valid rectangle.
        [Inferencia]: base = v0-v1, height = v1-v2
        """
        base = self.vertices[0].distance_to(self.vertices[1])
        height = self.vertices[1].distance_to(self.vertices[2])
        self.area = base * height
        return self.area