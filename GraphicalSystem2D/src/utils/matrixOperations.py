import numpy as np
from math import sin, cos

from structures.Point import Point
from structures.Line import Line
from structures.Wireframe import Wireframe


def generateMatrix(type: str, x: float, y: float = None) -> np.matrix:
    """ Creates the matrices of the given transformation
    """
    if type == "TRANSLATION":
        return np.matrix([[1, 0, 0], [0, 1, 0], [x, y, 1]])
    elif type == "SCALING":
        return np.matrix([[x, 0, 0], [0, y, 0], [0, 0, 1]])
    elif type == "ROTATION":
        rad = np.deg2rad(x)
        return np.matrix([[cos(rad), -sin(rad), 0], [sin(rad), cos(rad), 0], [0, 0, 1]])


def transform(
    object: Point | Line | Wireframe, matrix: np.matrix
) -> Point | Line | Wireframe:
    """Given a object and a matrix (np.matrix), returns the object
    with the given transformation applied
    """
    if isinstance(object, Point):
        return _transformPoint(object, matrix)
    elif isinstance(object, Line):
        ...
    elif isinstance(object, Wireframe):
        ...


def _transformPoint(point: Point, matrix: np.matrix):
    return np.matmul(np.array([point.getx(), point.getY(), 1]), matrix)


def matrixComposition(matrix_list: list) -> np.matrix:
    result = np.matmul(matrix_list[0], matrix_list[1])

    if len(matrix_list) > 2:
        for matrix in matrix_list[2:]:
            result = np.matmul(result, matrix)

    return result
