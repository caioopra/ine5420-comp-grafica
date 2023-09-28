from copy import deepcopy

from utils.clipping.PositionsEnum import Position

from structures.Point import Point
from structures.Wireframe import Wireframe


def sutherland_hodgman(
    wireframe: Wireframe,
    window_max: Point = Point(1, 1),
    window_min: Point = Point(-1, -1),
) -> Wireframe | None:
    # algorithm preparation
    wireframe_points = deepcopy(wireframe.getPoints())
    if len(wireframe_points) == 3:
        wireframe_points.sort(key=lambda point: point.getNormalX())

    wireframe_copy = deepcopy(wireframe)

    xw_min, yw_min = window_min.getCoordinates()
    xw_max, yw_max = window_max.getCoordinates()
    window = {"xw_min": xw_min, "yw_min": yw_min, "xw_max": xw_max, "yw_max": yw_max}
    # ============= end of preparation
    wireframe_points.append(wireframe_points[0])

    vertices = {}
    tmp = []
    i = 0

    for v in range(len(wireframe_points) - 1):
        rc_v1 = _getRegionCode(wireframe_points[v], window)
        rc_v2 = _getRegionCode(wireframe_points[v + 1], window)

        if rc_v1 != 0 and rc_v2 == 0:
            intersection = _newVertex(
                rc_v1, wireframe_points[v], wireframe_points[v + 1], window
            )
            vertices[f"i{i}"] = intersection
            vertices[f"v{v}"] = wireframe_points[v + 1]
            i += 1
            # cliped = true ???
        elif rc_v1 == 0 and rc_v2 != 0:
            intersection = _newVertex(
                rc_v2, wireframe_points[v], wireframe_points[v + 1], window
            )
            vertices[f"i{i}"] = intersection
            vertices[f"v{v}"] = wireframe_points[v]
            i += 1
        elif rc_v1 == 0 and rc_v2 == 0:
            vertices[f"v{i}"] = wireframe_points[v]
            vertices[f"v{v+1}"] = wireframe_points[v + 1]
            # somar um em i?
        else:  # both points outside of window
            positions = [
                Position.LEFT.value,
                Position.RIGHT.value,
                Position.BOTTOM.value,
                Position.TOP.value,
            ]
            if rc_v1 in positions and rc_v2 in positions and rc_v1 != rc_v2:
                try:
                    intersection = _newVertex(
                        rc_v1, wireframe_points[v], wireframe_points[v + 1], window
                    )
                    intersection_2 = _newVertex(
                        rc_v2, wireframe_points[v + 1], wireframe_points[v], window
                    )

                    if rc_v1 == 1 or rc_v1 == 2:
                        if (
                            window["yw_min"]
                            < intersection.getNormalY()
                            < window["yw_max"]
                        ):
                            vertices[f"i{i}"] = intersection
                            vertices[f"v{v}"] = intersection
                            vertices[f"i{i+1}"] = intersection_2
                            i += 2
                    elif (
                        rc_v1 == 4
                        or rc_v1 == 8
                        and window["xw_min"] < intersection.getNormalX() < window["xw_max"]
                    ):
                        vertices[f"i{i}"] = intersection
                        vertices[f"v{v}"] = intersection
                        vertices[f"i{i+1}"] = intersection_2
                        i += 2
                except:
                    pass

        if wireframe.getIsFilled():
            if (
                rc_v1 in [2, 8, 10]
                and rc_v2 == 10
                or rc_v1 == 10
                and rc_v2 in [2, 8, 10]
            ):
                vertices[f"v{v}"] = Point(window["xw_max"], window["yw_max"])
            if rc_v1 in [1, 8, 9] and rc_v2 == 9 or rc_v1 == 9 and rc_v2 in [1, 8, 9]:
                vertices[f"v{v}"] = Point(window["xw_min"], window["yw_max"])
            if rc_v1 in [1, 4, 5] and rc_v2 == 5 or rc_v1 == 5 and rc_v2 in [1, 4, 5]:
                vertices[f"v{v}"] = Point(window["xw_min"], window["yw_min"])
            if rc_v1 in [2, 4, 6] and rc_v2 == 6 or rc_v1 == 6 and rc_v2 in [2, 4, 6]:
                vertices[f"v{v}"] = Point(window["xw_max"], window["yw_min"])
            if rc_v1 == 8 and rc_v2 == 2 or rc_v1 == 2 and rc_v2 == 8:
                vertices[f"v{v}"] = _newVertex(
                    10, wireframe_points[v], wireframe_points[v + 1], window
                )
            if rc_v1 == 4 and rc_v2 == 2 or rc_v1 == 2 and rc_v2 == 4:
                vertices[f"v{v}"] = _newVertex(
                    6, wireframe_points[v], wireframe_points[v + 1], window
                )
            if rc_v1 == 4 and rc_v2 == 1 or rc_v1 == 1 and rc_v2 == 4:
                vertices[f"v{v}"] = _newVertex(
                    5, wireframe_points[v], wireframe_points[v + 1], window
                )
            if rc_v1 == 1 and rc_v2 == 8 or rc_v1 == 8 and rc_v2 == 1:
                vertices[f"v{v}"] = _newVertex(
                    9, wireframe_points[v], wireframe_points[v + 1], window
                )

    try:
        sub_polygons = [[list(vertices.values())[0]]]

        for i in range(1, len(vertices)):
            vertices_keys = list(vertices.keys())
            if (
                "i" in vertices_keys[i - 1] and "i" in vertices_keys[i]
            ):  # duas interseções consecutivas, divide a lista
                sub_polygons.append([list(vertices.values())[i]])
            else:
                sub_polygons[len(sub_polygons) - 1].append(list(vertices.values())[i])
    except IndexError:
        sub_polygons = []  # outside window

    if tmp != []:
        sub_polygons.insert(0, tmp)
    
    print("\n\nsub", sub_polygons)

    wireframe.setPoints(sub_polygons)
    print(wireframe.getPoints())
    
    return wireframe


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


