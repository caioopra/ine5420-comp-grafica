import numpy as np
from math import sin, cos, radians, degrees, atan


def generateMatrix(type: str, x: float, y: float = None, z: float = None) -> np.matrix:
    """Creates the matrices of the given transformation"""
    if type == "TRANSLATION":
        return np.matrix(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [float(x), float(y), float(z), 1],
            ]
        )
    elif type == "SCALING":
        return np.matrix(
            [
                [float(x), 0, 0, 0],
                [0, float(y), 0, 0],
                [0, 0, float(z), 0],
                [0, 0, 0, 1],
            ]
        )
    elif type == "ROTATION":
        # rad = radians(float(x))
        # return np.matrix([[cos(rad), sin(rad), 0], [-sin(rad), cos(rad), 0], [0, 0, 1]])
        return _rZRotatioMatrix(float(x))

def _rXRotatioMatrix(angle: float) -> np.matrix:
    rad = radians(angle)
    return np.matrix(
        [
            [1, 0, 0, 0],
            [0, cos(rad), sin(rad), 0],
            [0, -sin(rad), cos(rad), 0],
            [0, 0, 0, 1],
        ]
    )


def _rYRotatioMatrix(angle: float) -> np.matrix:
    rad = radians(angle)
    return np.matrix(
        [
            [cos(rad), 0, -sin(rad), 0],
            [0, 1, 0, 0],
            [sin(rad), 0, cos(rad), 0],
            [0, 0, 0, 1],
        ]
    )


def _rZRotatioMatrix(angle: float) -> np.matrix:
    rad = radians(angle)
    return np.matrix(
        [
            [cos(rad), 0, sin(rad), 0],
            [-sin(rad), cos(rad), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )


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
        - data (dict): necessary data for the transformation (see code for key name)
            - Translation: X and Y values to translate
            - Scaling: center of the current object and scaling factor
            - Rotation: type and amount of rotation and center of object/point (optional)

    Returns:
        np.matrix: matrix that apply the necessary transformation
    """
    if operation == "TRANSLATION":
        return generateMatrix("TRANSLATION", data["xInput"], data["yInput"], data["zInput"])
    elif operation == "SCALING":
        translation_matrix = generateMatrix(
            "TRANSLATION", -data["centerX"], -data["centerY"], data["centerZ"]
        )
        scaling_matrix = generateMatrix(
            "SCALING",
            data["xInput"],
            data["yInput"],
            #data["zInput"]
        )
        undo_translation_matrix = generateMatrix(
            "TRANSLATION", data["centerX"], data["centerY"], data["centerZ"]
        )

        return matrixComposition(
            [translation_matrix, scaling_matrix, undo_translation_matrix]
        )

    elif operation == "ROTATION":
        if data.get("type") == "SELF":
            translation_matrix = generateMatrix(
                "TRANSLATION", -data["centerX"], -data["centerY"], -data["centerZ"]
            )
            rotation_matrix = generateMatrix("ROTATION", data["rotation"])
            undo_translation_matrix = generateMatrix(
                "TRANSLATION", data["centerX"], data["centerY"], data["centerZ"]
            )

            return matrixComposition(
                [translation_matrix, rotation_matrix, undo_translation_matrix]
            )

        elif data.get("type") == "ORIGIN":
            return generateMatrix("ROTATION", data["rotation"])
        elif data.get("type") == "POINT":
            translation_matrix = generateMatrix(
                "TRANSLATION", -data["pointX"], -data["pointY"], -data["pointZ"]
            )
            rotation_matrix = generateMatrix("ROTATION", data["rotation"])
            undo_translation_matrix = generateMatrix(
                "TRANSLATION", data["pointX"], data["pointY"], data["pointZ"]
            )
            return matrixComposition(
                [translation_matrix, rotation_matrix, undo_translation_matrix]
            )

def parallel_projection(window):
    vpr = _get_vpr(window)

    translation = generateMatrix("TRANSLATION", -vpr[0], -vpr[1], -vpr[2])

    vpn = [2, 1, 2]

    theta_x, theta_y = _angle_with_vpn(vpn)

    rotation_x = _rXRotatioMatrix(theta_x)
    rotation_y = _rYRotatioMatrix(theta_y)

    m = np.dot(translation, rotation_x)
    m = np.dot(m, rotation_y)
    print("\n\nM :", m)

    return m

def _get_vpr(window):
    vpr_x = (window.xw_min + window.xw_max) / 2
    vpr_y = (window.yw_min + window.yw_max) / 2
    vpr_z = (window.zw_min + window.zw_max) / 2 
    # vpr_x = (window_coords[0].getX() + window_coords[1].getX() + window_coords[2].getX() + window_coords[3].getX()) / 4
    # vpr_y = (window_coords[0].getY() + window_coords[1].getY() + window_coords[2].getY() + window_coords[3].getY()) / 4
    # vpr_z = (window_coords[0].getZ() + window_coords[1].getZ() + window_coords[2].getZ() + window_coords[3].getZ()) / 4

    return [vpr_x, vpr_y, vpr_z]


def _angle_with_vpn(vpn: list[float]):
    theta_x = degrees(atan(vpn[1] / vpn[2]))
    theta_y = degrees(atan(vpn[0] / vpn[2]))

    return theta_x, theta_y