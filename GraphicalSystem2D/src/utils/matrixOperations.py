import numpy as np
from math import sin, cos

from structures.Point import Point
from structures.Line import Line
from structures.Wireframe import Wireframe


def generateMatrix(type: str, x: float, y: float = None) -> np.matrix:
    """Creates the matrices of the given transformation"""
    if type == "TRANSLATION":
        return np.matrix([[1, 0, 0], [0, 1, 0], [x, y, 1]])
    elif type == "SCALING":
        return np.matrix([[x, 0, 0], [0, y, 0], [0, 0, 1]])
    elif type == "ROTATION":
        rad = np.deg2rad(float(x))
        return np.matrix([[cos(rad), -sin(rad), 0], [sin(rad), cos(rad), 0], [0, 0, 1]])


def matrixComposition(matrix1: np.matrix, matrix2: np.matrix) -> np.matrix:
    return np.matmul(matrix1, matrix2)