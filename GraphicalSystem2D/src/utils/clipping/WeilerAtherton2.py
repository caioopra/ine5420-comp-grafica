from structures.Wireframe import Wireframe


def weilerAtherton(wireframe: Wireframe) -> Wireframe:
    window = {"xw_min": -1, "yw_min": -1, "xw_max": 1, "yw_max": 1}
    
    vertices = wireframe.getPoints()
    labels = _createLabels(vertices, window)
    
    new_polygon = []

    for i in range(len(vertices)):
        start = vertices[i]
        start_label = labels[i]
        end = vertices[(i+1) % len(vertices)]
        end_label = labels[(i+1) % len(vertices)]

        if start_label == "inside" and end_label == "inside":
            new_polygon.append(end)  # TODO: toList
        elif start_label == "inside" and end_label == "outside":
            intersection = _getIntersection(start, end, window)
            new_polygon.append(list(intersection))
        elif start_label == "outside" and end_label == "inside":
            intersection = _getIntersection(start, end, window)
            new_polygon.append(list(intersection))
            new_polygon.append(end)
        
        if new_polygon:
            flat = []
            for point in new_polygon:
                if isinstance(point, (list, tuple)) and isinstance(point[0], (list, tuple)):
                    flat.extend(point)
                else:
                    flat.append(point)

        new = Wireframe(flat[0])
        new.setName(wireframe.getName())
        new.setWindow(wireframe.getWindow())
        new.setPoints(flat)

    print("new",new.getPoints())
    return new


def _createLabels(points: list, window: dict) -> list:
    labels = []
    
    for p in points:
        if _isInsideWindow(p, window):
            labels.append("inside")
        else:
            labels.append("outside")

    return labels


def _isInsideWindow(point, window: dict) -> bool:
    return window["xw_min"] <= point.getNormalX() <= window["xw_max"] and window["yw_min"] <= point.getNormalY() <= window["yw_max"]

def _getIntersection(p1, p2, window):
    x1, y1 = p1.getNormalCoordinates()
    x2, y2 = p2.getNormalCoordinates()

    RC1 = 0
    RC2 = 0

    if (x1 > window["xw_max"]):
        RC1 += 2
    elif (x1 < window["xw_min"]):
        RC1 += 1

    if y1 > window["yw_max"]:
        RC1 += 8
    elif y1 < window["yw_min"]:
        RC1 += 4

    if (x2 > window["xw_max"]):
        RC2 += 2
    elif (x2 < window["xw_min"]):
        RC2 += 1

    if y2 > window["yw_max"]:
        RC2 += 8
    elif y2 < window["yw_min"]:
        RC2 += 4

    if RC1 & RC2:
        return None, None

    m = (y2 - y1) / (x2 - x1) if x2 != x1 else None

    if RC1 != 0:
        if RC1 & 1:
            y1 = m * (window["xw_min"] - x1) + y1
            x1 = window["xw_min"]
        elif RC1 & 2:
            y1 = m * (window["xw_max"] - x1) + y1
            x1 = window["xw_max"]
        if RC1 & 4:
            x1 = x1 + (1/m) * (window["yw_min"] - y1)
            y1 = window["yw_min"]
        elif RC1 & 8:
            x1 = x1 + (1/m) * (window["yw_max"] - y1)
            y1 = window["yw_max"]

    if RC2 != 0:
        if RC2 & 1:
            y2 = m * (window["xw_min"] - x1) + y2
            x2 = window["xw_min"]
        elif RC2 & 2:
            y2 = m * (window["xw_max"] - x2) + y2
            x2 = window["xw_max"]
        if RC2 & 4:
            x2 = x2 + (1/m) * (window["yw_min"] - y2)
            y2 = window["yw_min"]
        elif RC2 & 8:
            x2 = x2 + (1/m) * (window["yw_max"] - y2)
            y2 = window["yw_max"] 

    p1.setNormalCoordinates(x1, y1)
    p2.setNormalCoordinates(x2, y2)

    return p1, p2
