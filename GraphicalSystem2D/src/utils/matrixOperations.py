import numpy as np
from math import sin, cos, radians


def generateMatrix(type: str, x: float, y: float = None) -> np.matrix:
    """Creates the matrices of the given transformation"""
    if type == "TRANSLATION":
        return np.matrix([[1, 0, 0], [0, 1, 0], [float(x), float(y), 1]])
    elif type == "SCALING":
        return np.matrix([[float(x), 0, 0], [0, float(y), 0], [0, 0, 1]])
    elif type == "ROTATION":
        rad = radians(float(x))
        return np.matrix([[cos(rad), sin(rad), 0], [-sin(rad), cos(rad), 0], [0, 0, 1]])

def matrixComposition(matrices: list) -> np.matrix:
    resultant_matrix = np.matmul(matrices[0], matrices[1])
    
    for matrix in matrices[2:]:
        resultant_matrix = np.matmul(resultant_matrix, matrix)
        
    return resultant_matrix