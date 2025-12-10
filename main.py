from core.ui.menu import Menu
from core.domain.point import Point
from core.detector.shape_detector import ShapeDetector
from core.ui.draw_service import DrawService
from core.ui.cartesian_plane_component import CartesianPlaneComponent


def main():
    menu = Menu()
    
    """
    points = [
        Point(0, 0),
        Point(3, 0),
        Point(0, 4),
        Point(3, 4),
        Point(-1,2)
    ]

    figures = ShapeDetector.detect_shapes(points)
    plane = CartesianPlaneComponent(DrawService())
    plane.update(points)


    for f in figures:
        print(f"Figura detectada: {f.type.name} -> x:{f.vertices}")
    """
        

if __name__ == "__main__":
    Menu().run()
