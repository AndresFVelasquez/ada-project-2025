import json
from core.point import Point
from core.figure import Figure

class DataManager:
    """
    Manages points and figures storage and persistence.
    """
    def __init__(self):
        self.points: list[Point] = []
        self.figures: list[Figure] = []

    def save_points(self, filename: str = "data.json"):
        """Save points and figures to a JSON file."""
        pass

    def load_points(self, filename: str = "data.json"):
        """Load points and figures from a JSON file."""
        pass