from abc import ABC, abstractmethod
from core.domain.figure_type import FigureType

class Figure(ABC):
    """
    Abstract base class for geometric figures.
    """
    def __init__(self, name: str, vertices: list, num_sides: int, figure_type: FigureType):
        self.name = name
        self.vertices = vertices # List[Point]
        self.area = 0.0
        self.num_sides = num_sides
        self.type = figure_type

    @property
    def name(self):
        return self._name

    @abstractmethod
    def calculate_area(self) -> float:
        """Abstract method to calculate figure area."""
        raise NotImplementedError("Abstract method")

    @abstractmethod
    def is_valid(self) -> bool:
        """Abstract method to validate if figure is valid."""
        raise NotImplementedError("Abstract method")

    
    def __repr__(self):
        return f"{self._name} with {len(self._points)} points"