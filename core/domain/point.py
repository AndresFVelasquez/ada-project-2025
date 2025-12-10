import math


class Point:
    
    """
    Represents a point in a 2D Cartesian plane with integer coordinates.
    """
    def __init__(self, x: int, y: int):
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Coordinates must be integers.")

        self.x = x
        self.y = y


    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def distance_to(self, other: "Point") -> float:
        """
        Calculate the Euclidean distance between this point and another.
        """
        if not isinstance(other, Point):
            raise TypeError("Argument must be a Point.")

        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)

    def equals(self, other: "Point") -> bool:
        """
        Check whether two points have exactly the same coordinates.
        """
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    