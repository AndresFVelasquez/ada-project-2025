from abc import ABC, abstractmethod

class Figure(ABC):
    """
    Abstract base class for geometric figures.
    """

    def __init__(self, points: list, name: str = "Figure"):
        self._name = name
        self._points = points
        self._area = 0.0
        self._number_sides = len(points)


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