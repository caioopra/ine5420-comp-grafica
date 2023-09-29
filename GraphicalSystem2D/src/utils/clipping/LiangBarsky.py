from structures.Line import Line
from structures.Point import Point

def liang_barsky(line: Line, window_max: Point = Point(1, 1), window_min: Point = Point(-1, -1),) -> Line | None:

    point1, point2 = line.getPoints()

    xw_min, yw_min = window_min.getCoordinates()
    xw_max, yw_max = window_max.getCoordinates()

    delta_x = point2.getNormalX() - point1.getNormalX()
    delta_y = point2.getNormalY() - point1.getNormalY()

    p = [- delta_x, delta_x, - delta_y, delta_y]
    q = [point1.getNormalX() - xw_min, xw_max - point1.getNormalX(), point1.getNormalY() - yw_min, yw_max - point1.getNormalY()]

    inside = False

    for i in range(4):
        if p[i] == 0 and q[i] < 0:
            return None
    
    positivos = []
    negativos = []
    for i in range(4):
        if p[i] > 0:
            positivos.append(i)
        elif p[i] < 0:
            negativos.append(i)

    # interseccao de fora pra dentro
    r1 = q[negativos[0]] / p[negativos[0]]
    if len(negativos) > 1:
        r2 = q[negativos[1]] / p[negativos[1]]
    else:
        r2 = 0
    zeta_1 = max(0, r1, r2) # se der 0, interseccao nao existe e valores sao rejeitados

    # interseccao de dentro pra fora
    r3 = q[positivos[0]] / p[positivos[0]]
    if len(positivos) > 1:
        r4 = q[positivos[1]] / p[positivos[1]]
    else:
        r4 = 1
    zeta_2 = min(1, r3, r4) # se der 1, interseccao nao existe e valores sao rejeitados

    # se zeta 1 > zeta 2, a linha ta completamente fora
    if zeta_1 > zeta_2:
        print("completamente fora")
        return None

    new_x1 = point1.getNormalX() + zeta_1 * delta_x
    new_y1 = point1.getNormalY() + zeta_1 * delta_y

    new_x2 = point1.getNormalX() + zeta_2 * delta_x
    new_y2 = point1.getNormalY() + zeta_2 * delta_y

    point_1 = Point(new_x1, new_y1)
    point_2 = Point(new_x2, new_y2)
    print(point_1, point_2)
    line.setNormalCoordinates(point1, point2) 
    return line