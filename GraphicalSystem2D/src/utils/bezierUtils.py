import numpy as np

from structures.Point import Point

BEZIER_MATRIX = [[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]]


class BezierGeoMatrix:
    def __init__(self, x: list[list[float]], y: [list[list[float]]]):
        self.x = x
        self.y = y


def getGBBezier(p0: Point, p1: Point, p2: Point, p3: Point) -> BezierGeoMatrix:
    gb_x = [[p0.getX()], [p1.getX()], [p2.getX()], [p3.getX()]]

    gb_y = [[p0.getY()], [p1.getY()], [p2.getY()], [p3.getY()]]

    return BezierGeoMatrix(gb_x, gb_y)


def blendingFunction(t: float, gb: list[list[float]]) -> float:
    m_t = [[t**3, t**2, t, 1]]
    blending = np.dot(m_t, BEZIER_MATRIX)
    
    return np.dot(blending, gb)[0][0]
