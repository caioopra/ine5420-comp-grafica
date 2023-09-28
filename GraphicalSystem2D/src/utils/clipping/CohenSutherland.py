from utils.clipping.PositionsEnum import Position

from structures.Point import Point
from structures.Line import Line


def cohen_sutherland(
    line: Line,
    window_max: Point = Point(1, 1),
    window_min: Point = Point(-1, -1),
) -> Line | None:
    xw_min, yw_min = window_min.getCoordinates()
    xw_max, yw_max = window_max.getCoordinates()
    window = {"xw_min": xw_min, "yw_min": yw_min, "xw_max": xw_max, "yw_max": yw_max}

    point1, point2 = line.getPoints()
    rc_point1 = _getRegionCode(point1, window)
    rc_point2 = _getRegionCode(point2, window)

    while True:
        if rc_point1 == 0 and rc_point2 == 0:
            return line
        elif (rc_point1 & rc_point2) != 0:
            return None
        else:
            newX, newY = 0, 0

            if rc_point1 != 0:
                rc_out = rc_point1
            else:
                rc_out = rc_point2

            if rc_out & Position.TOP.value:
                newX = point1.getNormalX() + (
                    point2.getNormalX() - point1.getNormalX()
                ) * (window["yw_max"] - point1.getNormalY()) / (
                    point2.getNormalY() - point1.getNormalY()
                )
                newY = window["yw_max"]

            elif rc_out & Position.BOTTOM.value:
                newX = point1.getNormalX() + (
                    point2.getNormalX() - point1.getNormalX()
                ) * (window["yw_min"] - point1.getNormalY()) / (
                    point2.getNormalY() - point1.getNormalY()
                )
                newY = window["yw_min"]

            elif rc_out & Position.RIGHT.value:
                newY = point1.getNormalY() + (
                    point2.getNormalY() - point1.getNormalY()
                ) * (window["xw_max"] - point1.getNormalX()) / (
                    point2.getNormalX() - point1.getNormalX()
                )
                newX = window["xw_max"]

            elif rc_out & Position.LEFT.value:
                newY = point1.getNormalY() + (
                    point2.getNormalY() - point1.getNormalY()
                ) * (window["xw_min"] - point1.getNormalX()) / (
                    point2.getNormalX() - point1.getNormalX()
                )
                newX = window["xw_min"]

            if rc_out == rc_point1:
                point1 = Point(newX, newY)
                rc_point1 = _getRegionCode(point1, window)
            else:
                point2 = Point(newX, newY)
                rc_point2 = _getRegionCode(point2, window)


def _getRegionCode(point1: Point, window: dict) -> int:
    x, y = point1.getNormalCoordinates()
    rc = Position.INSIDE.value

    if x > window["xw_max"]:
        rc |= Position.RIGHT.value
    elif x < window["xw_min"]:
        rc |= Position.LEFT.value

    if y > window["yw_max"]:
        rc |= Position.TOP.value
    elif y < window["yw_min"]:
        rc |= Position.BOTTOM.value

    return rc
