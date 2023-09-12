import os
from matplotlib.colors import to_hex


def readObjFile(name: str):
    if not os.path.isfile(f"../objects/{name}"):
        name = f"{name}.obj"
        if not os.path.isfile(f"objects/{name}"):
            print("não existe o arquivo")

            return

    with open(f"../objects/{name}") as file:
        content = file.readlines()
        content = _clearContent(content)

        vertices, materials, object, window = _processContent(content)


def _clearContent(content: list[str]) -> list[str]:
    new_content = []
    for string in content:
        new_content.append(string.replace("\n", ""))

    return new_content


def _processContent(content: list[str]) :
    vertices = []
    materials_files = []
    objects = {}
    window = None

    currentObj = None

    for string in content:
        string = string.split(" ")
        if string[0] == "v":
            vertices.append([float(val) for val in string[1:]])
        elif string[0] == "mtllib":
            materials_files.append(string[1])
        elif string[0] == "o":
            objects[string[1]] = {}
            currentObj = string[1]
        elif string[0] == "usemtl":
            objects[currentObj]["material"] = string[1]
        elif string[0] == "w":
            window = [string[1]]
        elif string[0] == "l":
            objects[currentObj]["points"] = [string[1:]]
        elif string[0] == "p":
            objects[currentObj]["points"] = [string[1]]
        elif string[0] == "f":  # for now, the same behavior as l
            objects[currentObj]["points"] = [string[1:]]
        else:  # string is the list of points
            objects[currentObj]["points"] = string[0:]

    if "window" in objects.keys():
        del objects["window"]

    materials = _readMaterialFile(materials_files)

    return vertices, materials, object, window


def _readMaterialFile(materials_files: list[str]) -> dict:
    data = {}
    for file in materials_files: 
        opened_file = open(f"../objects/{file}")
        materials = opened_file.readlines()
        materials = _clearContent(materials)

        current = None
        for string in materials:
            string = string.split(" ")
            if string[0] == "newmtl":
                data[string[1]] = []
                current = string[1]
            if string[0] == "Kd":
                data[current] = _convertToHEX(string[1:])
        opened_file.close()

    return data

def _convertToHEX(values: list[str]):
    return to_hex([float(val) for val in values])

readObjFile("sample.obj")
