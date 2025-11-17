import json
from core.domain.point import Point
from core.domain.figure import Figure

class DataManager:
    """
    Handles saving and loading points and figures from files.
    """


    points = []
    figures = []


    @staticmethod
    def save_points():
        """Persist the list of points to a file (JSON recommended)."""
        pass


    @staticmethod
    def load_points():
        """Load points from a file and restore internal structure."""
        pass


    @staticmethod
    def save_figures():
        """Persist the list of figures to a file (JSON recommended)."""
        pass


    @staticmethod
    def load_figures():
        """Load figures from a file and restore internal structure."""
        pass


    @staticmethod
    def add_point(point: Point):
        """Add a point ensuring no duplicates exist."""
        pass


    @staticmethod
    def remove_point(point: Point):
        """Remove a point if present."""
        pass


    @staticmethod
    def get_points() -> list:
        """Return the list of stored points."""
        pass


    @staticmethod
    def get_figures() -> list:
        """Return the list of stored figures."""
        pass