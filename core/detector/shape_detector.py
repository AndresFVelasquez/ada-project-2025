import math
from core.domain.point import Point
from core.factory.figure_factory import FigureFactory
from core.domain.figure_type import FigureType


class ShapeDetector:
    """
    Static class responsible for detecting geometric shapes from
    combinations of 3 and 4 points.
    """

    # ----------------------------------------------------
    # MÉTODOS PRINCIPALES
    # ----------------------------------------------------
    @staticmethod
    def detect_shapes(point_list: list) -> list:
        figures = []

        # 1. Triángulos
        for combo in ShapeDetector.combine_three_points(point_list):
            if ShapeDetector.is_right_triangle(combo):
                fig = FigureFactory.create_figure(
                    ShapeDetector.normalize_vertices(combo),
                    FigureType.RIGHT_TRIANGLE,
                )
                figures.append(fig)
            elif ShapeDetector.is_acute_triangle(combo):
                fig = FigureFactory.create_figure(
                    ShapeDetector.normalize_vertices(combo),
                    FigureType.ACUTE_TRIANGLE,
                )
                figures.append(fig)

        # 2. Cuadriláteros
        for combo in ShapeDetector.combine_four_points(point_list):
            if ShapeDetector.is_square(combo):
                fig = FigureFactory.create_figure(
                    ShapeDetector.normalize_vertices(combo),
                    FigureType.SQUARE,
                )
                figures.append(fig)
            elif ShapeDetector.is_rectangle(combo):
                fig = FigureFactory.create_figure(
                    ShapeDetector.normalize_vertices(combo),
                    FigureType.RECTANGLE,
                )
                figures.append(fig)

        return figures

    # ----------------------------------------------------
    # NORMALIZACIÓN / UTILIDADES
    # ----------------------------------------------------
    @staticmethod
    def normalize_vertices(points: list) -> list:
        if len(points) not in (3, 4):
            raise ValueError("normalize_vertices solo acepta 3 o 4 puntos")

        n = len(points)

        # 1. Calcular centroide
        cx = 0
        cy = 0
        for p in points:
            cx += p.x
            cy += p.y
        cx /= n
        cy /= n

        # 2. Calcular ángulos polares
        angles = []
        for p in points:
            ang = math.atan2(p.y - cy, p.x - cx)
            angles.append(ang)

        # 3. Ordenamiento por inserción (descendente: sentido horario)
        for i in range(1, n):
            key_point = points[i]
            key_angle = angles[i]
            j = i - 1

            while j >= 0 and angles[j] < key_angle:
                points[j + 1] = points[j]
                angles[j + 1] = angles[j]
                j -= 1

            points[j + 1] = key_point
            angles[j + 1] = key_angle

        return points
        

    @staticmethod
    def side_length(p1: Point, p2: Point) -> float:
        return p1.distance_to(p2)

    # ----------------------------------------------------
    # COMBINACIONES
    # ----------------------------------------------------
    @staticmethod
    def combine_three_points(points: list) -> list:
        results = []
        n = len(points)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    results.append([points[i], points[j], points[k]])
        return results

    @staticmethod
    def combine_four_points(points: list) -> list:
        results = []
        n = len(points)
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        results.append([points[i], points[j], points[k], points[l]])
        return results

    # ----------------------------------------------------
    # TRIÁNGULOS
    # ----------------------------------------------------

    @staticmethod
    def angle_at(points, i):
        p = points[i]
        p_prev = points[(i - 1) % 3]
        p_next = points[(i + 1) % 3]

        v1 = (p_prev.x - p.x, p_prev.y - p.y)
        v2 = (p_next.x - p.x, p_next.y - p.y)

        dot = v1[0] * v2[0] + v1[1] * v2[1]
        return dot

    @staticmethod
    def is_right_triangle(points: list) -> bool:
        if len(points) != 3:
            return False

        for i in range(3):
            dot = ShapeDetector.angle_at(points, i)
            if abs(dot) < 1e-6:
                return True
        return False

    @staticmethod
    def is_acute_triangle(points: list) -> bool:
        if len(points) != 3:
            return False

        for i in range(3):
            if ShapeDetector.angle_at(points, i) <= 0:
                return False
        return True

    # ----------------------------------------------------
    # CUADRILÁTEROS
    # ----------------------------------------------------
    @staticmethod
    def is_rectangle(points: list) -> bool:
        if len(points) != 4:
            return False

        vertices = ShapeDetector.normalize_vertices(points)

        for i in range(4):
            p = vertices[i]
            p_prev = vertices[(i - 1) % 4]
            p_next = vertices[(i + 1) % 4]

            v1 = (p_prev.x - p.x, p_prev.y - p.y)
            v2 = (p_next.x - p.x, p_next.y - p.y)

            dot = v1[0] * v2[0] + v1[1] * v2[1]
            if abs(dot) > 1e-6:
                return False

        sides = [
            ShapeDetector.side_length(vertices[i], vertices[(i + 1) % 4])
            for i in range(4)
        ]

        return abs(sides[0] - sides[2]) < 1e-6 and abs(sides[1] - sides[3]) < 1e-6

    @staticmethod
    def is_square(points: list) -> bool:
        if not ShapeDetector.is_rectangle(points):
            return False

        vertices = ShapeDetector.normalize_vertices(points)
        s = ShapeDetector.side_length

        side0 = s(vertices[0], vertices[1])
        for i in range(1, 4):
            if abs(s(vertices[i], vertices[(i + 1) % 4]) - side0) > 1e-6:
                return False

        return True
