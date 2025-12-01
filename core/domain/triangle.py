import math
from core.domain.figure import Figure
from core.domain.figure_type import FigureType

class Triangle(Figure):
    def __init__(self, name, vertices, figure_type=FigureType.ACUTE_TRIANGLE):
        super().__init__(name, vertices, figure_type)

    def calculate_area(self) -> float:
        """Calculate area using Heron's formula."""
        a = self.vertices[0].distance_to(self.vertices[1])
        b = self.vertices[1].distance_to(self.vertices[2])
        c = self.vertices[2].distance_to(self.vertices[0])

        s = (a + b + c) / 2
        self.area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return self.area