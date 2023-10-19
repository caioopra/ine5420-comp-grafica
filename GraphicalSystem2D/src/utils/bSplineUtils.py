from numpy import array, dot

from structures.Point import Point

from utils.viewportTransformation import viewportTransformation
from utils.clipping.CurveClipping import curveClip

BSPLINE_MATRIX = [
    [-1 / 6, 1 / 2, -1 / 2, 1 / 6],
    [1 / 2, -1, 1 / 2, 0],
    [-1 / 2, 0, 1 / 2, 0],
    [1 / 6, 2 / 3, 1 / 6, 0],
]


class BSplineGeoMatrix:
    def __init__(self, x: list[list[float]], y: list[list[float]]):
        self.x = x
        self.y = y


def calculateDeltaMatrix(delta: float) -> array:
    delta2 = delta**2
    delta3 = delta2 * delta

    return array(
        [
            [0, 0, 0, 1],
            [delta3, delta2, delta, 0],
            [6 * delta3, 2 * delta2, 0, 0],
            [6 * delta3, 0, 0, 0],
        ]
    )


def getGBSpline(p0: Point, p1: Point, p2: Point, p3: Point) -> BSplineGeoMatrix:
    gb_spline_x = [[p0.getX()], [p1.getX()], [p2.getX()], [p3.getX()]]
    gb_spline_y = [[p0.getY()], [p1.getY()], [p2.getY()], [p3.getY()]]

    return BSplineGeoMatrix(gb_spline_x, gb_spline_y)


def getInitialCurve(delta_matrix: array, gb: BSplineGeoMatrix) -> tuple:
    cx = dot(BSPLINE_MATRIX, gb.x)
    cx = dot(delta_matrix, cx)

    cy = dot(BSPLINE_MATRIX, gb.y)
    cy = dot(delta_matrix, cy)

    return cx, cy


def forward_difference(n: int, dx: array, dy: array, painter, window) -> None:
    x, dx, d2x, d3x = [x[0] for x in dx]
    y, dy, d2y, d3y = [y[0] for y in dy]

    i = 1

    x_old = x
    y_old = y

    while i < n:
        i += 1

        x += dx
        dx += d2x
        d2x += d3x

        y += dy
        dy += d2y
        d2y += d3y

        x1, y1 = _normalize(x_old, y_old, window)
        x2, y2 = _normalize(x, y, window)

        x1, y1, x2, y2 = curveClip(x1, y1, x2, y2)

        _drawLines(x1, y1, x2, y2, painter, window)

        x_old = x
        y_old = y


def _normalize(x, y, window):
    yw_min, yw_max, xw_min, xw_max = window.getMinsAndMaxes()
    normal_x = (x - xw_min) / (xw_max - xw_min) * 2 - 1
    normal_y = (y - yw_min) / (yw_max - yw_min) * 2 - 1
    return (normal_x, normal_y)


def _drawLines(x1, y1, x2, y2, painter, window):
    if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
        x1, y1 = viewportTransformation(x1, y1, window)
        x2, y2 = viewportTransformation(x2, y2, window)
        print(x1, y1, x2, y2)
        painter.drawLine(x1, y1, x2, y2)