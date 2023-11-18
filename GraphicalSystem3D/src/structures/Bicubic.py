from structures.Point import Point
from utils.bSplineUtils import BSPLINE_MATRIX
from utils.bezierUtils import BEZIER_MATRIX
from utils.matrixOperations import transpose, concat_transformation_matrixes
from numpy import dot

TRANSPOSED_BSPLINE_MATRIX = transpose(BSPLINE_MATRIX)


class BicubicSurfaceCurve:
    def __init__(
        self, x: list[list[float]], y: list[list[float]], z: list[list[float]]
    ):
        self.x = x
        self.y = y
        self.z = z


def getBicubicGB(points: Point) -> BicubicSurfaceCurve:
    gb_x = [
        [p.getNormalX() for idx, p in enumerate(points) if idx < 4],
        [p.getNormalX() for idx, p in enumerate(points) if 3 < idx < 8],
        [p.getNormalX() for idx, p in enumerate(points) if 7 < idx < 12],
        [p.getNormalX() for idx, p in enumerate(points) if idx > 11],
    ]

    gb_y = [
        [p.getNormalY() for idx, p in enumerate(points) if idx < 4],
        [p.getNormalY() for idx, p in enumerate(points) if 3 < idx < 8],
        [p.getNormalY() for idx, p in enumerate(points) if 7 < idx < 12],
        [p.getNormalY() for idx, p in enumerate(points) if idx > 11],
    ]

    gb_z = [
        [p.getNormalZ() for idx, p in enumerate(points) if idx < 4],
        [p.getNormalZ() for idx, p in enumerate(points) if 3 < idx < 8],
        [p.getNormalZ() for idx, p in enumerate(points) if 7 < idx < 12],
        [p.getNormalZ() for idx, p in enumerate(points) if idx > 11],
    ]
    
    return BicubicSurfaceCurve(gb_x, gb_y, gb_z)

def getBicubicGeometryMatrix(points: list[Point]):

    gb_x = [[0.0,0.0,0.0,0.0], [0.0,0.0,0.0,0.0], [0.0,0.0,0.0,0.0], [0.0,0.0,0.0,0.0]]
    gb_y = [[0.0,0.0,0.0,0.0], [0.0,0.0,0.0,0.0], [0.0,0.0,0.0,0.0], [0.0,0.0,0.0,0.0]]
    gb_z = [[0.0,0.0,0.0,0.0], [0.0,0.0,0.0,0.0], [0.0,0.0,0.0,0.0], [0.0,0.0,0.0,0.0]]

    for i in range(4):
        for j in range(4):
            index = i + j + 4
            point = points[index]
            gb_x[i][j] = point.getNormalX()
            gb_y[i][j] = point.getNormalY()
            gb_z[i][j] = point.getNormalZ()
    
    return BicubicSurfaceCurve(gb_x, gb_y, gb_z)

def generate_surface_initial_values(delta_matrix_s: list, delta_matrix_t: list, gb: BicubicSurfaceCurve):
    # Cx = M * Gx * M^T
    c_x = concat_transformation_matrixes([BSPLINE_MATRIX, gb.x, TRANSPOSED_BSPLINE_MATRIX])
    c_y = concat_transformation_matrixes([BSPLINE_MATRIX, gb.y, TRANSPOSED_BSPLINE_MATRIX])
    c_z = concat_transformation_matrixes([BSPLINE_MATRIX, gb.z, TRANSPOSED_BSPLINE_MATRIX])

    # DDx = delta_s * Cx * delta_t^T
    DD_x = concat_transformation_matrixes([delta_matrix_s, c_x, delta_matrix_t])
    DD_y = concat_transformation_matrixes([delta_matrix_s, c_y, delta_matrix_t])
    DD_z = concat_transformation_matrixes([delta_matrix_s, c_z, delta_matrix_t])

    return DD_x, DD_y, DD_z

def blending_function_bicubic(s:float, t: float, gb: list[list[float]]) -> float:

    param_s = [[pow(s, 3), pow(s, 2), s, 1]]

    param_t = [
        [pow(t, 3)],
        [pow(t, 2)], 
        [t],
        [1]
    ]

    blending = dot(param_s, BEZIER_MATRIX)
    blending = dot(blending, gb)
    blending = dot(blending, BEZIER_MATRIX)
    blending = dot(blending, param_t)

    return blending