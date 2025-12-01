from core.domain.triangle import Triangle
from core.domain.figure_type import FigureType

class RightTriangle(Triangle):
    def __init__(self, name, vertices):
        super().__init__(name, vertices, FigureType.RIGHT_TRIANGLE)

    