from structures.Drawable import Drawable
from structures.Point import Point

from DisplayFile import displayFile

def clip(self, method: str):
    objects_inside_window: list[Drawable] = []

    for point in displayFile.getPoints():
        ...

    for line in displayFile.getLines():
        ...

    for wireframe in displayFile.getWireframes():
        if method == "CS":
            ...
        elif method == "LB":
            ...

def _clipPoint(point: Point) -> bool:
    ...
