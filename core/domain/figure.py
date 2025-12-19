from abc import ABC, abstractmethod
from core.domain.figure_type import FigureType

class Figure(ABC):
    """
    Abstract base class for geometric figures.
    """
    def __init__(self, name: str, vertices: list, figure_type: FigureType):
        self.id = 0
        self.name = name
        self.vertices = vertices
        self.type = figure_type
        self.num_sides = len(vertices)
        self.area = 0.0
        # Calculate the area before returning the figure
        self.calculate_area()

    @abstractmethod
    def calculate_area(self) -> float:
        """Calculate and return the area of the figure."""
        pass

    def __repr__(self):
        return f"{self.name} ({self.type}) with {self.num_sides} sides"