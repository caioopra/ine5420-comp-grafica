from structures.Wireframe import Wireframe
from structures.Line import Line
from structures.Point import Point

from utils.clipping.CohenSutherland import cohen_sutherland


def weilerAtherton(wireframe: Wireframe) -> Wireframe:
    window = {"xw_min": -1, "yw_min": -1, "xw_max": 1, "yw_max": 1}
    
    vertices = wireframe.getPoints()    

    if all([outside_window(p) for p in vertices]):
        return None

    # First step: build two lists of vertices
    window_vertices = [((-1, 1), 0), ((1, 1), 0), ((1, -1), 0), ((-1, -1), 0)]
    object_vertices = [(c, 0) for c in vertices]

    number_points = len(object_vertices)
    enter_points = []
    # Second step: calculate intersections
    for index in range(number_points):
        p0 = vertices[index]
        p1 = vertices[(index + 1) % number_points]

        linha = cohen_sutherland(Line(p0, p1))
        if linha != None:
            if linha.getPoints()[1] != p1:
                # Exit point
                point_index = object_vertices.index((p0, 0)) + 1
                # Append new point right after the original
                object_vertices.insert(point_index, (linha.getPoints()[1], 2))
                window_vertices = w_a_get_window_index(window_vertices, linha.getPoints()[1], 2)

            if linha.getPoints()[0] != p0:
                # Enter point
                point_index = object_vertices.index((p0, 0)) + 1
                # Append new point right after the original
                object_vertices.insert(point_index, (linha.getPoints()[0], 1))
                enter_points.append((linha.getPoints()[0], 1))
                window_vertices = w_a_get_window_index(window_vertices, linha.getPoints()[0], 1)

    new_polygons = []
    new_points = []
    if enter_points != []:
        # Repeat until empty enter points
        while enter_points != []:
            # Get first point from enter
            reference_point = enter_points.pop(0)
            rf_p, _ = reference_point
            inside_points = [rf_p]
            point_index = object_vertices.index(reference_point) + 1
            new_points.append(reference_point)

            obj_len = len(object_vertices)
            for aux_index in range(obj_len):
                (p, c) = object_vertices[(point_index + aux_index) % obj_len]
                new_points.append((p, c))
                inside_points.append(p)
                if c != 0:
                    break

            last_point = new_points[-1]
            point_index = window_vertices.index(last_point)
            window_len = len(window_vertices)
            for aux_index in range(window_len):
                (p, c) = window_vertices[(point_index + aux_index) % window_len]
                new_points.append((p, c))
                inside_points.append(p)
                if c != 0:
                    break

            new_polygons.append(inside_points)
        coordinates = new_polygons
    else:
        coordinates = [vertices]

    # print(f"Coordinates after weiler_atherton={coordinates}")
    new_wireframe = Wireframe(coordinates[0][0])
    new_wireframe.setPoints(coordinates[0])
    new_wireframe.setIsFilled(wireframe.getIsFilled())
    new_wireframe.setColor(wireframe.getColor())
    return new_wireframe

def w_a_get_window_index(window_vertices, point, code):
    x = point.getNormalX()
    y = point.getNormalY()
    # The index from window vertices list must be the
    # right before the next window vertice
    if x == 1:
        # Right, so right bottom
        index = window_vertices.index(((1, -1), 0))
        window_vertices.insert(index, (point, code))
    if x == -1:
        # Left, so left top
        index = window_vertices.index(((-1, 1), 0))

        window_vertices.insert(index, (point, code))
    if y == 1:
        # Top, so right top
        index = window_vertices.index(((1, 1), 0))
        window_vertices.insert(index, (point, code))
    if y == -1:
        # Bottom, so left bottom
        index = window_vertices.index(((-1, -1), 0))
        window_vertices.insert(index, (point, code))
    return window_vertices


def outside_window(point):
    return (point.getNormalX() > 1 or point.getNormalX() < -1) or (point.getNormalY() > 1 or point.getNormalY() < -1)

