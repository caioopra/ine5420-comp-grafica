from structures.Point import Point
from structures.Line import Line 
from structures.Wireframe import Wireframe

from utils.clipping.CohenSutherland import cohen_sutherland

def weilerAtherton(wireframe: Wireframe) -> Wireframe | None:
    points = wireframe.getPoints()

    if all([_point_is_outside_window(p) for p in points]):
        return None

    window = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    object_vertices = [(p, 0) for p in points]  # (Point(), 0)

    number_points = len(object_vertices)
    enter_points = []
    for index in range(number_points):
        p0 = object_vertices[index]
        p1 = object_vertices[(index + 1) % number_points] 
        
        line = cohen_sutherland(Line(p0[0], p1[0]))
        if line:
            new_p0, new_p1 = line.getPoints()

            if new_p0.getNormalCoordinates() != p0[0].getNormalCoordinates():
                point_index = object_vertices.index((p0, 0)) + 1
                object_vertices.insert(point_index, (new_p1, 2))
                window = _WA_getWindowIndex(window, new_p1, 2)

            if new_p1.getNormalCoordinates() != p1[0].getNormalCoordinates():
                point_index = object_vertices.index((p0, 0)) + 1
                object_vertices.insert(point_index, (new_p0, 1))
                enter_points.append((new_p0, 1))
                window = _WA_getWindowIndex(window, new_p0, 1)

    new_polygons = []
    new_points = []

    if enter_points != []:
        while enter_points != []:
            reference = enter_points.pop(0)
            rf_p, _ = reference  # gets only the point
            inside_points = [rf_p] 
            point_index = object_vertices.index(reference) + 1
            new_points.append(reference)

            obj_len = len(object_vertices)
            for aux_index in range(obj_len):
                (p, c) = object_vertices[(point_index + aux_index) % obj_len]
                new_points.append((p, c))
                inside_points.append(p)
                print("p, c", p, c)
                if c != 0:
                    break #?

            last_point = new_points[-1]
            point_index = window.index(last_point)
            window_len = len(window)

            for aux_index in range(window_len):
                (p, c) = window[(point_index + aux_index) % window_len]
                new_points.append((p, c))
                inside_points.append(p)
                if c != 0:
                    break

            new_polygons.append(inside_points)
        coordinates = new_polygons

    else:
        coordinates = points

    print("coords")
    for p in coordinates:
        print(p)

        
    wireframe.setPoints(coordinates)
    return wireframe
    


def _point_is_outside_window(point: Point) -> bool:
    x = point.getNormalX() > 1 or point.getNormalX() < -1
    y = point.getNormalY() > 1 or point.getNormalY() < -1

    return x or y

def _WA_getWindowIndex(window_vertices, point, code):
    x, y = point.getNormalX(), point.getNormalY()

    if x == 1:
        index = window_vertices.index((1, -1), 0)
        window_vertices.insert(index, (point, code))
    elif x == -1:
        index = window_vertices.index((-1, 1), 0)
        window_vertices.insert(index, (point, code))

    if y == 1:
        index = window_vertices.index((1, 1), 0)
        window_vertices.insert(index, (point, code))
    elif y == -1:
        index = window_vertices.index((-1, -1), 0)
        window_vertices.insert(index, (point, code))

    return window_vertices
