import unittest
from core.domain.point import Point

class TestPoint(unittest.TestCase):

    def test_coordinates_are_integers(self):
        with self.assertRaises(ValueError):
            Point(3.5, 2)
        with self.assertRaises(ValueError):
            Point(1, "x")

    def test_equals(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(2, 3)

        self.assertTrue(p1.equals(p2))
        self.assertFalse(p1.equals(p3))

    def test_distance(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)

        self.assertEqual(p1.distance_to(p2), 5.0)

    def test_distance_with_invalid_object(self):
        p1 = Point(0, 0)
        with self.assertRaises(TypeError):
            p1.distance_to("not a point")

"""if __name__ == "__main__":
    unittest.main()"""