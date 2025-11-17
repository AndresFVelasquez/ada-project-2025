import math


class Point:
    """
    Represents a point in a 2D Cartesian plane with integer coordinates.
    """
    def __init__(self, x: int, y: int):
        # Integer coordinates
        self.x = x
        self.y = y


    def distance_to(self, other: "Point") -> float:
        """
        Calculate the Euclidean distance between this point and another.
        Returns: float
        """
        pass


    def equals(self, other: "Point") -> bool:
        """
        Check whether two points have exactly the same coordinates.
        Returns: bool
        """
        pass   