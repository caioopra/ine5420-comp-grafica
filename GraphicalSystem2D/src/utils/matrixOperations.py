from numpy import array, matmul

from structures.Point import Point
from structures.Line import Line
from structures.Wireframe import Wireframe

def transform(object: Point | Line | Wireframe, matrix: array) -> Point | Line | Wireframe:
    """ Given a object and a matrix (np.array), returns the object
    with the given transformation applied
    """
    if isinstance(object, Point):
        ...
    elif isinstance(object, Line):
        ...
    elif isinstance(object, Wireframe):
        ...

def _transformPoint(point: Point, matrix: array):
    


def matrix_composition(matrix_list: list) -> array: 
    result = matmul(matrix_list[0], matrix_list[1])

    if len(matrix_list) > 2:
        for matrix in matrix_list[2:]:
            result = matmul(result, matrix)
    
    return result