def _newVertex(rc, point1: Point, point2: Point, window: dict):
    point1_x = point1.getNormalX()
    point1_y = point1.getNormalY()

    point2_x = point2.getNormalX()
    point2_y = point2.getNormalY()

    if rc == 1:
        new_y = point1_y + (point2_y - point1_y) * (window["xw_min"] - point1_x) / (
            point2_x - point1_x
        )
        new_x = window["xw_min"]
    if rc == 2:
        new_y = point1_y + (point2_y - point1_y) * (window["xw_max"] - point1_x) / (
            point2_x - point1_x
        )
        new_x = window["xw_max"]
    if rc == 4:
        new_x = point1_x + (point2_x - point1_x) * (window["yw_min"] - point1_y) / (
            point2_y - point1_y
        )
        new_y = window["yw_min"]
    if rc == 8:
        new_x = point1_x + (point2_x - point1_x) * (window["yw_max"] - point1_y) / (
            point2_y - point1_y
        )
        new_y = window["yw_max"]

    if rc == 5:
        # Primeiro caso:
        x_bot = point1_x + (point2_x - point1_x) * (window["yw_min"] - point1_y) / (
            point2_y - point1_y
        )
        # Segundo caso:
        y_esq = point1_y + (point2_y - point1_y) * (window["xw_min"] - point1_x) / (
            point2_x - point1_x
        )

        if x_bot > window["xw_min"]:
            new_x = x_bot
            new_y = window["yw_min"]
        elif y_esq > window["yw_min"]:
            new_x = window["xw_min"]
            new_y = y_esq
        else:
            new_x = window["xw_min"]
            new_y = window["yw_min"]

    if rc == 6:
        # Primeiro caso:
        x_bot = point1_x + (point2_x - point1_x) * (window["yw_min"] - point1_y) / (
            point2_y - point1_y
        )
        # Segundo caso:
        y_dir = point1_y + (point2_y - point1_y) * (window["xw_max"] - point1_x) / (
            point2_x - point1_x
        )

        if x_bot < window["xw_max"]:
            new_x = x_bot
            new_y = window["yw_min"]
        elif y_dir > window["yw_min"]:
            new_x = window["xw_max"]
            new_y = y_dir
        else:
            new_x = window["xw_max"]
            new_y = window["yw_min"]

    if rc == 9:
        # Primeiro caso:
        x_top = point1_x + (point2_x - point1_x) * (window["yw_max"] - point1_y) / (
            point2_y - point1_y
        )
        # Segundo caso:
        y_esq = point1_y + (point2_y - point1_y) * (window["xw_min"] - point1_x) / (
            point2_x - point1_x
        )

        if x_top > window["xw_min"]:
            new_x = x_top
            new_y = window["yw_max"]
        elif y_esq < window["yw_max"]:
            new_x = window["xw_min"]
            new_y = y_esq
        else:
            new_x = window["xw_min"]
            new_y = window["yw_max"]

    if rc == 10:
        # Primeiro caso:
        x_top = point1_x + (point2_x - point1_x) * (window["yw_max"] - point1_y) / (
            point2_y - point1_y
        )
        # Segundo caso:
        y_dir = point1_y + (point2_y - point1_y) * (window["xw_max"] - point1_x) / (
            point2_x - point1_x
        )

        if x_top < window["xw_max"]:
            new_x = x_top
            new_y = window["yw_max"]
        elif y_dir < window["yw_max"]:
            new_x = window["xw_max"]
            new_y = y_dir
        else:
            new_x = window["xw_max"]
            new_y = window["yw_max"]

    return Point(new_x, new_y)
