from structures.Point import Point
from structures.Line import Line
from structures.Wireframe import Wireframe

from PyQt5.QtGui import QColor


def writeObjectsToFile(filename: str, objects: list, window: list):
    vectors = {"SIZE": 0}

    points = {}
    lines = {}
    wireframes = {}

    colors = {}
    reverse_color = {}
    qtd_cores = 0

    for obj in objects:
        objColorToRGB = _convertColorToRGB(obj.getColor())
        if not objColorToRGB in colors.values():
            colors[f"cor{qtd_cores}"] = objColorToRGB
            reverse_color[objColorToRGB] = f"cor{qtd_cores}"
            qtd_cores += 1

        current_color = reverse_color[objColorToRGB]
        obj_name = obj.getName().replace(" ", "_")
        if isinstance(obj, Point):
            string = f"p{_getVectors([obj], vectors, current_color)}"
            points[obj_name] = [string, current_color]
        elif isinstance(obj, Line):
            objPoints = obj.getPoints()
            string = f"l{_getVectors(objPoints, vectors, current_color)}"
            lines[obj_name] = [string, current_color]
        elif isinstance(obj, Wireframe):
            objPoints = obj.getPoints()
            string = f"l{_getVectors(objPoints, vectors, current_color)}"
            wireframes[obj_name] = [string, current_color]
            
    window = f"w{ _getVectors(window, vectors, current_color)}"

    del vectors["SIZE"]

    _save_mtl_file(colors, filename)
    _save_obj_file(filename, points, lines, wireframes, vectors, window)


def _getVectors(points: list[Point], vectors: dict, color: str) -> str:
    reversed_vectors = {v: k for k, v in vectors.items()}
    point_as_string = ""
    for point in [p.getPointAsVector() for p in points]:
        point = point.replace("0.0", "0")
        if not point in vectors.values():
            vectors[f"{vectors['SIZE'] + 1}"] = point
            vectors["SIZE"] += 1

            reversed_vectors[point] = f"{vectors['SIZE']}"

        point_as_string = f"{point_as_string} {reversed_vectors[point]}"

    return point_as_string


def _convertColorToRGB(color):
    color = QColor(color).getRgb()[0:3]
    return str([c / 255 for c in color])


def _save_mtl_file(colors: dict, filename: str) -> None:
    string = ""
    for name, color in colors.items():
        color = str(color).replace("[", "").replace("]", "").replace(",", "")
        string += f"newmtl {name}\nKd {color}\n\n"

    with open(f"objects/{filename}.mtl", "w+") as f:
        f.write(string)


def _save_obj_file(
    filename: str,
    points: dict,
    lines: dict,
    wireframes: dict,
    vectors: dict,
    window: str
) -> None:
    string = ""

    for v in vectors.values():
        string += v + "\n"

    string += f"mtllib {filename}.mtl\n"
    string += "o window\n"
    string += window + "\n"

    string = _addObjectTypeToString(points, string)
    string = _addObjectTypeToString(lines, string)
    string = _addObjectTypeToString(wireframes, string)
    
    with open(f"objects/{filename}.obj", "w+") as f:
        f.write(string)


def _addObjectTypeToString(objects: list, currentString: str) -> str:
    for name, data in objects.items():
        currentString += f"o {name}\n"
        currentString += f"usemtl {data[1]}\n"
        currentString += f"{data[0]}\n"

    return currentString
