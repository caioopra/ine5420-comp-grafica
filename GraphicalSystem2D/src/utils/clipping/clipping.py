from structures.Drawable import Drawable
from structures.Point import Point
from structures.Line import Line
from structures.Wireframe import Wireframe
from structures.BezierCurve import BezierCurve

from DisplayFile import displayFile

from utils.clipping.CohenSutherland import cohen_sutherland
from utils.clipping.LiangBarsky import liang_barsky
from utils.clipping.SutherlandHodgman import sutherland_hodgman
from utils.clipping.WeilerAtherton2 import weilerAtherton


def clip(line_method: str) -> list[Drawable]:
    objects_inside_window: list[Drawable] = []

    for point in displayFile.getPoints():
        if _clipPoint(point):
            objects_inside_window.append(point)

    for line in displayFile.getLines():
        new_line = _clipLine(line_method, line=line)

        if new_line is not None:
            objects_inside_window.append(new_line)

    for wireframe in displayFile.getWireframes():
        new_wireframe = _clipWireframe(wireframe)

        if new_wireframe is not None:
            objects_inside_window.append(new_wireframe)

    buffer_obj = displayFile.getBuffer()
    print(buffer_obj)
    if buffer_obj is not None:
        if isinstance(buffer_obj, Point):
            if _clipPoint(buffer_obj):
                objects_inside_window.append(buffer_obj)
        elif isinstance(buffer_obj, Line):
            if buffer_obj.getPoints()[1] is not None:
                new_line = _clipLine(line_method, line=buffer_obj)

                if new_line is not None:
                    objects_inside_window.append(new_line)
            else:
                if _clipPoint(buffer_obj.getPoints()[0]):
                    objects_inside_window.append(buffer_obj)
        elif isinstance(buffer_obj, Wireframe):
            if len(buffer_obj.getPoints()) > 1:
                new_wireframe = _clipWireframe(wireframe=buffer_obj)

                if new_wireframe is not None:
                    print(p for p in new_wireframe.getPoints())
                    objects_inside_window.append(new_wireframe)
            else:
                if _clipPoint(buffer_obj.getPoints()[0]):
                    objects_inside_window.append(buffer_obj)
        elif isinstance(buffer_obj, list):  # curve
            for p in buffer_obj:
                # TODO: clipping
                objects_inside_window.append(p)

    return objects_inside_window


def _clipPoint(
    point: Point,
    window_max: Point = Point(1, 1),
    window_min: Point = Point(-1, -1),
) -> bool:
    return point.between(min=window_min, max=window_max)


def _clipLine(clipping_method: str, line: Line) -> Line | None:
    if clipping_method == "CS":
        return cohen_sutherland(line)

    return liang_barsky(line)


def _clipWireframe(wireframe: Wireframe) -> Wireframe | None:
    # return weilerAtherton(wireframe)

    return wireframe

