from structures.Point import Point


class BicubicSurfaceCurve:
    def __init__(
        self, x: list[list[float]], y: list[list[float]], z: list[list[float]]
    ):
        self.x = x
        self.y = y
        self.z = z


def getBicubicGB(points: Point) -> BicubicSurfaceCurve:
    gb_x = [
        [p.x() for idx, p in enumerate(points) if idx < 4],
        [p.x() for idx, p in enumerate(points) if 3 < idx < 8],
        [p.x() for idx, p in enumerate(points) if 7 < idx < 12],
        [p.x() for idx, p in enumerate(points) if idx > 11],
    ]

    gb_y = [
        [p.y() for idx, p in enumerate(points) if idx < 4],
        [p.y() for idx, p in enumerate(points) if 3 < idx < 8],
        [p.y() for idx, p in enumerate(points) if 7 < idx < 12],
        [p.y() for idx, p in enumerate(points) if idx > 11],
    ]

    gb_z = [
        [p.z() for idx, p in enumerate(points) if idx < 4],
        [p.z() for idx, p in enumerate(points) if 3 < idx < 8],
        [p.z() for idx, p in enumerate(points) if 7 < idx < 12],
        [p.z() for idx, p in enumerate(points) if idx > 11],
    ]
    
    return BicubicSurfaceCurve(gb_x, gb_y, gb_z)
