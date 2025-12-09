from core.domain.triangle import Triangle
from core.domain.figure_type import FigureType

class RightTriangle(Triangle):
    def __init__(self, vertices):
        super().__init__("Triángulo rectángulo", vertices, FigureType.RIGHT_TRIANGLE)

    