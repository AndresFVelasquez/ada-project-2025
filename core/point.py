import math


class Point:
    """
    Represents a point in a 2D Cartesian plane.
    """
     
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other_point):
        """Calculate the distance between this point and another."""
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
    def show_cords(self):
        """Show the coordinates of this point"""
        print(f"X = {self.x} ; Y = {self.y}")
        