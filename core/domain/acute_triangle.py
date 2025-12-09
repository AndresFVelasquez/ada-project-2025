from core.domain.triangle import Triangle
from core.domain.figure_type import FigureType

class AcuteTriangle(Triangle):
    def __init__(self, vertices):
        super().__init__("Triángulo Agudo", vertices, FigureType.ACUTE_TRIANGLE)

    