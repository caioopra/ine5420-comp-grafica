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


def createTransformationMatrix(operation: str, data: dict) -> np.matrix:
    """Creates the transformation matrix for the given operation.
    Each type of transformation has its unique required data in the data dict

    Args:
        - operation (str): name of the operation in upper case
            - SCALING, TRANSLATION and ROTATION (specify type in data)
        - data (dict): necessary data for the transformation
            - Scaling:
            - Rotation:
            - Translation:

    Returns:
        np.matrix: matrix that apply the necessary transformation
    """
    if operation == "TRANSLATION":
        return generateMatrix("TRANSLATION", data["xInput"], data["yInput"])
    elif operation == "SCALING":
        translation_matrix = generateMatrix(
            "TRANSLATION", -data["centerX"], -data["centerY"]
        )
        scaling_matrix = generateMatrix(
            "SCALING",
            data["xInput"],
            data["yInput"],
        )
        undo_translation_matrix = generateMatrix(
            "TRANSLATION", data["centerX"], data["centerY"]
        )

        return matrixComposition(
            [translation_matrix, scaling_matrix, undo_translation_matrix]
        )

    elif operation == "ROTATION":
        if data.get("type") == "SELF":
            translation_matrix = generateMatrix(
                "TRANSLATION", -data["centerX"], -data["centerY"]
            )
            rotation_matrix = generateMatrix("ROTATION", data["rotation"])
            undo_translation_matrix = generateMatrix(
                "TRANSLATION", data["centerX"], data["centerY"]
            )

            return matrixComposition(
                [translation_matrix, rotation_matrix, undo_translation_matrix]
            )

        elif data.get("type") == "ORIGIN":
            return generateMatrix("ROTATION", data["rotation"])
        elif data.get("type") == "POINT":
            translation_matrix = generateMatrix(
                "TRANSLATION", -data["pointX"], -data["pointY"]
            )
            rotation_matrix = generateMatrix("ROTATION", data["rotation"])
            undo_translation_matrix = generateMatrix(
                "TRANSLATION", data["pointX"], data["pointY"]
            )
            return matrixComposition(
                [translation_matrix, rotation_matrix, undo_translation_matrix]
            )
